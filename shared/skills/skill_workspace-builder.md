# Skill: Workspace Builder
## Primary Departments: D.S.C, D.S.E, D.I.I
## Load at: New project inception, new client onboarding, new department build

Builds customized workspace structures for any Pandora OS project. Diagnosis before assembly. Never build before understanding. The questions ARE the skill.

---

## WHEN TO USE

- Morph initiates a new project, department subdomain, or client engagement
- An existing workflow needs restructuring for handoff readiness
- A new content format or business service needs a dedicated workspace

---

## PHASE 1 — DIAGNOSIS (ask before building)

Ask these questions. Wait for each answer before proceeding.

**Q1: What does this workspace produce?**
The core deliverable. Not the process — the output. What exists at the end that did not exist at the start?

**Q2: How does work enter the workspace?**
What triggers a new cycle? Where does the input come from? Is it complete when it arrives or does it require triage?

**Q3: What are the distinct cognitive modes in the work?**
Each mode that requires you to think differently = one stage. Research mode and writing mode are different. Analysis mode and delivery mode are different. Do not combine modes into a single stage.

**Q4: Where does human judgment matter most?**
These are the leverage points — the stage transitions where review happens before moving forward. If you automate past a judgment point, quality degrades downstream.

**Q5: What reference material stays stable across all cycles?**
Brand rules, voice constraints, business rules, quality standards. These go in _config/. They should never sit inside a stage folder.

**Q6: What does "done" look like for the most common output?**
Specific. Testable. Not "good quality" — the criteria by which done is determined.

---

## PHASE 2 — ASSEMBLY

Based on answers:

**1. Determine stages.** Map each distinct cognitive mode to a numbered stage. Most workflows: 3-5 stages. Fewer than 3 = stages are being combined (split them). More than 5 = stages are too granular for now (combine, add back when the workflow earns it).

**2. Build folder structure:**
```
[workspace-name]/
  CLAUDE.md          ← L0: entry point, orientation, routing table
  CONTEXT.md         ← L1: stage map, how stages connect, reference list
  01_[stage-name]/
    CONTEXT.md       ← L2: stage contract (inputs, process, done criteria)
    output/          ← handoff point to next stage
  02_[stage-name]/
    CONTEXT.md
    output/
  [...]
  _config/           ← L3: stable reference (constraints, rules, standards)
  _templates/        ← L3: reusable output structures
```

**Naming rules:**
- Numbered prefix (01_, 02_) = workflow stages, in execution order
- Underscore prefix (_config, _templates) = support folders, not stages
- output/ in every stage = explicit handoff point

**3. Write CLAUDE.md (L0):**
```
# [Workspace Name]
## What This Is
[One paragraph: what it produces and for whom]
## Current State
[Three lines: done / in progress / next]
## Structure
[Folder map with one-line purpose per folder]
## How to Use
[3-5 steps from start to finish]
## Key Decisions
[Bullet list: significant design choices and why — ADR pattern]
```

**4. Write CONTEXT.md (L1):**
- Stage map table: stage name, purpose, inputs, output location
- How stages connect (what feeds what)
- Where human review happens
- Reference material locations

**5. Write stage contracts (L2 per stage) — ICM format:**

Every stage CONTEXT.md uses exactly this three-section shape. No exceptions.

```markdown
## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | ../01-[name]/output/ | Full file | Source material |
| Constraints | _config/constraints.md | "Non-negotiables" section | Rules to apply |
| Skill | shared/skills/skill_X.md | [Specific section] | [What it provides] |

## Process

1. Step one
2. Step two — ⚑ CHECKPOINT (present [X] before proceeding)
3. Step three

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| [artifact-name] | output/[topic-slug]-[artifact].md | Markdown |
```

**Stage handoff rule:** Stage N writes to `stages/0N-name/output/`. Stage N+1's CONTEXT.md reads from `../0N-name/output/`. Human edits the output file — next stage picks up the edited version. No orchestration layer. Just files.

**File naming in output folders:** `[topic-slug]-[stage-artifact].md`
Example: `sovereign-entity-script.md`, `sovereign-entity-spec.md`

**6. Populate _config/:**
- constraints.md — non-negotiable rules for this workspace
- quality-standards.md — what "good" looks like, stated as testable criteria
- [domain-specific context] — business rules, voice file, client brief

**7. Add checkpoints to creative stages:**

Any stage where the model makes creative or interpretive decisions needs at least one checkpoint — a pause where a completed unit of work is presented and Morph steers before the next unit begins. Linear stages (extraction, conversion, rendering) run straight through.

```markdown
## Checkpoints

| After Step | Agent Presents | Morph Decides |
|------------|----------------|---------------|
| Step 2 | Draft framework options | Which direction to develop |
| Step 4 | Full first draft | Approve or redirect before polish |
```

**8. Add audit sections to build stages:**

Build and creative stages run a quality audit after completing the process but before writing to output/. Each check must have an unambiguous pass/fail condition. If any check fails, agent revises before saving.

```markdown
## Audit

| Check | Pass Condition |
|-------|---------------|
| [Check name] | [Specific, testable condition] |
| Stage outputs nothing unnecessary | Output file contains only deliverable — no process notes |
```

---

## PHASE 3 — ORIENTATION

Walk through what was built:
- "The stage split is here because [Q3 answer]"
- "The _config/ files are where [stable reference] lives — never duplicate them inside stages"
- "Human review happens at [Q4 answer] — these are non-negotiable"
- "First thing to populate after this build: [most impactful _config/ file]"

---

## QUESTIONNAIRE DESIGN RULES (ICM Pattern 8)

When building a workspace that will be used repeatedly, design a setup questionnaire. Rules:

1. **Flat structure.** No category groupings. Numbered list only.
2. **All at once.** Every question appears in one pass. Morph answers everything in a single message.
3. **System-level only.** Configure things that stay stable across runs: brand, voice, design, defaults. Per-run details are collected conversationally at each pipeline start.
4. **Derive, do not ask.** If a field can be inferred from another answer, the agent fills it in. Do not add a question for something that can be derived.
5. **Sensible defaults.** Every question has a default or example so Morph can skip what they don't care about.
6. **Ask once, never again.** After setup, answers are baked into workspace files permanently via `{{PLACEHOLDER}}` replacement.

**Questionnaire structure:**
```markdown
# [Workspace] Setup

Answer all questions in one message. Defaults shown where applicable.

1. [System-level question] (default: [example])
2. [System-level question] (default: [example])
   — Derived from Q2: [derived field] (agent fills this in)
3. [System-level question]
```

---

## PANDORA OS WORKSPACE TYPES

| Type | Primary Dept | Template |
|------|-------------|---------|
| Research pipeline | D.R.D | 6-stage (deconstruct → deploy) |
| Content production | D.C.E | 3-stage (research → script → produce) |
| Client engagement | D.S.E | 4-stage (discovery → build → review → handoff) |
| Software build | D.I.I | 4-stage (nigredo → albedo → citrinitas → rubedo) |
| Project creation | D.S.C | 4-stage (nigredo → albedo → citrinitas → rubedo) |

---

## HANDOFF READINESS CHECKLIST

Before considering any workspace complete:

```
□ Can someone open the folder and know what it is? (CLAUDE.md answers in first paragraph)
□ Can someone see the workflow? (Stages numbered, CONTEXT.md explains flow)
□ Can someone run a stage without asking? (Each stage contract has Inputs/Process/Done/Outputs table)
□ Can someone change a reference without breaking things? (_config/ separate from stages)
□ Can someone understand why things are this way? (Key Decisions in CLAUDE.md)

ICM quality guardrails:
□ All CONTEXT.md / ref files: under 80 lines (routing only — never content)
□ All reference/skill files: under 200 lines (split if longer)
□ Inputs tables specify SECTIONS not just files (selective section routing)
□ All references are ONE-WAY (no circular dependencies — if A→B then B does not →A)
□ No content duplicated across files (one home per piece of information)
□ Creative stages have at least one checkpoint and an audit section
□ No stage outputs committed (output/ folders contain only .gitkeep before first run)
```

If any answer is NO — the workspace is not complete. Fix the weakest point first.
