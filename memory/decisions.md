---
name: Decisions
description: Decisions Noam has made, with date and reasoning. Searched by decision-recall skill when a similar question comes up.
updated: 2026-05-04
---

# Decisions

_Format: each decision is a level-2 heading with date and reasoning. Add new ones at the top._

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
