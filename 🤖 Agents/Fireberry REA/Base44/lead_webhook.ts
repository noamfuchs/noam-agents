/**
 * Lead Webhook — REA System
 * ==========================
 * Receives a new lead from any landing page.
 * 1. Creates the account in Fireberry with full source tagging
 * 2. Sends a WhatsApp welcome message to the lead
 * 3. Notifies Itay and Noam on WhatsApp
 * 4. Updates lead status to "MSG sent"
 *
 * HOW TO ADD IN BASE44:
 *   App Settings → Backend Functions → New Function
 *   Name it "rea_lead_webhook"
 *   Paste this file
 *
 * CALL FROM LANDING PAGE (POST):
 * {
 *   "name": "ישראל ישראלי",
 *   "phone": "0501234567",
 *   "email": "email@example.com",         // optional
 *   "source": "webinar",                  // webinar | instagram | campaign | referral | organic
 *   "campaign_name": "וובינר אפריל 2026", // optional
 *   "landing_page": "https://...",        // optional
 *   "utm_source": "facebook",             // optional
 *   "utm_medium": "cpc",                  // optional
 *   "utm_campaign": "webinar_apr_2026",   // optional
 *   "utm_content": "variant_a"            // optional
 * }
 *
 * ENV VARS (App Settings → Environment Variables):
 *   FIREBERRY_TOKEN          — Fireberry API token
 *   WHATSAPP_TOKEN           — Meta permanent access token
 *   WHATSAPP_PHONE_NUMBER_ID — WhatsApp business phone number ID
 *   TEAM_PHONE_ITAY          — Itay's WhatsApp number (e.g. 972521234567)
 *   TEAM_PHONE_NOAM          — Noam's WhatsApp number (e.g. 972501234567)
 *   LEAD_TEMPLATE_WEBINAR    — WhatsApp template name for webinar leads
 *   LEAD_TEMPLATE_CAMPAIGN   — WhatsApp template name for campaign/other leads
 */

import { createLead, updateStatus, formatIsraeliPhone, STATUS } from "./fireberry.ts";
import { sendTemplate, sendText } from "./whatsapp.ts";

const TEAM_PHONE_ITAY         = Deno.env.get("TEAM_PHONE_ITAY")!;
const TEAM_PHONE_NOAM         = Deno.env.get("TEAM_PHONE_NOAM")!;
const LEAD_TEMPLATE_WEBINAR   = Deno.env.get("LEAD_TEMPLATE_WEBINAR")  ?? "rea_lead_welcome_webinar";
const LEAD_TEMPLATE_CAMPAIGN  = Deno.env.get("LEAD_TEMPLATE_CAMPAIGN") ?? "rea_lead_welcome_campaign";

// ── Source labels (Hebrew) ───────────────────────────────────────────────────

const SOURCE_LABELS: Record<string, string> = {
  webinar:   "וובינר",
  instagram: "אינסטגרם",
  campaign:  "קמפיין ממומן",
  referral:  "הפניה",
  organic:   "אורגני",
};

// ── Main handler ─────────────────────────────────────────────────────────────

export default async function handler(event: {
  body: {
    name: string;
    phone: string;
    email?: string;
    source?: string;
    campaign_name?: string;
    landing_page?: string;
    utm_source?: string;
    utm_medium?: string;
    utm_campaign?: string;
    utm_content?: string;
  };
}) {
  const {
    name, phone, email,
    source = "organic",
    campaign_name,
    landing_page,
    utm_source, utm_medium, utm_campaign, utm_content,
  } = event.body;

  if (!name || !phone) {
    return { success: false, error: "Missing name or phone" };
  }

  const firstName  = name.split(" ")[0];
  const formattedPhone = formatIsraeliPhone(phone);

  // ── 1. Create lead in Fireberry ──────────────────────────────────────────

  const utmParams: Record<string, string> = {};
  if (utm_source)   utmParams.utm_source   = utm_source;
  if (utm_medium)   utmParams.utm_medium   = utm_medium;
  if (utm_campaign) utmParams.utm_campaign = utm_campaign;
  if (utm_content)  utmParams.utm_content  = utm_content;

  const account = await createLead({
    name,
    phone,
    email,
    source,
    campaign_name,
    landing_page,
    utm_params: Object.keys(utmParams).length > 0 ? utmParams : undefined,
  });

  console.log(`[REA Lead Webhook] Created account ${account.accountid} for ${name}`);

  // ── 2. Send WhatsApp welcome to lead ────────────────────────────────────

  const templateName = source === "webinar" ? LEAD_TEMPLATE_WEBINAR : LEAD_TEMPLATE_CAMPAIGN;
  const campaignLabel = campaign_name ?? SOURCE_LABELS[source] ?? source;

  try {
    await sendTemplate(formattedPhone, templateName, [firstName, campaignLabel]);
    console.log(`[REA Lead Webhook] WhatsApp sent to ${formattedPhone}`);

    // Update status to "MSG sent"
    await updateStatus(account.accountid, STATUS.MSG_SENT);
  } catch (err) {
    // Don't fail the whole webhook if WhatsApp fails — lead is already in CRM
    console.error(`[REA Lead Webhook] WhatsApp failed for ${formattedPhone}:`, err);
  }

  // ── 3. Notify team ───────────────────────────────────────────────────────

  const sourceLabel = SOURCE_LABELS[source] ?? source;
  const now = new Date().toLocaleString("he-IL", { timeZone: "Asia/Jerusalem" });
  const teamMsg = buildTeamNotification({ name, phone, email, sourceLabel, campaignLabel, now });

  await Promise.allSettled([
    sendText(TEAM_PHONE_ITAY, teamMsg),
    sendText(TEAM_PHONE_NOAM, teamMsg),
  ]);

  return {
    success: true,
    accountId: account.accountid,
    accountNumber: account.accountnumber,
  };
}

// ── Team notification message ────────────────────────────────────────────────

function buildTeamNotification(data: {
  name: string;
  phone: string;
  email?: string;
  sourceLabel: string;
  campaignLabel: string;
  now: string;
}): string {
  const lines = [
    `🆕 *ליד חדש נכנס ל-CRM*`,
    ``,
    `👤 *שם:* ${data.name}`,
    `📱 *טלפון:* ${data.phone}`,
  ];

  if (data.email) lines.push(`📧 *מייל:* ${data.email}`);

  lines.push(
    `📌 *מקור:* ${data.sourceLabel}`,
    `📣 *קמפיין:* ${data.campaignLabel}`,
    `🕐 *שעה:* ${data.now}`,
    ``,
    `➡️ נכנס אוטומטית ל-Fireberry ✅`,
  );

  return lines.join("\n");
}
