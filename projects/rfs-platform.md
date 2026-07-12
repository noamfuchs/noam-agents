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

## Noam's prototype + build decision (2026-06-21)
Noam built a **functional admin-dashboard prototype** with ~15 AI prompts and demoed it (to [[people/yonatan-buntzel|Yonatan Buntzel]]) to prove the core logic is sound. Features shown:
- **Group & session management** — create recurring session series (e.g. 12 weekly sessions), each with its own coffee-order link.
- **Member networking** — a "Networking" link populates a community directory of member profiles (LinkedIn, Instagram, etc.).
- **CRM pipeline** — simple member-status tracking (e.g. "Hosted").
- **Calendar** — visualizes all group sessions, pulling guest data from the CRM pipeline.

**Open strategic decision (NOT yet decided):** use the prototype as a *temporary data-gathering tool* (ship fast, deliver value now while a pro version is built — risk: not professional/scalable) **vs.** as a *blueprint for a professional build* (leverage the proven logic — risk: a pro dev may dismiss it as "vibe code" and start from scratch). The core challenge is delivering member value, which needs a digital platform for networking + event registration.

**Developer candidate — Yuval (Five Fingers app):** built the "Five Fingers" app (now being sold to other sports events — proven he can build + monetize a robust platform); has offered ~3–4 hrs/day. Candidate for the professional build. ⚠️ Not the same person as [[people/yuval-avramov]] (travel friend) — surname/contact TBD; no person file yet.

**Path forward:** Noam refines the prototype (member-facing value first); a **2026-06-22 21:00 Zoom with Yuval + Yonatan** decides the development strategy.

> Note: this is Noam's own AI-built prototype, distinct from [[ori-rozental]]'s core platform build above — the 06-22 meeting is partly about which becomes the basis for the professional product. ^[inferred]

## RFS website MVP kickoff — new dev team (2026-06-22)
Project kickoff for the new RFS website, with a dedicated two-developer team. Attendees: [[people/yonatan-buntzel|Yonatan Buntzel]], [[people/etay-zaslavsky|Etay Zaslavsky]], [[people/yuval-klein|Yuval Klein]], Noam. From [[Meetings/2026-06-22 - התנעת אתר RFS (157161442)]].

**Strategic decision resolved (the open question above):** the team **rejected** using Noam's Vercel prototype for a pilot and will **build the MVP from scratch** — the prototype's backend logic is unknown and its UX isn't polished enough for the core CEO-connection flow; building fresh avoids technical debt and gives a clean, scalable foundation (the recurring failure mode has been rebuilding projects twice on weak foundations).

- **MVP scope (in):** user onboarding & auth; group management & permissions; CEO directory + contact functionality.
- **MVP scope (out):** mentoring features — explicitly deferred.
- **Architecture:** backend/frontend separation in a **monorepo** (server + UI), chosen so the web UI can later be swapped for a native app without rebuilding the core logic. UI for internal roles (group managers) stays simple/functional, not polished; effort goes to end-user value (runners, CEOs).
- **Roles:** Yonatan — oversight, logistics, unblocking. Noam — technical guidance, UX/UI input, writes user stories (with Yonatan). Etay + Yuval — backend/frontend dev (split internally, report their plan). **Rotem (Base44)** — branding + UI design, starts in parallel once brand language + wireframes exist.
- **Process:** dev is **blocked** until Yonatan + Noam deliver user stories + wireframes (deadline 2026-06-23); async work with a 10-min weekly WhatsApp sync.

> ⚠️ Relationship to [[ori-rozental]]'s build is now unclear: the 06-22 kickoff stood up a fresh Etay+Yuval team building from scratch and did not mention Ori. Whether this replaces, forks from, or runs parallel to Ori's earlier core-platform effort is unconfirmed. ^[ambiguous]

## Open items
- [ ] Noam: refine the prototype — add group-specific registration links, then a group-level member view; focus on member-facing value (from 2026-06-21).
- [ ] Noam: send the 2026-06-22 21:00 Zoom invite to Yuval + Yonatan, and a coffee invite to Yonatan for 2026-06-22.
- [ ] Ori: share the Notion bug/improvement table; activate Noam & Yonatan's accounts + grant roles; dev setup package + Claude/Codex prompt by Sunday 2026-06-14.
- [ ] Ori: contact-owner assignment + reassignment for group managers; LinkedIn + photo on CEO profiles; "Suggest a CEO" form with duplicate check → then coming-soon + binary status; profile visibility/privacy controls; calendar view → group-specific views + coffee/attendance tools.
- [ ] Yonatan: send Ori a written summary of the proposed features/changes.
- [ ] Yonatan + Noam: test per assigned roles, log everything to the Notion table; send Ori the master community member list with emails.
- [ ] Noam: send Ori the accepted Global application form; send the one-pager to the team (ping Yonatan if no reply); update the landing page once copy + assets land.
- [ ] Draft site spec (owner TBD — from 2026-06-11 action items).
- [ ] Noam + Yonatan: deliver the MVP user stories + wireframes to Etay + Yuval by 2026-06-23 (dev is blocked on this) — from 2026-06-22 kickoff.
- [ ] Etay + Yuval: define MVP architecture (monorepo, server/UI split) + user types/roles + permissions; share with Yonatan + Noam by 2026-06-23.
- [ ] Yonatan: schedule the recurring 10-min weekly WhatsApp sync (Etay, Yuval, Noam).

## Decisions
- 2026-06-22 — Build the RFS website MVP **from scratch** with a dedicated dev team (Etay + Yuval); rejected piloting on Noam's Vercel prototype (unknown backend logic, unpolished UX) to avoid technical debt. Resolves the open prototype-vs-pro-build question.
- 2026-06-22 — MVP scope: onboarding/auth, group management/permissions, CEO directory + contact; mentoring features out of scope.
- 2026-06-22 — Architecture: backend/frontend separation in a monorepo, to allow a future native app without rebuilding core logic.
- 2026-06-11 — Testing-first: bugs over features; testing split by role/device (Noam mobile-member, Yonatan desktop-C-suite); Notion table as single source of truth.
- 2026-06-07 — Widened scope from internal-only pipeline to a member-facing product (CEO directory + calendar) to drive adoption.
- 2026-06-07 — Two-tier UX: public simplified directory for members, full internal pipeline for managers; onboarding pipeline deferred.
