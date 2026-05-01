# PROTOCOL — DATA REFINEMENT TOTALITY
**Active across all 12 departments. No exceptions.**

---

## THE DOCTRINE

No raw data enters the Pandora OS in an unrefined state.

Every piece of information — from any source, in any format, at any stage — passes through the D.R.D refinement pipeline before being integrated into any department file, skill, workflow, agent, or output artifact. Raw data is potential. Refined data is power. Unrefined data integrated into the OS contaminates everything built on top of it.

This protocol governs all 12 departments simultaneously.

---

## WHAT "RAW DATA" MEANS

```
Raw data includes:
  - Content from open source repositories
  - PDF documents, books, papers
  - Web articles, blog posts, forum content
  - AI-generated outputs from any model
  - Transcript content from audio or video
  - External API responses
  - Personal notes not yet processed
  - Any information not yet tiered and evaluated
```

---

## THE REFINEMENT REQUIREMENT

Before any data is written into a Pandora OS file as established fact or integrated into a workflow, skill, or agent, it must have:

```
[ ] Source tier assigned (D.R.D tier 1–5)
[ ] Claims separated from interpretations
[ ] Contradicting data identified and logged
[ ] Confidence level assigned (ESTABLISHED / PROBABLE / POSSIBLE / CONTESTED / NEEDS EVIDENCE)
[ ] Distortions and gaps noted
[ ] Sovereign position stated with appropriate certainty
```

Data that has not passed these checks is filed in `research/` as raw extract only. It does not graduate to reconstructions, workflows, skills, or agent definitions until refinement is complete.

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
