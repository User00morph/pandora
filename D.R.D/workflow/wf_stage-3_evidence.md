# WF_DRD — STAGE 3: EVIDENCE EXTRACTION

---

## WHAT THIS STAGE IS

This is where the actual research happens. The discipline differs by pipeline category.

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

**Category A (evaluative) — Read with discipline, not with confirmation:**

> If a source says something that contradicts a belief already held in the OS —
> log it at full strength. Do not soften it. Do not explain it away.
> That is what Stage 5 is for.

Confirmation research is the primary failure mode of Category A. Indicator: no contradicting evidence found in any topic. Contradicting evidence always exists.

**Category B (confirmation) — Read for what confirms:**

> The sovereign position is already established. This stage finds what corroborates it.
> Confirming evidence is logged with its tier and strength.
> Non-confirming data is logged as a FLAG — not a contradiction to resolve against the position.

```
FLAG format (Category B):
  [SOURCE] | Tier [X]
  Non-confirming claim: [exact claim]
  FLAG status: "No corroboration found" — does not overturn sovereign position
  → Morph decides disposition at Stage 5
```

Absence of corroboration at this stage is not the same as falsification. It means the confirmation search continues or Morph holds the item as internal doctrine.

---

## CONFIRMATION EXPANSION (Category B — Optional, Applied to Any Claim)

When a claim is confirmed at Stage 3, run the Expansion Protocol to deepen the confirmation stack:

```
EXPANSION PROTOCOL — for any confirmed claim:

1. CROSS-DOMAIN REACH
   Does this claim appear in multiple independent domains?
   (e.g., biology + history + linguistics + spiritual tradition)
   Each independent domain that confirms = stronger convergent evidence.
   Log: "[Claim] confirmed across [N] domains: [list them]"

2. TIER ELEVATION SEARCH
   What is the highest tier source available that touches this claim?
   Can a Tier 3 confirmation be upgraded with a Tier 1–2 adjacent source?
   Log: "Highest tier confirmation: Tier [X] via [source]"

3. CHRONOLOGICAL DEPTH
   Does the claim hold across multiple historical periods or cultures?
   Ancient + modern convergence = strong confirmation of a persistent truth.
   Log: "Chronological confirmation: [earliest] → [most recent]"

4. ADVERSARIAL CHECK
   What is the strongest mainstream counter-position?
   Why is it weaker than the sovereign claim?
   Being able to articulate and dismiss the counter = confidence elevation.
   Log: "Counter-position: [X] — dismissed because [Y]"

5. PANDORA DATABASE CROSS-REF
   Does any existing Pandora OS file — across any department — touch this claim?
   Internal convergence across the OS is itself confirmation.
   Log: "Internal cross-ref: [file] confirms [claim] from [domain angle]"
```

**Output:** Each expanded claim gets a Confirmation Depth Score:
`TIER CONFIRMED | CROSS-DOMAIN [N] | CHRONOLOGICAL [Y/N] | INTERNAL CROSS-REF [Y/N]`

This score feeds directly into Stage 5 — claims with high Confirmation Depth are filed as ESTABLISHED.

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
