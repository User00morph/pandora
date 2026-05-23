# SKILL — Morning Brief Protocol (P.M.I.B)
**Pandora Market Intelligence Brief | Daily Pre-Session Execution**
**Load when:** Opening any trading session. First thing, before any chart analysis.

---

## WHAT THIS IS

The P.M.I.B is the sovereign field read for every instrument on the watchlist. It is not a prediction. It is a mapping of where each instrument sits within the institutional architecture before the session opens. The brief surfaces Grade A setups only — everything else is observation.

**Watchlist (default):** EURUSD, GBPUSD, USDJPY, USDCHF, AUDUSD, USDCAD, GBPJPY, XAUUSD

---

## EXECUTION SEQUENCE

```
STEP 0 — OBSERVER GATE
  → Run skill_observer-gate.md FIRST
  → If Observer Gate BLOCKED → stop. Log "Observer Gate Blocked" + date. No brief.
  → If clear → proceed

STEP 1 — REGIME CLASSIFICATION (L1b + L1c — NEW)
  → Run skill_gex-regime-read.md:
     Check HVL: is price above or below? → gamma regime [mean-reverting/trending]
     Check VIX direction → Vanna bias [tailwind/headwind/neutral]
     Map GEX levels: HVL, call resistance, put support, GEX 1-3
  → Check markov_state_matrix.pine on primary instrument:
     Current state: [BULL/SIDEWAYS/BEAR]
     Signal: [+X.XX / -X.XX] | Stickiness: [X]%
  → Log: "Regime: Gamma [mean-rev/trending] | Vanna [bias] | Markov [state] sig [X.XX]"

STEP 2 — MACRO CONTEXT (L3 — Jiang)
  → What is DXY doing? (trend direction, key level proximity)
  → Any BIS/Fed/ECB/BOJ actions in the past 48h?
  → Which tier of the Jiang price hierarchy is winning? (Resources / Manufacturing / Knowledge / Finance)
  → Is there a game-reset signal active? (see pandora_frameworks.json layer_3_jiang_gt7.game_reset_signals)
  → Log: "Macro field: [one line]"

STEP 3 — CYCLIC POSITION (L4 — Bailey + Earik Beann)
  → Run python3 pmib.py (if available) for DS forecast + active aspects
  → What day of the week is it? (Mon = map only | Tue = highest probability | Fri = trap day)
  → Where are we in the weekly cycle? (early expansion / mid-expansion / exhaustion / reversal zone)
  → Is any major instrument at a Three-Hit Reversal completion point?
  → Active Earik Beann aspects today? (DS turning point zone? Applying aspect?)
  → Kp index state: calm or disturbed? (Schumann proxy)
  → Log: "Cyclic: [one line] | Aspects: [one line] | Kp: [calm/disturbed]"

STEP 4 — COT READ (L2 — collective consciousness)
  → For each instrument: what is current retail % long?
  → Flag: >65% retail long = institutional sweep target | <35% = potential long setup support
  → Identify instruments with extreme COT positioning
  → Log per instrument: "COT: [X]% retail long — [flag if extreme]"

STEP 5 — PER-INSTRUMENT ANALYSIS (L1 — Nathan/Kim/Todd + Footprint)
  For each watchlist instrument, run skill_chart-read-5-layer.md:
  a. Chart tool sequence (execute for each pair):
     → chart_set_symbol → quote_get → data_get_study_values
     → data_get_pine_lines → data_get_pine_labels → data_get_ohlcv (summary: true)
  b. Identify: IEC phase (skill_iec-phase-detection.md)
  c. Check: GEX regime applies? (price vs HVL | VIX direction)
  d. Check: Footprint read (skill_footprint-read.md): cum delta, VAH/VAL position, imbalances
  e. Identify: Session position (skill_session-architecture.md)
  f. Identify: Weekly cycle day implication
  g. Grade: Is there a Grade A setup forming? (skill_grade-a-filter.md — use full 9-criteria version)
  h. Log per instrument (see OUTPUT FORMAT below)

STEP 6 — SYNTHESIS
  → Which instruments have Grade A/A+ setups? (list with grade)
  → Which are Grade B (observing, reduced size)?
  → Which to ignore entirely today?
  → Primary focus: top 1-2 instruments only
  → Session posture: TREND / FADE / OBSERVE / NO TRADE (based on regime read)

STEP 7 — LOG THE BRIEF
  → File: ~/Desktop/Pandora/D.S.E/trading/logs/pmib/
  → Filename: YYYY-MM-DD_pmib_[session].md
  → Include: date, session, regime read, macro, cyclic, COT, per-instrument table, synthesis, primary focus
  → capture_screenshot for visual record of primary instrument
```

---

## PER-INSTRUMENT OUTPUT FORMAT

```
INSTRUMENT: [SYMBOL]
Price: [current] | Session: [Asia/London/NY/Pre-Market]
IEC Phase: [Accumulation / Impulse Trap / Expansion / Exhaustion / Mitigation]
Gamma Regime: [mean-reverting / trending] | HVL: [level] | Price [above/below] HVL
Vanna: [long tailwind / short headwind / neutral]
GEX Levels: HVL [X] | GEX1 [X] | GEX2 [X] | CR [X] | PS [X]
Markov: [BULL/SIDEWAYS/BEAR] | Signal: [X.XX] | Stick: [X]%
Footprint: Cum Delta [rising/falling/flat] | VA position [above/inside/below] | Imbalance: [Y/N/cluster]
Asia Grab: [UP/DOWN/NEUTRAL — where did 2-4am ET go?]
Weekly Cycle: [Mon-map / Tue-entry / Wed-expansion / Thu-expansion / Fri-avoid]
EMA Stack: [Bullish aligned / Bearish aligned / Mixed / Compressing]
Key Levels: [3-5 price levels from pine_lines/pine_labels]
COT: [X]% retail long — [EXTREME / NEUTRAL / CROWDED]
Grade: [A++ / A+ / A / B / NONE — criteria that failed]
Bias: [LONG / SHORT / NEUTRAL / WAIT]
Size modifier: [Markov multiplier × base risk]
Note: [one line on what to watch for this session]
```

---

## RULES

- Never skip Step 1 (Observer Gate). A clear brief from a reactive state is worse than no brief.
- Never trade on Monday (map only). Never trade on Friday (trap day). Log observations only.
- Never skip the macro context — a Grade A setup against the Jiang macro tide is not Grade A.
- If fewer than 3 of 7 Grade A criteria are met → do not grade. Log as observation.
- The brief is complete when ALL watchlist instruments have been assessed. Not before.
- Log every brief, including "nothing to trade today" briefs. The no-trade days are data.

---

## TOOL SEQUENCE (TradingView MCP)

```javascript
// Per instrument cycle
chart_set_symbol({ symbol: "EURUSD" })
quote_get()
data_get_study_values()
data_get_pine_lines({ study_filter: "" })
data_get_pine_labels({ study_filter: "" })
data_get_ohlcv({ summary: true })
capture_screenshot({ region: "chart" })
```

---

*D.S.E/trading/skills | P.M.I.B Protocol | Pandora OS*
*Load this skill at the start of every trading session. Do not begin analysis without running the Observer Gate first.*
