# SKILL — SESSION INTAKE
**Fire at the start of every session, before department routing and before skill confirmation.**
**Loadable by: ALL departments. Primary home: D.R.D.**

---

## WHAT THIS SKILL IS

The sovereign front door of the Pandora OS. Every session passes through here first — no exceptions. It extracts raw context from Morph via a structured questionnaire, refines the answers through D.R.D logic, and routes a clean brief to the correct department. Nothing starts until intake is complete and routing is confirmed.

---

## WHEN TO TRIGGER

```
ACTIVATE THIS SKILL WHEN:
  - A new session begins and no department is already active
  - Morph opens with a vague or broad statement ("let's work", "I want to build X")
  - The task could belong to more than one department
  - No workflow stage has been identified yet
  - Morph explicitly says "start fresh" or "new topic"
```

---

## THE INTAKE PROTOCOL — FOUR STEPS

### STEP 1 — OPEN THE INTAKE WINDOW

Present this block to Morph immediately:

```
─────────────────────────────────────────────
PANDORA OS — SESSION INTAKE
─────────────────────────────────────────────
Answer these questions before we begin.
Short answers are fine. Skip any that don't apply.

1. WHAT ARE WE WORKING ON?
   One line — topic, task, or project name.

2. WHAT DOES DONE LOOK LIKE?
   The goal / desired output. What exists when this session ends?

3. OUTPUT TYPE?
   Research · Content · Build · Analysis · Ritual · Deal · System · Other

4. WHAT RAW MATERIAL EXISTS?
   Files, URLs, notes, transcripts, PDFs, voice notes, nothing — list what you have.

5. TIMEFRAME / URGENCY?
   Today · This week · No deadline · Urgent

6. CONSTRAINTS OR NON-NEGOTIABLES?
   Things to avoid, limits, requirements I need to know before starting.

─────────────────────────────────────────────
```

### STEP 2 — REFINE THROUGH D.R.D

Once Morph answers, apply D.R.D data refinement logic before routing:
- Identify the core intent (what Morph actually wants, not just what was said)
- Flag any ambiguity or missing information — ask one clarifying question if needed
- Determine the data tier: raw input / structured brief / refined directive
- Map output type and material to the correct department (see routing table below)

### STEP 3 — CONFIRM ROUTING

Present the routing decision for confirmation before proceeding:

```
─────────────────────────────────────────────
INTAKE COMPLETE — ROUTING DECISION
─────────────────────────────────────────────
TASK:         [one-line summary]
GOAL:         [desired output]
OUTPUT TYPE:  [type]
MATERIAL:     [what exists]
URGENCY:      [timeframe]

ROUTED TO:    [Department name + code]
ENTRY POINT:  [workflow stage or ref card section]
SKILLS FLAGGED: [skills likely needed — confirmed in skill_session-init.md next]

Confirm routing or redirect?
─────────────────────────────────────────────
```

### STEP 4 — HAND OFF

Once Morph confirms:
- State the department you're entering
- Load the department's ref card
- Trigger `skill_session-init.md` for skill confirmation
- Begin the workflow stage

---

## DEPARTMENT ROUTING TABLE

| Output Type | Primary Department | Mirror Departments |
|-------------|-------------------|-------------------|
| Research / decode / analysis | D.R.D | → target dept based on domain |
| Content / writing / scripts | D.C.E | D.R.D (intake only) |
| Software / tools / systems build | D.I.I | D.S.C |
| Project management / new initiative | D.S.C | D.I.I, D.S.E |
| Business / client / revenue | D.S.E | D.S.C |
| Real estate / property | D.R.A | D.S.E |
| Home environment | D.H.S | D.R.A |
| Body / health / nutrition | D.B.S | D.S.S |
| Ritual / practice / magik | D.O.M | D.P.S.A |
| Spiritual / personal agency | D.P.S.A | D.O.M |
| Science / technical research | D.S.S | D.I.I, D.R.D |
| Mechanics / physical systems | D.S.M | D.S.C |
| Consciousness / esoteric | D.R.D | D.P.S.A, D.I.I |

**When in doubt: route to D.R.D first. D.R.D refines. Then mirrors out.**

---

## WHAT THIS PREVENTS

```
BLIND STARTS
Beginning work without knowing the goal, output type, or available material.

WRONG DEPARTMENT ENTRY
Loading the wrong workflow stage because context wasn't extracted first.

MID-SESSION PIVOTS
Discovering constraints or redirects halfway through — intake catches them at the door.

SKILL MISMATCHES
Skill confirmation (skill_session-init.md) works better when intake has already
mapped the output type — the right skills surface naturally.
```

---

*SKILL_SESSION_INTAKE | All departments | Primary home: D.R.D | Pandora OS*
*"D.R.D is the front door. Nothing enters untested."*
