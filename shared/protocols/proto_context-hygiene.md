# Protocol: Context Hygiene
## OS-Wide | All Departments

Context hygiene is token sovereignty. Every token loaded competes for attention. Noise buries signal. This protocol governs what loads, when, and in what proportion.

---

## THE 5-LAYER SYSTEM (ICM)

```
L0 — pandora.md / CLAUDE.md     "Where am I?"        Always loaded. ~800 tokens.
L1 — ref_[dept].md              "Where do I go?"     Read on department entry. ~300 tokens.
L2 — wf_stage-[N].md           "What do I do?"      Read per task. ~200-500 tokens.
L3 — skills/*.md / _config/     "What rules apply?"  Loaded selectively per stage.
L4 — working files / outputs    "What am I working with?"  Loaded selectively per task.
```

L0-L2 = ROUTING. Small, always relevant. They navigate — not produce.
L3 = FACTORY. Skills, voice rules, constraints. Stable. Load only what THIS stage needs.
L4 = PRODUCT. Source material, previous outputs, live artifacts. Load only what THIS task needs.

**Critical distinction:** L3 material is internalized as constraints. L4 material is transformed as input. Never mix them in undifferentiated context. Label explicitly when both are present:
```
REFERENCE (L3 — do not transform, apply as constraints): [filename]
SOURCE (L4 — transform this into the output): [filename]
```

---

## TOKEN BUDGET

```
Routing    L0 + L1 + L2    10-15% of context budget
Reference  L3              20-30%
Source     L4              30-40%
Output room                20-30%
```

If L3 reference consumes >30% — the reference file is too large. Split it. A 50-line constraint file outperforms a 500-line comprehensive guide. Condense.

---

## SELECTIVE SECTION ROUTING (ICM Pattern 4 — the primary token saver)

Inputs tables in stage context files do NOT just say "read file.md." They say "read the Voice Rules section of voice-rules.md." Load only the section the current stage needs — not the whole file.

**Format in any stage CONTEXT.md Inputs table:**
```
| File | Section to Load | Why |
|------|----------------|-----|
| voice-rules.md | "Voice Rules" through "What the Voice Is NOT" | Tone constraints |
| ref_drd.md | "SESSION ROUTING" table only | Stage routing |
| skill_source-evaluation.md | "TIER DEFINITIONS" section | Confidence calibration |
```

When a full file is needed: write "Full file" in the Section/Scope column. The default is PARTIAL. Full-file loads require justification.

**Token impact:** A 150-line file with 60 lines of actionable rules = 60 lines loaded, not 150. Applied consistently across a 4-stage pipeline: 40-60% context reduction.

---

## FILE SIZE LIMITS (ICM Quality Guardrails)

```
CONTEXT.md / ref_*.md files      Under 80 lines     (routing only — never content)
Reference / skill files          Under 200 lines     (split if longer — max one cognitive domain per file)
```

If a skill file exceeds 200 lines — it is doing too much. Split into domain files that the skill CONTEXT.md routes to. Every token of irrelevant context is a token of diluted attention.

---

## CANONICAL SOURCES (ICM Pattern 5)

Every piece of information has ONE home. Other files point there. They do not duplicate it.

If you need to update a rule, update it in one place. If the same content exists in two files with both meant to be authoritative — one becomes a pointer.

**Smell test:** Search the repo for a specific phrase. If it appears in more than one file and both are authoritative — one needs to become a reference link.

**One-way references only (ICM Pattern 3):** If Stage 02 references Stage 01's output, Stage 01 does NOT reference Stage 02. If skill_A is referenced by three departments, skill_A does NOT reference any department. One-way prevents N-squared reference growth as the OS scales.

---

## DOCS OVER OUTPUTS (ICM Pattern 14)

Reference docs (skills, _config, frameworks) are the authoritative source for how to work. Previous outputs in output/ folders are artifacts — not templates.

Agents do NOT read other outputs to learn patterns. Early outputs are the worst outputs. If future agents learn from them, quality never improves. Load the skill. Not the old example.

---

## CONTEXT WINDOW RULES

1. **Count layers before loading.** L0 + L2 + 1-2 L3 files + 1 L4 file = sufficient for most tasks. More than 5 files loaded = audit what is actually needed.

2. **Remove before adding.** Before loading new context, ask: what existing context is no longer relevant? The context window is a workbench, not an archive.

3. **Front-load constraints.** Due to attention mechanics, opening context gets more weight than middle context. Critical constraints go first, source material after.

4. **Bash scouts before Read loads.** Never open a file to search it.
   ```bash
   find . -name "*.md" -type f        # locate by name
   grep -n "^##" file.md              # section headers + line numbers
   wc -l file.md                      # size check before loading
   grep -rl "keyword" path/           # find by content
   ```

5. **Start fresh when context decays.** When response quality degrades mid-session — open new conversation. Paste only what the next task needs. Long context with accumulated noise consistently underperforms clean context with targeted information.

6. **Compress in-session (don't wait for decay).** Active compression prevents accumulation before it becomes a problem:
   - Tool results older than 10 steps: replace with 1-line summary of what was found and acted on
   - Phase transition (research → build, decode → reconstruct): summarize + clear the prior phase before starting the next
   - Failed attempts: compress to "Attempt [X] failed: [reason]. Resolution: [fix]." — never leave dead-end debugging chains in context
   - Conversation history: keep last 10 turns verbatim, summarize everything older
   - Tool count ceiling: **≤19 tools in context** before any reasoning task. Above 19, model reasoning degrades (benchmark: Llama 3.1 8B failed at 46 tools, succeeded at 19)
   - MCP tool schemas are expensive: GitHub MCP = 80 tools = ~55K tokens loaded at init. Use CLI (Bash) when the model already knows the tool from training. Use MCP only when abstraction or governance justifies the token tax.

---

## DEPARTMENT CONTEXT BUDGETS

```
Department      L1 target       L2 target       Max L3 per stage
D.S.C           ref_dsc.md      wf_stage-N.md   2 skills
D.R.D           ref_drd.md      wf_stage-N.md   2 skills (source-eval always)
D.C.E           ref_dce.md      wf_stage-N.md   voice-architecture (3 files)
D.S.E           ref_dse.md      wf_stage-N.md   2 skills
D.I.I           ref_dii.md      wf_stage-N.md   2 skills (software-build always)
```

---

## VIOLATION SIGNALS

- Model contradicts earlier instructions → constraints buried in mid-context. Restate at top or start fresh.
- Model treats reference material as content to transform → missing REFERENCE/SOURCE labels.
- Quality degrades at conversation turn 10-15 → accumulated noise. Fresh conversation.
- Model "forgets" department context → L1 ref card not loaded at session start.
