# TIKITRADES.MD
## The Master Context File — Read First Every Session

---

## WHAT THIS IS

TikiTrades is Tiki's own file-system OS — a standalone mirror of the Pandora OS architecture, built so that any agent can read this folder and act on her behalf directly, without the rest of Pandora loaded.

It is derived from Pandora's structure (Layer 1 master file → Layer 2 department context → Layer 3 skills) but stands independently. It grows the same way Pandora does: one department at a time, each with its own orientation card, workflow, and skills, loaded on demand rather than all at once.

**Current scope:** Trading only. Additional departments (whatever domains of Tiki's life she wants a file system for) are added later, following the same pattern.

---

## THE DEPARTMENTS

| # | Code | Department | Core Purpose | Status |
|---|------|-----------|--------------|--------|
| 1 | D.TRD | Trading | Day-trading strategy, execution, and trade journaling | Active — build in progress |

*(New rows added here as new departments are created.)*

---

## THE ROUTING TABLE

| Task or Topic | Department | Read First | Then Read | Workflow |
|--------------|-----------|-----------|----------|----------|
| Trading strategy, charts, trade execution, trade review | D.TRD | `D.TRD/ref_trd.md` | Skill routing table | `D.TRD/workflow/` |
| Anything outside trading | — | Not built yet — flag to Tiki/Morph before proceeding | — | — |

---

## CONTEXT HYGIENE (Same 5-Layer System as Pandora)

```
L0 — tikitrades.md              Always loaded. Identity + routing.
L1 — ref_[code].md              On department entry. Routing card.
L2 — wf_stage-[N].md            Per task. Stage contract.
L3 — skills / frameworks        Selective. Apply as strategy logic.
L4 — logs / config              Selective. Read/write as working data.
```

Never load a full department `context.md` when the ref card already answers the question. Never load all skills — only what the active workflow stage calls for.

---

## FILE NAMING CONVENTION

```
[dept-code]_[type]_[descriptive-name]_[status/version].md

DEPARTMENT CODES:
trd (Trading) — more added as new departments are created

TYPE EXAMPLES:
framework / strategy / log / config / protocol

STATUS:
_draft / _active / _v1 / _v2 / _archived

EXAMPLES:
trd_framework_support-resistance-system_v1.md
trd_log_trades_2026-07.md
trd_config_tiki-profile.md
```

---

## OPERATING PROTOCOL

```
STEP 1 — READ
Read tikitrades.md in full at the start of every session.

STEP 2 — ORIENT
Identify the department from the task (currently: Trading only).

STEP 3 — NAVIGATE
Open the department's ref card. Read only what the task requires.

STEP 4 — LOAD WORKFLOW AND SKILLS
Read the active workflow stage file.
Load only the skill(s) that stage calls for.

STEP 5 — ALIGN
Confirm understanding of the task before executing — especially
before anything that touches real capital.

STEP 6 — EXECUTE
Produce the analysis, plan, or trade action with precision.

STEP 7 — LOG
Update the trade log and the department's ref card Current State
(DONE / DECIDED / NEXT) before the session ends.
```

**Confirmation required before:**
- Placing or closing any live trade
- Changing risk parameters (position size, stop-loss, capital allocated)
- Deleting any file or record
- Any irreversible action

**How Claude (or any agent) handles ambiguity:**
Ask one precise clarifying question. Never assume Tiki's risk tolerance, capital, or intent on a live trade.

---

## RELATIONSHIP TO PANDORA

TikiTrades is derived from Pandora's Sovereign Trading Intelligence System (STIS) — the strategy logic here is refined and simplified from `D.S.E/trading/` in the parent Pandora repository, scoped specifically to Tiki's trading profile and starting focus (support/resistance based strategies). It does not require Pandora to be loaded to function, but the parent system is the reference source when a strategy needs deeper research or expansion.

---

*TikiTrades | v0.1 | 1 Department Active | Owner: Tiki*
