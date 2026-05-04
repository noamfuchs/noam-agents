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
CONV_DIR = BRAIN / "system" / "conversations"
CONV_LOG = CONV_DIR / "telegram.md"
INBOX.mkdir(parents=True, exist_ok=True)
INBOX_AUDIO.mkdir(parents=True, exist_ok=True)
LOGS.mkdir(parents=True, exist_ok=True)
CONV_DIR.mkdir(parents=True, exist_ok=True)

# Local whisper CLI — installed via `pip3 install openai-whisper` against
# the system python at /Library/Frameworks/Python.framework/Versions/3.13.
# Runs entirely on-device, no API cost.
WHISPER_BIN = "/Library/Frameworks/Python.framework/Versions/3.13/bin/whisper"
WHISPER_MODEL = SECRETS.get("WHISPER_MODEL", "small")  # base|small|medium|large

# Conversation context — how much of the recent log to inject into each
# `claude -p` call so replies stay coherent across turns.
CONTEXT_MAX_CHARS = 8000

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


def write_voice_to_inbox(audio_path: Path, transcript: str | None = None) -> Path:
    name = f"{stamp()}-tg-voice.md"
    path = INBOX / name
    if transcript:
        body = (
            f"---\n"
            f"source: telegram-voice\n"
            f"timestamp: {datetime.now().isoformat()}\n"
            f"audio: {audio_path}\n"
            f"---\n\n"
            f"{transcript}\n"
        )
    else:
        body = (
            f"---\n"
            f"source: telegram-voice\n"
            f"timestamp: {datetime.now().isoformat()}\n"
            f"audio: {audio_path}\n"
            f"transcript: failed\n"
            f"---\n\n"
            f"_Voice memo — local transcription failed. Audio file saved at `{audio_path}`._\n"
        )
    path.write_text(body, encoding="utf-8")
    return path


# ---- Voice transcription (local, free) -------------------------------------


def transcribe_voice(audio_path: Path) -> str | None:
    """Run local whisper on the .ogg file. Returns transcript text or None.

    Uses the openai-whisper Python package via its CLI (no API call). Hebrew
    is hinted but whisper auto-detects if the speaker switches.
    """
    if not Path(WHISPER_BIN).exists():
        log.error("whisper binary missing at %s", WHISPER_BIN)
        return None
    out_dir = audio_path.parent
    try:
        result = subprocess.run(
            [
                WHISPER_BIN, str(audio_path),
                "--model", WHISPER_MODEL,
                "--language", "he",
                "--output_dir", str(out_dir),
                "--output_format", "txt",
                "--fp16", "False",
                "--verbose", "False",
            ],
            capture_output=True,
            text=True,
            timeout=600,
        )
        txt_file = out_dir / (audio_path.stem + ".txt")
        if txt_file.exists():
            transcript = txt_file.read_text(encoding="utf-8").strip()
            return transcript or None
        log.error("whisper produced no txt; rc=%s stderr=%s", result.returncode, result.stderr[:500])
        return None
    except subprocess.TimeoutExpired:
        log.error("whisper timed out on %s", audio_path)
        return None
    except Exception as e:
        log.exception("whisper error: %s", e)
        return None


# ---- Conversation context --------------------------------------------------


def append_conversation(role: str, text: str) -> None:
    """Append one turn to the persistent telegram conversation log."""
    ts = datetime.now().isoformat(timespec="seconds")
    try:
        with CONV_LOG.open("a", encoding="utf-8") as f:
            f.write(f"\n## {role} — {ts}\n{text.strip()}\n")
    except Exception as e:
        log.error("failed to append conversation log: %s", e)


def recent_context() -> str:
    """Return the tail of the conversation log, capped at CONTEXT_MAX_CHARS."""
    if not CONV_LOG.exists():
        return ""
    try:
        text = CONV_LOG.read_text(encoding="utf-8")
    except Exception as e:
        log.error("failed to read conversation log: %s", e)
        return ""
    if len(text) <= CONTEXT_MAX_CHARS:
        return text.strip()
    return "...(earlier turns omitted)...\n" + text[-CONTEXT_MAX_CHARS:].strip()


# ---- Command handling ------------------------------------------------------


# Tool whitelist for the network-exposed bot. Reads everywhere in the brain.
# Writes allowed via filesystem-brain MCP — Claude must follow CLAUDE.md
# rules about which files are safe to modify (memory/* except boundaries.md;
# inbox/, journal/, people/, projects/, outbox/). Never CLAUDE.md, never
# boundaries.md silently, never .archive/, never .obsidian/, never .git/.
# No Bash, no external network, no git mutations.
CLAUDE_ALLOWED_TOOLS = " ".join([
    "Read",
    "Glob",
    "Grep",
    "TodoWrite",
    # filesystem MCP — read
    "mcp__filesystem-brain__read_text_file",
    "mcp__filesystem-brain__read_multiple_files",
    "mcp__filesystem-brain__list_directory",
    "mcp__filesystem-brain__list_directory_with_sizes",
    "mcp__filesystem-brain__directory_tree",
    "mcp__filesystem-brain__search_files",
    "mcp__filesystem-brain__get_file_info",
    # filesystem MCP — write (Claude must follow CLAUDE.md about safe paths)
    "mcp__filesystem-brain__write_file",
    "mcp__filesystem-brain__edit_file",
    "mcp__filesystem-brain__create_directory",
    # reasoning
    "mcp__sequential-thinking__sequentialthinking",
])


def call_claude(prompt: str, chat_id: int, with_context: bool = True) -> None:
    """Invoke claude -p in the brain dir. Reply with response.

    When with_context=True, the recent telegram conversation log is prepended
    so the assistant has continuity across turns. The user message and the
    assistant's reply are then appended to that log.
    """
    log.info("→ claude: %s", prompt[:120].replace("\n", " "))
    tg_send_chat_action(chat_id, "typing")

    if with_context:
        ctx = recent_context()
        if ctx:
            full_prompt = (
                "Below is the recent Telegram conversation between you (Claude, "
                "Noam's personal assistant) and Noam, oldest first. Treat it as "
                "your prior turns — don't repeat past replies, build on them.\n\n"
                "=== RECENT CONVERSATION ===\n"
                f"{ctx}\n"
                "=== END CONVERSATION ===\n\n"
                f"## Noam — now\n{prompt}\n\n"
                "Reply to Noam's latest message. Match his language."
            )
        else:
            full_prompt = prompt
    else:
        full_prompt = prompt

    try:
        # Pipe prompt via stdin to avoid argparse swallowing it as a flag value
        # (since --allowedTools is a variadic flag).
        result = subprocess.run(
            [
                "claude", "-p",
                "--allowedTools", CLAUDE_ALLOWED_TOOLS,
            ],
            input=full_prompt,
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
        if with_context:
            append_conversation("Noam", prompt)
            append_conversation("Assistant", out)
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

    if cmd_lower == "reset":
        # Clear conversation context (keep the file but archive it).
        if CONV_LOG.exists():
            archive = CONV_DIR / f"telegram-{stamp()}.md"
            CONV_LOG.rename(archive)
            tg_send(chat_id, f"🧹 הקונטקסט אופס. (גובה ל־{archive.name})")
        else:
            tg_send(chat_id, "🧹 אין מה לאפס.")
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
                    if not tg_download_voice(file_id, audio_path):
                        tg_send(chat_id, "❌ Voice download failed.")
                        continue
                    tg_send_chat_action(chat_id, "typing")
                    tg_send(chat_id, "🎤 מתמלל...")
                    transcript = transcribe_voice(audio_path)
                    if not transcript:
                        write_voice_to_inbox(audio_path, transcript=None)
                        tg_send(chat_id, "❌ תמלול נכשל. ההקלטה נשמרה ב־inbox/audio/.")
                        continue
                    path = write_voice_to_inbox(audio_path, transcript=transcript)
                    log.info("voice → %s (%d chars)", path, len(transcript))
                    tg_send(chat_id, f"📝 {transcript}")
                    call_claude(transcript, chat_id)
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
