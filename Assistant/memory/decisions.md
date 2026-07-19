---
name: Decisions
description: Decisions Noam has made, with date and reasoning. Searched by decision-recall skill when a similar question comes up.
updated: 2026-07-19
---

# Decisions

_Format: each decision is a level-2 heading with date and reasoning. Add new ones at the top._

## 2026-07-19 — RFS Global team restructure for expansion
**Decision:** Restructure the RFS Global leadership for expansion: **[[arad-fruchter|Arad]]** moves out of the 3-person leadership arrangement into a **focused, project-based role** — Noam will speak with him to define it (per [[dafne-bennatan|Dafne]]'s advice, first prompt [[adam-teer-run-for-startups|Adam]], who brought Arad in, to talk to him). **Elinor** leads NY collaborations (local presence, proactive sourcing — e.g., found a runner with 10k followers). **Mika + Eitan** lead the new Israel group launching early October.
**Why:** A 3-person leadership team is inefficient for decision-making, and Arad's undefined role had become a bottleneck (e.g., delayed forming the Mika/Eitan group). A defined, focused role leverages his engagement while unblocking expansion. See [[rfs-global]]. From [[Meetings/2026-07-19 - Impromptu Zoom Meeting (165053320)]].

## 2026-06-28 — RFS Global takes social-media editing in-house, with defined content roles
**Decision:** The RFS Global team takes over Instagram **video editing** from Dana (who keeps Stories + community engagement), standardizing on a reusable video template (intro/middle/outro) and ≥2 Reels/week. Content roles are split: **[[dafne-bennatan|Dafne]] → Instagram Stories**, **Noam + [[arad-fruchter|Arad]] → Instagram/LinkedIn posts**. A dedicated LinkedIn page launches alongside Instagram.
**Why:** Dana's edits followed a different aesthetic vision, causing constant revisions and team friction; she felt her work wasn't appreciated. Defining clear roles ensures brand consistency, removes the feedback-loop friction, and frees Dana for the work she's best placed to own. See [[rfs-global]]. From the 2026-06-28 social-strategy sessions [[Meetings/2026-06-28 - Impromptu Google Meet Meeting (158846476)]] + [[Meetings/2026-06-28 - Impromptu Google Meet Meeting (158848973)]].

## 2026-06-22 — RFS website MVP built from scratch by a dedicated dev team
**Decision:** Build the new RFS website MVP **from scratch** with a dedicated two-developer team ([[etay-zaslavsky|Etay Zaslavsky]] + [[yuval-klein|Yuval Klein]], overseen by [[yonatan-buntzel|Yonatan]]); **reject** piloting on Noam's existing Vercel prototype. MVP scope = onboarding/auth + group management/permissions + CEO directory/contact (mentoring out of scope). Architecture = backend/frontend separation in a monorepo, so a native app can later replace the web UI without rebuilding core logic.
**Why:** The prototype's backend logic is unknown and its UX isn't polished enough for the core CEO-connection flow; the team's recurring failure mode has been rebuilding projects twice on weak foundations. Building fresh on a clean, scalable foundation is worth the extra time. Dev is blocked until Noam + Yonatan deliver user stories + wireframes (due 2026-06-23). See [[rfs-platform]]. From 2026-06-22 kickoff [[Meetings/2026-06-22 - התנעת אתר RFS (157161442)]].

## 2026-06-16 — RFS guest policy (2–4 max, observe-only)
**Decision:** Limit guests across all Run For Startups groups to **2–4 per session**; guests must **observe, not lead/dominate** the conversation, register via a **Manda link**, and are **not** provided coffee.
**Why:** Guests were monopolizing the CEO's attention and making core members feel ignored and disengaged. The policy protects group intimacy and keeps the CEO's focus on the core members. Finalization of the exact per-group cap is owned by Adam. See [[rfs-global]]. From 2026-06-16 leadership sync [[Meetings/2026-06-16 - Impromptu Google Meet Meeting (155349341)]].

## 2026-06-16 — Mandatory structured format for group-only meetings
**Decision:** All group-only meetings (no CEO present) must use a **mandatory structured format** with timed activities (e.g. 1-min intros, "speed dating").
**Why:** Unstructured group-only meetings fail — a few members monopolize time and the rest disengage. A ready-to-use plan ensures equitable participation and removes last-minute prep. See [[rfs-global]]. From 2026-06-16 leadership sync [[Meetings/2026-06-16 - Impromptu Google Meet Meeting (155349341)]].

## 2026-06-16 — Noam + Dafne proactively lead RFS Global expansion (NY first)
**Decision:** Noam and [[dafne-bennatan]] take the initiative on Run For Startups' global expansion — starting with a **New York** group (targeting a firm launch date, ~September) and later Miami — positioning themselves as the de facto leaders of global expansion. Supporting moves: elevate speakers from "filler" to high-impact founders/CEOs; build a distinct "RFS Global" brand (unique colors/shirts); pursue NY sponsorship via Or Segal (Base44); recruit using Taglit Excel alumni as ambassadors.
**Why:** The org is decentralized with no formal command center, and Adam is pushing rapid expansion but lacks capacity to execute on all fronts. Demonstrating initiative lets Noam + Dafne establish a clear center of control. See [[rfs-global]]. From 2026-06-16 strategy meeting [[Meetings/2026-06-16 - Impromptu Google Meet Meeting (155364484)]].

## 2026-06-15 — Back Dafne's push for more team autonomy (RFS Global)
**Decision:** Support [[dafne-bennatan]]'s push for greater autonomy in running RFS Global, rather than keeping decisions tightly centralized.
**Why:** Noam views the autonomy as a positive driver for engagement and progress; the recent event validated the approach — it ignited passion for the project and clarified team dynamics. See [[rfs-global]].

## 2026-06-11 — RFS platform: testing-first, split by role and device
**Decision:** Bug discovery takes priority over new features. Testing is split by permission level and device: Noam tests exclusively as a mobile "community member", Yonatan as a desktop "C-suite" user (highest permissions). All bugs and improvement suggestions go into a shared Notion table — the single source of truth — preferably via the in-app bug reporter (auto page/device context). Dev access opens via Ori's setup package + Claude/Codex prompt (due Sunday 2026-06-14); parallel development must be coordinated to avoid conflicts.
**Why:** Role/device split gives comprehensive coverage across permission levels; centralized Notion tracking prevents lost reports; bugs-first protects the release. See [[rfs-platform]].

## 2026-06-08 — RFS speaker pipeline shifts to founders
**Decision:** Re-weight the Run For Startups speaker pipeline away from VCs and toward founders/entrepreneurs. Active leads: Sari Hillel (Descartes AI), Sagi Schleisser (Crazy Labs), a ServiceNow-exit ($80M) founder via Arad, a $116M-exit founder (Arad's stepfather), Greg Kinross.
**Why:** The current pipeline is VC-heavy; founders are more relatable and valuable for the runners. See [[rfs-global]].

## 2026-06-08 — RFS run-safety / war-alarm protocol
**Decision:** Standing protocol for runs during alarms — 1 alarm → run as planned; 2 alarms → start 07:00; 3 alarms → cancel. Plus a Google Map of the route with shelter locations and close 1:1 contact with each runner.
**Why:** A previous conflict caused heavy attrition (12 of 20 runners left). Clear rules + reassurance protect safety and group cohesion. See [[rfs-global]].

## 2026-06-08 — RFS standardized weekly operations
**Decision:** [[lev-wolf]] leads program management across all RFS groups, with a recurring 15-min weekly management sync and a mandatory weekly checklist (speaker outreach 2–3 weeks ahead, fixed member-comms cadence, post-meeting summary + speaker follow-up + content to Adam) standardizing every group.
**Why:** Earlier groups treated programs as one-off events, causing inconsistency and low community conversion. Standardization ensures continuity and a community-first experience. See [[rfs-global]].

## 2026-06-07 — RFS platform: two-tier UX + scope
**Decision:** The RFS web platform expands from an internal-only CEO pipeline to a member-facing product (public CEO directory + meeting calendar + internal pipeline). Two tiers: members get a clean public directory with only a simplified status (coming-soon + binary "in pipeline" to prevent duplicate outreach), managers get the full internal pipeline. The application/onboarding pipeline is deferred.
**Why:** A standalone pipeline offers members little value; a directory + calendar drives adoption, while hiding internal labels keeps the public view professional. Deferring onboarding protects the deadline. See [[rfs-platform]].

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

## 2026-06-07 — Instagram personal brand
**Decision:** Grow personal IG from 1,030 → 5,000 by 2027-06. Personal brand (not a topic page), Hebrew-first (English from ~m9), reach-now/monetize-later. Lead with the cross-cultural relationship pillar as the virality engine; 5 pillars total, 2 reels/week (Tue + Motzash). Full plan in [[instagram-growth]].
**Why:** 0→1k already cleared (hardest part). Multi-topic brand needs one spine; the relationship angle is the unfair, high-reach differentiator. Test all pillars for 8 weeks, let shares/saves/follows pick the 2 to scale.
