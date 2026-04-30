# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

Pandora OS is a knowledge architecture and sovereign operating system created by Morph. It is not a software codebase — it is a structured markdown-based framework of 12 interconnected departments, each with its own context file, workflow, skills, and output artifacts. The master context file is `pandora.md` — **read it at the start of every session**.

## Session Protocol

1. Read `pandora.md` first — it contains the sovereign declaration, all 12 department definitions, the routing table, naming conventions, and operating protocol.
2. Identify which department the user's task belongs to using the routing table (Section 5 of `pandora.md`).
3. Read the relevant department's `context.md` (or `Context.md`) — it contains the department's purpose, functions, and **skill routing table**.
4. Read the department's `workflow.md` when executing a multi-step task.
5. Load specific skills from `skills/` only when the workflow stage calls for them — do not read all skills upfront.
6. Confirm understanding before executing consequential tasks.

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
skills/                     — Layer 3: Loadable skill files (on-demand, not global)
skills/INDEX.md             — Skill library index with department mappings

D.S.C/                      — Systems Cultivation & Project Creations (the spine)
D.R.D/                      — Sovereign Research & Deconstruction / Reconstruction
D.C.E/                      — Content Creation & Expression
D.S.E/                      — Sovereign Entrepreneurship
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
celestial archetypes.pdf    — Reference material
```

Each department folder contains:
- `context.md` (or `Context.md`) — department purpose, functions, skill routing table
- `workflow.md` — staged pipeline for the department's core process

## Skills Library

Skills are reusable process files in `skills/` that are loaded at specific workflow stages. Each department's context file has a **Skill Routing Table** that maps stages to skills.

| Skill | File | Primary Departments |
|-------|------|-------------------|
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
