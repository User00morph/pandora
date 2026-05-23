# SKILL — MULTI-SYMBOL SCAN
**Load when: screening multiple instruments for Grade A setups, comparing strategy performance across symbols, or building a watchlist ranking.**
**Department: D.S.E trading workspace.**

---

## PROTOCOL

### STEP 1 — DEFINE THE SCAN
```
SYMBOLS:    User-provided list, or pull via watchlist_get()
TIMEFRAME:  Active session timeframe
CRITERIA:   What to screen for — IEC phase, COT extreme, indicator value, strategy performance
```

### STEP 2 — RUN THE SCAN

**Strategy performance comparison (batch):**
```
batch_run(
  symbols=["ES1!", "NQ1!", "YM1!", "RTY1!"],
  timeframes=["15"],
  action="get_strategy_results"
)
```

**Visual comparison (batch screenshots):**
```
batch_run(
  symbols=["EURUSD", "GBPUSD", "USDJPY"],
  timeframes=["D"],
  action="screenshot"
)
```

**Custom per-symbol analysis loop:**
```
For each symbol:
  1. chart_set_symbol(symbol) + chart_set_timeframe(tf)
  2. chart_manage_indicator — add required studies
  3. data_get_ohlcv — pull price data
  4. data_get_indicator — read indicator values
  5. Apply STIS confluence check (Layer 1: IEC phase, Layer 2: COT reading)
  6. Record findings and grade
```

### STEP 3 — COMPILE RESULTS
Build a ranked comparison table:

```
| Symbol | IEC Phase | COT State | Setup Grade | Key Level | Note |
|--------|-----------|-----------|-------------|-----------|------|
```

Sort by confluence score: Grade A first.

### STEP 4 — REPORT
```
SCAN DATE:      [date]
INSTRUMENTS:    [list scanned]
GRADE A:        [instruments with all three convergence gates]
GRADE B:        [mechanical + psychological only]
STAND ASIDE:    [instruments with no confluence]
TOP SETUP:      [primary instrument + direction + entry trigger to watch]
```

Capture screenshots of Grade A top 1–2 charts for session brief.

### WATCHLIST INTEGRATION
```
watchlist_get()           — pull current watchlist
watchlist_add(symbol)     — add new Grade A candidate
```

---

*SKILL_MULTI_SYMBOL_SCAN | D.S.E trading | Pandora OS*
