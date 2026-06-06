# SKILL — WORKFLOW ENGINEERING
**Load when:** deciding whether / how to automate any workflow, or evaluating any build decision before committing engineering effort.
**Primary departments:** D.S.C, D.I.I, D.S.E
**Source:** `D.R.D/deconstructions/drd_decode_jake-vip-agentic-business-os_v1.md` (Findings A2, A3)

---

## WHAT THIS SKILL IS

A two-part triage system for any automation or build decision:
1. **Effort-to-Output Ladder** — which rung does this workflow actually belong on?
2. **60/30/10 Architecture Rule** — once you're building, how should the layers be distributed?

Apply BEFORE any build begins. These are decision gates, not design patterns.

---

## PART 1 — EFFORT-TO-OUTPUT LADDER

### The Frame

Every automatable workflow sits on a three-rung ladder. The mistake is assuming higher is better. The right rung is the one that gets you to the outcome with the least effort that still meets the quality bar.

**Ask first:** which rung does the desired outcome require? THEN ask: how do I build that rung?

---

### L1 — Manual Hand-off

**What it is:** a human moves the data, runs the script, uploads the file. Zero or minimal engineering.

**Right for:**
- Low volume (time saved < time to automate)
- Judgment required at the hand-off point
- Data quality is unreliable (agent would silently propagate errors)
- Workflow hasn't proven it will stick yet
- You're still learning what the workflow actually is

**The Pacific Life error:** 50 people building a Snowflake agent to pull data into a ticketing flow. The agent kept breaking files. The answer was someone uploading an Excel file every few days. L1 was correct the whole time. The team climbed the ladder before checking which rung they needed.

---

### L2 — Light Scripts + Structured Prompts

**What it is:** templates, structured prompts, simple scripts, folder structures. Middle effort. Most real workflows live here.

**Right for:**
- Workflow runs often enough that templates save real time
- Steps are stable (not changing every week)
- Process is describable clearly enough for a prompt or script to replicate it
- Enough data exists to know what the output should look like

**This is the natural home of Pandora OS workflows.** Skills, workflow stage files, and prompt templates = L2. They give leverage without the maintenance burden of L3.

---

### L3 — Custom Pipelines

**What it is:** custom code, integrated services, multi-agent orchestration.

**Right for:**
- Scale requires it (L2 cannot handle the volume)
- Specialty work where no L2 pattern exists
- Competitive position depends on owning that piece of the stack

**ABSORPTION WARNING:** L3 work gets absorbed by platform releases. Before committing, ask:
*"Does this look like a feature someone at a bigger company will just add a button for in the next 12 months?"*

If yes — do not build L3 competing with that. Build the opinionated, bespoke, domain-expertise-required version that only someone with Morph's specific knowledge would design.

Three years ago, generating a coherent image required harnesses, multi-step prompting, custom pipelines. Today it takes two prompts. That L3 work is now L1 in every consumer chat product. Build above the layer that's about to get commoditized.

---

### Decision Protocol

Before any build decision, answer in order:

1. **What rung does the current state live on?**
2. **What rung does the desired state live on?**
3. **What does the move actually require in time + cost?**
4. **What is the realistic chance the AI vendors absorb this in the next 24 months?**
5. **Given the above — what is the minimum viable build?**

If the answer to question 4 is "high" and you're planning L3 — step back. Build the opinionated version that requires domain expertise, not the generic pipeline.

---

## PART 2 — 60/30/10 ARCHITECTURE RULE

### The Rule

For every AI-augmented workflow or system build:

**60% — Traditional code, files, folders, deterministic logic**
The foundation. Folder structures, file naming, deterministic scripts, established data flows. This is load-bearing. Do not skip it for the sake of "letting AI handle everything." It handles nothing reliably without this layer.

**30% — Rule-based or database-driven logic**
THIS IS WHERE MORPH'S SOVEREIGN FRAMEWORKS LIVE. Decision trees, evaluation criteria, protocol steps, refinement rules, workflow stage definitions. Encode the opinions here. This is the layer that doesn't commoditize. This is what Claude executes within.

**10% — AI judgment**
Only 10% of the workflow should require genuine AI reasoning. Applied to fresh inputs, within the container the 30% rule-based layer defines.

### The Common Error

Most workflow design errors invert this ratio — building at 90% AI judgment and 10% deterministic logic. This produces: fragile outputs, expensive token burns, unpredictable results, and a workflow that breaks every time the model updates.

The instinct is to make AI do more. The design principle is to make deterministic logic do more, so that AI's 10% is applied precisely where it's actually needed.

### Pandora OS Application

Every department in Pandora OS already follows this pattern:
- 60%: folder structure, file naming, the routing table, the session protocol
- 30%: skills files, workflow stages, protocols, ref cards — this is the encoded opinion layer
- 10%: Claude's live judgment applied within the stage definition

When adding new automation to any department: build the 60% first (files + folders), write the 30% explicitly (decision rules + evaluation criteria in skills), then let the 10% execute.

---

## COMBINED DECISION CHECKLIST

Before any build or automation decision:

- [ ] What rung does this actually need to be on? (L1/L2/L3)
- [ ] Have I solved this manually for at least 2-3 uses first?
- [ ] Can I describe the 30% rule-based logic explicitly before asking AI to apply it?
- [ ] Does this get absorbed by AI vendors in the next 12-24 months?
- [ ] Is the 60% deterministic foundation in place before the AI layer goes on top?
- [ ] Am I building the opinionated, bespoke version — or the generic one?

---

*SKILL_WORKFLOW_ENGINEERING | D.S.C + D.I.I + D.S.E | Source: Jake VIP Sessions decode | Pandora OS*
*"Ask which rung before you ask how to build the rung."*
