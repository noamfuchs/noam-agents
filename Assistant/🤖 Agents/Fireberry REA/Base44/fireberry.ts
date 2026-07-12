/**
 * Fireberry API Client — REA System
 * ==================================
 * Wrapper around the Fireberry REST API.
 * Base URL: https://api.fireberry.com/api/
 * Auth: tokenid header
 */

const FIREBERRY_TOKEN = Deno.env.get("FIREBERRY_TOKEN")!;
const FIREBERRY_BASE  = "https://api.fireberry.com/api";

// ── Status codes ────────────────────────────────────────────────────────────

export const STATUS = {
  NEW_LEAD:       6,
  MSG_SENT:       12,
  FOLLOW_UP:      14,
  CONTRACT_SENT:  2,
  PAID:           11,
  IRRELEVANT:     5,
} as const;

// ── Types ────────────────────────────────────────────────────────────────────

export interface NewLead {
  name:           string;
  phone:          string;
  email?:         string;
  source?:        string;  // webinar | instagram | campaign | referral | organic
  campaign_name?: string;
  landing_page?:  string;
  utm_params?:    Record<string, string>;
}

export interface FireberryAccount {
  accountid:      string;
  accountname:    string;
  telephone2:     string | null;
  emailaddress1:  string | null;
  statuscode:     number;
  status:         string;
  pcfsystemfield3: string | null; // Lead source
  pcfsystemfield5: string | null; // Campaign name
  description:    string | null;
  createdon:      string;
  modifiedon:     string;
  ownername:      string;
  accountageindays: number;
}

// ── API helpers ──────────────────────────────────────────────────────────────

async function fbFetch(path: string, options: RequestInit = {}) {
  const url = `${FIREBERRY_BASE}${path}`;
  const res = await fetch(url, {
    ...options,
    headers: {
      "tokenid": FIREBERRY_TOKEN,
      "Content-Type": "application/json",
      ...(options.headers ?? {}),
    },
  });

  const json = await res.json();
  if (!res.ok || json.success === false) {
    throw new Error(`Fireberry API error at ${path}: ${JSON.stringify(json)}`);
  }
  return json;
}

// ── Create a new lead ────────────────────────────────────────────────────────

export async function createLead(lead: NewLead): Promise<FireberryAccount> {
  const body: Record<string, unknown> = {
    accountname:      lead.name,
    telephone2:       formatIsraeliPhone(lead.phone),
    statuscode:       STATUS.NEW_LEAD,
  };

  if (lead.email)         body.emailaddress1   = lead.email;
  if (lead.source)        body.pcfsystemfield3 = lead.source;
  if (lead.campaign_name) body.pcfsystemfield5 = lead.campaign_name;
  if (lead.landing_page)  body.websiteurl      = lead.landing_page;
  if (lead.utm_params)    body.description     = JSON.stringify(lead.utm_params);

  const res = await fbFetch("/record/account", {
    method: "POST",
    body: JSON.stringify(body),
  });

  return res.data.Record as FireberryAccount;
}

// ── Update lead status ───────────────────────────────────────────────────────

export async function updateStatus(accountId: string, statusCode: number): Promise<void> {
  await fbFetch(`/record/account/${accountId}`, {
    method: "PUT",
    body: JSON.stringify({ statuscode: statusCode }),
  });
}

// ── Query accounts ───────────────────────────────────────────────────────────

export async function getAccounts(params: {
  pageSize?: number;
  pageNumber?: number;
  filter?: string;
} = {}): Promise<{ total: number; records: FireberryAccount[] }> {
  const qs = new URLSearchParams();
  if (params.pageSize)   qs.set("PageSize",   String(params.pageSize));
  if (params.pageNumber) qs.set("PageNumber",  String(params.pageNumber));
  if (params.filter)     qs.set("$filter",     params.filter);

  const res = await fbFetch(`/record/account?${qs}`);
  return {
    total:   res.data.Total_Records,
    records: res.data.Records as FireberryAccount[],
  };
}

// ── Get accounts by status ────────────────────────────────────────────────────

export async function getAccountsByStatus(statusCode: number, pageSize = 50) {
  return getAccounts({ filter: `statuscode eq ${statusCode}`, pageSize });
}

// ── Get all accounts (paginated) ─────────────────────────────────────────────

export async function getAllAccounts(): Promise<FireberryAccount[]> {
  const first = await getAccounts({ pageSize: 50, pageNumber: 1 });
  const all: FireberryAccount[] = [...first.records];

  const totalPages = Math.ceil(first.total / 50);
  for (let page = 2; page <= totalPages; page++) {
    const next = await getAccounts({ pageSize: 50, pageNumber: page });
    all.push(...next.records);
  }

  return all;
}

// ── Helpers ──────────────────────────────────────────────────────────────────

export function formatIsraeliPhone(raw: string): string {
  let digits = raw.replace(/\D/g, "");
  if (digits.startsWith("972")) return digits;
  if (digits.startsWith("0"))   digits = digits.slice(1);
  return "972" + digits;
}

export function daysSince(dateStr: string): number {
  const ms = Date.now() - new Date(dateStr).getTime();
  return Math.floor(ms / (1000 * 60 * 60 * 24));
}
