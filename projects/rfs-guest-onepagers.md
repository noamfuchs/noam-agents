---
name: Run For Startups Guest One-Pagers
status: active
goal: "Briefing one-pager PDFs sent to the RFS runners community before meeting each new guest"
started: 2026-06-03
---

# Run For Startups Guest One-Pagers

**Goal:** A single-page briefing PDF the Run For Startups community sends out before meeting a new guest (founders, VCs, investors).
**Tool:** the `guest-one-pager` skill at `~/.claude/skills/guest-one-pager/`.
**How to trigger:** give the skill a guest **name** + (usually) **LinkedIn / company URL**. It researches the guest, finds a photo, and renders an A4 PDF into `~/Downloads/`.

## Workflow (summary - full version in the skill's SKILL.md)
1. **Research** with WebSearch + WebFetch (English + Hebrew + company). Gather role, career, exits/IPOs/funding, education, niche personal details, fund facts (AUM, check size, focus, portfolio), and 4-6 strong links. LinkedIn is usually auth-walled - rely on search snippets + company team page + news, but still link the profile.
2. **Headshot** - best from the company team page; save to the skill's `tmp/`. No photo → builder draws a neon initials badge.
3. **Write tight** (one page): `role` (one line, two clauses split by ` | `), `background` (5-6 bullets, `<b>` key facts), `questions` (3-4 sharp, tailored), `links` (about 5).
4. **Build:** `python3 ~/.claude/skills/guest-one-pager/build_one_pager.py <guest.json>` (output to `~/Downloads/<Full Name>.pdf`).
5. **Verify:** script prints `pages: 1` + link count. Trim until single page. Read the PDF back.

## Style rules (Noam cares)
- **No em dashes (-).** Natural sentences, periods/commas. No `~` for "about". Compound hyphens (defense-tech) are fine. See [[preferences]].
- Plain factual tone, no hype. Default English (LTR); Hebrew via `"rtl": true`.

## Brand (baked into the builder)
- Background charcoal `#0C0F0B` with faint green-tinted gradient. Accent neon green `#CCFF00`. Text near-white `#f2f3ef`. Font Heebo. Logo `assets/logo.jpeg` (blended). Reference color source: run-for-startups.base44.app.

## Pages produced
- **Sarel Eldor** (Key1 Capital) - first page, the reference for all future ones. `~/Downloads/Sarel Eldor.pdf`. See [[sarel-eldor]].

## Related
- [[adam-teer-run-for-startups]] - community owner.
- RFS mentor-shortlist web page generator (separate tool) - see [[rfs-mentor-shortlist]].
