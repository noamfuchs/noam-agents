#!/usr/bin/env python3
"""Stop-hook helper. Reads JSON from stdin (Claude Code Stop event), extracts
the last assistant text from the transcript, and appends to the unified
conversation log with dedupe via a marker file.
"""

import json
import sys
import os
import datetime
import pathlib

LOG = pathlib.Path("/Users/noamfuchs/Desktop/MY BRAIN/system/conversations/main.md")
MARKER = pathlib.Path("/Users/noamfuchs/Desktop/MY BRAIN/system/conversations/.last_terminal_response_uuid")
LOG.parent.mkdir(parents=True, exist_ok=True)


def main() -> int:
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except Exception:
        return 0

    transcript = data.get("transcript_path")
    if not transcript or not os.path.exists(transcript):
        return 0

    last_uuid = None
    last_text = None
    with open(transcript, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
            except Exception:
                continue
            if msg.get("type") != "assistant":
                continue
            content = (msg.get("message") or {}).get("content") or []
            text_parts = [
                c.get("text", "")
                for c in content
                if isinstance(c, dict) and c.get("type") == "text"
            ]
            text = "\n".join(t for t in text_parts if t).strip()
            if not text:
                continue
            last_uuid = msg.get("uuid") or (msg.get("message") or {}).get("id")
            last_text = text

    if not last_text:
        return 0

    prev = ""
    try:
        prev = MARKER.read_text(encoding="utf-8").strip()
    except Exception:
        pass
    key = last_uuid or last_text[:80]
    if key == prev:
        return 0

    ts = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"\n## Assistant (terminal) — {ts}\n{last_text}\n")
    MARKER.write_text(key, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
