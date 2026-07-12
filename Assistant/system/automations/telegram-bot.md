# Telegram Bot — Setup & Operations

Personal capture/digest bot. Long-polling (no public webhook), runs as launchd agent on this Mac.

## What it does
- **Text → inbox.** Anything you type to the bot lands as a markdown file in `~/Desktop/MY BRAIN/inbox/{timestamp}-tg.md` with frontmatter.
- **Voice → inbox.** Voice memos saved as `.ogg` in `inbox/audio/`, with a `-tg-voice.md` placeholder. Transcription is not configured (use iOS Shortcuts on-device transcription instead — it sends already-transcribed text).
- **Commands:**
  - `/digest` or `/preview` → runs the `morning-preview` skill via `claude -p`, replies with result
  - `/ping` → pong
  - `/id` → returns your chat_id (useful for setup)
  - `/{any-skill-name} [args]` → forwards to `claude -p "Run skill: {name} {args}"`
  - `/vault*` → refused. Vault queries only via SSH (open Termius). Hard-coded for safety.

## One-time setup

### 1. Create the bot
1. Open Telegram, search **@BotFather**.
2. Send `/newbot`.
3. Pick a name (e.g. "Noam's Second Brain").
4. Pick a username ending in `bot` (e.g. `noam_brain_bot`).
5. BotFather gives you a token like `1234567890:ABC-DEF...`. Copy it.

### 2. Save the token
Edit `~/.config/second-brain/secrets.env`:
```
TELEGRAM_BOT_TOKEN=1234567890:ABC-DEF...
TELEGRAM_CHAT_ID=
```
Leave `TELEGRAM_CHAT_ID` empty for now.

### 3. Capture your chat_id
Run the bot manually once to capture your chat_id:
```bash
python3 "/Users/noamfuchs/Desktop/MY BRAIN/system/automations/telegram_bot.py"
```
Open Telegram, message your bot anything. The bot replies with your chat_id. Copy it.

Edit `secrets.env` again and fill in `TELEGRAM_CHAT_ID`. Stop the bot (Ctrl+C).

### 4. Load the launchd agent
```bash
launchctl unload ~/Library/LaunchAgents/com.user.secondbrain.telegram.plist 2>/dev/null
launchctl load -w ~/Library/LaunchAgents/com.user.secondbrain.telegram.plist
launchctl list | grep secondbrain.telegram
```
You should see the agent listed with PID > 0.

### 5. Test
- Send "test capture" to the bot → check `~/Desktop/MY BRAIN/inbox/` for a new `.md` file (within 5s).
- Send `/ping` → "pong".
- Send `/digest` → runs morning-preview (slow first time — Claude warms up).

## Daily ops

### Check status
```bash
launchctl list | grep secondbrain.telegram
tail -f "/Users/noamfuchs/Desktop/MY BRAIN/system/logs/telegram.log"
```

### Restart after config change
```bash
launchctl unload ~/Library/LaunchAgents/com.user.secondbrain.telegram.plist
launchctl load -w ~/Library/LaunchAgents/com.user.secondbrain.telegram.plist
```

### Stop entirely
```bash
launchctl unload ~/Library/LaunchAgents/com.user.secondbrain.telegram.plist
```

### Logs
- `system/logs/telegram.log` — application log (info, errors, captures)
- `system/logs/telegram-stdout.log`, `telegram-stderr.log` — launchd captured output

## Security model
- Bot ignores any chat_id that isn't `TELEGRAM_CHAT_ID`. If your token leaks, an attacker can talk to the bot but can't reach your inbox.
- Token lives in `~/.config/second-brain/secrets.env` (chmod 600). Never in the plist, never in the repo.
- `/vault*` commands are refused at the bot layer. Vault queries require SSH (Termius via Tailscale).
- The bot runs as your user, with the same filesystem access you have. It can write to `inbox/` and read the brain. It cannot read `~/.personal-vault/` because the bot script never touches it.

## Failure modes
- **Bot offline / not responding** → check `launchctl list | grep secondbrain.telegram`. If no PID, restart. Check `telegram-stderr.log` for the cause.
- **Token rejected (401)** → token wrong or revoked. Get a new one from BotFather, update secrets.env.
- **Network errors** → bot retries every 5s automatically.
- **`/digest` times out** → Claude CLI took >3min. Logs in `telegram.log`. May need to invoke skill manually first time to warm up.
