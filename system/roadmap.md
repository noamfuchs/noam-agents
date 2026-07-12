---
name: roadmap
description: Build phases and infrastructure status for the second-brain system. Moved out of the root README 2026-07-12 so the root stays lean. Aspirational — not all phases are live.
updated: 2026-07-12
---

# Second-brain build roadmap

Historical/aspirational build plan. The vault works today without the unchecked phases; this is here for reference, not as a promise.

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
- [x] Phase 7 — Core skills written (capture, morning-preview, evening-review, weekly-digest, person-prep, draft-message, decision-recall)
- [ ] Phase -1 — FileVault (Noam to enable in System Settings)
- [ ] Phase 3b — Google Workspace MCP (needs Noam's OAuth)
- [ ] Phase 4 — Tailscale + Termius (iPhone live SSH)
- [ ] Phase 5 — Telegram bot
- [ ] Phase 6 — iPhone Shortcuts capture
- [ ] Phase 7b — Skills deferred: research, vault-query (Phase 9), form-fill (Phase 9)
- [ ] Phase 8 — Onboarding interview (gives the assistant real personality)
- [ ] Phase 9 — Personal vault import (REQUIRES FileVault complete)
- [ ] Phase 10 — Scheduled rhythms via launchd + Time Machine + GitHub backup

## Skills available
Each is a single file at `~/.claude/skills/{name}.md`. Invoke with `/{name}` in Claude Code.

| Skill | Purpose |
|---|---|
| `/capture` | Process inbox/ items — classify, file, link, log |
| `/morning-preview` | 7am: today's calendar + top 3 priorities + open inbox |
| `/evening-review` | 9pm: what shipped, what's open, things learned about Noam |
| `/weekly-digest` | Sunday 6pm: this week's decisions, flushes learned-this-week |
| `/person-prep` | Pre-meeting brief on a specific person |
| `/draft-message` | Draft 2-3 variants of a message → outbox/ (never sends) |
| `/decision-recall` | Find past decisions on similar questions |
| `/copywrite` | Hebrew marketing/course copy (existing) |
