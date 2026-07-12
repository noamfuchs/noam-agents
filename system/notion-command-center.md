# Notion Command Center

My Notion workspace is the **front-of-house** for everything I actually work on or look at. This vault (MY BRAIN) stays the full background: raw notes, meeting transcripts, the people CRM, daily logs. Notion only holds what is important and active.

**Rule — where does it go?**
- Thinking, raw notes, history, CRM, transcripts -> **Obsidian (here)**.
- Action, status, goals, anything I read or check daily -> **Notion**.
- Flow is one-way: Obsidian / local jobs -> Notion. I never edit canonical content back from Notion.

**Dashboard:** https://app.notion.com/p/38106ac6f07b814299bee0f6b9ce2ea1

## Structure
Pillars (life areas) -> Goals -> Projects -> Tasks, with progress bars rolling upward. Plus an Inbox (where automations drop things to triage) and a 75 Hard tracker (Attempts + Daily Log).

**8 life areas (each a color):** Health (green), School/IDC (blue), Real-Estate Course (yellow), Nona (purple), RFS (orange), Personal Brand (pink), Finances (brown), Personal & Growth (red).

## What flows in automatically
- **75 Hard** — daily check-ins from the bot mirror into the Notion tracker (streak + the 6 daily boxes).
- **Meeting action items** — Fathom recordings -> action items become Notion tasks.
- **Important WhatsApp messages** — AI-flagged messages land in the Inbox.
- **Calendar** — today's events land in the Inbox.

Sync code lives in `~/notion-sync`. To turn the syncs on I need to create a Notion integration token and share the databases with it (see `~/notion-sync/SETUP.md`).

Built 2026-06-16.
