# PROTOCOL — DATA REFINEMENT TOTALITY
**Active across all 12 departments. No exceptions.**

---

## THE DOCTRINE

No raw data enters the Pandora OS in an unrefined state.

Every piece of information — from any source, in any format, at any stage — passes through the D.R.D refinement pipeline before being integrated into any department file, skill, workflow, agent, or output artifact. Raw data is potential. Refined data is power. Unrefined data integrated into the OS contaminates everything built on top of it.

This protocol governs all 12 departments simultaneously.

---

## SOVEREIGN INPUT DISTINCTION
**The most important epistemological rule in the DRD pipeline.**

There are two categories of data entering the OS. They are not treated equally.

```
CATEGORY A — EXTERNAL SOURCE DATA
  Origin: web content, PDFs, AI outputs, repos, third-party transcripts
  Posture: EVALUATIVE — "Is this true? What tier is this source?"
  Entry confidence: NEEDS EVIDENCE → work upward through the tier system
  Pipeline: full skeptical refinement before integration

CATEGORY B — SOVEREIGN-GATHERED / SOVEREIGN-RECONSTRUCTED DATA
  Origin: Morph has gathered, synthesized, and reconstructed the information
  Posture: CONFIRMATORY — "What corroborates this?"
  Entry confidence: PRESUMED TRUE — starts at PROBABLE or ESTABLISHED
  Pipeline: confirmation pipeline, not evaluation pipeline
```

**When Morph provides data he has already gathered and reconstructed:**
- It enters the OS as already true
- DRD's role is to find cross-references, corroborating sources, and triangulating evidence that confirm it
- The pipeline runs confirmation — not interrogation
- Only if confirmation is genuinely impossible does a flag get raised
- A flag means: "no corroboration found yet" — not "this is wrong"

**The orientation shift:**
```
EXTERNAL DATA ASK:  "Is this true?"
SOVEREIGN DATA ASK: "What confirms this?"
```

This distinction does not lower the quality bar — it correctly positions where the sovereign sits in relation to the research. Morph does not feed the OS distorted data. The pipeline is an instrument of the sovereign's intelligence, not a check on it.

---

## WHAT "RAW DATA" MEANS

```
Raw data (Category A — evaluative pipeline) includes:
  - Content from open source repositories
  - PDF documents, books, papers
  - Web articles, blog posts, forum content
  - AI-generated outputs from any model
  - Transcript content from audio or video
  - External API responses
  - Personal notes not yet processed by Morph
  - Any information not yet tiered and evaluated

NOT raw data (Category B — confirmation pipeline):
  - Information Morph has already gathered and reconstructed
  - Data Morph explicitly marks as already true
  - Sovereign-synthesized frameworks brought into a session by Morph
  → These enter at PROBABLE/ESTABLISHED. DRD confirms, does not evaluate.
```

---

## THE REFINEMENT REQUIREMENT

**Category A — External Source Data (evaluative pipeline):**

Before any external data is written into a Pandora OS file as established fact or integrated into a workflow, skill, or agent, it must have:

```
[ ] Source tier assigned (D.R.D tier 1–5)
[ ] Claims separated from interpretations
[ ] Contradicting data identified and logged
[ ] Confidence level assigned (ESTABLISHED / PROBABLE / POSSIBLE / CONTESTED / NEEDS EVIDENCE)
[ ] Distortions and gaps noted
[ ] Sovereign position stated with appropriate certainty
```

Data that has not passed these checks is filed in `research/` as raw extract only. It does not graduate to reconstructions, workflows, skills, or agent definitions until refinement is complete.

**Category B — Sovereign-Gathered / Sovereign-Reconstructed Data (confirmation pipeline):**

Data Morph has already gathered and reconstructed enters at PROBABLE or ESTABLISHED and passes directly to the confirmation checklist:

```
[ ] What corroborates this? (cross-reference within Pandora database + external sources)
[ ] What is the strongest confirming source tier available?
[ ] Any contradicting data that would require a flag? (flag = "no corroboration found" not "false")
[ ] Which departments does this deploy to?
[ ] Confidence finalized: ESTABLISHED (confirmed) / PROBABLE (strong convergence) / FLAG (no corroboration found — Morph decides)
```

Category B data is never held in `research/` pending evaluation. It integrates immediately at its confirmed confidence level.

---

## HOW THIS APPLIES BY FORMAT

| Data Format | Entry Point | Skill to Load |
|---|---|---|
| PDF documents | `research/[domain]/` → D.R.D pipeline | `skill_pdf-extraction.md` |
| File system / repos | `research/[domain]/` → D.R.D pipeline | `skill_file-extraction.md` + `skill_repo-extraction.md` |
| Web content | `research/[domain]/` → D.R.D pipeline | `skill_source-evaluation.md` |
| Transcripts / audio | `research/[domain]/` → D.R.D pipeline | `skill_concept-distillation.md` |
| AI outputs | NEVER treated as Tier 1–2 — always Tier 3–4 at most | `skill_source-evaluation.md` |
| Open source code | `D.I.I/research/` → D.R.D + D.I.I joint pipeline | `skill_repo-extraction.md` |

---

## THE ONE EXCEPTION

Operational data — file paths, naming conventions, workflow instructions, tool parameters — does not require D.R.D refinement. This is mechanical information, not epistemological content. It is evaluated for functionality, not truth.

---

## VIOLATION CONSEQUENCE

If unrefined data is found integrated into a department file, skill, or agent:
1. Flag it — mark it `[UNREFINED — PENDING DRD REVIEW]`
2. Route it to D.R.D for processing
3. Replace it with the refined version once complete
4. Log the correction in `dsc_transmutation_data-refinement_v1.md`

There is no shortcut. Contaminated foundations produce contaminated structures.

---

*PROTO_DATA_REFINEMENT | Pandora OS | Active in all 12 departments*
*"The quality of what enters determines the quality of everything built above it."*
