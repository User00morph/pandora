# Skill: Layer Triage
## Primary Departments: D.S.C, D.S.E, D.I.I, D.R.D
## Load at: Project inception, workflow design, build planning

Before any build begins, every task in the workflow must pass through layer triage. This skill prevents the most expensive error in sovereign system design: running deterministic or rule-based tasks through AI when simpler tools handle them better, faster, and cheaper.

---

## THE 60/30/10 FRAMEWORK

```
60% — TRADITIONAL CODE / DATABASES / ESTABLISHED TOOLS
        Deterministic. Exact answers. Never hallucinates. Zero tokens.
        Spreadsheets, file systems, databases, scripts, purpose-built software.

30% — RULE-BASED LOGIC
        If/then routing. Automation workflows. Decision trees. Templates with conditional sections.
        Zapier, Make, n8n, email rules, bash scripts, form logic.

10% — AI (SOVEREIGN INTELLIGENCE)
        Judgment. Synthesis. Creative work. Analysis of unstructured data.
        Writing, pattern recognition across domains, concept distillation, reconstruction.
```

Most workflows are inverted: 60% AI, 30% manual process, 10% automation. This is expensive, inconsistent, and slow. The goal is to reach the correct ratio by routing tasks to their proper layer.

---

## THE THREE-QUESTION DIAGNOSTIC

Run in order. Stop at the first YES.

```
QUESTION 1: Is the answer deterministic?
            Is there one right answer — calculable, lookable-up, exact?
            YES → Spreadsheet, database query, established tool. STOP.

QUESTION 2: Can it be expressed as if/then?
            If category = X, do Y. If amount > threshold, flag.
            YES → Automation script, bash rule, template logic. STOP.

QUESTION 3: Does it require judgment across unstructured information?
            Synthesis, interpretation, pattern recognition, creative work?
            YES → AI task. Proceed with sovereign intelligence.
```

If you start with Question 3 ("can AI do this?") — the answer is almost always yes, and you will over-index on AI. Always run the diagnostic in order.

---

## PANDORA OS LAYER MAPPING

### DETERMINISTIC LAYER (60%)
| Task | Tool |
|------|------|
| File naming and organization | bash scripts, naming conventions |
| Pipeline stage tracking | DRD_INDEX.md, structured tables |
| Source tier assignment | defined tier system (Tier 1-5) |
| Date-stamping artifacts | file naming convention |
| Output routing by domain | routing tables in ref cards |

### RULE-BASED LAYER (30%)
| Task | Tool |
|------|------|
| Department routing | pandora.md routing table |
| Skill selection per workflow stage | department context.md routing |
| Stage transitions (when done = move to next) | stage contract Done criteria |
| Context hygiene enforcement | proto_context-hygiene.md |
| Data refinement routing (format → pipeline) | proto_data-refinement.md |

### AI LAYER (10%) — SOVEREIGN INTELLIGENCE
| Task | Department |
|------|------------|
| Research deconstruction and reconstruction | D.R.D |
| Content creation and scripting | D.C.E |
| System design and project architecture | D.S.C |
| Sovereign business positioning | D.S.E |
| Technology evaluation and build | D.I.I |
| Concept distillation | all departments |

---

## BUILD WORKFLOW AUDIT

Before starting any build (software, workflow system, multi-department project):

```
LAYER TRIAGE AUDIT — [Project Name] — [Date]

For each task in the workflow:

Task: [description]
Q1 deterministic? YES/NO
Q2 rule-based?    YES/NO  
Q3 AI judgment?   YES/NO
Assigned layer:   TRADITIONAL / RULE-BASED / AI
Tool/skill:       [specific tool or skill]
```

A project where more than 30% of tasks land on the AI layer has been under-designed. Return to the workflow and identify what can move down.

---

## THE COCA-COLA PRINCIPLE

The value is not in having AI. The value is in what AI makes possible for the specific domain.

Companies that won from refrigeration were not the ones who built better refrigerators — they were the ones who figured out what refrigeration made possible (Coca-Cola, cold supply chains, global food distribution).

For Pandora OS: the sovereign intelligence layer exists to produce what no deterministic or rule-based system could — reconstructed sovereign positions, original content voice, novel system architectures. If AI is being used for tasks a bash script handles, the real leverage is being missed.

---

## SCALING VS AUTOMATING

These are not the same:
- **Automation** = task runs without human involvement
- **Scaling** = capacity increases without proportional effort

Scale through documentation (making judgment criteria explicit so others — or future sessions — can apply them). Automate the deterministic and rule-based layers. Keep judgment tasks human-reviewed.

Human review checkpoints are NOT optional. They go at every stage transition where:
1. The output quality affects everything downstream
2. The task required AI judgment (not deterministic output)
3. A new person (or session) will inherit the output

Remove a human checkpoint only when the deterministic tools have demonstrated consistent accuracy on that specific task.
