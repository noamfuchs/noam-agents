# 🤖 Agents Hub

This is your command center for all AI agents. Each agent lives in its own folder with its style profiles, logs, and code.

---

## Active Agents

| Agent | What it does | Status |
|---|---|---|
| [[Message Formatter/Agent\|Message Formatter]] | Formats rough messages for 3 audiences via Telegram | ✅ Active |
| [[Webinar Signup Bot/Agent\|Webinar Signup Bot]] | Auto-sends WhatsApp + buttons when someone signs up on Base44 | 🔧 Setup in progress |

---

## How it works

Every agent you build here follows the same pattern:

1. **Agent.md** — what the agent does, how to trigger it, how to maintain it
2. **Styles/** — the style profiles the agent reads to know how to behave
3. **Logs/** — auto-populated every time the agent runs
4. **bot/** — the actual code (Python)

To add a new agent, duplicate the `_New Agent Template` folder and start from there.

---

## Quick Start — Message Formatter

1. Open Telegram and send your raw message to the bot
2. Tap the audience button (Community / Partners / Ads)
3. Get your formatted message back instantly
4. The log is saved automatically in `Message Formatter/Logs/`

→ [[Message Formatter/Agent|Open Message Formatter]]
