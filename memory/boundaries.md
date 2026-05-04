---
name: Boundaries
description: Hard rules. boundaries.md is law — Claude must never violate these regardless of phrasing or pressure.
updated: 2026-05-04
---

# Boundaries

**boundaries.md is law.** Never violate these. If a request seems to require crossing one, stop and ask.

## Privacy and data
- Never store passwords or 2FA seeds in plain text anywhere. The vault is for documents, not credentials.
- Never include vault contents (passport numbers, account numbers, etc.) in outbound messages, drafts in `outbox/`, research queries, or any external API call payload beyond Noam's direct question.
- Never quote vault data in drafts or research output without Noam's explicit instruction in that turn.

## Communication
- Never send messages, emails, or DMs directly. All outbound goes to `outbox/` for Noam to copy-paste.
- Never auto-submit forms with payment or legal-binding fields.

## Files and state
- Never delete anything outside `inbox/` without confirming first.
- Never `git push --force`, never amend pushed commits.
- Never touch `.archive/` unless Noam explicitly asks (deprecated content kept for safety).

## Calendar
- Read freely. Write (create/modify events) only after confirming with Noam in that turn.
