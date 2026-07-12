# Crohn's Companion (Israel) — Build Plan

Status: build, Phase 0 (validate + design partner)
Owner: Noam + brother (co-founder, has Crohn's, domain expert + community channel)
Created: 2026-06-21

## One-line
An iOS-first, Hebrew companion app for Crohn's patients in Israel: log diet and symptoms, import your own blood/lab results, and see your inflammation, symptoms, and diet on one timeline with plain-language insights. No HMO deal required to launch.

## Locked decisions
- **Scope:** Crohn's-focused messaging. (Build the data model IBD-generic so flipping on ulcerative colitis later is a config flag, not a rewrite. Market: ~28k Crohn's, ~52k total IBD.)
- **Platform:** iOS native via Expo / React Native (HealthKit + wearables are core).
- **Commitment:** Real build, brother as co-founder and first design partner.

## The strategic core: the data workaround
No HMO data pipe at launch. The patient already owns their data and sees it in their kupah app (Clalit / Maccabi / Meuhedet / Leumit) as viewable or downloadable PDFs. Architecture is patient-mediated, bring-your-own-data:

- Patient pulls their own blood panel from their kupah app and uploads the PDF or a photo. **Claude vision reads the Hebrew lab report** and extracts the IBD markers: fecal calprotectin, CRP, hemoglobin, albumin, ferritin, platelets, white count.
- Works identically across all four kupot because we never integrate with any of them. Sidesteps the killer risk (live HMO API access) entirely.
- Direct HMO integration becomes a later upgrade that removes upload friction, negotiated from a position of leverage once there are users + outcome data.

Other inputs, also no HMO needed:
- Wearables/trackers via Apple HealthKit (steps, sleep, HR, weight; Apple Watch, Oura, Garmin, Whoop, Fitbit).
- Home calprotectin (IBDoc / CalproSmart) photographed or entered.
- Diet via photo-based food logging (Claude vision) + quick-add favorites.
- Symptoms via fast daily check-in (Bristol, pain, urgency, blood, fatigue, BM count).

## MVP (build only this first)
One loop: log diet + symptoms, import labs, see the correlation, get a plain-language insight.

Killer screen (nobody has localized this for Israel): a single timeline overlaying calprotectin/CRP trend vs symptoms vs diet patterns, with a weekly Hebrew Claude-generated insight ("flare-ups cluster 1-2 days after high-fat dairy; calprotectin rose 180 -> 340 over that period").

Cut for v1: community feed, clinician dashboard, meal-plan generator, medication-interaction engine, anything needing a third party.

## Differentiation vs the ~10 existing trackers
1. Hebrew/RTL-first, built around Israeli lab reports.
2. Near-automatic lab capture via AI OCR (the #1 friction point in every competitor).
3. Genuinely useful correlation insights, not just charts.
4. Crohn's-specific framing and education (brother as authentic voice).

## Tech stack (matches Noam's existing stack)
- Expo / React Native (iOS first) — HealthKit access requires native.
- Supabase: auth, Postgres + RLS, encrypted storage for lab files.
- Vercel: marketing site + API.
- Claude API: lab parsing (vision), food-photo parsing, insight narration.

## Roadmap
| Phase | Window | Goal | Exit signal |
|---|---|---|---|
| 0 Validate | Weeks 0-2 | Brother + 15-20 design-partner patients (Israel Foundation, Hebrew FB groups); lock marker list + symptom schema; sketch 4 screens; test Claude on real lab PDFs | 15+ patients commit to upload labs + log daily; lab parsing works |
| 1 MVP | Weeks 2-12 | Build the loop, Hebrew-first, ship TestFlight to brother + 20 | People log 2 weeks unprompted |
| 2 Insights + trackers | Months 3-6 | Correlation engine, HealthKit, retention; grow to a few hundred; capture outcome signal | 30%+ week-4 retention |
| 3 Monetize | Months 6-12 | Pharma-sponsored program pitch (Takeda/AbbVie/J&J Israel) + clinic pilot (Schneider or Sheba) using real usage + outcome data | First paid pilot signed |
| 4 Direct integration | 12+ | Kupat-cholim API access to kill the upload step | Clalit/Maccabi data deal |

## Guardrails (lock before launch)
- Stay out of medical-device regulation (AMAR): position as wellness/tracking/education, never diagnosis or treatment. Insights are lifestyle/diet patterns, not medical advice. Get a 1-hour legal read first.
- Israeli Privacy Law: explicit consent, encryption at rest, data residency, easy delete. Health data is sensitive-category.

## Kill criterion
The whole thesis rests on one behavior: will patients upload their labs and log for two weeks? If the first 20 will not, no feature fixes it — pivot. Retention in Phase 1, not features, is the only metric that matters.

## First five actions this week
1. Brother lists every value on his last kupah blood report -> fix the exact marker schema.
2. Collect 3-5 real anonymized Israeli lab PDFs (different kupot); test Claude vision extraction. This one experiment validates the whole workaround.
3. Post in 2-3 Israeli IBD Facebook groups + the Israel Foundation -> line up 15-20 design partners.
4. Draw the 4 core screens (daily check-in, lab upload, correlation timeline, weekly insight).
5. Scaffold the Expo + Supabase project.

## Open / next
- Run Vera (devil's advocate) on the plan, killer question = will patients actually upload labs.
- Competitive teardown of what Israeli Crohn's patients already have (Hebrew apps, kupah app features).
- Monetization detail: pharma patient-support program economics in Israel.
