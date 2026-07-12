---
name: hot
description: Recent-context cache. Read me FIRST every session. Refreshed at session end. Keep under 500 words.
updated: 2026-07-12
---

# 🔥 Hot (as of 2026-07-12, Sunday maintenance)

## This week's reality
- **Second quiet week in a row (07-06 to 07-12):** no new journal entries, no new Fathom meetings, no new decisions, learned-this-week.md still empty. Today Noam wrote in his own journal for the first time in a while — reflective/grateful morning pages, no new operational facts.
- **Vault restructured today (2026-07-12):** hubs/ (6 files) folded into a single [[HOME]]; Noam's own writing moved to `../📓 Journal/` at the vault root (read-only to the assistant); CLAUDE.md rewritten. Graph health verified clean post-restructure — 0 real orphans, HOME.md covers all 13 core projects + people (via [[relationships]]).
- **RFS website — dev STILL BLOCKED.** Team: [[etay-zaslavsky|Etay]] + [[yuval-klein|Yuval]], overseen by [[yonatan-buntzel|Yonatan]]. Wireframes due 2026-06-23 — **now 19 days overdue**.
- **NEW open question:** `projects/rfs-platform.md` — relationship between [[ori-rozental|Ori]]'s earlier build and the new from-scratch Etay+Yuval team (since 06-22) never clarified — missed by the last 2 audits. The active commitment "join Ori's build" (06-08) may be moot.
- **"Dana" identity STILL unresolved** — 3 threads (Biliyo, medical-data-marketplace, Dana Gerichter), stuck 4+ weeks.
- **Biliyo** — MVP deadline 2026-08-04 (Stiko Ventures), now <4 weeks out. Co-founder decision still pending.
- **75 Hard** — 21 days of bot silence (was 14). NEW: 75hard-sync's git push is failing on DNS (`Could not resolve host: github.com`) — a real, fixable piece of the stall, though may not be the whole story (check if Noam is still doing daily check-ins).
- **Instagram** — 35 days, 0 reels since strategy set (plan: 2/week).

## Commitment backlog — CRITICAL, now a 3-audit pattern
48 active commitments, **zero closed in THREE consecutive weekly audits** (06-28 → 07-05 → 07-12). This is the top risk in the vault right now, ahead of any single pipeline issue.
Top overdue: Chapter 4 to Amit — 65 days · RFS wireframes — 19 days overdue 🚨 · Zak Feingold acceptance email — 37 days (already accepted, just not told) · Eitan Solow decision — ~37 days · Dana Gerichter / Sari Hillel / RFS Global IG setup — 34 days each.
→ Close at least 5 before adding new ones. Third week this ask hasn't landed.

## NEW: provenance bug found (systemic, not one-off)
4 of 12 people/ notes with both a frontmatter `last_interaction` and a body "**Last interaction:**" line disagree between the two: arad-fruchter, dafne-bennatan, lev-wolf, gal-halfon. Same shape every time — frontmatter updated by a later meeting pass, body text not. Likely a pipeline/prompt bug, not 4 separate data errors. Proposed fix not yet applied (body-text edit, outside this week's hub-link-only scope).

## In flight
1. Biliyo / Dana — co-founder decision (MVP 08-04, closing in)
2. Dana identity — unresolved, 4+ weeks
3. rfs-platform Ori question — new, needs a one-line answer from Noam
4. Or Segal (Base44) NY sponsorship — Dafne assessing
5. NY launch — ~September, Noam + Dafne leading
6. Git: uncommitted files across sessions — still unverified (git commands not approved in automated runs, 2 weeks running)

## Pipelines — mixed, one likely common root cause found
- **wa-people-sync:** watermark frozen 16 days straight (was 9) — almost certainly an ingestion stall.
- **wa-bridge:** still fully gone from launchctl, 12+ days — likely feeds wa-people-sync, likely root cause of the freeze above.
- **brain-bot (Telegram):** flapping on DNS resolution failures (`api.telegram.org`) all day but self-healing each time. PASS with caveat.
- **75hard-sync:** DNS failures on `github.com` for git push — same failure signature as brain-bot. **Worth checking Mac-level DNS/network health directly — could explain multiple pipeline symptoms at once.**
- **weekly-audit:** PASS, ran on schedule today (18:00).

## How to read this vault
1. This file. 2. [[HOME]] — the single index (no hubs/ anymore). 3. Drill into specific notes. Never load the whole vault.
