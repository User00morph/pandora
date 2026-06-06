# SKILL — DRAWDOWN SURVIVAL PROTOCOL
**Maintaining System Discipline Through Extended Losing Periods**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Account is in drawdown exceeding 15%, or three consecutive losing weeks,
            or when doubt about the system is growing
DEPARTMENT: D.S.E | STIS Observer Layer | Psychological survival
LOADS:      skill_decade-planning-horizon.md (frame recalibration)
            skill_edge-decay-monitoring.md (diagnose: decay vs. variance)
PRODUCES:   Clear determination: normal variance vs. edge decay + prescribed action
CROSS-REF:  skill_observer-calibration.md (restore Observer position)
            skill_multi-year-performance-frame.md (year/decade perspective)
            skill_system-robustness-stack.md (verify system is still valid)
```

---

## WHAT THIS IS

Drawdowns are built into every positive-expectancy system. The question is never whether a drawdown will occur — it's whether you can survive it psychologically and mathematically to reach the other side. This protocol distinguishes between a system that is failing and a system that is working normally through a difficult period.

---

## INPUT

```
REQUIRED:
  - Current drawdown from peak (%)
  - Duration of drawdown (weeks)
  - Rolling 20-trade win rate
  - Rolling 20-trade expectancy
  - Historical worst drawdown from backtest (%)

OPTIONAL:
  - Regime state across all instruments (Markov + GEX)
  - Whether this drawdown correlates with a specific market regime
```

---

## THE DIAGNOSTIC SEQUENCE

### STEP 1 — MEASURE THE DRAWDOWN

```
Current peak equity: $[X]
Current equity:      $[X]
Drawdown:            [X%]

Compare to historical:
  Within historical worst drawdown from backtest → NORMAL VARIANCE
  Exceeds historical worst drawdown → INVESTIGATE IMMEDIATELY
```

---

### STEP 2 — CHECK THE EDGE (5-signal test from skill_edge-decay-monitoring.md)

```
Run the 5 signals:
  □ Rolling 20-trade expectancy: [+ or -]
  □ Win rate vs. historical floor: [above/below]
  □ Drawdown vs. expected range: [within/exceeded]
  □ Market regime mismatch: [yes/no]
  □ Parameter drift: [within range/drifted]

RESULT:
  0-1 flags: NORMAL VARIANCE — continue the system as-is
  2 flags:   YELLOW — reduce to half size, increase monitoring
  3+ flags:  EDGE DECAY — pause, investigate, possibly suspend
```

---

### STEP 3 — APPLY THE CORRECT FRAME

```
IF NORMAL VARIANCE:
  "I am inside a decade that has produced positive returns 100% of the time.
   This drawdown was in the backtest distribution.
   The system is working correctly.
   My only job is to continue executing the rules."
   
  → Do NOT adjust parameters
  → Do NOT skip signals
  → Do NOT reduce size beyond what the daily budget already enforces
  → DO continue daily ritual as normal

IF EDGE DECAY SUSPECTED:
  → Move to paper trading only (do not close live positions — let stops work)
  → Run full robustness stack check (skill_system-robustness-stack.md)
  → Re-run walk-forward with recent data
  → Do not re-deploy capital until system passes validation again
```

---

## THE HISTORICAL CONTEXT TABLE

```
SYSTEM       MAX DRAWDOWN    HOW LONG BEFORE RECOVERY
─────────────────────────────────────────────────────
Richard Dennis (Turtles): 50%        Multiple times on path to $200M
Travis Woo MTP:           47-78%     Varied by configuration
Travis Woo crypto bots:   ~100%      4+ months before new highs

LESSON: Every great systematic system has gone through periods that
        felt like "this is broken." Every single one of those periods
        was followed by the system going to new highs — for those
        who held through.
```

---

## THE PSYCHOLOGICAL TOOLKIT

When in drawdown and doubt is growing:

```
QUESTION TO ASK:
  "Is this the system failing or is this the price I'm paying for the system's edge?"

REFRAME:
  Every losing trade is paying the cost of finding the next big winner.
  The tail events (big wins) are unpredictable. You must be in the system to catch them.
  Exiting during a drawdown guarantees missing the recovery.

ACTION:
  1. Run the 5-signal edge check — let data answer the question
  2. If data says normal variance: close the platform and do something else
  3. If data says edge decay: adjust systematically, not emotionally
```

---

## RULES

- Never adjust parameters during a drawdown — that's overfit chasing
- Never reduce position size below what the daily budget already sets — that's abandoning the system
- The diagnostic determines the response — not the feeling of discomfort
- A drawdown within the historical range is NORMAL. Treating it as abnormal creates abnormal decisions.

*D.S.E/trading/skills | STIS Observer Layer | Drawdown Survival*
