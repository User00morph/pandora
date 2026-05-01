# WF_DII — STAGE 3: MASTERY (CITRINITAS)
**Learn the technology deeply enough to use it with precision. Then build.**

---

## FOR TECHNOLOGY MASTERY

```
ACTION:
  Study documentation — primary sources first (Tier 1–2)
  Build test implementations and run experiments locally
  Document key patterns, edge cases, and limits discovered
  Identify the 20% of features producing 80% of the value
  Map failure modes — what breaks it and why

FOR AI / LLM TOOLS SPECIFICALLY:
  Prompt architecture testing — what input structure produces best output?
  Context window behavior — how does quality degrade as context fills?
  Output evaluation framework — what does good output look like for this tool?
  Multi-model workflow design — where does this tool sit vs. others?

LOAD: skill_system-design.md (for integration architecture)
OUTPUT: dii_mastery_[technology]_guide.md
```

---

## FOR SOFTWARE BUILDS

At this stage, technology mastery and build execution merge.

```
LOAD BOTH:
  skill_agentic-architecture.md   ← understand the agent building the system
  skill_software-build-protocol.md ← execute the build with this protocol

EXECUTE:
  Stage 1 (Nigredo) of the build protocol → seed the structure
  Stage 2 (Albedo) → architecture layer
  Stage 3 (Citrinitas) → component build loop

LANGUAGES IN SCOPE:
  Python    → FastAPI, data pipelines, MCP servers, AI integration
  JavaScript → Node, frontend, local tooling
  HTML/CSS  → interface layer, content delivery
  Bash      → automation, deployment scripts, system tooling
  Markdown  → OS artifacts, documentation, agent definitions

CHECKPOINT AFTER EACH COMPONENT:
  git commit -m "build: [component] complete"
  Test passes before moving forward.
```

---

## GATE

> Does the technology work as described in an actual test implementation?
> For builds: does each component pass its test before the next begins?

**PASS → load `wf_stage-4_integration.md`**

---

*D.I.I | Stage 3 of 5 | WF_DII_TECHNOLOGY_INTEGRATION*
