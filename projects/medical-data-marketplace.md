---
name: Medical Data Marketplace
status: idea
goal: "Niche marketplace / 'data bank' for medical data, starting with pathology slides (biopsies)"
started: 2026-06-18
---

# Medical Data Marketplace

**Goal:** A niche marketplace ("data bank") that connects medical-data holders (hospitals) with data users (MedTech, researchers, AI labs), starting with a single vertical — **pathology slides / biopsies** — before expanding. ^[inferred — early-stage idea, from the 2026-06-18 brainstorm]
**Current state:** Brainstorm / concept-validation stage. Co-explored with **Dana** (medical-data collaborator; not yet matched to a person file — see below).
**Blockers:** Concept unvalidated; needs domain input from a medical-industry expert (Dana's father) and a competitive scan.

## The thesis (from 2026-06-18 brainstorm)
- **Problem:** Acquiring medical data is a major bottleneck — slow/bureaucratic vendor negotiations, late discovery of unusable data (e.g. slides scanned at 20x when 40x is needed), no common format or quality metric across vendors, and a heavy anonymization/compliance burden.
- **Solution:** A platform that (1) standardizes data quality + format, (2) streamlines anonymization/compliance, (3) turns hospitals' unused data archives into a new revenue stream.
- **Value:** hospitals get revenue from dormant archives; users get a reliable standardized source; the industry gets fresher, more diverse datasets for AI models + research.
- **Strategy:** niche-first (one vertical, deep) rather than broad.

## Model evolution — the "cable" vs "warehouse" framing (2026-06-28)
A solo working session ([[Meetings/2026-06-28 - Impromptu Google Meet Meeting (158840046)]]) sharpened the concept into a clear contrast:
- **"Warehouse" model (incumbents, e.g. Protege):** acquire large static data batches, sell as one-off historical datasets. Problems: enterprise-only (no simple B2C/research access), stale data (updated ~monthly), high storage/management overhead — unsuitable for training on fast-evolving techniques.
- **"Cable" model (the proposed pivot):** a **subscription** service streaming continuous, real-time anonymized data straight from hospitals to consumers. An automated pipeline pulls anonymized data daily; the platform handles cleaning/standardization/anonymization and verifies both providers and consumers; revenue = a **commission on each data transaction** (middleman).
- **Niche-first refinement:** start with **new pathology stains (e.g. IHC)** — historical data is scarce, so a continuous stream of fresh samples is essential for training/retraining models on emerging techniques. Avoids a "scattered" approach.

**Two critical unknowns (must validate before building):**
1. **Provider friction** — how hard is it to get data-sharing agreements with hospitals (Helsinki Committee approval, strict security, regulatory hurdles)? The plug-and-play "cable" could turn dormant hospital data into passive revenue and lower this friction — but that's a hypothesis.
2. **Market demand** — do medical-AI startups actually need a *continuous* stream (live retraining, new modalities), or is a large *static historical* dataset more efficient for initial product development? Unresolved counterpoint.

Validation plan: interview medical-AI startups + data-acquisition managers on both unknowns, then refine the concept.

## Open items
- [ ] Research existing data marketplaces / competitors; find differentiation; share findings with Dana
- [ ] Schedule a Zoom with Dana + her father (medical-industry expert) to validate the concept and tap his connections; then hold the session
- [ ] Send the 2026-06-18 brainstorm summary to Dana
- [ ] Saturday (2026-06-20) — follow-up working session with Dana to continue
- [ ] Noam: ping [[paps|Tomer]] for the promised intros, then schedule a call with Dana + Tomer on next steps (2026-06-28).
- [ ] Tomer: email Noam + Dana intros to medtech AI startups + data-acquisition managers (re: the subscription model).
- [ ] Team: interview those contacts to validate provider friction + market demand; refine the "cable" concept from feedback.

## Decisions
- _none yet — the "cable" subscription model + niche on new pathology stains (IHC) is the current leaning, not a committed decision; viability still hinges on the two unknowns above._

## Notes
- Sources: [[Meetings/2026-06-18 - Impromptu Google Meet Meeting (156210341)]], [[Meetings/2026-06-28 - Impromptu Google Meet Meeting (158840046)]].
- ❓ **Who is Dana?** The only Dana in the vault is [[dafne-bennatan|Dana Gerichter]] (RFS Global candidate, building an AI ops platform "Second Desk") — a different domain. This Dana has hands-on medical-data-acquisition experience. Unconfirmed whether same person; see also the [[biliyo]] Dana. Do not merge until Noam confirms. ^[ambiguous]
- ⚠️ The earlier (06-18) note flagged a "Noam's father vs Dana's father" ambiguity. New data (06-28): **Tomer (Noam's father)** is providing intros to medtech AI startups + data-acquisition managers — so Tomer does have relevant medtech contacts and is now active on this venture. This doesn't confirm Tomer is the "medical-industry expert father" from 06-18 (that may still be Dana's father); both can be true. ^[ambiguous]
