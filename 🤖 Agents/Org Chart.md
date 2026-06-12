# 🏛️ Noam Fuchs — Life-OS Org Chart

> **Operating contract:** You are the CEO. Ari runs the team. Agents execute. You decide. Everything is remembered in the Brain.

You talk to **one** agent (Ari, the Chief of Staff). Ari routes work, runs the quality gate, and files every output back into this vault. You never have to remember skill names or folder paths.

This is a **Unified Life-OS**: one company, divided by life-area, not a collection of separate bots.

---

## Line legend (how to read the chart)

- **Solid line** = you talk to them directly.
- **Dotted line** = coordinate via Ari (the orchestrator).
- **Dashed line** = advisory (they advise you, they do not execute).

---

## The chart

```
            NOAM — CEO   "You decide. Everything is remembered in the Brain."
                                   |
   Iris ········  ARI — Chief of Staff (COO)  ········ Finn
   System Guide    orchestrates · routes · runs         CFO
   [advisory]      the gate · files to the Brain     [advisory]
                                   |
                    "You talk only to Ari"
   +--------------------- OPERATING TEAM (Ari manages) ---------------------+
   |  PRODUCERS                                                             |
   |   Remy        Sloan        Quinn        Dex          Cora              |
   |   Researcher  Strategist   Copywriter   Analyst      Archivist         |
   |   web/deep    ventures     your voice   structures   capture into      |
   |   research    & growth                  raw input    the vault         |
   |                                                                        |
   |  QUALITY GATE                          SPECIALISTS                     |
   |   Gabe — Gatekeeper                      Mona   Personal Assistant     |
   |    verifies before anything             Tess   Studies Coach          |
   |    lands or ships                        Hale   Health Coach          |
   |   Vera — Devil's Advocate                Nina   Relationships         |
   |    challenges decisions                  Sol    Social Ops            |
   +------------------------------------------------------------------------+
```

---

## Roster

| Persona | Role | Division | Line | Backed by | Status |
|---|---|---|---|---|---|
| **Noam** | CEO | — | — | you | — |
| **Ari** | Chief of Staff (orchestrator) | Command | solid | `CLAUDE.md` agent-manager role + this Claude session | live |
| **Iris** | System Guide | Advisory | dashed | `onboard` skill | live |
| **Finn** | CFO | Advisory | dashed | `finance` skill | live |
| **Cora** | Archivist / capture | Knowledge | dotted | `brain-bot` + `wa-bridge` | live (bridge flapping) |
| **Dex** | Analyst | Knowledge | dotted | `process-meetings`, `fathom-sync`, `capture` | live |
| **Remy** | Researcher | Knowledge | dotted | `deep-research` skill | live |
| **Sloan** | Strategist | Ventures | dotted | Nona, Real Estate course, RFS, REA | live |
| **Quinn** | Copywriter | Ventures | dotted | `copywrite`, `draft-message`, `whatsapp-formatting` | live |
| **Gabe** | Gatekeeper (quality gate) | QA | dotted | `~/.claude/agents/gatekeeper.md` | **new** |
| **Vera** | Devil's Advocate | QA | dotted | `~/.claude/agents/devils-advocate.md` | **new** |
| **Mona** | Personal Assistant | Cadence | dotted | `morning-preview`, `evening-review`, `schedule`, `weekly-digest` | live |
| **Tess** | Studies Coach | Growth | dotted | `sem2-coach` subagent | live |
| **Hale** | Health Coach | Health | dotted | `fitness` skill | live |
| **Nina** | Relationships | People | dotted | `person-prep`, `guest-one-pager` | live |
| **Sol** | Social Ops | People | dotted | `igunfollow` | live |

---

## How "agents check each other" (the gate)

Producing agents never write to the Brain or send anything outbound on their own. They hand the result to **Gabe (Gatekeeper)** first.

```
  agent produces  ->  Gabe verifies  ->  PASS -> lands in Brain / goes outbound
                                     \->  FAIL -> back to the agent with fixes
```

Gabe checks four things: factual correctness (no invented numbers, names, or dates), correct filing location, no duplication of an existing note, and compliance with `memory/boundaries.md`. For high-volume capture, Gabe **samples** rather than reviewing every line, to stay cheap.

**Vera (Devil's Advocate)** is invoked on demand for decisions, not on every output. Before a real-estate move, a venture call, or a strategy commit, Ari sends the plan to Vera to surface the strongest counter-arguments and failure modes. Vera pairs with `decision-recall`.

---

## Org hygiene (from the 2026-06-05 audit)

Three launch agents are dead or duplicate and should be retired:

- `com.user.secondbrain.bot` — exact duplicate of the live `brain-bot`. Dormant.
- `com.user.texti-bot` — second copy of Message Formatter (in `noam-agents/`). Dormant.
- `com.noam.messageformatter` — points at `~/Desktop/MY BRAIN`, which no longer exists. Failing (exit 78).

One live risk: `com.user.secondbrain.wa-bridge` (Cora's transport) is running but exiting 1. Capture reliability depends on fixing it.

Source of truth is clean: canonical vault is `~/Dropbox/MY BRAIN`; `~/MY BRAIN` and `~/second-brain` are symlinks to it.

---

*Maintained by Ari. Last updated from the agent audit on 2026-06-05.*
