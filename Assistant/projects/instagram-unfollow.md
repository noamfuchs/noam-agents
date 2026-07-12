---
name: Instagram Unfollow Tool
status: active
goal: "Auto-unfollow accounts that don't follow Noam back (@fuchs.noam)"
started: 2026-05-27
---

# Instagram Unfollow Tool

**Goal:** Bulk-unfollow non-followers. Python + Playwright driving a logged-in Chromium profile.
**Code:** `~/instagram-unfollow/` (local only).
**Status:** Active - daily batch of 100 via LaunchAgent at 11:00 Asia/Jerusalem.

## State (as of 2026-05-27)
- Following about 5,149 / followers about 1,030 / about 4,459 non-followers to remove (6 protected in `keep.txt`).
- about 45 days to complete at 100/day.

## How it works
- `collect_lists.py` - scrapes following + followers (opens the count dialog; direct /following/ URL no longer works).
- `unfollow.py --non-followers --limit N` - unfollows accounts not in keep.txt / unfollowed.csv, randomized, 22–55s delays, long break every 25, auto-stops on "Action Blocked". Finds buttons by inner_text (IG leaves the accessibility name blank).
- Progress tracked in `unfollowed.csv` (resumable); `keep.txt` = never-unfollow list.

## Automation
- LaunchAgent `com.noam.igunfollow` (`~/Library/LaunchAgents/com.noam.igunfollow.plist`) runs `run_daily.sh` daily at 11:00. Mac must be awake.

## Caveats
- IG session cookie can expire after some weeks → the run hangs about 6 min then fails. Fix: re-run login manually from a GUI terminal (the browser window only appears when launched from a GUI session, not from Claude's bash).
- Pace 100/day; Noam accepts the ToS/ban risk. No paid dependencies.

## Notes
- Account: @fuchs.noam
