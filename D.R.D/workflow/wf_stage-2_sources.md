# WF_DRD — STAGE 2: SOURCE IDENTIFICATION
**Find where the answers actually live. Tier every source before reading it.**

---

## WHAT THIS STAGE IS

Before consuming any content, identify what types of sources exist for this topic and assign them to the D.R.D tier system. The tier is assigned before reading — not after, based on whether the finding is liked.

---

## SOURCE TIER SYSTEM

| Tier | Type | Weight |
|------|------|--------|
| 1 | Primary: original research, primary texts, archaeological records, peer-reviewed studies with no major conflicts of interest | Highest |
| 2 | Credentialed secondary: academic books, peer-reviewed reviews, credentialed experts with evaluable work | High |
| 3 | Serious independent: non-credentialed researchers with documented methodology, primary source engagement, transparent reasoning | Medium-High |
| 4 | Secondary claims: information not traceable to primary source, unclear origin, aggregator content | Medium |
| 5 | Unsourced assertion: no traceable origin, no methodology — used only to map what is being claimed, never as factual foundation | Investigate only |

**The tier is determined by the source's methodology and accountability — not by whether the finding is significant or resonant.**

---

## ACTION

For each sub-question from Stage 1:
1. What tier of source is available?
2. Where specifically does that source live?
3. What is the source's relationship to the topic? (author, funder, incentive structure)

**Check existing source files first:**
`sources/drd_sources_[domain].md` — has this source been evaluated before?
- Yes → use existing tier assignment unless new information warrants re-evaluation
- No → evaluate, assign tier, register in both domain source file AND `sources/drd_sources_master.md`

---

## OUTPUT

Source map: each sub-question matched to source(s) with tier assigned.

**File:** Save the source map inside the raw-extract file:
`research/[domain]/drd_research_[topic]_raw-extract.md`

**Index:** Add row to `DRD_INDEX.md` with stage `raw-extract`

---

## GATE

> Is every sub-question from Stage 1 matched to at least one source, even if Tier 4-5?
> If a sub-question has no source at any tier — log it as "no evidence located" and proceed.

**PASS → load `wf_stage-3_evidence.md`**

---

*D.R.D | Stage 2 of 6 | WF_DRD_RESEARCH_TOPIC*
