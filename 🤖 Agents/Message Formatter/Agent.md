# 🗂️ Message Formatter Agent

Takes a rough, quickly written message and formats it into a polished, ready-to-send message — with the right emojis, tone, and structure for each audience.

---

## Audiences

| Audience | Style | When to use |
|---|---|---|
| 🏘️ Course Community | Warm, encouraging, community Hebrew | Lesson updates, webinar reminders, recordings |
| 🤝 Partners | Operational morning briefing | Task assignments, daily updates, coordination |
| 📣 Ads & Webinars | Sales, excitement, bold Hebrew | Webinar invites, registration pushes, follow-ups |

---

## How to Use

1. **Open Telegram** and message the bot
2. **Type your raw message** — bullet points, quick notes, doesn't matter
3. **Tap the audience button** that appears
4. **Copy the formatted result** and paste into WhatsApp / wherever

---

## Style Profiles

Edit these to update how the agent writes for each audience:

- [[Styles/Course Community|Course Community Style]]
- [[Styles/Partners|Partners Style]]
- [[Styles/Ads & Webinars|Ads & Webinars Style]]

---

## Logs

Every formatted message is saved here automatically:
→ [[Logs/]]

---

## Adding a New Audience

1. Create a new file in `Styles/` — e.g. `Styles/Investors.md`
2. Fill in the style profile (tone, structure, emoji rules, examples)
3. Add the new audience key in `bot/formatter.py` under `STYLE_FILES`
4. Add the button label in `bot/bot.py` under `AUDIENCES`
5. Restart the bot

---

## Bot Setup

→ [[bot/SETUP|Setup Guide]]
