# Noam's Personal Assistant — Vault

This is the daily-use brain. Open it via:
```
cd ~/second-brain && claude
```
(or `cd "~/Desktop/MY BRAIN" && claude` — same place via symlink)

## Quick map
- `CLAUDE.md` — operating manual, read first by every session
- `memory/` — what Claude remembers about Noam
- `inbox/` — captured items from phone/voice/quick-text, pending classification
- `people/` — one file per person Noam interacts with
- `projects/` — active projects
- `outbox/` — drafts Noam copy-pastes (assistant never sends directly)
- `system/automations/` — Telegram bot, launchd plists
- `_References/` — Noam's reference material (CV, profile, etc.)
- `🤖 Agents/` — Noam's existing personal agents
- `.archive/` — deprecated content; never touched by Claude

## MCP servers configured (Claude Code CLI, user scope)
| Name | Purpose |
|---|---|
| `filesystem-brain` | Read/write inside this vault |
| `sequential-thinking` | Step-by-step reasoning for complex tasks |
| `fetch` | HTTP fetch for research |
| `git-brain` | Git operations on this vault |

Run `claude mcp list` to verify health.

**Skipped:**
- `apple-mcp` — archived January 2026, no longer maintained. AppleScript via Bash if Calendar/Reminders/Mail needed locally.
- Memory MCP — using plain markdown in `memory/` instead (simpler, Obsidian-readable).
- Whisper-cpp — iOS native transcription handles voice on capture path.

**Pending:**
- Google Workspace MCP (Gmail + Calendar + Drive + Docs + Sheets) — Phase 3b, needs OAuth.
- Playwright — Phase 7 if research skill needs headless browsing.

## Phase status
- [x] Phase 1 — folder structure
- [x] Phase 2 — CLAUDE.md operating manual
- [x] Phase 3a — core MCP servers (filesystem, sequential-thinking, fetch, git)
- [ ] Phase -1 — FileVault (Noam to enable in System Settings)
- [ ] Phase 3b — Google Workspace MCP (needs Noam's OAuth)
- [ ] Phase 4 — Tailscale + Termius (iPhone live SSH)
- [ ] Phase 5 — Telegram bot
- [ ] Phase 6 — iPhone Shortcuts capture
- [ ] Phase 7 — Skills (capture, morning-preview, evening-review, etc.)
- [ ] Phase 8 — Onboarding interview
- [ ] Phase 9 — Personal vault import (REQUIRES FileVault complete)
- [ ] Phase 10 — Scheduled rhythms via launchd + Time Machine + GitHub backup
