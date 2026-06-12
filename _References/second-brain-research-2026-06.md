---
name: Second Brain Research (June 2026)
description: Verified findings on Obsidian + Claude Code second-brain best practices. 21 sources, 25 claims adversarially verified (24 confirmed, 1 refuted).
updated: 2026-06-12
---

# Second Brain Research, June 2026

Deep-research run for [[second-brain-levelup]]. Each claim below survived 3-skeptic adversarial verification.

## The reference architecture: Karpathy's "LLM wiki"
The dominant 2025-2026 pattern (Karpathy gist, Apr 2026). Three layers with strict boundaries:
1. **Raw sources, immutable.** The agent reads them, never edits them. They are the source of truth.
2. **The wiki (this vault).** The agent writes it, the human reads it. Distilled, interlinked, compounding.
3. **The schema (CLAUDE.md).** Conventions and workflows. A router that points, not a store.

Key idea: synthesis happens at INGEST time (cross-references and contradictions flagged when data arrives), not at query time. Source: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

## Navigation that controls token cost (high confidence)
- **hot.md**: ~500-word recent-context cache, refreshed each session
- **index layer**: every page with a one-line summary (our [[HOME]] + hubs play this role)
- **log.md**: append-only chronological record, newest on top
- Read order: hot, then index, then drill into specific pages. Never load the whole vault.
- Reference implementations: claude-obsidian (6.6k stars) and obsidian-wiki (1.8k stars), both Apr 2026, both "Obsidian is the viewer, the LLM is the maintainer".

## Provenance tags (high confidence)
Every claim a pipeline writes into the wiki gets tagged: **extracted** (default, from source), **^[inferred]** (LLM synthesis), **^[ambiguous]** (sources disagree). Plus a periodic lint pass for contradictions, stale claims, and missing cross-references. This is prompt-enforced convention, not a guarantee.

## CLAUDE.md consensus (high confidence)
Write it first, treat it as an API contract, keep it short (under ~300-500 lines; Anthropic warns bloated files get ignored). It can live at multiple levels (root + per-folder). Cross-project pattern: OTHER repos' CLAUDE.md files point at the vault with the hot-then-index read protocol, so every Claude session shares one knowledge base.

## Structure (high confidence)
No single methodology wins. Documented working setups are hybrids (PARA + Zettelkasten + MOC hubs), folders only for project-specific material, wikilinks for everything else. The one claim refuted in verification was a rigid prescriptive folder taxonomy. Conclusion: do NOT reorganize folders wholesale.

## Cadence (medium confidence, Herk's AIS-OS)
Order is Context, Connections, Capabilities, Cadence, and Cadence is LAST: "don't automate workflows that don't work manually." His kit ships exactly three skills: /onboard (day 1 interview), /audit (weekly lint), /level-up (weekly improvement review).

## Tooling (high confidence)
Claude Code needs no MCP server or Obsidian plugin for vault work; it operates on plain markdown directly. Emerging retrieval pattern: qmd by Tobi Lütke (BM25 + vector + LLM re-ranking, fully local, official Claude Code plugin, 26.4k stars) plus the official Obsidian CLI.

## Cautions and open questions
- The whole ecosystem is months old; star counts signal interest, not proven long-term use.
- Critics warn the wiki pattern may degrade past ~1,000 files or 50-100k-token indexes. Keep hot and index lean.
- The field has NO verified answers on privacy practices for feeding personal chats to agents, nor on how deep to distill chat threads. Our own tier design stands.
- Heuristic numbers (500-word hot, 300-500-line CLAUDE.md) are author rules of thumb, not measurements.

## Sources (main)
Karpathy gist · github.com/AgriciDaniel/claude-obsidian · github.com/Ar9av/obsidian-wiki · github.com/nateherkai/AIS-OS · kennethreitz.org (vaults + Claude Code essay) · stefanimhoff.de (6,000-note agentic vault) · noahvnct.substack.com · pasqualepillitteri.it · github.com/tobi/qmd · MemGPT/Letta + Mem0 (tiered agent memory)
