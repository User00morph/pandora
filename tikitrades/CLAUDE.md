# CLAUDE.md

This file provides guidance to Claude (or any agent) when working inside this repository.

## What This Repository Is

TikiTrades is Tiki's personal file-system OS, structured as a standalone mirror of the Pandora OS architecture (the parent system it was derived from). It exists so that any agent — running on Tiki's own computer — can open this folder, orient itself, and act on her behalf without needing the rest of Pandora loaded.

It starts with one department (Trading). More departments are added over time, following the same mirrored pattern, as Tiki's needs expand beyond trading.

## Session Protocol

1. Read `tikitrades.md` first — the master context file. Identity, department list, routing table, naming conventions, operating protocol.
2. Identify which department the task belongs to (currently: Trading only).
3. Read that department's **`ref_[code].md`** first — the orientation card. It tells you exactly which files to load next. Do not load the full `context.md` unless the ref card routes there.
4. Load only the active workflow stage file from `D.[code]/workflow/`.
5. Load only the skill file(s) the current stage needs from `D.[code]/skills/`.
6. Confirm understanding before executing any trade, or any action that commits real capital.
7. Update the department's ref card Current State (DONE / DECIDED / NEXT) at the end of every session.

## Context Hygiene

Same discipline as the parent Pandora OS — load only what the current task needs:

```
L0 — tikitrades.md              Always loaded. Identity + routing.
L1 — ref_[code].md              On department entry. Routing card.
L2 — wf_stage-[N].md            Per task. Stage contract.
L3 — skills / frameworks        Selective. Apply as strategy logic.
L4 — logs / config              Selective. Read/write as working data.
```

## Confirmation Required Before

- Placing or closing any live trade
- Changing risk parameters (position size, stop-loss rules, capital allocated)
- Deleting any log or record
- Any irreversible action

## File Naming Convention

```
[dept-code]_[type]_[descriptive-name]_[status/version].md
```
- Dept codes: `trd` (Trading) — new codes added as new departments are created
- Types: `framework`, `strategy`, `log`, `config`, `protocol`
- Status: `_draft`, `_active`, `_v1`, `_v2`, `_archived`

## Repository Structure

```
tikitrades.md         — Master context file (read first every session)
D.TRD/                 — Trading department
  ref_trd.md           — Orientation card
  context.md           — Full department context (load only when ref card routes to it)
  workflow/            — Stage-split workflow files
  skills/              — Loadable strategy/process skills
  frameworks/          — Core strategy documents
  logs/                — Trade journal, one file per month
  _config/             — Tiki's trading profile (capital, broker, risk rules)
```

Each future department follows this same shape: `ref_[code].md`, `context.md`, `workflow/`, `skills/`, plus whatever working-file folders that domain needs (mirroring `frameworks/` + `logs/` + `_config/` here).
