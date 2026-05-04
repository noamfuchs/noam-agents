/**
 * WhatsApp Cloud API Client — REA System
 * ========================================
 * Sends WhatsApp messages via the Meta Cloud API.
 *
 * ENV VARS:
 *   WHATSAPP_TOKEN          — Meta permanent access token
 *   WHATSAPP_PHONE_NUMBER_ID — Business phone number ID
 */

const WHATSAPP_TOKEN    = Deno.env.get("WHATSAPP_TOKEN")!;
const PHONE_NUMBER_ID   = Deno.env.get("WHATSAPP_PHONE_NUMBER_ID")!;
const GRAPH_URL         = `https://graph.facebook.com/v20.0/${PHONE_NUMBER_ID}/messages`;

// ── Send a WhatsApp template message ────────────────────────────────────────

export async function sendTemplate(
  to: string,
  templateName: string,
  params: string[] = [],
  language = "he"
): Promise<void> {
  const body: Record<string, unknown> = {
    messaging_product: "whatsapp",
    to,
    type: "template",
    template: {
      name: templateName,
      language: { code: language },
      components: params.length > 0
        ? [{ type: "body", parameters: params.map(p => ({ type: "text", text: p })) }]
        : [],
    },
  };

  await post(body);
}

// ── Send a plain text message ────────────────────────────────────────────────

export async function sendText(to: string, text: string): Promise<void> {
  await post({
    messaging_product: "whatsapp",
    to,
    type: "text",
    text: { body: text, preview_url: false },
  });
}

// ── Send a text message with quick-reply buttons ─────────────────────────────

export async function sendButtons(
  to: string,
  body: string,
  buttons: Array<{ id: string; title: string }>
): Promise<void> {
  await post({
    messaging_product: "whatsapp",
    to,
    type: "interactive",
    interactive: {
      type: "button",
      body: { text: body },
      action: {
        buttons: buttons.map(b => ({
          type: "reply",
          reply: { id: b.id, title: b.title },
        })),
      },
    },
  });
}

// ── Internal POST helper ─────────────────────────────────────────────────────

async function post(payload: unknown): Promise<unknown> {
  const res = await fetch(GRAPH_URL, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${WHATSAPP_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const json = await res.json();
  if (!res.ok) {
    console.error("[WhatsApp] API error:", json);
    throw new Error(json?.error?.message ?? "WhatsApp API call failed");
  }
  return json;
}
