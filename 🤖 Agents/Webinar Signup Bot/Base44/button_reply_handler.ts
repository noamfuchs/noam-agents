/**
 * Button Reply Handler — Base44 Backend Function
 * ================================================
 * Receives WhatsApp webhook events when someone taps a quick-reply button.
 *
 * Button 1: "לקבלת סרטון מידע"  → sends them the info video link
 * Button 2: "הוסף לי ליומן"     → sends them the calendar link
 *
 * HOW TO ADD THIS IN BASE44:
 *   App Settings → Backend Functions → New Function
 *   Name it "whatsapp_webhook"
 *   Then go to App Settings → Webhooks → Add Webhook
 *   Point Meta's WhatsApp webhook to: https://your-base44-app.base44.app/api/whatsapp_webhook
 *
 * ENV VARS:
 *   WHATSAPP_TOKEN          — your Meta permanent access token
 *   WHATSAPP_PHONE_NUMBER_ID — your WhatsApp phone number ID
 *   WEBHOOK_VERIFY_TOKEN    — any random string you choose (set same in Meta dashboard)
 *   VIDEO_LINK              — link to your info video
 *   CALENDAR_LINK           — Google Calendar event link for the webinar
 */

const WHATSAPP_TOKEN    = Deno.env.get("WHATSAPP_TOKEN")!;
const PHONE_NUMBER_ID   = Deno.env.get("WHATSAPP_PHONE_NUMBER_ID")!;
const VERIFY_TOKEN      = Deno.env.get("WEBHOOK_VERIFY_TOKEN")!;
const VIDEO_LINK        = Deno.env.get("VIDEO_LINK") ?? "";
const CALENDAR_LINK     = Deno.env.get("CALENDAR_LINK") ?? "";

// ── Main handler ─────────────────────────────────────────────────────────────

export default async function handler(event: any) {
  const { method, query, body } = event;

  // ── Webhook verification (Meta calls this once when you set up the webhook)
  if (method === "GET") {
    if (query["hub.verify_token"] === VERIFY_TOKEN) {
      return new Response(query["hub.challenge"], { status: 200 });
    }
    return new Response("Forbidden", { status: 403 });
  }

  // ── Incoming message/button tap
  if (method === "POST") {
    const entry = body?.entry?.[0];
    const change = entry?.changes?.[0];
    const message = change?.value?.messages?.[0];

    if (!message) return { received: true }; // status update, not a message

    const from = message.from; // sender's phone number

    // Handle quick-reply button tap
    if (message.type === "interactive" && message.interactive?.type === "button_reply") {
      const buttonId = message.interactive.button_reply.id;
      await handleButtonTap(from, buttonId);
    }

    // Handle regular text reply (e.g. someone replies "הסר")
    if (message.type === "text") {
      const text = message.text?.body?.trim();
      if (text === "הסר" || text === "הסר " || text?.toLowerCase() === "stop") {
        await sendTextMessage(from,
          "הוסרת מהרשימה. מצטערים לראותך עוזב — תמיד תוכל לחזור ולהירשם מחדש 🙏"
        );
      }
    }

    return { received: true };
  }
}

// ── Button tap logic ──────────────────────────────────────────────────────────

async function handleButtonTap(to: string, buttonId: string) {
  switch (buttonId) {
    case "btn_video":
      await sendTextMessage(to,
        `🎥 *הנה הסרטון שלנו*\n\n` +
        `צפה בסרטון הקצר שמסביר בדיוק מה נעבור בוובינר:\n${VIDEO_LINK}\n\n` +
        `מחכים לראותך! 💪`
      );
      break;

    case "btn_calendar":
      await sendTextMessage(to,
        `📅 *הוספנו לך את הוובינר ליומן*\n\n` +
        `לחץ כאן להוספה ל-Google Calendar:\n${CALENDAR_LINK}\n\n` +
        `תזכורת תישלח גם ב-WhatsApp לפני הוובינר ✅`
      );
      break;

    default:
      console.log(`Unknown button ID: ${buttonId}`);
  }
}

// ── Send plain text WhatsApp message ─────────────────────────────────────────

async function sendTextMessage(to: string, text: string) {
  const url = `https://graph.facebook.com/v20.0/${PHONE_NUMBER_ID}/messages`;

  const res = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${WHATSAPP_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      messaging_product: "whatsapp",
      to,
      type: "text",
      text: { body: text },
    }),
  });

  if (!res.ok) {
    const err = await res.json();
    console.error("[Button Reply Handler] Error:", err);
  }
}
