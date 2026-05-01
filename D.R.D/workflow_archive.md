# WF_DRD_RESEARCH_TOPIC
**D.R.D — Sovereign Research & Deconstruction/Reconstruction**
**Workflow: Research Any Topic to Documented Output**

---

## WHAT THIS WORKFLOW IS

The core executable sequence of D.R.D. Takes any topic — from any department, at any scale — from raw question to fully tiered, documented research output. This workflow runs every time a department needs research done rather than opinion generated.

---

## TRIGGER

Any of the following activates this workflow:

- A department file routes to `DRD.md` for sourcing or investigation
- A direct research request with a specific topic or question
- An existing belief or claim in the OS that needs evidence evaluation
- A new concept or framework encountered that requires understanding before integration

---

## INPUT REQUIRED

Before beginning, establish:

```
TOPIC: What is being researched?
ORIGIN DEPARTMENT: Which department is requesting this?
RESEARCH DEPTH: Surface (overview) / Standard (documented) / Deep (exhaustive)?
SPECIFIC QUESTION: What specifically needs to be answered?
EXISTING POSITION: Is there already a belief or claim being held about this?
                   If yes — state it explicitly before researching.
                   Researching to confirm is different from researching to find.
DEADLINE: Is this time-sensitive or open-ended?
```

---

## THE WORKFLOW — STEP BY STEP

### STEP 1 — DECONSTRUCTION
**Break the topic into its component questions.**

No topic is a single question. Before researching anything, map what actually needs to be answered.

```
PRE-STEP:
Check DRD_INDEX.md — has this topic already been researched?
If yes: read the existing file and determine whether to
        extend it or start a parallel investigation.
If no:  proceed.

Assign the topic to one of the 6 research domains:
  1. Human History & Origins
  2. Suppressed & Alternative Science
  3. Pre-Western Knowledge Systems
  4. The Divine Feminine
  5. Consciousness Research
  6. Systemic Analysis

ACTION:
Take the stated topic and write out every sub-question
it contains. Do not answer yet — only map.

Example:
Topic: "Does ashwagandha reduce cortisol?"
Sub-questions:
- What is cortisol and how is it measured?
- What does ashwagandha actually contain?
- What studies exist on this specific claim?
- What populations were studied?
- What were the dosages and forms used?
- What were the effect sizes?
- Are there contradicting studies?
- What are the confounding factors?

OUTPUT: A numbered list of sub-questions.
        This list governs all subsequent steps.
```

---

### STEP 2 — SOURCE IDENTIFICATION
**Find where the answers actually live.**

Before consuming any content, identify what types of sources exist for this topic and assign them to the D.R.D tier system before reading.

```
SOURCE TIER SYSTEM:

TIER 1 — Primary sources
Original research, primary texts, archaeological records,
peer-reviewed studies with no major conflicts of interest,
direct transcripts or documents

TIER 2 — Credentialed secondary sources
Academic books, peer-reviewed review articles,
credentialed experts whose work can be evaluated

TIER 3 — Serious independent researchers
Non-credentialed researchers with documented methodology,
primary source engagement, transparent reasoning,
consistent track record

TIER 4 — Secondary claims
Information that cannot be traced to a primary source,
claims with unclear origin, aggregator content

TIER 5 — Unsourced assertion
No traceable origin, no methodology, no primary source
Used only to identify what is being claimed in the field —
never as factual foundation

ACTION:
For each sub-question from Step 1, identify:
- What tier of source is available?
- Where specifically does that source live?
- What is the source's relationship to the topic?
  (author, funder, incentive structure)

Check drd_sources_[domain].md — has this source been evaluated before?
If yes: use the existing tier assignment unless new information warrants re-evaluation.
If no:  evaluate, assign tier, and register in both the domain source file
        AND drd_sources_master.md.

OUTPUT: Source map — sub-question matched to source(s) with tier assigned.

FILING:
Save as: drd_research_[topic]_raw-extract.md
    in: research/[domain]/
Update: DRD_INDEX.md — add row with stage "raw-extract"
```

---

### STEP 3 — EVIDENCE EXTRACTION
**Read with discipline, not with confirmation.**

This step is where the actual research happens. The discipline: extract what the source actually says, not what supports the prior position.

```
FOR EACH SOURCE:

READ: What does this source actually claim?
EXTRACT: The specific claim, with precision
         (not paraphrase that loses important nuance)
TIER: Confirm the tier assigned in Step 2
NOTE: What is this source's limitation?
      (sample size, funding, methodology, date)
FLAG: Does this source contradict another source?
      If yes — log the contradiction. Do not resolve it yet.

CRITICAL DISCIPLINE:
If a source says something that contradicts
a belief already held in the OS —
log it at full strength.
Do not soften it. Do not explain it away in this step.
That is what Step 5 is for.

OUTPUT: Evidence log — each source entry with:
        [SOURCE] [TIER] [CLAIM] [LIMITATION] [CONTRADICTION FLAG]

FILING:
Save as: drd_decode_[topic]_decoded.md
    in: deconstructions/[domain]/
Update: DRD_INDEX.md — move stage to "decoded"
The raw-extract file in research/ is preserved as the evidence trail.
```

---

### STEP 4 — PATTERN RECOGNITION
**Find what the evidence actually shows.**

With all evidence extracted, step back and look at the whole picture.

```
QUESTIONS TO ANSWER IN THIS STEP:

1. WHERE IS THERE GENUINE CONSENSUS?
   Multiple Tier 1-2 sources pointing in the same direction
   = high confidence finding

2. WHERE IS THERE GENUINE DISAGREEMENT?
   Tier 1-2 sources contradicting each other
   = document the disagreement honestly, do not pick a side
   without examining why the disagreement exists

3. WHERE IS THE EVIDENCE THIN?
   Only Tier 3-4 sources available
   = finding is possible, not established

4. WHERE IS THE EVIDENCE ABSENT?
   Widely claimed but no traceable primary source
   = Tier 5 — flag as assertion, not finding

5. WHAT IS THE STRONGEST CASE FOR AND AGAINST?
   Even if a conclusion seems clear —
   articulate the strongest version of the opposing evidence.
   If the opposing case cannot be articulated,
   the research is incomplete.

OUTPUT: Pattern summary — findings organized by confidence level:
        ESTABLISHED / PROBABLE / POSSIBLE / CONTESTED / NEEDS EVIDENCE

NOTE ON "NEEDS EVIDENCE":
This replaces the former "UNSUPPORTED" label. A claim labeled
NEEDS EVIDENCE is not dismissed — it is flagged as requiring
more sourcing before it can be confidently placed. The label
includes a brief note on what specific evidence would strengthen
or resolve the claim. This keeps the research pipeline alive
rather than closing doors prematurely.
```

---

### STEP 4.5 — CONCEPT DISTILLATION
**Extract the fundamentals. Make them receivable.**

Before building the sovereign position, distill the core concepts that emerged from pattern recognition. This ensures the reconstruction is built on clearly understood foundations — not on half-absorbed complexity.

```
LOAD: shared/skills/skill_concept-distillation.md

FOR EACH KEY CONCEPT identified in Step 4:

1. EXTRACT THE ROOT — one sentence, no jargon
2. IDENTIFY THE PILLARS — 3-5 load-bearing elements
3. MAP THE RELATIONSHIPS — how pillars connect
4. BUILD THE LAYERS:
   - Layer 1 (The Seed): 1-3 sentences, zero background needed
   - Layer 2 (The Scaffold): ~1 page, terms defined inline
   - Layer 3 (The Full Architecture): complete with nuance
5. DISTORTION CHECK — does Layer 1 still carry Layer 3's truth?

OUTPUT: Concept distillation(s) embedded in or appended to
        the decoded file in deconstructions/[domain]/
        These distillations feed directly into Step 5.
```

---

### STEP 5 — RECONSTRUCTION
**Build the sovereign position.**

This is where D.R.D produces its actual output — not just what the sources say, but what the sovereign mind concludes after honest evaluation of all of it. The distillations from Step 4.5 are the building blocks.

```
THE RECONSTRUCTION ANSWERS:

- What is now known with high confidence?
- What is probable but not established?
- What remains genuinely uncertain?
- What was believed before this research that requires revision?
- What does this finding mean for the department that requested it?
- What follow-up research would strengthen the weakest findings?

CRITICAL RULE:
The reconstruction must be honest about uncertainty.
"The evidence suggests X, though Y remains contested"
is a stronger sovereign position than false certainty.
False certainty fails when tested.
Honest uncertainty can be built on.

OUTPUT: Sovereign position document — structured as:
        FINDINGS → CONFIDENCE LEVELS → IMPLICATIONS → OPEN QUESTIONS

FILING:
Save as: drd_reconstruct_[topic]_reconstructed.md
    in: reconstructions/[domain]/
Update: DRD_INDEX.md — move stage to "reconstructed", assign confidence level
```

---

### STEP 6 — DOCUMENTATION AND FILING
**Make the research retrievable.**

Research that is not filed is research that has to be redone.

```
DEPLOYMENT:
Create: drd_brief_[dept-code]_[topic]_deployed.md
    in: briefs/
Format the brief for the receiving department's needs.
Each destination department gets its own brief if the framing differs.

CROSS-LINK:
Add a reference to the brief in the destination department's context file
so it is findable from both directions.

UPDATE INDEX:
DRD_INDEX.md — move stage to "deployed"
Move entry from ACTIVE RESEARCH to COMPLETED & DEPLOYED table.
Update DOMAIN COUNTS.

SOURCE REGISTRY:
Confirm all sources used are registered in:
  - drd_sources_[domain].md (domain-specific)
  - drd_sources_master.md (central registry)

OUTPUT: Brief filed in briefs/
        Index updated.
        Source registry updated.
        Destination department cross-linked.
```

---

## QUALITY CHECKS

Before the workflow output is considered complete, confirm:

```
[ ] Every sub-question from Step 1 was addressed
    (even if the answer is "no evidence found")

[ ] No source was used above its assigned tier

[ ] Contradicting evidence was logged at full strength,
    not softened or omitted

[ ] The reconstruction distinguishes what is known
    from what is concluded from what is speculated

[ ] The file is named correctly and cross-linked
    to the requesting department
```

---

## OUTPUT FORMATS BY DEPTH

```
SURFACE (overview requested)
Steps 1, 4, 5 only — abbreviated
Produces: 1-2 page position summary
Pipeline: Goes directly to reconstructed stage (no raw-extract or decode file)
Filed in: reconstructions/[domain]/
Turnaround: Single session

STANDARD (documented requested)
All 6 steps — standard depth
Produces: Full pipeline — raw-extract → decoded → reconstructed → deployed
Filed across: research/ → deconstructions/ → reconstructions/ → briefs/
Turnaround: 1-3 sessions depending on topic

DEEP (exhaustive requested)
All 6 steps — maximum source coverage
Multiple passes through Steps 2-4 as new sources are identified
Produces: Comprehensive pipeline with expanded evidence logs
Filed across: research/ → deconstructions/ → reconstructions/ → briefs/
Turnaround: Multiple sessions, topic-dependent
```

---

## CONNECTS TO

```
ALL DEPARTMENTS — D.R.D research serves the entire OS.
Specific handoff points:

→ DSS.md       Ancient knowledge, cosmological frameworks,
                suppressed science — route findings there

→ DBS.md       Herb library, nutrition, women's health —
                route findings to relevant herb or topic file

→ DII.md       Technology and AI research findings

→ DPSA.md      Consciousness research, identity frameworks

→ DSE.md       Business, legal, financial research

→ DRA.md       Property data, market research, architecture

→ pandora.md   If findings require OS-level doctrine update
```

---

## FAILURE MODES TO AVOID

```
CONFIRMATION RESEARCH
Searching for sources that support a prior position
rather than mapping what the evidence actually shows.
Indicator: No contradicting evidence found in any topic.
           Contradicting evidence always exists.

TIER INFLATION
Treating a Tier 3-4 source as Tier 1-2
because it says something important or resonant.
The tier is determined by the source's methodology
and accountability — not by whether the finding is significant.

PREMATURE CLOSURE
Moving to reconstruction before extraction is complete.
Indicator: The reconstruction does not address
           all sub-questions from Step 1.

FALSE CERTAINTY IN OUTPUT
Stating a finding as established when it is only probable.
The sovereign position is stronger when it is honest
about its own confidence levels.
```

---

*WF_DRD_RESEARCH_TOPIC | D.R.D | Pandora OS*
*"The quality of what you build is determined by the quality of what you know. The quality of what you know is determined by the honesty of how you found it."*