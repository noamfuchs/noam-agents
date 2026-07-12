/**
 * Webinar Signup Bot — Base44 Backend Function
 * =============================================
 * Trigger: Form submission on the webinar signup page
 * Action:  Sends a personalized WhatsApp message with 2 quick-reply buttons
 *
 * HOW TO ADD THIS IN BASE44:
 *   App Settings → Backend Functions → New Function
 *   Paste this file, name it "webinar_signup_handler"
 *   Then connect it to your signup form's "On Submit" event
 *
 * ENV VARS TO SET IN BASE44 (App Settings → Environment Variables):
 *   WHATSAPP_TOKEN          — your Meta permanent access token
 *   WHATSAPP_PHONE_NUMBER_ID — your WhatsApp phone number ID from Meta
 *   TEMPLATE_NAME           — webinar_signup_confirmation (or whatever you named it)
 *   CALENDAR_LINK           — the Google Calendar link for the webinar (optional)
 */

const WHATSAPP_TOKEN       = Deno.env.get("WHATSAPP_TOKEN")!;
const PHONE_NUMBER_ID      = Deno.env.get("WHATSAPP_PHONE_NUMBER_ID")!;
const TEMPLATE_NAME        = Deno.env.get("TEMPLATE_NAME") ?? "webinar_signup_confirmation";

// ── Main handler ─────────────────────────────────────────────────────────────

export default async function handler(event: {
  body: {
    name: string;   // full name from the signup form
    phone: string;  // phone number from the signup form
    email?: string; // optional
  };
}) {
  const { name, phone } = event.body;

  if (!name || !phone) {
    return { success: false, error: "Missing name or phone" };
  }

  const to = formatIsraeliPhone(phone);
  const firstName = name.split(" ")[0]; // use first name only for the greeting

  const result = await sendWhatsAppTemplate(to, firstName);

  // Log the result (visible in Base44 function logs)
  console.log(`[Webinar Signup Bot] Sent to ${to} (${name}):`, result);

  return { success: true, whatsapp: result };
}

// ── Send WhatsApp template message ───────────────────────────────────────────

async function sendWhatsAppTemplate(to: string, firstName: string) {
  const url = `https://graph.facebook.com/v20.0/${PHONE_NUMBER_ID}/messages`;

  const payload = {
    messaging_product: "whatsapp",
    to,
    type: "template",
    template: {
      name: TEMPLATE_NAME,
      language: { code: "he" },
      components: [
        {
          // Fills in {{1}} in the template body with the person's first name
          type: "body",
          parameters: [
            { type: "text", text: firstName },
          ],
        },
      ],
    },
  };

  const res = await fetch(url, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${WHATSAPP_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const json = await res.json();

  if (!res.ok) {
    console.error("[Webinar Signup Bot] WhatsApp API error:", json);
    throw new Error(json?.error?.message ?? "WhatsApp API call failed");
  }

  return json;
}

// ── Phone number formatter ────────────────────────────────────────────────────
// Converts Israeli phone numbers to international format (e.g. 050-1234567 → 972501234567)

function formatIsraeliPhone(raw: string): string {
  // Strip everything except digits
  let digits = raw.replace(/\D/g, "");

  // If already has country code (972...) just return as-is
  if (digits.startsWith("972")) return digits;

  // Strip leading 0 and prepend 972
  if (digits.startsWith("0")) digits = digits.slice(1);

  return "972" + digits;
}
