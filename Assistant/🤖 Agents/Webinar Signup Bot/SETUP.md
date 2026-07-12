# Webinar Signup Bot — Full Setup Guide

**What it does:** Sends an automatic WhatsApp message (with 2 buttons) the moment someone signs up on your Base44 webinar form.

**Time to set up:** ~30 minutes + 1-2 days for Meta template approval

---

## Part 1 — Meta WhatsApp API (15 min)

### Step 1 — Create a Meta Developer account
1. Go to [developers.facebook.com](https://developers.facebook.com)
2. Log in with any Facebook account
3. Click "My Apps" → "Create App"
4. Choose **"Business"** type
5. Give it a name (e.g. "Fuchs Real Estate Bot")

### Step 2 — Add WhatsApp to your app
1. Inside your app, click **"Add Product"**
2. Find **WhatsApp** → click **"Set Up"**
3. You'll land on the WhatsApp Getting Started page

### Step 3 — Get your test phone number (immediate, free)
1. In WhatsApp → Getting Started, Meta gives you a **free test number**
2. Copy the **Phone Number ID** (you'll need it)
3. Copy the **Temporary Access Token** (valid 24h) or create a **Permanent Token**:
   - Go to Business Settings → System Users → Add System User
   - Assign WhatsApp app with "full" permission
   - Generate token → copy it (this is your `WHATSAPP_TOKEN`)

### Step 4 — Add your real number (when ready)
1. WhatsApp → Phone Numbers → Add Phone Number
2. Use your new SIM/virtual number
3. Verify via SMS or call
4. This replaces the test number

---

## Part 2 — Submit the message template (wait 1-2 days)

Go to **WhatsApp → Message Templates → Create Template**

Fill in exactly:

| Field | Value |
|---|---|
| Template name | `webinar_signup_confirmation` |
| Category | Marketing |
| Language | Hebrew (he) |

**Header (optional):**
```
ברוכים הבאים לוובינר! 🏠
```

**Body:**
```
אהלן {{1}}! 😎
כאן Amit מצוות Fuchs Real Estate.

נרשמת לוובינר בנושא השקעות נדל"ן בארה"ב - תודה! 🏠🇺🇸

רצינו לאשר את ההרשמה שלך!
בוובינר נעבור על מודל ההשקעה, מימון לנכסים בארה"ב ודוגמאות לעסקאות אמיתיות.

להסרה השב "הסר"
```

**Buttons (type: Quick Reply):**
| # | Button text | Button ID |
|---|---|---|
| 1 | לקבלת סרטון מידע | btn_video |
| 2 | הוסף לי ליומן | btn_calendar |

Submit → wait for approval (usually 24-48 hours, sometimes same day).

---

## Part 3 — Set up Base44 (20 min, do while waiting for template approval)

### Step 1 — Add environment variables in Base44
Go to your app → **App Settings → Environment Variables** → add:

| Variable | Value |
|---|---|
| `WHATSAPP_TOKEN` | your Meta permanent access token |
| `WHATSAPP_PHONE_NUMBER_ID` | your phone number ID from Meta |
| `TEMPLATE_NAME` | `webinar_signup_confirmation` |
| `WEBHOOK_VERIFY_TOKEN` | any random string, e.g. `fuchs_bot_2026` |
| `VIDEO_LINK` | your info video URL |
| `CALENDAR_LINK` | your Google Calendar event link |

### Step 2 — Add the signup function
1. Go to **App Settings → Backend Functions → New Function**
2. Name it: `webinar_signup_handler`
3. Paste the entire contents of `Base44/signup_handler.ts`
4. Save

### Step 3 — Connect it to your signup form
1. Open your webinar signup form in Base44 editor
2. Find the form's **"On Submit"** action
3. Add action: **"Call Function"** → `webinar_signup_handler`
4. Map the form fields:
   - `name` → your name field
   - `phone` → your phone number field

### Step 4 — Add the button reply handler
1. Backend Functions → New Function
2. Name it: `whatsapp_webhook`
3. Paste the entire contents of `Base44/button_reply_handler.ts`
4. Save

### Step 5 — Connect the webhook in Meta
1. In Meta Developer → WhatsApp → Configuration
2. Webhook URL: `https://YOUR-APP.base44.app/api/whatsapp_webhook`
3. Verify Token: same string you set as `WEBHOOK_VERIFY_TOKEN`
4. Subscribe to: **messages**
5. Save

---

## Part 4 — Test it

1. Go to your webinar signup form
2. Submit with your own name + phone number
3. You should receive the WhatsApp message within ~3 seconds
4. Tap each button to confirm they work

---

## What each file does

| File | What it does |
|---|---|
| `Base44/signup_handler.ts` | Fires when someone submits the signup form. Calls WhatsApp API and sends the welcome message. |
| `Base44/button_reply_handler.ts` | Fires when someone taps a quick-reply button. Sends them the video link or calendar link. |

---

## Customizing the message

Edit the template text in Meta's dashboard (**WhatsApp → Message Templates → your template → Edit**). Any edits need re-approval (usually faster the second time).

To change the button responses (what's sent when someone taps a button), edit `button_reply_handler.ts` in Base44 — no approval needed for those.
