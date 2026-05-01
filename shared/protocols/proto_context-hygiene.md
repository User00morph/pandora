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
