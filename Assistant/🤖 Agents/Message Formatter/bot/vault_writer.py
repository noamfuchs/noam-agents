"""
Vault writer — saves logs and permanent instructions into the Obsidian vault.

Local mode (Mac):  writes files directly.
Cloud mode (GitHub Actions): writes files + commits & pushes to GitHub so
    the change appears in Obsidian next time obsidian-git pulls.
"""

import os
import subprocess
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

STYLE_FILES = {
    "community": "Styles/Course Community.md",
    "partners":  "Styles/Partners.md",
    "ads":       "Styles/Ads & Webinars.md",
}

IN_CLOUD = os.environ.get("GITHUB_ACTIONS_MODE") == "true"


def _git_commit_and_push(file_path: Path, message: str):
    """Commit a changed file and push — only runs in cloud mode."""
    if not IN_CLOUD:
        return
    try:
        vault_root = Path(os.environ["VAULT_PATH"])
        rel_path = file_path.relative_to(vault_root)
        subprocess.run(["git", "add", str(rel_path)], cwd=str(vault_root), check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=str(vault_root), check=True)
        subprocess.run(["git", "push"], cwd=str(vault_root), check=True)
        logger.info(f"Committed and pushed: {rel_path}")
    except subprocess.CalledProcessError as e:
        logger.warning(f"Git commit failed (non-critical): {e}")


def log_to_vault(
    raw: str,
    formatted: str,
    audience_label: str,
    vault_path: Path,
) -> None:
    """Append a log entry to today's log file in the vault."""
    logs_dir = vault_path / "🤖 Agents" / "Message Formatter" / "Logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    today     = datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.now().strftime("%H:%M")
    log_file  = logs_dir / f"{today}.md"

    if not log_file.exists():
        log_file.write_text(f"# Message Formatter Logs — {today}\n\n", encoding="utf-8")

    entry = (
        f"## {timestamp} — {audience_label}\n\n"
        f"**Raw input:**\n{raw}\n\n"
        f"**Formatted output:**\n{formatted}\n\n"
        f"---\n\n"
    )
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry)

    # In cloud mode, commit the log so it shows up in Obsidian
    _git_commit_and_push(log_file, f"bot: log {audience_label} {timestamp}")


def save_instruction(audience_key: str, instruction: str, vault_path: Path) -> None:
    """
    Permanently append a learned instruction to the style profile.
    In cloud mode, also commits the change to GitHub so Obsidian gets it.
    """
    relative = STYLE_FILES.get(audience_key)
    if not relative:
        raise ValueError(f"Unknown audience key: {audience_key}")

    profile_path = vault_path / "🤖 Agents" / "Message Formatter" / relative
    content = profile_path.read_text(encoding="utf-8")

    if "## Learned Instructions" not in content:
        content = content.rstrip() + (
            "\n\n---\n\n"
            "## Learned Instructions\n\n"
            "_These rules were saved from real feedback and always apply._\n\n"
        )

    timestamp = datetime.now().strftime("%Y-%m-%d")
    content   = content.rstrip() + f"\n- [{timestamp}] {instruction}\n"

    profile_path.write_text(content, encoding="utf-8")

    # In cloud mode, commit so the rule appears in Obsidian
    _git_commit_and_push(
        profile_path,
        f"bot: save rule for {audience_key} — {instruction[:60]}"
    )
