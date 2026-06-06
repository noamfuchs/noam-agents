---
name: Decisions
description: Decisions Noam has made, with date and reasoning. Searched by decision-recall skill when a similar question comes up.
updated: 2026-05-04
---

# Decisions

_Format: each decision is a level-2 heading with date and reasoning. Add new ones at the top._

## 2026-06-04 — RFS Global gets its own brand
**Decision:** The English-speaking RFS Global cohort gets a distinct brand: a new `@RFSGlobal` Instagram account and `rfs.global@gmail.com`, using Instagram Collabs with the main RFS account to borrow its audience.
**Why:** A separate English-language identity for the international/olim cohort, kept distinct from the Hebrew RFS brand. See [[rfs-global]].

## 2026-06-04 — Accepted Zak Feingold into RFS Global
**Decision:** Admit Zak Feingold to the first RFS Global cohort.
**Why:** Strong profile — CS student at Reichman (ASEG scholar), running a service-delivery startup with his brother, founding a university robotics club. Good fit and energy for the global group.

## 2026-06-02 — Real Estate Academy ad-campaign strategy
**Decision:** Target audience = people who want US real estate as a *primary income / career change* (not a side hustle). Creative approach = one core video + 5 hooks, combined into 5 distinct test creatives; Amit films on Sundays.
**Why:** Sharper positioning for higher-intent buyers, and a cheap way to test multiple angles fast. Run by [[neria-ogen]]; see [[real-estate-course]].

## 2026-05-04 — Brain location
**Decision:** Personal assistant lives inside the existing Obsidian vault at `~/Desktop/MY BRAIN/`, not a parallel `~/second-brain/`.
**Why:** Existing PARA Obsidian vault has the daily-journal habit and `.git`. Splitting into two trees would kill the journal habit. `~/second-brain` is a symlink to the vault for spec compatibility.

## 2026-05-04 — Removed Tom Even's ABC-TOM system
**Decision:** Archived `the-system-v8 2/` (ABC-TOM AI Agent Team by Tom Even) to `.archive/`. Building Noam's own assistant from scratch instead.
**Why:** Noam doesn't need someone else's framework — wants his own system tailored to his workflows.
**Reversible:** Files preserved in `.archive/the-system-v8 2/` until Noam confirms full deletion.

## 2026-05-04 — Reply language
**Decision:** Auto-match the message language. Hebrew in → Hebrew out. English in → English out.
**Why:** Noam works primarily in Hebrew. Forced English replies would feel foreign.
**Constraint:** Filenames, folder names, frontmatter, shell-touched fields stay English regardless.

## 2026-05-04 — Backup approach
**Decision:** Time Machine to external drive (covers vault). Brain pushed to private GitHub weekly (vault excluded).
**Why:** Spec excludes vault from GitHub backup; Mac failure would lose vault. Time Machine restores everything including the encrypted vault.

## 2026-05-04 — FileVault
**Decision:** Enable as Phase -1 (background). Required before Phase 9 vault import.
**Why:** Vault holds passport/financial scans. FileVault is the at-rest encryption that makes that acceptable.
