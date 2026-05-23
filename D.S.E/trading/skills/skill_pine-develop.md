# SKILL — PINE SCRIPT DEVELOPMENT
**Load when: building a new indicator, writing a strategy, or modifying existing Pine Script in TradingView.**
**Department: D.S.E trading workspace.**

---

## PROTOCOL

### STEP 1 — CLARIFY THE GOAL
Before writing a single line, confirm:
```
TYPE:       Indicator / Strategy / Library
FUNCTION:   What does it do? (entry/exit logic, overlay, oscillator, signal)
PANE:       Overlay on chart or separate pane?
INPUTS:     What parameters should the user control?
VISUALS:    Lines, shapes, fills, labels, table?
```

### STEP 2 — PULL EXISTING SOURCE (if modifying)
```bash
node scripts/pine_pull.js         # pulls current TV script to scripts/current.pine
```
Read `scripts/current.pine` before touching anything.

If creating new: start from scratch in `scripts/current.pine`.

### STEP 3 — WRITE THE PINE SCRIPT

Every script requires:
```pine
//@version=6
indicator("Name", overlay=true)    // or strategy("Name", overlay=true)

// Inputs
length = input.int(14, "Length", group="Settings")

// Logic
// ...

// Plots
plot(series, "Label", color.green)
```

**Strategy declaration must include:**
```pine
strategy("Name", overlay=true, default_qty_type=strategy.percent_of_equity,
         default_qty_value=1, commission_type=strategy.commission.percent,
         commission_value=0.05, slippage=2)
```

### STEP 4 — PUSH AND COMPILE
```bash
node scripts/pine_push.js         # injects into Pine Editor, compiles, reports errors
```

### STEP 5 — FIX ERRORS

Common Pine Script errors:
```
"Mismatched input"          → indentation issue (use 4 spaces, not braces)
"Could not find function"   → typo or wrong version syntax
"Undeclared identifier"     → variable used before declaration
"Cannot call X with Y"      → wrong parameter type passed
```

Fix the specific line in `scripts/current.pine` → push again → repeat until 0 errors.

### STEP 6 — VERIFY ON CHART
```
capture_screenshot(region="chart")            — confirm visual looks correct
data_get_strategy_results()                   — if strategy: check initial performance
```

### STEP 7 — ITERATE
```bash
node scripts/pine_pull.js    # always pull fresh before editing
# edit locally
node scripts/pine_push.js    # push + compile
# screenshot to verify
```

**Hard rule:** Always compile after every change. Never report "done" without a clean compile and a screenshot confirming the visual output.

---

## STIS INTEGRATION FOR STRATEGY BUILDS

When building strategies based on STIS frameworks, encode these mechanical rules:

**IEC Phase detection pattern:**
```pine
// Detect equal highs (potential Impulse Trap zone)
equal_high = math.abs(high - high[1]) < atr * 0.1
equal_low = math.abs(low - low[1]) < atr * 0.1
```

**Asia range mapping:**
```pine
// Asia session = 19:00–02:00 ET (adjust for timezone)
in_asia = (hour >= 19 or hour < 2)
asia_high = ta.highest(high, asia_bars)
asia_low = ta.lowest(low, asia_bars)
```

**Three-Hit exhaustion signal:**
```pine
// Count touches of key level
level_touches = 0
level_touches := math.abs(close - key_level) < atr * 0.2 ?
  nz(level_touches[1]) + 1 : nz(level_touches[1])
exhaustion = level_touches >= 3
```

---

*SKILL_PINE_DEVELOP | D.S.E trading | Pandora OS*
