# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

Pandora OS is a knowledge architecture and sovereign operating system created by Morph. It is not a software codebase — it is a structured markdown-based framework of 12 interconnected departments, each with its own context file, workflow, skills, and output artifacts. The master context file is `pandora.md` — **read it at the start of every session**.

## Session Protocol

1. Read `pandora.md` first — it contains the sovereign declaration, all 12 department definitions, the routing table, naming conventions, and operating protocol.
2. **INTAKE — MANDATORY before routing:** Load `shared/skills/skill_session-intake.md` and run the intake protocol. Ask the 6 questions. Refine answers through D.R.D logic. Confirm routing before proceeding. Skip only if continuing mid-session with no ambiguity.
3. Read the department's **`ref_[dept].md`** first (25–35 lines) — this is the orientation card that tells you exactly which files to load. Do NOT load the full context file unless the ref card explicitly routes to it.
4. Load only the active workflow stage file from `D.*/workflow/wf_stage-[N]_[name].md` — never the full workflow.
5. **SKILL SELECTION — MANDATORY before any build or research:**
   Load `shared/skills/skill_session-init.md` and run the full protocol.
   Surface the default active skills from the ref card.
   Present the full skill library to Morph.
   Ask which additional skills to activate.
   Do not begin work until Morph confirms the active skill set.
6. Load only the confirmed skills — targeted reads, headers + relevant sections.
7. Confirm understanding before executing consequential tasks.

## File Reading Protocol (Token Efficiency)

**Load `shared/skills/skill_file-extraction.md` before reading any file > 50 lines.**

- Header scan first (lines 1–15) before deciding to read further
- Use grep to locate sections before reading them — never scan by reading
- Use `offset` + `limit` on the Read tool for targeted section reads
- Read index files (DRD_INDEX.md, ref_*.md) before opening individual files
- Never load a full department context file when a ref card covers the session need

## Data Refinement Law

**All data entering the OS passes through D.R.D refinement before integration.**
See `shared/protocols/proto_data-refinement.md` for the full protocol.

## OS-Wide Protocols

| Protocol | File | Scope |
|----------|------|-------|
| Data Refinement | `shared/protocols/proto_data-refinement.md` | All departments — governs data entry |
| Context Hygiene (ICM) | `shared/protocols/proto_context-hygiene.md` | All departments — governs token loading |
| Session Log | `shared/protocols/proto_session-log.md` | All departments — end-of-session update |
| MCP Connectors | `shared/protocols/proto_mcp-connectors.md` | All departments — external tool connections |
| Development Railway | `shared/protocols/proto_dev-railway.md` | D.S.C + D.I.I — governs all repos, builds, agentic systems |

No raw content — from PDFs, repos, web, transcripts, or AI outputs — is written into department files, skills, workflows, or agent definitions without first passing the D.R.D tier and confidence system. Raw content is filed in `research/` only until refined.

## The Three-Layer Routing System

```
LAYER 1 — THE MAP (pandora.md)
Read first. Contains identity, all 12 departments, routing table,
naming conventions, operating protocol.
Always loaded. Tells Claude where to go.

LAYER 2 — DEPARTMENT CONTEXT (D.*/context.md + workflow.md)
Read when working in a specific department.
Contains: purpose, functions, skill routing table, workflow stages.
Only load the active department — not all 12.

LAYER 3 — SKILLS (skills/*.md)
Loaded on demand at specific workflow stages.
Each department's context file has a SKILL ROUTING TABLE
that maps workflow stages to specific skill files.
Never load all skills — only what the current stage requires.
```

## Repository Structure

```
pandora.md                  — Layer 1: Master context file (read first every session)
shared/skills/              — Loadable skill files (on-demand, not global)
shared/protocols/           — OS-wide operating protocols (active in all departments)
tools/mcp-servers/          — Local MCP server implementations
tools/apis/                 — Local API implementations
.claude/agents/             — Department and swarm agent definitions

D.S.C/                      — Systems Cultivation & Project Creations (the spine)
  ref_dsc.md                — Orientation card (read first, load only what it routes to)
  workflow/                 — Stage-split workflow files (load active stage only)
D.R.D/                      — Sovereign Research & Deconstruction / Reconstruction
  ref_drd.md                — Orientation card
  workflow/                 — Stage-split workflow files
D.C.E/                      — Content Creation & Expression
  ref_dce.md                — Orientation card
  workflow/                 — Stage-split workflow files
  _config/                  — Voice architecture (voice-and-tone / format-patterns / constraints)
D.S.E/                      — Sovereign Entrepreneurship
  ref_dse.md                — Orientation card
  workflow/                 — Stage-split workflow files
  clients/_template/        — Client engagement workspace (copy per new client)
D.R.A/                      — Real Estate & Sacred Architecture
D.H.S/                      — Holistic Home Sovereignty
D.I.I/                      — Infinite Intelligence — Techgnosis
D.S.S/                      — Sovereign Science
D.O.M/                      — Magik
D.P.S.A/                    — Personal Spiritual Autonomy & Personal Agency
D.B.S/                      — Holistic Body Sovereignty & Bodily Autonomy
D.S.M/                      — Sovereign Mechanics

the scrolls/                — The Pandora Codex (living doctrine)
research-deconstruction /   — Deconstructed research materials (note trailing space)
celestial archetypes.pdf    — Reference material (use skill_pdf-extraction.md)
```

Each department folder contains:
- `ref_[dept].md` — orientation card (read first — tells you what else to load)
- `context.md` (or `Context.md`) — full department context (load only when ref card routes to it)
- `workflow/` — stage-split workflow files (load active stage only, never the full set)

## Context Hygiene (ICM 5-Layer System)

All context loads follow this hierarchy. See `shared/protocols/proto_context-hygiene.md` for full rules.

```
L0 — pandora.md / CLAUDE.md      Always loaded. ~800 tokens. Orientation.
L1 — ref_[dept].md               On department entry. ~300 tokens. Routing.
L2 — wf_stage-[N].md             Per task. ~200-500 tokens. Stage contract.
L3 — skills / _config/           Selective. Reference material. Apply as constraints.
L4 — working files / outputs     Selective. Source material. Transform as input.
```

Token budget: Routing 10-15% | Reference (L3) 20-30% | Source (L4) 30-40% | Output room 20-30%

When loading both L3 reference and L4 source in the same session, label them explicitly:
`REFERENCE (L3 — apply as constraints):` and `SOURCE (L4 — transform this):`

## Session Log Discipline

At the end of every session, update the active department's ref card Current State section. Three bullets: DONE / DECIDED / NEXT. See `shared/protocols/proto_session-log.md`.

## Skills Library

Skills are reusable process files in `shared/skills/` loaded at specific workflow stages.

| Skill | File | Primary Departments |
|-------|------|-------------------|
| Session Intake | `skill_session-intake.md` | ALL — fire first, before routing, every new session |
| File Extraction | `skill_file-extraction.md` | ALL — load before reading any file > 50 lines |
| PDF Extraction | `skill_pdf-extraction.md` | D.R.D, D.I.I, D.S.S, D.B.S, D.R.A |
| Repo Extraction | `skill_repo-extraction.md` | D.I.I, D.S.C, D.R.D |
| System Design | `skill_system-design.md` | D.S.C, D.S.E, D.I.I, D.R.A, D.S.M |
| Source Evaluation | `skill_source-evaluation.md` | D.R.D, D.S.S, D.B.S, D.I.I, D.O.M |
| Sovereign Copywriting | `skill_copywriting.md` | D.C.E, D.S.E, D.S.C |
| Framework Synthesis | `skill_framework-synthesis.md` | D.R.D, D.S.C, D.S.S, D.I.I, D.P.S.A |
| Deal Analysis | `skill_deal-analysis.md` | D.R.A, D.S.E |
| Content Production | `skill_content-production.md` | D.C.E, D.S.E |
| Client Transmutation | `skill_client-transmutation.md` | D.S.E |
| Environment Audit | `skill_environment-audit.md` | D.H.S, D.R.A |
| Ritual Design | `skill_ritual-design.md` | D.O.M, D.P.S.A |
| Herb Profiling | `skill_herb-profiling.md` | D.B.S, D.R.D |
| Concept Distillation | `skill_concept-distillation.md` | D.R.D, D.C.E, D.S.S, D.P.S.A, D.I.I |
| Diagnostic Method | `skill_diagnostic-method.md` | D.S.M, D.S.C |
| PRD Creation | `skill_prd-creation.md` | D.S.C, D.I.I, D.S.E |
| Agentic Architecture | `skill_agentic-architecture.md` | D.I.I, D.S.C |
| Software Build Protocol | `skill_software-build-protocol.md` | D.I.I, D.S.C, D.S.E |
| Voice Architecture | `skill_voice-architecture.md` | D.C.E, D.S.E |
| Layer Triage | `skill_layer-triage.md` | D.S.C, D.S.E, D.I.I, D.R.D — load at project inception |
| Workspace Builder | `skill_workspace-builder.md` | D.S.C, D.S.E, D.I.I — load for new workspace creation |
| Capability Routing | `skill_capability-routing.md` | ALL — load when task type or output mode is unclear |
| YT-DLP Extraction | `skill_yt-dlp-extraction.md` | D.R.D, D.I.I, D.S.S, D.C.E, D.S.E — load when processing YouTube content |

## PRD Pattern

Before any complex build begins (software, multi-phase projects, autonomous Claude execution), a **Product Requirements Document** is produced first via `skills/skill_prd-creation.md`. Claude generates the draft; Morph reviews and approves before execution begins. Filed as `dsc_prd_[project-name]_v[X].md`.

## Key Relationships Between Departments

- **D.S.C connects to ALL** — it is the project conception and tracking spine.
- **D.R.D feeds ALL** — decoded research flows upstream into every department.
- **D.R.A and D.H.S** are parallel tracks (property + home environment).
- **D.I.I and D.O.M** overlap (technology and magik share the root "magh").
- **D.B.S and D.S.S** are intertwined (body sovereignty + sovereign science).
- **D.S.M and D.S.E** connect (mechanical shop as both knowledge domain and business).

## File Naming Convention

All output files follow this pattern — it serves as the navigation system:
```
[dept-code]_[type]_[descriptive-name]_[status/version].md
```
- Dept codes: `dsc_`, `drd_`, `dce_`, `dse_`, `dra_`, `dhs_`, `dii_`, `dss_`, `dom_`, `dpsa_`, `dbs_`, `dsm_`
- Types: `blueprint`, `research`, `protocol`, `script`, `ritual`, `decode`, `reconstruct`, `formula`, `framework`, `archive`, `project`, `audit`, `SOP`, `concept`, `log`, `prd`
- Status: `_draft`, `_final`, `_active`, `_v2`, `_v3`, `_archived`
- Time-sensitive files get a `YYYY-MM-DD` prefix.

## Important Operating Principles

- The five sub-doctrines (Channeling, Transmutation, Mirror, Data, Sovereignty) are active in every session regardless of department.
- There is no failure — only transmutation. Missed outputs become refined data about what better output requires.
- Never assume or guess on consequential tasks — ask one precise clarifying question.
- Confirmation is required before: publishing content, sending communications, executing financial transactions, deleting files, or any irreversible action.
- The `research-deconstruction ` directory has a trailing space in its name — use quotes when referencing it in commands.
