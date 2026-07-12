# Fireberry REA — CRM Automation System

Automated lead capture, WhatsApp messaging, and daily reporting for REA (Real Estate Academy).

---

## What This Does

1. **Lead Webhook** — any landing page posts a lead here → automatically creates it in Fireberry with source tagging, sends a WhatsApp welcome message to the lead, and notifies the team
2. **Daily Morning Report** — every day at 8:00am, sends Itay and Noam a WhatsApp summary of the pipeline status
3. **Source Tracking** — every lead is tagged with where it came from (webinar / instagram / campaign / referral) and the campaign name

---

## Flow

```
Landing page form submit
        ↓
lead_webhook (Base44)
        ↓
Create account in Fireberry
  - Name, phone, email
  - Source + campaign name
  - Status: "New Lead"
  - UTM params in description
        ↓
Send WhatsApp to lead         Send WhatsApp to team
  "תודה שנרשמת..."              "ליד חדש: שם | מקור"
        ↓
Update status: "MSG sent"
```

```
Every day at 8:00am
        ↓
daily_report (Base44 cron)
        ↓
Query Fireberry for:
  - New leads (last 24h)
  - Leads not touched in 2+ days
  - Stuck in Follow Up 3+ days
  - Contract sent (close to closing)
        ↓
Send report to Itay + Noam via WhatsApp
```

---

## Files

- [[Base44/fireberry|fireberry.ts]] — Fireberry API client
- [[Base44/whatsapp|whatsapp.ts]] — WhatsApp Cloud API client
- [[Base44/lead_webhook|lead_webhook.ts]] — main webhook, handles new leads
- [[Base44/daily_report|daily_report.ts]] — morning report cron
- [[SETUP|Full Setup Guide]]

---

## Fireberry Field Mapping

| Field | Usage |
|---|---|
| `accountname` | Full name |
| `telephone2` | Phone number |
| `emailaddress1` | Email |
| `pcfsystemfield3` | Lead source (webinar / instagram / campaign / referral) |
| `pcfsystemfield5` | Campaign / webinar name |
| `websiteurl` | Landing page URL |
| `description` | UTM params (JSON) |
| `statuscode` | Lead status (see below) |

## Status Codes

| Code | Status | Meaning |
|---|---|---|
| 6 | New Lead | Just entered, not contacted yet |
| 12 | MSG sent | WhatsApp message was sent |
| 14 | Follow Up | In active follow-up |
| 2 | Contract sent | Almost closed |
| 11 | Paid | Converted |
| 5 | Irrelevant | Not relevant |

---

## Status

- [ ] Base44 env vars configured
- [ ] `lead_webhook` function added to Base44
- [ ] `daily_report` function added to Base44
- [ ] Daily report cron scheduled (8:00am)
- [ ] WhatsApp templates submitted and approved
- [ ] Webhook URL added to landing pages
- [ ] Tested end-to-end
