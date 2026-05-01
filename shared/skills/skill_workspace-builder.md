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

**5. Write stage contracts (L2 per stage):**
```
# [Stage Name]
## Purpose
[What happens here in one sentence]
## Inputs
[Specific files from previous stage or config]
## Process
[Steps — with judgment checkpoints marked explicitly]
## Done looks like
[One sentence, testable]
## Output goes to
[Exact path]
```

**6. Populate _config/:**
- constraints.md — non-negotiable rules for this workspace
- quality-standards.md — what "good" looks like, stated as testable criteria
- [domain-specific context] — business rules, voice file, client brief

---

## PHASE 3 — ORIENTATION

Walk through what was built:
- "The stage split is here because [Q3 answer]"
- "The _config/ files are where [stable reference] lives — never duplicate them inside stages"
- "Human review happens at [Q4 answer] — these are non-negotiable"
- "First thing to populate after this build: [most impactful _config/ file]"

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
□ Can someone run a stage without asking? (Each stage contract has Inputs/Process/Done)
□ Can someone change a reference without breaking things? (_config/ separate from stages)
□ Can someone understand why things are this way? (Key Decisions in CLAUDE.md)
```

If any answer is NO — the workspace is not complete. Fix the weakest point first.
