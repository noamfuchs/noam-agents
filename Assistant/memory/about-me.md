---
name: About Me
description: Identity, situation, role, active projects, backstory. Expanded 2026-06-12 from Noam's own documents (levelup Phase 1). "(confirm?)" tags mark inferences.
updated: 2026-06-12
---

# About Me

## Identity
- **Name:** Noam Fuchs (נעם פוקס)
- **Preferred name:** Noam
- **Born:** 2000-04-08 (Facebook export)
- **Email:** fooxsound@gmail.com
- **Nationality:** Israeli
- **Location:** Herzliya (מגורים במעונות רייכמן)
- **Timezone:** Asia/Jerusalem
- **WhatsApp (business):** +972 55-932-2359 — REA business line only.
- **WhatsApp (personal):** +972 52-644-8875 (Facebook export 2014 + the CRM test-lead note) ^[inferred]

## Education / current studies
- **University:** Reichman University (IDC)
- **School:** Adelson School of Entrepreneurship
- **Degree:** B.A. Economics
- **Status:** Semester 2 of academic year 2026 — 9 courses (mix of economics core, math/stats, R / data science, Gen AI, entrepreneurship)
- **State:** in catch-up mode after a trip; tracking through `Dropbox/IDC/SEM 2/MY SEM 2 COACH/STATUS.md` (the `sem2-coach` Claude project).

## Languages
- **Native:** Hebrew
- **English:** C1 (CV)
- **French:** A2, learned in Geneva 2023-2024 (CV)
- **Default for Claude/technical work:** English (per his explicit preference in sem2-coach + REA CRM contexts)
- **Default on Telegram bot:** match his message — Hebrew in → Hebrew out, English in → English out (he mixes freely mid-message)
- **Outbound to others:** Hebrew for Israeli contacts; English otherwise.

## Backstory (full arc in [[story]], goals in [[goals]])
- Grew up in Tamra (Wadi Ara) then Zikhron Yaakov; homeschooled grades 3-8; left school at 16 for the music industry.
- **FUCHS-SOUND** (founded 2020-09): producer, keyboardist, live-show programmer for top Israeli artists (Static, Ivri Lider, Ninet Tayeb, Noa Kirel and more; see [[music]]). Rimon school 2018, SAE Institute 2022.
- Lived: Tamra → Zikhron Yaakov → Tel Aviv loft (2021-2023) → Geneva (Oct 2023, ~10 months, war period, relatives Constantine and [[camilla]]) → Herzliya dorms.
- Bagrut completed May 2024 in 5 months, GPA 96. Accepted to Ben Gurion, Technion, Reichman; chose Reichman.
- OD SIFRA (2025-05 to 2025-11): investor relations in US residential real estate; the bridge to REA. ^[inferred]
- Family: mother **Tal** [[mom]], father **Tomer** [[paps]] (names confirmed 2026-06-12), brothers [[ran]] (Ran Fuchs, closest confidant) and [[shai-my-brother]] (eldest, partner Avital), sister [[hila-my-sister]] (in army); cousins [[tom-fox]] and Jonathan Fuchs; Geneva relatives Constantine and [[camilla]]. Note: [[babi]] is a business partner (appraiser), not family.

## Role / what he does
- **Entrepreneur & operations** — running a real-estate education business with two partners.
- **Coordinator / producer** of the online course product (not the speaker, not the investor himself).
- **Owner of the CRM build** for the same business (REA = Real Estate Academy).
- **Student** (alongside the business).

## Life situation
- **Partner:** Qiu Qiqian — סינית מצ'נגדו, בת 23, סטודנטית להנדסת מכונות (B.Sc) + הנדסת אוויר (M.Sc) בטכניון, על מלגה. סופר חכמה.
- **מגורים משותפים:** מעונות רייכמן יחד.
- **מורכבויות:** פערי תרבות ושפה בזוגיות.

## Active projects (cross-referenced)
- **Real Estate Course** — 12-chapter Hebrew online course for Israeli investors, on US real estate investing (fix-and-flip, rehab, long-term rentals). Speaker: Amit Shalfar. Partner: Itay Liani. Chapters 1–3 done; 4 next. See `projects/real-estate-course.md`.
- **REA CRM** — custom Next.js + Supabase + Vercel CRM replacing Base44, GoHighLevel-style, going to real production. WhatsApp Cloud API for messaging, BoldSign for contracts, Calendly for appointments. Code at `~/Documents/code_projacts/REA/crm-rea`. Pipeline + automations + KPI dashboard scoped. _(See `projects/crm-rea.md`.)_
- **Webinar Signup Bot** — pipeline for webinar registrations at `~/Dropbox/CLAUDE CODE`.
- **Personal assistant (this)** — Telegram bot **@Noam_brain_bot, RUNNING and REWIRED 2026-06-12**: every message now runs `claude -p` (sonnet) with cwd = this vault, so the vault CLAUDE.md governs the bot too (hot-first reads, capture protocol, outbox drafts, provenance, mirror-language; the old English-only rule is retired). Voice notes auto-detect language now (was locked to English). It cannot send WhatsApp messages anymore: drafts go to outbox/ + shown in chat. Replies take ~15-30s (claude -p startup) by design: one brain, zero drift. Launchd agent `com.user.brain-bot`, codebase at `~/Documents/code_projacts/my personal assistent/` (old API-agent brain retired; ANTHROPIC_API_KEY stripped from the subprocess so it runs on the subscription). Network note: Mac often on iPhone hotspot; bot now backs off exponentially instead of log-flooding. The OLD label `com.user.secondbrain.bot` and the Fly.io cloud bot remain retired.
- **Studies** — `sem2-coach` Claude project tracks 9 IDC courses, syllabi, deadlines.

## People in active rotation
- **Amit Shalfar** — real estate course speaker; REA CRM marketing. See `people/amit-schleffer.md`.
- **Itay Liani** — real estate course partner; REA CRM sales (works from Costa Rica, calls Israeli leads via WhatsApp). See `people/itay-liani.md`.
- **Qiu Qiqian** — בת זוג, סינית, טכניון, מעונות רייכמן.

## Channels he uses to talk to me
- **Telegram bot** (_currently inactive_ — previously the primary mobile channel via launchd on the Mac; not running right now).
- **Claude Code on the Mac** in each project directory (CRM_REA, sem2-coach, real-estate course, etc.).
- **Obsidian Mobile** for vault reads (no two-way conversation there — read/write notes only).
