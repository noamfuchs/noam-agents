# 📲 Webinar Signup Bot

Automatically sends a personalized WhatsApp message with quick-reply buttons the moment someone submits the webinar signup form on Base44.

---

## Flow

`Base44 signup form` → `signup_handler.ts` → `WhatsApp Cloud API` → `Message delivered in ~3 seconds`

When someone taps a button → `button_reply_handler.ts` → sends video link or calendar link

---

## Message Preview

> אהלן [שם]! 😎
> כאן Amit מצוות Fuchs Real Estate.
>
> נרשמת לוובינר בנושא השקעות נדל"ן בארה"ב - תודה! 🏠🇺🇸
>
> רצינו לאשר את ההרשמה שלך!
> בוובינר נעבור על מודל ההשקעה, מימון לנכסים בארה"ב ודוגמאות לעסקאות אמיתיות.
>
> [לקבלת סרטון מידע] [הוסף לי ליומן]

---

## Status

- [ ] Meta Developer account created
- [ ] Template submitted for approval
- [ ] Template approved
- [ ] `signup_handler.ts` added to Base44
- [ ] `button_reply_handler.ts` added to Base44
- [ ] Webhook connected in Meta
- [ ] Tested end-to-end ✅

---

## Files

- [[Base44/signup_handler|signup_handler.ts]] — fires on form submit
- [[Base44/button_reply_handler|button_reply_handler.ts]] — handles button taps
- [[SETUP|Full Setup Guide]]
