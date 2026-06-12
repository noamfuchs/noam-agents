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
- [x] finance/ and gym/ deleted (Noam decided 2026-06-12; /fitness and /finance skills now dormant, retire via /level-up if never missed)
- Graph after Phase 0: 115 active notes, 13 fully isolated (11%), nearly all logs/templates

### Phase 0.5: Navigation + schema (done 2026-06-12, one item with Noam)
- [x] hot.md (recent-context cache) and log.md (append-only, newest first) created at vault root
- [x] CLAUDE.md rewired: hot-first read order, navigate via HOME/hubs on demand, provenance section, hot/log refresh at session end, layout map updated (~170 lines)
- [x] Provenance instructions added to the wa-people-sync prompt in run.sh (no names from jokes, contradictions become ^[ambiguous], inferences tagged)
- [ ] qmd local search: install blocked for the agent (unverified-package guard); command verified against the official repo, waiting for Noam to run it

### Phase 1: Identity core (done 2026-06-12)
- [x] Distilled: dream list, 30-day self-interview, heart statements, Byron Katie sheets, Reichman application, CV arc 2024-2026, recommendation letters
- [x] memory/goals.md created (every goal with source; financial, impact, body, mind, relationships)
- [x] memory/story.md created (Tamra → Zikhron → music at 16 → keyboards at 18 → FUCHS-SOUND → Tel Aviv loft → 2023 burnout → Geneva → bagrut in 5 months → Reichman; identity arc, how others see him, inner world with quotes, tensions)
- [x] about-me.md expanded (birthday 2000-04-08, languages, backstory, family incl. Facebook-confirmed brother/cousins, personal WhatsApp number); voice.md gained a self-directed-writing section
- [x] Bonus: Facebook 2024 export distilled (profile anchors, Rimon 2018 / SAE 2022, interest phases)
- Note: the 30-day project's date is ambiguous (2024 vs 2026); if it's running now, re-distill as days accumulate ^[ambiguous]

### Phase 2: People and relationships (done 2026-06-12, one item gated)
- [x] Top-30 DM chats mined; 6 new notes ([[qiu-qiqian]], [[sinai-tzarfati]], [[roman-shumunov]], [[yuval-avramov]], [[gal-fadlon]], [[yonatan-automations]]); existing top-30 notes verified current
- [x] [[qiu-qiqian]] built from ~75 cross-chat mentions (she lives on WeChat, no WhatsApp DM); visa/finance/medical excluded per tier rules
- [x] Identities: Boss = Gilad Klein (OD SIFRA invoice + 3 independent namings) ^[inferred]; [[ran]] = biological brother Ran Fuchs (confirmed); [[babi]] = business partner (appraiser), not family; [[bitton]] joke-name removed, real first name still unknown ^[ambiguous]; mom/paps first names absent from archive ^[ambiguous]
- [x] relationships.md rebuilt as index + new "Active groups" table (ההכשרה course group = 2,279 Noam messages); boss.md renamed gilad-klein.md; hubs and about-me corrected
- [ ] iMessage + Contacts second pass: BLOCKED by macOS (iMessage needs Full Disk Access granted by Noam; Contacts is iCloud-only with no local db)
- First /audit ran (verdict ATTENTION); its duplicate-people catch was confirmed by Noam same evening: ONE Itay and ONE Amit. Merged into itay-liani.md and amit-schleffer.md (skeleton notes deleted, links rewired). Parents named: Tal (mom), Tomer (paps). Still open from the audit: commitments.md overdue triage; watch tonight's wa-sync

### Phase 3: Life-area expansion (done 2026-06-12)
- [x] [[music]]: full career arc + real artist list from the Ableton archive + what the letters say about him
- [x] [[money]]: goals with sources, work history, accountant pointers (numbers stay in source docs)
- [x] [[body]]: training history, 75 Hard, dream-list sport goals (2025 medical tests stay tier-2, referenced only)
- [x] [[people]] hub built; family enrichment + [[qiu-qiqian]] via the WhatsApp deep mine (Phase 2)
- [x] [[mind]]: goals/story wired in, education thread, sem2-coach bridge (CLAUDE.md router placed in the coach folder)
- [x] dreams/travel live inside [[goals]]

### Phase 4: Live connections
- [ ] Noam requests Instagram export (Accounts Center, "Download your information") and LinkedIn export (Settings, "Get a copy of your data"). Only he can do this.
- [ ] Process exports on arrival: own posts/captions feed voice.md and [[instagram-growth]]
- [ ] Parse the 2024 Facebook export (low priority)
- [ ] Google Workspace MCP (calendar + Gmail) per existing Phase 3b plan
- [ ] Cross-project routers: REA CRM, sem2-coach, and other repos get a CLAUDE.md pointer at this vault (hot then index read protocol), one shared brain across all sessions

### Phase 5: Capabilities and cadence (done 2026-06-12, activation with Noam)
- [x] /audit skill created AND proven manually (first run 2026-06-12, report in system/logs/audit.log)
- [x] /level-up skill created (includes the codify-as-you-go habit)
- [x] /grill-me skill created (sources-before-interviews, files answers with provenance)
- [x] /voice-to-tasks skill created (whisper.cpp Metal preferred, CPU warn per preferences)
- [x] Sunday 18:00 weekly digest + audit: runner at ~/brain-weekly/run.sh + launchd plist written. ACTIVATION needs Noam (agent blocked from self-scheduling, correctly): `launchctl load ~/Library/LaunchAgents/com.user.secondbrain.weekly-audit.plist`
- Morning preview / evening review stay manual until Google Workspace (calendar) lands in Phase 4

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
