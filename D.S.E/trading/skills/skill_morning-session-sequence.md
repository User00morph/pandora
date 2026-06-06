# SKILL — MORNING SESSION SEQUENCE
**The Complete Pre-Market to Market Open Protocol**

```
STATUS:     active
VERSION:    2.0
LOAD WHEN:  Start of every trading session — this is the first skill loaded
DEPARTMENT: D.S.E | STIS Master Protocol | Session initiation
LOADS:      skill_observer-gate.md → skill_vanna-protocol.md → skill_four-forces-dominance-read.md
            → skill_gex-regime-read.md → skill_markov-signal-generation.md
            → skill_multi-timeframe-dashboard.md → skill_poc-trend-filter.md
PRODUCES:   Completed session log entry + session grade (A+/A/B/Observe)
            + level stack for the session + daily bias statement
CROSS-REF:  skill_pre-trade-checklist.md (run after this when a setup forms)
            skill_daily-risk-budget.md (position sizing reference)
            skill_kill-zone-entry-timing.md (when to act on setups)
            skill_stis-layer-synthesis.md (how layers interact)
```

---

## WHAT THIS IS

The definitive sequence for preparing every trading session. Every step is ordered by dependency — each one uses the output of the previous. Miss a step and you're trading with incomplete context. Run all steps and you enter the session with maximum clarity.

---

## THE COMPLETE SEQUENCE (30 minutes before market open)

### STEP 1 — OBSERVER GATE (2 min)
Run `skill_observer-gate.md`. Am I in the Observer position or am I reacting?
- If reactive → do not proceed until Observer is restored
- If Observer present → continue to Step 2

---

### STEP 2 — VIX CHECK (2 min)
Run `skill_vanna-protocol.md`. Check the 5-day VIX trend.
```
Log: "Vanna: VIX [X.XX] | [declining/rising/flat] → [tailwind/headwind/neutral]"
```

---

### STEP 3 — FOUR FORCES DIAGNOSTIC (3 min)
Run `skill_four-forces-dominance-read.md`. Which force is dominant today?
```
Log: "Dominant force: [Gamma/Vanna/Charm/Mixed] | Session posture: [fade/follow/observe]"
```

---

### STEP 4 — GEX REGIME READ (5 min)
Run `skill_gex-regime-read.md`. Pull GEX data for primary instrument.
```
python3 tools/gex-engine/gex_engine.py --symbol [INSTRUMENT] --save
Log: Level stack, HVL, regime, daily range
```

---

### STEP 5 — MARKOV SIGNAL (3 min)
Run `skill_markov-signal-generation.md`. Check current state + transition probabilities.
```
Log: "Markov: [Bull/Bear/Sideways] state | Signal: P(bull) - P(bear) = [+/-X%]"
```

---

### STEP 6 — MTF ALIGNMENT (3 min)
Run `skill_multi-timeframe-dashboard.md`. How many timeframes are aligned?
```
Log: "[X]/4 timeframes [bullish/bearish] | Structure: [strong/moderate/weak/mixed]"
```

---

### STEP 7 — POC BIAS READ (2 min)
Run `skill_poc-trend-filter.md`. Where is price relative to prior session POC?
```
Log: "Price [above/below/at] Asia POC [X.XXXX] | London POC [X.XXXX]"
```

---

### STEP 8 — ESOTERIC CONTEXT (2 min, Sunday only — weekly)
Run `skill_esoteric-market-reading.md` weekly. On other days: quick check of active planetary transits.
```
Log: "Dominant Ray: [R#] | Cycle phase: [phase] | Key dates this week: [dates]"
```

---

### STEP 9 — LEVEL STACK COMPILATION (5 min)
Compile all levels from Steps 4-7 into a single ordered stack:
```
RESISTANCE STACK (top to bottom):
  [GEX Call Wall] — [PDH] — [PWH] — [VAH] — [GEX-1] — [GEX-2]

CURRENT PRICE: [X.XXXX]

SUPPORT STACK (top to bottom):
  [GEX-3] — [VAL] — [PDL] — [GEX Put Wall] — [PWL]

POC: [X.XXXX] — BIAS: [LONG/SHORT/NEUTRAL]
```

---

### STEP 10 — SESSION GRADE (1 min)
What grade is today's session?
```
All layers aligned + kill zone = A+ session (full size available)
3 layers aligned = A session (standard size)
2 layers = B session (half size)
Mixed/unclear = Observation only (no entries)
```

---

## SESSION LOG ENTRY FORMAT

```
DATE/TIME:   [YYYY-MM-DD HH:MM UTC]
INSTRUMENT:  [pair/asset]
VANNA:       [tailwind/headwind/neutral] | VIX: [X.XX]
DOMINANT FORCE: [force] | POSTURE: [fade/follow/observe]
GEX REGIME:  [mean-reverting/trending] | HVL: [X.XXXX]
MARKOV:      [state] | SIGNAL: [+/-X%]
MTF:         [X]/4 aligned | BIAS: [bull/bear/mixed]
POC BIAS:    [above/below/at] | BIAS: [long/short/neutral]
LEVEL STACK: [key resistance and support levels]
SESSION GRADE: [A+/A/B/Observe]
```

*D.S.E/trading/skills | STIS Master Protocol | Morning Session Sequence*
