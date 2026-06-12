---
name: Second Brain Level-Up
status: active
goal: The vault knows Noam deeply, built from what he already created, with a connected graph and live data feeds
started: 2026-06
updated: 2026-06-12
---

# Second Brain Level-Up (plan v2)

Two inputs shaped this plan:
1. Nate Herk's "I Turned Claude Fable Into The Ultimate Second Brain" (watched 2026-06-12). The Four C's: Context, Connections, Capabilities, Cadence. Gut check: ask the brain "what do you know about me?" and the answer should sound like a co-founder, not a stranger.
2. Deep research, 2026-06-12: 21 sources, 24 adversarially verified claims. Full findings in [[second-brain-research-2026-06]].

Noam's twist: the brain learns who he is from what he already created (documents, chats, posts, notes), not from him explaining himself. The vault holds the distilled understanding, not the raw data. This matches the field's reference pattern exactly (Karpathy's LLM wiki: synthesis at ingest time, raw sources immutable, agent writes the wiki, human reads it).

## Architecture (v2, from verified research)

Three layers, strict boundaries:
1. **Raw layer (immutable, agent reads only):** whatsapp.db + digests, Fathom API, מסמכים, ABLETON, future Instagram/LinkedIn exports. Source of truth. Never edited by agents.
2. **Wiki layer (this vault):** distilled notes, heavily wikilinked. Agents write, Noam reads.
3. **Schema (CLAUDE.md):** a router under 300 lines that points instead of stores.

Navigation, token-cheap read order: **hot.md** (500-word recent cache) then **[[HOME]] + hubs** (the index layer, built in Phase 0) then specific notes. Plus **log.md**, append-only, newest first.

**Provenance convention:** anything a pipeline writes is tagged. Default = extracted from source. ^[inferred] = agent synthesis. ^[ambiguous] = sources disagree. The WhatsApp digest already produced two real errors this convention would have caught ([[bitton]] named from an in-joke, [[shir]] called "girlfriend"). A weekly lint hunts contradictions, stale claims, and orphans.

## Guiding principles

1. **Distill, don't dump.** Insights in the vault, raw files stay where they are, every distilled claim cites its source.
2. **Everything connects.** Every new note links to at least 2 existing notes; hubs make the graph readable.
3. **Sources before interviews.** Mine what exists; /grill-me only fills gaps documents can't answer.
4. **Privacy tiers.** Tier 1 vault. Tier 2 ~/.personal-vault/ (medical, visa, bank: referenced only). Tier 3 never stored (credentials). The research found NO field consensus on privacy, so our design stands. boundaries.md is law.
5. **Plain markdown, tool-agnostic.** No databases. Works with any model.
6. **Cadence last.** Don't automate a workflow that doesn't work manually (verified Herk principle).
7. **No folder reorg.** The only refuted claim in the research was a rigid folder taxonomy. Current folders stay; links do the organizing.
8. **Scale guard.** Hot stays ~500 words, index lean, vault well under ~1,000 notes; archive aggressively.

## Phases

### Phase 0: Graph hygiene (done 2026-06-12)
- [x] Processed all 23 inbox captures (20 trash, 3 filed into this plan)
- [x] Renamed 11 phone-number people files to named notes (ran, hila-my-sister, tom-fox, yahel-abrahams, shir, ziv, bitton, shaked-naor, taler, yoni-klipi, roey-kalifi), phone + WhatsApp label kept in frontmatter, relationships.md updated, cross-links added
- [x] Created [[HOME]] + hubs: [[work]], [[people]], [[mind]], [[body]], [[money]], [[music]]
- [x] 75 Hard cluster linked via [[body]]
- [x] wa-people-sync: diagnosed the 01:00 API failure, re-ran, 94 messages caught up, watermark advanced
- [ ] finance/ and gym/ keep-or-delete (decision with Noam)
- Graph after Phase 0: 115 active notes, 13 fully isolated (11%), nearly all logs/templates

### Phase 0.5: Navigation + schema (done 2026-06-12, one item with Noam)
- [x] hot.md (recent-context cache) and log.md (append-only, newest first) created at vault root
- [x] CLAUDE.md rewired: hot-first read order, navigate via HOME/hubs on demand, provenance section, hot/log refresh at session end, layout map updated (~170 lines)
- [x] Provenance instructions added to the wa-people-sync prompt in run.sh (no names from jokes, contradictions become ^[ambiguous], inferences tagged)
- [ ] qmd local search: install blocked for the agent (unverified-package guard); command verified against the official repo, waiting for Noam to run it

### Phase 1: Identity core (mine the gold documents)
- [ ] Distill: dream list, 30-day self-interview, heart statements, Byron Katie sheets, Reichman application, CV arc 2024-2026, recommendation letters
- [ ] New: memory/goals.md (every stated goal, date, status, linked to the projects serving it)
- [ ] New: memory/story.md (life timeline: music career, FUCHS-SOUND, pivot to entrepreneurship, Reichman, ventures)
- [ ] Expand about-me.md and voice.md; every claim cites its source file; inferences tagged
- Output test: "what drives Noam and what is he afraid of?" answered from the vault alone

### Phase 2: People and relationships (WhatsApp deep mine)
- [ ] Mine top ~30 chats by volume + all family from whatsapp.db into person notes (with provenance tags)
- [ ] Create missing core people: [[qiu-qiqian]] first, then closest friends not yet covered
- [ ] Fix known digest errors: [[bitton]] real name, [[shir]] relationship label; resolve [[boss]]; confirm Ran is a brother
- [ ] Every person linked to projects, meetings, journal mentions; relationships.md stays a pure index
- [ ] Second pass: iMessage + Apple Contacts enrichment

### Phase 3: Life-area expansion (fill the hubs)
- [ ] [[music]]: FUCHS-SOUND, the 28 artist collaborations, current career status
- [ ] [[money]]: independence goal, accountant picture, 20% savings target, income streams
- [ ] [[body]]: health context (2025 tests stay tier-2), training, 75 Hard arc
- [ ] [[people]]: family + Qiu depth (per Noam's flagged decision)
- [ ] [[mind]]: learning, 15 books/year, sem2-coach bridge (Noam asked 2026-05-07: "שאתה תדע הכללללל" about sem2)
- [ ] dreams/travel from the dream list

### Phase 4: Live connections
- [ ] Noam requests Instagram export (Accounts Center, "Download your information") and LinkedIn export (Settings, "Get a copy of your data"). Only he can do this.
- [ ] Process exports on arrival: own posts/captions feed voice.md and [[instagram-growth]]
- [ ] Parse the 2024 Facebook export (low priority)
- [ ] Google Workspace MCP (calendar + Gmail) per existing Phase 3b plan
- [ ] Cross-project routers: REA CRM, sem2-coach, and other repos get a CLAUDE.md pointer at this vault (hot then index read protocol), one shared brain across all sessions

### Phase 5: Capabilities and cadence (cadence LAST, after skills prove out manually)
- [ ] /audit skill: weekly lint (orphans, stale claims, contradictions, duplicates, provenance check); replaces the earlier /graph-gardener idea
- [ ] /level-up skill: weekly "what should this system do better" review
- [ ] /grill-me skill: targeted interview for gaps the documents could not answer
- [ ] Voice-to-tasks: Noam's voice messages into a clear task list (asked 2026-05-06)
- [ ] Codify-as-you-go habit: after a productive session, turn what worked into a skill; update skills every time they're used
- [ ] Only then schedule: morning preview, evening review, Sunday digest + /audit via launchd

## Decisions flagged for Noam

1. **Medical records (בדיקות 2025):** recommend tier-2 (out of vault, referenced only). Confirm.
2. **Relationship depth (Qiu, partner visa, shared finances):** person note yes; visa/finance files tier-2. Confirm.
3. **finance/ and gym/ folders:** use them or delete them.
4. **Instagram + LinkedIn exports:** the two requests only Noam can click.

## Success criteria

- The gut check passes: "who am I, what matters to me, what am I building and why" gets a co-founder answer
- Graph: isolated notes under 10% and falling (Phase 0 brought it to 11%)
- Every person in people/ has a name, not a number (done) and provenance-clean content
- Each hub has real content and links
- Weekly /audit passes: no untagged inferences, no contradictions, no stale top-of-mind claims
- The brain answers with sources it can cite

## Log

- 2026-06-12: Audit completed (vault survey, מסמכים survey, data-source inventory). Plan v1 written.
- 2026-06-12: Phase 0 executed (inbox cleared, people renamed + linked, HOME + 6 hubs, WhatsApp sync repaired and caught up).
- 2026-06-12: Deep research completed (21 sources, 24 verified claims) and folded into plan v2: added Phase 0.5 (hot/log/provenance/router), provenance tags everywhere, /audit + /level-up, cross-project routers, qmd, scale guard. Findings: [[second-brain-research-2026-06]].
