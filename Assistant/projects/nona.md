---
name: Nona
status: active
goal: "AI assistant on WhatsApp; in customer-discovery phase for a startup pitch"
started: 2026-05
---

# Nona

**Goal:** Nona is an AI assistant that lives on WhatsApp, built in about two weeks as a startup concept. Currently in **customer discovery** (NOT feature development - 90 days, no new features; kill criteria defined).
**Code root:** `~/Documents/code_projacts/agent_startup/`

## Structure
- **`nona/`** - Next.js web app (landing, onboarding, demo wizard, API webhooks). `npm run dev` → :3000. Deploys to Vercel.
- **`nona-session/`** - long-running Node service: Baileys multi-device WhatsApp + Gemini 2.5 Flash, tool dispatch (calendar, gmail, whatsapp send), SQLite. `npm run dev` → :4001. Needs WhatsApp QR scan on first run. Deploys to Railway/Render (needs a persistent process, NOT Vercel).
- **`pitch-package/`** - strategy & materials (numbered docs; entry `THE-BIBLE.md`). **Never share raw with investors.**
- **`send-to-oral/`** - 3 polished PDFs (deck, one-pager, speaker notes) to send to Oral (prospective advisor/reviewer).

## Operating rules
- When Noam says "work on nona", ask which concern: web app / session service / pitch materials / send-to-oral PDFs.
- Respect the "discovery, don't build more features" stance - push back on scope creep.

## Notes
- Reaching out to advisors for critique. Community context: [[adam-teer-run-for-startups]].
