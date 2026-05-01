# WF_DRD — STAGE 3: EVIDENCE EXTRACTION
**Read with discipline, not with confirmation.**

---

## WHAT THIS STAGE IS

This is where the actual research happens. The discipline: extract what the source actually says — not what supports a prior position. Contradicting evidence is logged at full strength, not softened.

---

## ACTION

For each source identified in Stage 2:

**READ** — What does this source actually claim?
**EXTRACT** — The specific claim with precision (not paraphrase that loses nuance)
**TIER** — Confirm the tier assigned in Stage 2
**NOTE** — What is this source's limitation? (sample size, funding, methodology, date)
**FLAG** — Does this source contradict another source? If yes — log the contradiction. Do not resolve it here.

---

## CRITICAL DISCIPLINE

> If a source says something that contradicts a belief already held in the OS —
> log it at full strength. Do not soften it. Do not explain it away.
> That is what Stage 5 is for.

Confirmation research is the primary failure mode of this stage. Indicator: no contradicting evidence found in any topic. Contradicting evidence always exists.

---

## OUTPUT FORMAT

Evidence log — one entry per source:

```
[SOURCE NAME] | Tier [X]
Claim: [exact claim, precise]
Limitation: [sample size / funding / methodology / date]
Contradiction: [YES — conflicts with (source) on (point)] / NONE
```

---

## FILING

Save as: `deconstructions/[domain]/drd_decode_[topic]_decoded.md`
Update: `DRD_INDEX.md` — move stage to `decoded`

The raw-extract file in `research/` is preserved as the evidence trail. Do not overwrite it.

---

## GATE

> Has every source from Stage 2 been read and logged?
> Have contradictions been flagged rather than resolved?

**PASS → load `wf_stage-4_patterns.md`**

---

*D.R.D | Stage 3 of 6 | WF_DRD_RESEARCH_TOPIC*
