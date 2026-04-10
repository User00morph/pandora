# SKILL — PRD CREATION (Product Requirements Document)
**Loadable by: D.S.C, D.I.I, D.S.E**

---

## WHAT THIS SKILL IS

The ability to produce a Product Requirements Document before any complex build begins. A PRD translates a vision into a structured specification that an AI agent or a human builder can execute against without ambiguity. Loaded whenever a project moves from concept to build — especially in D.S.C when a blueprint needs to become an actionable build plan.

---

## WHEN TO USE

```
- Before building any software, tool, or application
- Before building any complex system with multiple phases
- Before starting any project that Claude will execute autonomously
- Before any build that involves external tools, APIs, or integrations
- Anytime the build is complex enough that "just start" will produce drift
```

---

## THE PRD STRUCTURE

```
1. PROJECT OVERVIEW
   - Project name
   - One-sentence description
   - Owner: Morph
   - Department(s) involved
   - Date created

2. PROBLEM STATEMENT
   What problem does this solve? For whom?
   What currently exists (if anything)?
   Why is the current state insufficient?

3. GOALS AND NON-GOALS
   GOALS — what this build MUST accomplish (numbered, specific)
   NON-GOALS — what this build explicitly does NOT do
   (prevents scope creep before it starts)

4. ARCHITECTURE
   - Tech stack / tools / frameworks (if applicable)
   - File structure — where does this live in the OS?
   - Dependencies — what does this rely on?
   - Integration points — what does this connect to?

5. PHASED BUILD PLAN
   Break the build into sequential phases.
   Each phase:
   - What is built
   - What it produces
   - What must be true before proceeding to next phase
   Maximum 4 phases initially — do not over-plan.

6. REFERENCES
   - Existing files in the OS that inform this build
   - External repos, tools, or resources to draw from
   - Skills to load at each phase

7. SUCCESS CRITERIA
   How do you know this build is done?
   How do you know it is working correctly?
   List measurable outcomes.

8. KILL CONDITIONS
   Under what conditions do you stop this build?
   (Budget exceeded, scope impossible, better solution found)
```

---

## OUTPUT FORMAT

```
File: dsc_prd_[project-name]_v[X].md
Location: D.S.C (or the primary department of the project)
Status: _draft until reviewed and approved by Morph
```

---

## RULES

```
- A PRD is edited by hand before execution begins — it is not fire-and-forget
- Claude can generate the first draft, but Morph reviews and approves
- The PRD is a living document — it gets updated as the build progresses
- If the build drifts significantly from the PRD, update the PRD or stop and reassess
```

---

*skill_prd-creation.md | Pandora OS Skills Library*
