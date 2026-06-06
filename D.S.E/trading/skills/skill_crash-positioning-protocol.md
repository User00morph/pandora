# SKILL — CRASH POSITIONING PROTOCOL
**What to Do When Markets Are in Sustained Decline**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Multiple systematic positions have been stopped out, or the portfolio is in
            sustained drawdown, or a broad market crash event is unfolding
DEPARTMENT: D.S.E | STIS Strategy Portfolio | Crash management
LOADS:      skill_cross-asset-correlation-read.md (identify which assets are still valid)
            skill_markov-state-machine.md (statistical state confirmation)
PRODUCES:   Current portfolio status + which positions remain valid + re-entry criteria
CROSS-REF:  skill_drawdown-survival-protocol.md (psychological layer)
            skill_multi-year-performance-frame.md (perspective)
            skill_edge-decay-monitoring.md (is this decay or normal variance?)
```

---

## WHAT THIS IS

A market crash is not a system failure. The systematic trend-following system's natural response to declining markets is to stop out of positions and move to the sidelines. This is correct behavior. This protocol handles that transition — from invested to sidelined — and defines the conditions for re-entry.

---

## INPUT

```
REQUIRED:
  - Which positions have been stopped out (list instruments + R-multiple)
  - Which positions remain open (if any)
  - Current Markov state for each instrument
  - Correlation state: are multiple assets declining together or independently?

OPTIONAL:
  - VIX level and trend (Vanna state)
  - M2 money supply trend (macro liquidity context)
```

---

## THE THREE CRASH PHASES

### PHASE 1 — STOP-OUT PHASE (system handles automatically)
```
Systematic positions stopped out one by one as price breaks below ATR stops
→ Let the system work. Do NOT manually exit before stops are hit.
→ Do NOT add to declining positions.
→ Do NOT "cut losses early" — the stop IS the loss limit.

After each stop-out:
  □ Log the exit: instrument, entry, stop, R-multiple (-1.0 R always)
  □ Do not re-enter that instrument until a new signal fires
  □ Do not look at that chart again until the next scheduled session
```

---

### PHASE 2 — SIDELINED PHASE (portfolio mostly cash)
```
State: Most or all systematic positions have been stopped out
Correct response: HAPPY POSITIONING

"I would be quite happy for the bear market to continue.
 I'm on the sidelines. It means cheaper prices for re-entry later."

During the sidelined phase:
  □ Continue running daily morning sequence (observer discipline)
  □ Monitor: which instruments are holding up? (relative strength scan)
  □ Identify: which assets have NOT been stopped out? (hidden bull markets)
  □ Note: TRX, Nikkei, uncorrelated assets may still be in bull signals
  □ Do NOT: force re-entry to avoid "missing out"
  □ Do NOT: switch to shorter timeframes to find trades
```

---

### PHASE 3 — RE-ENTRY CRITERIA
```
The ONLY valid re-entry signal: new structural high (new N-day high)

Re-entry checklist:
  □ Is the instrument making a new [25/55/calendar] day high?
  □ Has the Markov state returned to BULL (positive 20-day return)?
  □ Is the GEX regime consistent with a trending up environment?
  □ Has the overall macro context improved? (M2 expanding, risk appetite returning)

If ALL pass → re-enter at the breakout price
              with ATR stop below the breakout level
              at standard position size (not oversized to "make back losses")
```

---

## THE CORRELATION CRASH READ

When multiple assets crash simultaneously (S&P, Nasdaq, Bitcoin, Gold all declining):
```
This is a LIQUIDITY EVENT or FORCED SELLING event
→ The correlation will eventually break
→ Real assets (gold, quality equities) recover first
→ Speculative assets (crypto, small caps) recover last
→ Watch M2 for the inflection: when M2 turns up → real assets begin recovering
```

---

## OUTPUT FORMAT

```
CRASH STATUS — [DATE]
STOPPED OUT:    [list instruments + R-multiples]
STILL OPEN:     [list instruments + current profit/loss]
CASH POSITION:  [X% of portfolio]
SIDELINED SINCE: [date]
HIDDEN BULLS:   [any instruments still in bull signal]
RE-ENTRY WATCH: [instruments approaching new-high trigger]
MACRO CONTEXT:  [M2: expanding/contracting | Risk: on/off]
NEXT ACTION:    [Wait for new highs / Monitor X instrument]
```

---

## RULES

- A crash is not a system failure — it is the system working correctly
- The sidelines is a position — hold it with the same discipline as a long or short
- Never re-enter before a new structural high forms — declining prices do not produce buy signals
- Size re-entries at standard size, not larger (trying to recover losses = drawdown suicide)

*D.S.E/trading/skills | STIS Strategy Portfolio | Crash Management*
