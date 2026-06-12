---
name: RFS Platform
status: active
goal: "Web platform for Run For Startups: CEO directory + meeting calendar + internal CEO pipeline"
started: 2026-06
---

# RFS Platform

**Goal:** A web platform serving all Run For Startups groups — expanded beyond the original internal CEO pipeline to drive member adoption.
**Lead developer:** [[ori-rozental]] (building the core infrastructure). Noam joins via Git for feature work once the foundation is stable.
**Origin:** Scope was deliberately widened from a standalone manager pipeline (low value to members) to a member-facing product. See [[rfs-global]], [[adam-teer-run-for-startups]].

## Three core surfaces
- **CEO Search** — public, clean directory of CEO profiles for community members to browse and connect. CEOs self-edit their profile (incl. "what I'm looking for", e.g. "Data Analyst") so members can search by need. Contact-info privacy is per-CEO (public, or route through an assigned contact person).
- **Meeting Calendar** — central hub for group + community-wide schedules. Members propose CEOs; managers approve/schedule. Group-specific manager dashboards (members, meeting history, future plans).
- **CEO Pipeline** — the original internal manager tool for tracking outreach.

## Two-tier UX (decided 2026-06-07)
- **Members:** clean public directory; a simplified public status only — a "Coming Soon" category for CEOs with upcoming meetings, and a binary "already in pipeline / not" signal on search to prevent duplicate outreach **without** exposing internal labels like "Not Relevant".
- **Managers/owners:** full internal pipeline + per-group dashboards.
- **Out of scope (for now):** the application/onboarding pipeline — deferred to protect the deadline.

## Testing phase (kicked off 2026-06-11)
Ori demoed the system; bug discovery now takes priority over new features.
- **Split by role + device:** Noam tests exclusively as a mobile "community member"; Yonatan as a desktop "C-suite" user (highest permissions).
- **Reporting:** shared Notion table is the single source of truth; prefer the in-app bug reporter (auto page/device context). Verbal reports must include page, device, screenshot.
- **Noam's angle:** use Claude to automate bug discovery; once dev access lands, explore a major UX/UI overhaul.
- **Known bugs from the demo:** meeting counter shows "011" on all group cards; calendar color picker opens off-screen; CEO profile card UI is poor and fields aren't editable; CEO photo auto-pull from LinkedIn needs a fallback; overall UI/UX unpolished, copy needs work (e.g. "הערות התמה").

## Dev access & data import (2026-06-11)
- **Dev access:** Ori delivers a setup package + Claude/Codex prompt by Sunday 2026-06-14 — automates local env setup (Git, dependencies) for development on personal machines. Constraint: parallel dev work must be coordinated to avoid conflicts.
- **Bulk data import:** system will support imports to populate historical CEO data from Excel, onboard members from application forms, and parse one-pagers to auto-fill CEO profiles. Yonatan + Noam to provide the master community member list with emails for account pre-population.

## Timeline
- **2026-06-11:** demo done; testing phase begins (roles above).
- **By Sunday 2026-06-14:** Ori delivers the dev setup package; accounts activated for Noam & Yonatan.
- Tokens funded by the team as needed to avoid dev bottlenecks.

## Landing page overhaul
Current page is a placeholder. Goal: a professional one-pager that tells the RFS story, works as a partner asset, and serves as an application portal.
- **Yonatan** → draft copy for team review by Tuesday, then sync with Adam.
- **Adam** → compile high-res photos/videos from past events, send to Noam.
- **Noam** → build the page with approved copy + visuals once received.

## Open items
- [ ] Ori: share the Notion bug/improvement table; activate Noam & Yonatan's accounts + grant roles; dev setup package + Claude/Codex prompt by Sunday 2026-06-14.
- [ ] Ori: contact-owner assignment + reassignment for group managers; LinkedIn + photo on CEO profiles; "Suggest a CEO" form with duplicate check → then coming-soon + binary status; profile visibility/privacy controls; calendar view → group-specific views + coffee/attendance tools.
- [ ] Yonatan: send Ori a written summary of the proposed features/changes.
- [ ] Yonatan + Noam: test per assigned roles, log everything to the Notion table; send Ori the master community member list with emails.
- [ ] Noam: send Ori the accepted Global application form; send the one-pager to the team (ping Yonatan if no reply); update the landing page once copy + assets land.
- [ ] Draft site spec (owner TBD — from 2026-06-11 action items).

## Decisions
- 2026-06-11 — Testing-first: bugs over features; testing split by role/device (Noam mobile-member, Yonatan desktop-C-suite); Notion table as single source of truth.
- 2026-06-07 — Widened scope from internal-only pipeline to a member-facing product (CEO directory + calendar) to drive adoption.
- 2026-06-07 — Two-tier UX: public simplified directory for members, full internal pipeline for managers; onboarding pipeline deferred.
