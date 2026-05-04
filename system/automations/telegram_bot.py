#!/usr/bin/env python3
"""
Personal assistant Telegram bot — long-poll, no public webhook.

Incoming text     → write to inbox/YYYY-MM-DD-HHMMSS-tg.md (frontmatter)
Incoming voice    → save audio to inbox/audio/, note transcript-pending
/digest           → run morning-preview skill via `claude -p`, reply
/{any-other-cmd}  → forward to claude with "Run skill: {command}"
/vault*           → refused ("Vault queries available via SSH only — open Termius")

Reads secrets from ~/.config/second-brain/secrets.env
Logs to system/logs/telegram.log (under SECOND_BRAIN_PATH).
"""

import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

# ---- Config ----------------------------------------------------------------

SECRETS_PATH = Path.home() / ".config" / "second-brain" / "secrets.env"


def load_secrets(path: Path) -> dict:
    if not path.exists():
        sys.stderr.write(f"FATAL: secrets file missing at {path}\n")
        sys.exit(1)
    out = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


SECRETS = load_secrets(SECRETS_PATH)
TOKEN = SECRETS.get("TELEGRAM_BOT_TOKEN", "")
ALLOWED_CHAT_ID = SECRETS.get("TELEGRAM_CHAT_ID", "")  # may be empty on first run
BRAIN = Path(SECRETS.get("SECOND_BRAIN_PATH", str(Path.home() / "Desktop" / "MY BRAIN")))
LOG_LEVEL = SECRETS.get("LOG_LEVEL", "INFO")

if not TOKEN:
    sys.stderr.write("FATAL: TELEGRAM_BOT_TOKEN not set in secrets.env\n")
    sys.exit(1)

API = f"https://api.telegram.org/bot{TOKEN}"
FILE_API = f"https://api.telegram.org/file/bot{TOKEN}"

INBOX = BRAIN / "inbox"
INBOX_AUDIO = INBOX / "audio"
LOGS = BRAIN / "system" / "logs"
INBOX.mkdir(parents=True, exist_ok=True)
INBOX_AUDIO.mkdir(parents=True, exist_ok=True)
LOGS.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOGS / "telegram.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("telegram-bot")


# ---- Telegram API helpers --------------------------------------------------


def tg_get_updates(offset: int) -> list:
    r = requests.get(f"{API}/getUpdates", params={"offset": offset, "timeout": 30}, timeout=60)
    r.raise_for_status()
    data = r.json()
    if not data.get("ok"):
        log.error("getUpdates not ok: %s", data)
        return []
    return data.get("result", [])


def tg_send(chat_id: int, text: str) -> None:
    try:
        r = requests.post(f"{API}/sendMessage", json={"chat_id": chat_id, "text": text}, timeout=30)
        if not r.ok:
            log.error("sendMessage failed: %s", r.text)
    except Exception as e:
        log.error("sendMessage exception: %s", e)


def tg_send_chat_action(chat_id: int, action: str = "typing") -> None:
    """Show 'typing...' in the user's Telegram client. Best-effort, swallow errors."""
    try:
        requests.post(f"{API}/sendChatAction", json={"chat_id": chat_id, "action": action}, timeout=10)
    except Exception:
        pass


def tg_download_voice(file_id: str, dest: Path) -> bool:
    try:
        r = requests.get(f"{API}/getFile", params={"file_id": file_id}, timeout=30)
        r.raise_for_status()
        file_path = r.json()["result"]["file_path"]
        r2 = requests.get(f"{FILE_API}/{file_path}", timeout=60)
        r2.raise_for_status()
        dest.write_bytes(r2.content)
        return True
    except Exception as e:
        log.error("voice download failed: %s", e)
        return False


# ---- Inbox writers ---------------------------------------------------------


def stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d-%H%M%S")


def write_text_to_inbox(text: str, source: str = "telegram") -> Path:
    name = f"{stamp()}-tg.md"
    path = INBOX / name
    body = (
        f"---\n"
        f"source: {source}\n"
        f"timestamp: {datetime.now().isoformat()}\n"
        f"---\n\n"
        f"{text}\n"
    )
    path.write_text(body, encoding="utf-8")
    return path


def write_voice_to_inbox(audio_path: Path) -> Path:
    name = f"{stamp()}-tg-voice.md"
    path = INBOX / name
    body = (
        f"---\n"
        f"source: telegram-voice\n"
        f"timestamp: {datetime.now().isoformat()}\n"
        f"audio: {audio_path}\n"
        f"transcript: pending\n"
        f"---\n\n"
        f"_Voice memo — transcription not yet configured. Audio file saved at `{audio_path}`._\n"
    )
    path.write_text(body, encoding="utf-8")
    return path


# ---- Command handling ------------------------------------------------------


# Read-only tool whitelist. The bot is a network-exposed daemon — no Bash, no
# external network, no writes from Claude. Mutations to the brain happen only
# via interactive desktop Claude sessions where Noam approves them.
CLAUDE_ALLOWED_TOOLS = " ".join([
    "Read",
    "Glob",
    "Grep",
    "TodoWrite",
    "mcp__filesystem-brain__read_text_file",
    "mcp__filesystem-brain__read_multiple_files",
    "mcp__filesystem-brain__list_directory",
    "mcp__filesystem-brain__list_directory_with_sizes",
    "mcp__filesystem-brain__directory_tree",
    "mcp__filesystem-brain__search_files",
    "mcp__filesystem-brain__get_file_info",
    "mcp__sequential-thinking__sequentialthinking",
])


def call_claude(prompt: str, chat_id: int) -> None:
    """Invoke claude -p in the brain dir with read-only tools. Reply with response."""
    log.info("→ claude: %s", prompt[:120].replace("\n", " "))
    tg_send_chat_action(chat_id, "typing")
    try:
        # Pipe prompt via stdin to avoid argparse swallowing it as a flag value
        # (since --allowedTools is a variadic flag).
        result = subprocess.run(
            [
                "claude", "-p",
                "--allowedTools", CLAUDE_ALLOWED_TOOLS,
            ],
            input=prompt,
            cwd=str(BRAIN),
            capture_output=True,
            text=True,
            timeout=240,
        )
        out = result.stdout.strip()
        if not out:
            err = result.stderr.strip()
            log.error("claude empty stdout; stderr: %s", err[:500])
            out = err or "(no response)"
        # Telegram limit is 4096 chars per message
        for chunk in [out[i : i + 4000] for i in range(0, len(out), 4000)]:
            tg_send(chat_id, chunk)
    except subprocess.TimeoutExpired:
        tg_send(chat_id, "⏱️ זמן תגובה ארוך מדי (>4 דקות). נסה שוב.")
    except FileNotFoundError:
        tg_send(chat_id, "❌ `claude` CLI not found in PATH.")
    except Exception as e:
        log.exception("claude error: %s", e)
        tg_send(chat_id, f"❌ {e}")


def run_skill_via_claude(skill_with_args: str, chat_id: int) -> None:
    """Slash-command path: invoke a specific skill (read-only)."""
    call_claude(f"Run skill: {skill_with_args}", chat_id)


def handle_command(text: str, chat_id: int) -> None:
    cmd = text[1:].strip()  # strip leading /
    cmd_lower = cmd.lower().split()[0] if cmd else ""

    if cmd_lower.startswith("vault"):
        tg_send(chat_id, "🔒 Vault queries available via SSH only — open Termius.")
        return

    if cmd_lower == "digest" or cmd_lower == "preview":
        run_skill_via_claude("morning-preview", chat_id)
        return

    if cmd_lower == "ping":
        tg_send(chat_id, "🏓 pong")
        return

    if cmd_lower == "id":
        tg_send(chat_id, f"chat_id: {chat_id}")
        return

    # default — forward as a skill invocation
    run_skill_via_claude(cmd, chat_id)


# ---- Main loop -------------------------------------------------------------


def authorized(chat_id: int) -> bool:
    if not ALLOWED_CHAT_ID:
        # First-run mode: any chat is allowed but we tell Noam the chat_id so he can lock it down.
        return True
    return str(chat_id) == ALLOWED_CHAT_ID


def main() -> None:
    log.info("telegram-bot starting; brain=%s allowed_chat=%s", BRAIN, ALLOWED_CHAT_ID or "<UNSET — first-run mode>")
    offset = 0
    while True:
        try:
            updates = tg_get_updates(offset)
            for upd in updates:
                offset = upd["update_id"] + 1
                msg = upd.get("message") or upd.get("edited_message")
                if not msg:
                    continue
                chat_id = msg["chat"]["id"]

                if not authorized(chat_id):
                    log.warning("ignoring unauthorized chat_id=%s", chat_id)
                    continue

                if not ALLOWED_CHAT_ID:
                    tg_send(
                        chat_id,
                        f"👋 First-run mode. Your chat_id is {chat_id}. "
                        f"Add it to ~/.config/second-brain/secrets.env as TELEGRAM_CHAT_ID and restart the bot.",
                    )

                if "text" in msg:
                    text = msg["text"]
                    if text.startswith("/"):
                        handle_command(text, chat_id)
                    else:
                        # 1. Durable capture: write the message to inbox/ regardless.
                        path = write_text_to_inbox(text)
                        log.info("text → %s", path)
                        # 2. Conversational reply: ask Claude (read-only) and relay.
                        call_claude(text, chat_id)
                elif "voice" in msg:
                    file_id = msg["voice"]["file_id"]
                    audio_path = INBOX_AUDIO / f"{stamp()}.ogg"
                    if tg_download_voice(file_id, audio_path):
                        path = write_voice_to_inbox(audio_path)
                        log.info("voice → %s", path)
                        tg_send(chat_id, f"🎤 נשמר ב־inbox: {path.name} (transcription pending)")
                    else:
                        tg_send(chat_id, "❌ Voice download failed.")
                else:
                    log.info("ignoring message type: %s", list(msg.keys()))

        except requests.RequestException as e:
            log.warning("network error: %s; retrying in 5s", e)
            time.sleep(5)
        except KeyboardInterrupt:
            log.info("interrupted; exiting")
            return
        except Exception as e:
            log.exception("loop error: %s; sleeping 10s", e)
            time.sleep(10)


if __name__ == "__main__":
    main()
