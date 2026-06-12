---
name: REA CRM
status: active
goal: "Custom production CRM (GoHighLevel-style) replacing Base44 for Real Estate Academy"
started: 2026-04
---

# REA CRM

**Goal:** Custom production CRM replacing Base44, fully owned, cheap-to-operate, tailored to REA's real-estate training sales process.
**Code:** `~/Documents/code_projacts/REA/crm-rea/` (lowercase-hyphen — the empty `CRM_REA/` folder is a trap, ignore it).
**Status:** active build; canonical state in `docs/STATUS.md` inside the repo.

## Stack
Next.js (App Router) + Supabase + Tailwind + shadcn/ui + Vercel. WhatsApp Cloud API (Meta) for messaging. BoldSign for contracts. Calendly for appointments. Claude API for AI agent (Phase 5, later). Facebook Ads API as infra placeholder.

## Team (3 users, equal permissions)
- **Noam** — Operations (project owner)
- **Itay Liani** — Sales (Costa Rica; WhatsApp calls to Israeli leads)
- **Amit Shalfar** — Marketing (FB Ads when he starts spending)

## WhatsApp business
- Phone: +972 55-932-2359
- Phone Number ID: 1008458015694018
- WABA ID: 1312872774242392
- Verify token: rea_webhook_2026
- App: Rea-API. Token = rea-bot system user token (regenerate from business.facebook.com → System Users → rea-bot).

## Pipeline
New Lead → Unreplied → Replied → Appointment Booked → Follow Up → Contract Sent → Paid → Irrelevant.
Parallel tags: Cold Lead, Warm Lead, Hot Lead, Closed With Someone Else.

## Lead fields
Full name, source, tag, call count, message count, current pipeline stage, amount paid, payment date, plan type (1 / 3 payments), payment method (bank transfer / card). NO ID number field.

## Lead sources
Facebook, Instagram Organic (Stories), Web Form, Webinar, Referral, WhatsApp Group, Manual Entry.

## Automations (Hebrew drips, business hours 08:00–22:00 Asia/Jerusalem)
- New lead → immediate welcome → Unreplied
- Unreplied: same day, next day, +3 days, weekly → after 2 weeks no reply → Cold Lead → monthly
- Cold: monthly | Warm: every 12 days | Hot: every 5 days
- Stop instantly when a lead replies.

## Disqualification reasons
No money, No time, Not serious, Fear, Wants to think, Doesn't understand the investment, Found another solution, Doesn't fit profile, Closed with someone else, Other.

## KPI dashboard
Leads (total/net/by source), Quality (Cold/Warm/Hot), Activity (calls, messages, averages), Sales (contracts, paid, conversion), Marketing (CPL/CPC/CPA — placeholders until FB Ads on), Financial (revenue, avg deal, ROI per source), Monthly trends.

## UI rules (DO NOT REVERT)
Dark theme (slate/zinc). Temperature emojis everywhere (🔥/🌡️/❄️). Lead cards with gradient + colored avatar. WhatsApp-green Quick Chat button. Source pills in brand colors. Automation nodes with WhatsApp bubble previews + big duration numbers + YES/NO branches + radial-gradient canvas. shadcn/ui, rounded-2xl, `bg-card` not `bg-white`.
**Anti-patterns:** plain bg-card replacing gradients, removing emoji from temperature labels, equal-width nodes, native HTML selects. When in doubt: more color, more emoji, more gradient, more personality.

## Build phases
1. Core CRM + Pipeline (Kanban) — in progress
2. WhatsApp Inbox (two-way chat per lead)
3. Automations + drip sequences
4. KPI Dashboard
5. AI Agent (Claude) — later

## Operating rules
- **Source of truth = `docs/STATUS.md`** in the repo. Read at session start, update at session end. Don't duplicate state in memory.
- **Industry-standard tools only** — Sentry, UptimeRobot, Playwright, Supabase CLI migrations, security headers, staging env. No "just console.log".
- **Auto-commit + push pre-authorized** by Noam — don't ask each commit.

## Constraints
- Cheap to operate, free tiers maximized.
- High quality bar (production use, not prototype).
- Minimize third-party dependencies.
