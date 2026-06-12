---
name: Second Brain Level-Up
status: planning
goal: The vault knows Noam deeply, built from what he already created, with a connected graph and live data feeds
started: 2026-06
---

# Second Brain Level-Up

Source of the vision: Nate Herk, "I Turned Claude Fable Into The Ultimate Second Brain" (watched 2026-06-12). His framework is the Four C's: **Context** (the brain knows who you are), **Connections** (live data, not stale snapshots), **Capabilities** (skills), **Cadence** (runs while you sleep). The gut check: ask the brain "what do you know about me?" and the answer should sound like a co-founder, not a stranger.

Noam's twist on it: the brain should learn who he is from what he already created (documents, chats, posts, notes), not from him explaining himself. The vault holds the distilled understanding, not the raw data.

## Where the vault stands (2026-06-12 audit)

**Strong:** RFS + REA work core is dense and well-linked (Meetings 100% linked, journal is a daily hub, commitments.md and decisions.md actively maintained, CLAUDE.md is a solid operating manual). Fathom sync, WhatsApp nightly sync, and 75 Hard bot all run.

**Weak (why the graph looks disconnected):**
- 23 inbox captures from early May, never processed
- 11 phone-number people files (972...) from the WhatsApp import, never merged or linked, 71% of people/ is orphaned
- finance/ and gym/ are empty templates
- outbox/ never used, _References/ empty placeholders
- No goals file, no hub/MOC notes, no life-area structure

**Missing life areas entirely:** music career (the biggest one: 214GB of Ableton sessions with 28 artists including Noa Kirel, Daniel Solomon, Liraz), family depth, Qiu, health, personal money, dreams/goals, learning, travel.

## The raw material (what exists, ranked)

| Source | Where | Value |
|---|---|---|
| Dream list (רשימת החלומות שלי) | Dropbox root | Gold: stated life goals with dates |
| 30 days projact (self-interview, 7 days) | מסמכים | Gold: fears, money anxiety, identity |
| Reichman application + motivation letters | מסמכים/לימודים | Gold: self-narrative, ambitions |
| CVs 2024-2026 (6 versions) + recommendation letters | מסמכים/לימודים | Gold: career arc + how others see him |
| הצהרות הלב + Byron Katie worksheets | מסמכים | High: values, inner work |
| WhatsApp db (69k messages, 1,893 chats) | ~/.config/second-brain/whatsapp.db | Gold: every relationship, real voice |
| Ableton LIVE folder (28 artist projects) | Dropbox/ABLETON | High: full music career map |
| Accountant reports, financial plan, BOOK KEEP | מסמכים | High: real money picture |
| iMessage chat.db (100MB) + Apple Contacts | ~/Library | Medium: untouched |
| Facebook GDPR export (Feb 2024) | מסמכים | Low-medium: history snapshot |
| Instagram + LinkedIn | not on disk | Need Noam to request exports |

## Guiding principles

1. **Distill, don't dump.** The vault gets insights about Noam with a link to the source file. Raw documents stay where they are.
2. **Everything connects.** Every new or touched note links to at least 2 existing notes. Hubs make the graph readable.
3. **Sources before interviews.** Mine what exists first. A /grill-me interview only fills gaps the documents can't answer.
4. **Privacy tiers.** Tier 1 vault (normal life context). Tier 2 ~/.personal-vault/ (medical, visa, bank: referenced in vault only as "exists, see personal vault"). Tier 3 never stored (credentials). boundaries.md stays law.
5. **Plain markdown, tool-agnostic.** Folders and files, no databases, works with any model.

## Phases

### Phase 0: Graph hygiene (1 session)
- [ ] Process all 23 inbox captures through the capture protocol
- [ ] Merge the 11 phone-number people files into named notes (Ran, Mom, Paps, Babi, Shai, Hila...), archive the raw imports
- [ ] Delete finance/ and gym/ templates or commit to using them (decision for Noam)
- [ ] Create hub notes: HOME.md plus life-area maps (Work, People, Mind, Body, Money, Music)
- [ ] Link the self-contained clusters (75 Hard dailies to tracker, tracker to Body hub)
- [ ] Fix wa-bridge (Org Chart flags it "exiting 1")

### Phase 1: Identity core (mine the gold documents)
- [ ] Distill dream list, 30-day self-interview, heart statements, Byron Katie sheets, Reichman application, CV arc, recommendation letters
- [ ] New: memory/goals.md (every stated goal with date and status, linked to the projects that serve it)
- [ ] New: memory/story.md (life timeline: music career, FUCHS-SOUND, pivot to entrepreneurship, Reichman, ventures)
- [ ] Expand about-me.md and voice.md with what the documents reveal
- Output test: "what drives Noam and what is he afraid of?" answered from the vault alone

### Phase 2: People and relationships (the WhatsApp deep mine)
- [ ] Mine the top ~30 chats by volume + all family from whatsapp.db into real person notes
- [ ] Create the missing core people: Qiu (most important person, barely in the vault), parents, siblings, closest friends
- [ ] Every person note linked to projects, meetings, journal mentions
- [ ] Regenerate relationships.md as a pure index of people/, single source of truth
- [ ] Second pass: iMessage + Apple Contacts enrichment

### Phase 3: Life-area expansion (new notes, distilled)
- [ ] music.md: FUCHS-SOUND, the 28 artist collaborations, current status of that career
- [ ] money.md: financial independence goal, accountant picture, 20% savings target, course/REA income logic
- [ ] health.md: 75 Hard context, training, the 2025 tests referenced at tier-2 only
- [ ] family.md + relationship area (Qiu): depth level is Noam's call, flagged below
- [ ] learning.md: 15 books/year goal, IDC, what he's teaching himself
- [ ] dreams/travel: from the dream list (biweekly nature nights, marathon abroad yearly)

### Phase 4: Live connections
- [ ] Noam requests Instagram export (Accounts Center, "Download your information") and LinkedIn export (Settings, "Get a copy of your data"). Only he can do this.
- [ ] Process exports when they arrive: own posts and captions feed voice.md and instagram-growth
- [ ] Parse the 2024 Facebook export for history (low priority)
- [ ] Google Workspace MCP (calendar + Gmail) per the existing Phase 3b plan
- [ ] Keep existing syncs healthy: Fathom, WhatsApp nightly, 75 Hard

### Phase 5: Capabilities and cadence
- [ ] /grill-me skill: targeted interview for gaps the documents could not answer
- [ ] /graph-gardener skill: weekly orphan sweep, proposes links, reports graph health
- [ ] Revive capture flow as a weekly ritual, revive outbox drafting
- [ ] Schedule the daily rhythm already designed in CLAUDE.md (morning preview, evening review, Sunday digest)
- [ ] Rewrite CLAUDE.md as a router (per the video): shorter core, points to hubs and memory instead of holding everything

## Decisions flagged for Noam

1. **Medical records (בדיקות 2025):** recommend tier-2 (out of vault, referenced only). Confirm.
2. **Relationship depth (Qiu, partner visa, shared finances):** a person note yes, but how deep? Recommend normal person note + tier-2 for visa/finance files.
3. **finance/ and gym/ folders:** use them or delete them.
4. **Instagram + LinkedIn exports:** the two requests only Noam can click.

## Success criteria

- The gut check passes: "who am I, what matters to me, what am I building and why" gets a co-founder answer
- Graph: under 10% orphan notes (today: roughly 35%)
- Every person in people/ has a name, not a number
- Each life area has a hub note with real content and links
- The brain answers from sources it can cite (note links to file path)

## Log

- 2026-06-12: Audit completed (vault survey, מסמכים survey, data-source inventory). Plan written.
