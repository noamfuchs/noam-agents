# REA System — Full Setup Guide

**Total setup time: ~45 minutes** (plus 1-2 days waiting for WhatsApp template approval)

---

## Step 1 — Environment Variables in Base44

Go to **App Settings → Environment Variables** and add:

| Variable | Value |
|---|---|
| `FIREBERRY_TOKEN` | `9a3cb286-c7dd-4d4f-b793-9424f9f3f49d` |
| `WHATSAPP_TOKEN` | your Meta permanent access token (same as webinar bot) |
| `WHATSAPP_PHONE_NUMBER_ID` | your WhatsApp phone number ID (same as webinar bot) |
| `TEAM_PHONE_ITAY` | Itay's number in international format, e.g. `972521234567` |
| `TEAM_PHONE_NOAM` | Noam's number in international format, e.g. `972501234567` |
| `LEAD_TEMPLATE_WEBINAR` | `rea_lead_welcome_webinar` |
| `LEAD_TEMPLATE_CAMPAIGN` | `rea_lead_welcome_campaign` |

---

## Step 2 — Create WhatsApp Templates (wait 1-2 days for approval)

Go to **Meta → WhatsApp → Message Templates → Create Template**

### Template 1: Webinar leads

| Field | Value |
|---|---|
| Template name | `rea_lead_welcome_webinar` |
| Category | Marketing |
| Language | Hebrew (he) |

**Body:**
```
אהלן {{1}}! 🏠

תודה שנרשמת לוובינר *{{2}}*.

קיבלנו את ההרשמה שלך ✅
ניצור איתך קשר בקרוב עם כל הפרטים.

נשמח לראותך! 💪
— צוות REA
```

### Template 2: Campaign / other leads

| Field | Value |
|---|---|
| Template name | `rea_lead_welcome_campaign` |
| Category | Marketing |
| Language | Hebrew (he) |

**Body:**
```
אהלן {{1}}! 🏠

תודה שהשארת פרטים — קיבלנו אותם ✅

נציג מצוות REA יחזור אליך בהקדם.

— צוות REA
```

> **Note:** `{{1}}` = first name, `{{2}}` = webinar/campaign name. These fill in automatically.

---

## Step 3 — Add the Backend Functions in Base44

Go to **App Settings → Backend Functions** for each:

### Function 1: `rea_lead_webhook`
1. New Function → name: `rea_lead_webhook`
2. Paste entire contents of `Base44/lead_webhook.ts`
3. Save

### Function 2: `rea_daily_report`
1. New Function → name: `rea_daily_report`
2. Paste entire contents of `Base44/daily_report.ts`
3. Save

> These two functions import from `fireberry.ts` and `whatsapp.ts` — add those as functions too:
> - Function name: `fireberry` → paste `Base44/fireberry.ts`
> - Function name: `whatsapp` → paste `Base44/whatsapp.ts`

---

## Step 4 — Schedule the Daily Report

Go to **App Settings → Scheduled Tasks → Add Task**

| Field | Value |
|---|---|
| Function | `rea_daily_report` |
| Schedule | `0 8 * * *` |
| Timezone | Asia/Jerusalem |
| Description | Daily morning report — REA |

This runs every day at 8:00am Israel time.

---

## Step 5 — Connect Your Landing Pages

On every landing page form, add an **"On Submit" → Call Backend Function** action:

```json
POST /api/rea_lead_webhook
{
  "name": "[name field]",
  "phone": "[phone field]",
  "email": "[email field]",
  "source": "webinar",
  "campaign_name": "וובינר מחזור ג׳ — 2026",
  "utm_source": "[utm_source param]",
  "utm_medium": "[utm_medium param]",
  "utm_campaign": "[utm_campaign param]"
}
```

**Source values to use per landing page:**

| Landing Page | `source` value |
|---|---|
| Webinar signup | `webinar` |
| Instagram bio link | `instagram` |
| Paid ad funnel | `campaign` |
| Referral page | `referral` |
| Organic/blog | `organic` |

---

## Step 6 — Add UTM Links to Campaigns

All links to landing pages should have UTM parameters:

```
https://your-landing-page.com?utm_source=facebook&utm_medium=cpc&utm_campaign=webinar_may_2026
```

**Standard UTM structure for REA:**

| Parameter | Values |
|---|---|
| `utm_source` | `facebook`, `instagram`, `whatsapp`, `email` |
| `utm_medium` | `cpc` (paid), `organic`, `referral`, `direct` |
| `utm_campaign` | `webinar_[month]_[year]`, `retargeting_[date]` |
| `utm_content` | `video_ad`, `carousel`, `story` (for A/B testing) |

---

## Step 7 — Test End to End

1. Submit a test form with your own name + number
2. Check Fireberry — new account should appear with source tagging in `pcfsystemfield3`
3. Check your WhatsApp — welcome message should arrive within 5 seconds
4. Check Itay and Noam's WhatsApp — team notification should arrive
5. Manually trigger `rea_daily_report` to verify the morning report format

---

## What Your Existing 34 Contacts Keep

Nothing changes for existing contacts. The new fields (`pcfsystemfield3`, `pcfsystemfield5`) will simply be empty for them — they're added as new optional fields going forward. No existing data is touched.

---

## Fireberry Fields Used

| Field | What's Stored |
|---|---|
| `accountname` | Full name |
| `telephone2` | Phone (Israeli format → international) |
| `emailaddress1` | Email |
| `pcfsystemfield3` | Lead source (webinar / instagram / campaign / referral / organic) |
| `pcfsystemfield5` | Campaign or webinar name |
| `websiteurl` | Landing page URL |
| `description` | UTM params as JSON |
| `statuscode` | 6=New Lead → 12=MSG sent → 14=Follow Up → 2=Contract sent → 11=Paid |

---

## Daily Report — What It Shows

Every morning at 8:00 you and Itay get:

```
📊 דוח בוקר — REA | 28.04.2026

📈 סיכום כללי
• לידים פתוחים: 12
• לקוחות ששילמו: 9

🆕 לידים חדשים אתמול (2)
• ישראל ישראלי | 050-xxx | וובינר
• שרה כהן     | 052-xxx | קמפיין ממומן

🔴 מחכים לטיפול ראשוני (1)
• דוד לוי | 054-xxx | 1 ימים

📞 הודעה נשלחה אך לא טופלו (3)
• ...

⚠️ תקועים ב-Follow Up (2)
• ...

💰 חוזה נשלח — קרוב לסגירה (1)
• ...

‼️ 6 לידים דורשים טיפול היום
```
