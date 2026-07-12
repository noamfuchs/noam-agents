/**
 * Daily Morning Report — REA System
 * ====================================
 * Runs every day at 8:00am (set up as a Base44 cron).
 * Queries Fireberry for pipeline status and sends a WhatsApp report to the team.
 *
 * HOW TO ADD IN BASE44:
 *   App Settings → Backend Functions → New Function
 *   Name it "rea_daily_report"
 *   Paste this file
 *   Then go to App Settings → Scheduled Tasks → Add Task
 *     Function: rea_daily_report
 *     Schedule: 0 8 * * *  (every day at 8:00am Israel time)
 *
 * ENV VARS (same as lead_webhook — all shared):
 *   FIREBERRY_TOKEN
 *   WHATSAPP_TOKEN
 *   WHATSAPP_PHONE_NUMBER_ID
 *   TEAM_PHONE_ITAY
 *   TEAM_PHONE_NOAM
 */

import { getAllAccounts, STATUS, daysSince, FireberryAccount } from "./fireberry.ts";
import { sendText } from "./whatsapp.ts";

const TEAM_PHONE_ITAY = Deno.env.get("TEAM_PHONE_ITAY")!;
const TEAM_PHONE_NOAM = Deno.env.get("TEAM_PHONE_NOAM")!;

// Thresholds (days)
const DAYS_UNTOUCHED_WARN     = 2;  // MSG sent but no update for 2+ days
const DAYS_FOLLOWUP_STUCK     = 3;  // In "Follow Up" for 3+ days without change
const DAYS_NEW_LEAD_WAITING   = 1;  // In "New Lead" for 1+ day without contact

// ── Main handler ─────────────────────────────────────────────────────────────

export default async function handler() {
  const allAccounts = await getAllAccounts();

  const today   = new Date();
  const todayStr = today.toLocaleDateString("he-IL", { timeZone: "Asia/Jerusalem" });

  // ── Segment accounts ───────────────────────────────────────────────────

  const newToday   = allAccounts.filter(a => daysSince(a.createdon) === 0);
  const newYesterday = allAccounts.filter(a => daysSince(a.createdon) === 1);

  const untouched  = allAccounts.filter(a =>
    a.statuscode === STATUS.MSG_SENT &&
    daysSince(a.modifiedon) >= DAYS_UNTOUCHED_WARN
  );

  const newWaiting = allAccounts.filter(a =>
    a.statuscode === STATUS.NEW_LEAD &&
    daysSince(a.modifiedon) >= DAYS_NEW_LEAD_WAITING
  );

  const stuckFollowUp = allAccounts.filter(a =>
    a.statuscode === STATUS.FOLLOW_UP &&
    daysSince(a.modifiedon) >= DAYS_FOLLOWUP_STUCK
  );

  const contracts = allAccounts.filter(a =>
    a.statuscode === STATUS.CONTRACT_SENT
  );

  const paidTotal  = allAccounts.filter(a => a.statuscode === STATUS.PAID).length;
  const openLeads  = allAccounts.filter(a =>
    [STATUS.NEW_LEAD, STATUS.MSG_SENT, STATUS.FOLLOW_UP].includes(a.statuscode as any)
  ).length;

  // ── Build report message ────────────────────────────────────────────────

  const lines: string[] = [
    `📊 *דוח בוקר — REA | ${todayStr}*`,
    ``,
    `━━━━━━━━━━━━━━━━━━━━━`,
    ``,
    `📈 *סיכום כללי*`,
    `• לידים פתוחים: ${openLeads}`,
    `• לקוחות ששילמו: ${paidTotal}`,
    ``,
  ];

  // New leads yesterday
  if (newYesterday.length > 0) {
    lines.push(`🆕 *לידים חדשים אתמול (${newYesterday.length})*`);
    for (const a of newYesterday.slice(0, 10)) {
      lines.push(`• ${a.accountname} | ${a.telephone2 ?? "—"} | ${a.pcfsystemfield3 ?? "—"}`);
    }
    lines.push(``);
  } else {
    lines.push(`🆕 *לידים חדשים אתמול:* אין`, ``);
  }

  // Leads needing contact (New Lead, 1+ day)
  if (newWaiting.length > 0) {
    lines.push(`🔴 *מחכים לטיפול ראשוני (${newWaiting.length})*`);
    for (const a of newWaiting.slice(0, 10)) {
      lines.push(`• ${a.accountname} | ${a.telephone2 ?? "—"} | ${daysSince(a.createdon)} ימים`);
    }
    lines.push(``);
  }

  // Untouched after message sent
  if (untouched.length > 0) {
    lines.push(`📞 *הודעה נשלחה אך לא טופלו (${untouched.length})*`);
    for (const a of untouched.slice(0, 10)) {
      lines.push(`• ${a.accountname} | ${a.telephone2 ?? "—"} | ${daysSince(a.modifiedon)} ימים`);
    }
    lines.push(``);
  }

  // Stuck in follow-up
  if (stuckFollowUp.length > 0) {
    lines.push(`⚠️ *תקועים ב-Follow Up (${stuckFollowUp.length})*`);
    for (const a of stuckFollowUp.slice(0, 10)) {
      lines.push(`• ${a.accountname} | ${a.telephone2 ?? "—"} | ${daysSince(a.modifiedon)} ימים`);
    }
    lines.push(``);
  }

  // Contracts out — close to closing
  if (contracts.length > 0) {
    lines.push(`💰 *חוזה נשלח — קרוב לסגירה (${contracts.length})*`);
    for (const a of contracts) {
      lines.push(`• ${a.accountname} | ${a.telephone2 ?? "—"} | ${a.ownername}`);
    }
    lines.push(``);
  }

  // Footer
  const urgentCount = newWaiting.length + untouched.length + stuckFollowUp.length;
  if (urgentCount === 0) {
    lines.push(`✅ *הכל מטופל — יום מעולה!*`);
  } else {
    lines.push(`‼️ *${urgentCount} לידים דורשים טיפול היום*`);
  }

  const report = lines.join("\n");

  console.log("[REA Daily Report] Sending report to team...");
  console.log(report);

  await Promise.all([
    sendText(TEAM_PHONE_ITAY, report),
    sendText(TEAM_PHONE_NOAM, report),
  ]);

  return {
    success: true,
    reportDate: todayStr,
    stats: {
      openLeads,
      paidTotal,
      newYesterday: newYesterday.length,
      urgentCount,
    },
  };
}
