# Setup Guide — Message Formatter Bot

## What you need
- Python 3.11+
- A Telegram bot token (from [@BotFather](https://t.me/BotFather))
- Your Telegram user ID (from [@userinfobot](https://t.me/userinfobot))
- An Anthropic API key (from [console.anthropic.com](https://console.anthropic.com))

---

## Step 1 — Install Python dependencies

Open Terminal, navigate to this folder, and run:

```bash
cd "/Users/YOUR_USERNAME/Desktop/MY BRAIN/🤖 Agents/Message Formatter/bot"
pip3 install -r requirements.txt
```

---

## Step 2 — Create your .env file

Copy the example file and fill it in:

```bash
cp .env.example .env
```

Then open `.env` and fill in:
- `TELEGRAM_BOT_TOKEN` — from @BotFather
- `TELEGRAM_USER_ID` — your numeric ID from @userinfobot
- `ANTHROPIC_API_KEY` — from console.anthropic.com
- `VAULT_PATH` — full path to your Obsidian vault, e.g. `/Users/noam/Desktop/MY BRAIN`

---

## Step 3 — Run the bot

```bash
python3 bot.py
```

You should see: `Bot started — polling...`

Leave the Terminal window open while you use it.

---

## Step 4 — Test it

1. Open Telegram and find your bot
2. Send `/start`
3. Send a rough message like: `שיעור אתמול היה טוב, ההקלטה תעלה מחר, מחר יש שיעור שיפוצים ב20:00`
4. Tap `🏘️ קהילת הקורס`
5. Get the formatted message back

---

## Running it automatically on Mac startup (optional)

To keep the bot running without a Terminal window:

```bash
# Create a launch agent (runs on login)
mkdir -p ~/Library/LaunchAgents

cat > ~/Library/LaunchAgents/com.noam.messageformatter.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.noam.messageformatter</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/Users/YOUR_USERNAME/Desktop/MY BRAIN/🤖 Agents/Message Formatter/bot/bot.py</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/Users/YOUR_USERNAME/Desktop/MY BRAIN/🤖 Agents/Message Formatter/bot</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/message-formatter.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/message-formatter-error.log</string>
</dict>
</plist>
EOF

# Load it
launchctl load ~/Library/LaunchAgents/com.noam.messageformatter.plist
```

Replace `YOUR_USERNAME` with your Mac username.

---

## Adding a new audience

1. Create a new style profile in `Styles/` inside Obsidian (e.g. `Styles/Investors.md`)
2. In `formatter.py`, add to `STYLE_FILES`:
   ```python
   "investors": "Styles/Investors.md",
   ```
3. In `bot.py`, add to `AUDIENCES`:
   ```python
   "investors": "💼 משקיעים",
   ```
4. Restart the bot

---

## Troubleshooting

**Bot doesn't respond** → Check the Terminal for errors. Usually it's a wrong token or missing .env file.

**"Style profile not found"** → Make sure `VAULT_PATH` in `.env` is the exact path to the vault folder (not a subfolder).

**"Unknown audience"** → Make sure the key in `AUDIENCES` (bot.py) matches the key in `STYLE_FILES` (formatter.py).
