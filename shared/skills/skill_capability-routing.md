# SKILL — CAPABILITY ROUTING
**Loadable by: ALL departments. Load at session start or when a task type is unclear.**
**Paired with: `skill_layer-triage.md` (60/30/10 framework)**

---

## WHAT THIS SKILL IS

The decision framework for choosing the right Claude capability before any task begins. Context architecture beats prompt engineering every time. The biggest lever in output quality is not how you phrase the request — it is what information Claude can see and which tool it is using when it processes it.

This skill runs the 5-question decision sequence and maps tasks to the correct capability. It sits upstream of every workflow in Pandora OS.

---

## THE 5-QUESTION DECISION SEQUENCE

Run in order. Stop when you have a clear answer.

```
Q1 — DO I NEED PERSISTENT CONTEXT?
     Is this work you will return to repeatedly across sessions?
     Does it reference a stable body of documents, files, or domain knowledge?
     YES → This session is operating inside Pandora OS (a Project). Load the relevant
           department ref card and workflow stage. Continue to Q2.
     NO  → This is a one-off. Prompt directly. No context load needed.

Q2 — DO I NEED EXTERNAL DATA?
     Does this task require live information from outside Pandora OS?
     (Current prices, recent news, real-time data, data from external platforms)
     YES → Enable Web Search or MCP Connector. See OUTPUT MODES and MCP PROTOCOL below.
     NO  → Continue to Q3.

Q3 — IS THIS A REPEATABLE PROCESS?
     Have I done this task before with the same logic?
     Would a skill file prevent re-explaining the process each session?
     YES → Load the relevant skill from shared/skills/. If none exists — build one now.
     NO  → Prompt directly. Do not over-engineer one-off tasks.

Q4 — WHAT OUTPUT FORMAT DO I NEED?
     File (.docx, .pdf, .md)    → File Creation (see OUTPUT MODES)
     Interactive tool/prototype  → Artifact (see OUTPUT MODES)
     Data processing / math      → Code Execution (see OUTPUT MODES)
     Analysis / synthesis / text → Conversational response
     See OUTPUT MODES section below for full routing.

Q5 — DOES THIS NEED DEEP REASONING?
     Multiple interacting constraints? Trade-off analysis? Complex logic?
     YES → Extended Thinking (see OUTPUT MODES)
     NO  → Standard response. Proceed.
```

---

## OUTPUT MODES — THE FIVE TOOLS

### MODE 1 — CONVERSATIONAL RESPONSE
**What it is:** Claude thinking and writing in the conversation itself.
**Use when:** Analysis, synthesis, planning, explanation, writing, D.R.D reconstruction, concept distillation, coaching.
**60/30/10 layer:** 10% — Judgment and synthesis. The AI's core function.
**In Pandora OS:** Default mode for D.R.D stages 3–6, D.P.S.A, D.O.M, D.C.E, D.S.C planning work.

---

### MODE 2 — CODE EXECUTION
**What it is:** Claude writes and runs Python in a sandboxed environment. Results are real — not guesses. If code fails, Claude sees the error and fixes it.
**Use when:**
- Data processing (transcripts, CSVs, JSON, files)
- Math and calculations requiring precision
- Automated batch operations (extract transcripts, clean text, rename files)
- Verifying Claude's own outputs by running them

**Skip when:** The question is conceptual. Simple lookups. Questions Claude can answer from training data.
**60/30/10 layer:** 60% — The code is deterministic. AI writes it; the script does the work.
**In Pandora OS:** D.R.D (transcript cleaning, batch extractions via yt-dlp), D.I.I (script-based tools), D.S.C (data processing).

---

### MODE 3 — ARTIFACTS
**What it is:** Interactive, renderable outputs that appear alongside conversation — React components, HTML pages, SVG graphics, Mermaid diagrams, markdown documents.
**Use when:**
- Visual outputs: diagrams, flowcharts, architecture maps
- Interactive prototypes: calculators, dashboards, decision tools
- Documents that will be edited and iterated on
- Sharing proofs of concept

**Skip when:** The answer fits in a few sentences. You need a production-quality file format (use File Creation). Short lists or quick explanations.
**60/30/10 layer:** 30% — Interactive rule-based interfaces.
**In Pandora OS:** D.I.I (prototyping tools), D.S.C (system diagrams), D.S.E (ROI tools, client dashboards).

---

### MODE 4 — FILE CREATION
**What it is:** Claude creates professional documents in standard formats: Word (.docx), PowerPoint (.pptx), Excel (.xlsx), PDF. Real files with real formatting.
**Use when:**
- Deliverables someone else will open in Office or Google Workspace
- Reports, proposals, presentations for external use
- Output needs professional formatting: headers, tables, page layouts
- Modifying existing files

**Skip when:** Content is for internal reference (use markdown). Document is short enough to copy from chat. Needs custom layout requiring a design tool.
**60/30/10 layer:** 30% — Format and structure are rules. AI fills them with judgment.
**In Pandora OS:** D.C.E (content deliverables), D.S.E (client proposals, decks), D.R.D (brief packaging for Stage 6 deploy).

---

### MODE 5 — WEB SEARCH + DEEP RESEARCH
**What it is:** Claude pulls current information from the internet during a conversation. Deep Research mode conducts multi-step research across many sources and produces a comprehensive report.
**Use when:**
- Current information required (prices, news, events, recent releases)
- Research on topics that change frequently
- Verifying claims against live sources
- Comprehensive reports on complex, multi-source topics (use Deep Research)

**Skip when:** Established facts or stable concepts — training data is sufficient. Analyzing data you have already provided. The topic is fully within Claude's knowledge and has not changed.
**60/30/10 layer:** 60% for lookup, 10% for synthesis and analysis.
**In Pandora OS:** D.R.D (external source verification, Tier 1–2 source research), D.S.S (current scientific literature), D.I.I (current tech landscape), D.S.E (market intelligence).

---

### MODE 6 — EXTENDED THINKING
**What it is:** Claude reasons step by step through complex problems before producing an answer. The thinking process is visible as a collapsible block above the response.
**Use when:**
- Problem has multiple interacting constraints
- Trade-off analysis required
- Math, logic, or technical precision required
- You want to audit Claude's reasoning, not just its conclusion

**Skip when:** Straightforward question. Speed matters more than depth. Creative content (overthinking reduces quality).
**60/30/10 layer:** 10% — Reserved for tasks that require genuine judgment and synthesis. Do not use for tasks that do not need it.
**In Pandora OS:** D.S.C (complex system design), D.I.I (architecture decisions), D.R.D (Stage 5 reconstruction — building sovereign positions from contested evidence), D.R.A (deal analysis).

---

## CAPABILITY MAP — PANDORA OS DEPARTMENTS

| Department | Primary Capability | Secondary | Skip |
|------------|-------------------|-----------|------|
| D.R.D | Conversational (synthesis) | Code Execution (batch), Web Search (source research) | Artifacts |
| D.S.C | Conversational (planning) | Artifacts (diagrams), Extended Thinking (architecture) | — |
| D.I.I | Code Execution | Artifacts (prototypes), Extended Thinking (architecture) | — |
| D.C.E | File Creation | Conversational (writing), Artifacts (content tools) | Code Execution |
| D.S.E | File Creation (deliverables) | Web Search (market data), Artifacts (tools) | — |
| D.P.S.A | Conversational | Extended Thinking (framework analysis) | Code Execution |
| D.O.M | Conversational | Extended Thinking (ritual design logic) | File Creation |
| D.S.S | Web Search (current research) | Conversational (synthesis) | — |
| D.B.S | Conversational | Web Search (current studies) | — |
| D.R.A | Extended Thinking (deal analysis) | Web Search (market data) | Artifacts |
| D.H.S | Conversational | Web Search (product research) | — |
| D.S.M | Code Execution (diagnostics) | Conversational | — |

---

## COMBINATION STACKS

The capabilities compound. Well-designed sessions chain them:

```
RESEARCH SESSION (D.R.D):
  1. Web Search → find and verify Tier 1–2 sources
  2. Code Execution → batch extract transcripts (yt-dlp)
  3. Conversational → Stage 3 evidence extraction + Stage 4 distillation
  4. File Creation → Stage 6 brief packaged as .docx for department delivery

BUILD SESSION (D.I.I):
  1. Extended Thinking → architecture decision (monolith vs. modular)
  2. Code Execution → build the tool, run tests
  3. Artifacts → prototype the interface
  4. File Creation → technical spec for handoff

CLIENT SESSION (D.S.E):
  1. Web Search → current market data for positioning
  2. Conversational → strategy synthesis
  3. Artifacts → interactive ROI calculator for client
  4. File Creation → proposal deck (.pptx)
```

---

## ROUTING ANTI-PATTERNS

```
WRONG: Using conversational response for data processing
       → Use Code Execution. Conversational math is guessing. Code is exact.

WRONG: Using Extended Thinking for simple tasks
       → Wastes time. Reserved for genuine complexity.

WRONG: Using Web Search for stable knowledge
       → Training data suffices. Web Search is for current/changing information.

WRONG: Using File Creation for internal working documents
       → Use markdown. File creation is for external deliverables.

WRONG: Running the same instructions every session as prompts
       → If you've typed it twice, build a skill file. Prompts are one-off; skills are leverage.
```

---

*SKILL_CAPABILITY_ROUTING | Pandora OS | All Departments | Pairs with skill_layer-triage.md*
