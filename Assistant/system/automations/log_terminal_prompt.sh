#!/bin/bash
# UserPromptSubmit hook — append Noam's terminal prompt to the unified
# cross-channel conversation log so future sessions (terminal + telegram)
# share continuity.
#
# Receives a JSON object on stdin with a `prompt` field.

set -e

LOG="/Users/noamfuchs/Desktop/MY BRAIN/system/conversations/main.md"
mkdir -p "$(dirname "$LOG")"

input=$(cat)
prompt=$(printf '%s' "$input" | /usr/bin/python3 -c '
import json, sys
try:
    data = json.loads(sys.stdin.read())
    print(data.get("prompt", ""), end="")
except Exception:
    pass
')

# Empty prompt or system-reminder-only input — skip.
if [ -z "$prompt" ]; then
  exit 0
fi

ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
{
  printf '\n## Noam (terminal) — %s\n' "$ts"
  printf '%s\n' "$prompt"
} >> "$LOG"

exit 0
