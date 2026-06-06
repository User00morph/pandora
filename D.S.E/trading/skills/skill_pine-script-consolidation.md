# SKILL — PINE SCRIPT CONSOLIDATION
**Packaging Multiple Indicators Into a Single Script**
**Load when:** Building or restructuring the STIS TradingView indicator stack.
**Department:** D.I.I | STIS Infrastructure | Pine Script architecture

---

## WHAT THIS IS

One Pine Script file = one indicator slot. One indicator slot can contain unlimited functional modules. This is the architectural principle that unlocks the free TradingView stack.

---

## THE MODULE STRUCTURE

```pine
//@version=6
indicator("STIS All-In-One", overlay=true, max_lines_count=500, max_boxes_count=500)

// ═══════════════════════════════════════
// MODULE 1 — GEX LEVELS
// ═══════════════════════════════════════
// [GEX level rendering code]

// ═══════════════════════════════════════
// MODULE 2 — SESSION KILL ZONES
// ═══════════════════════════════════════
// [Session box rendering code]

// ═══════════════════════════════════════
// MODULE 3 — VOLUME PROFILE / POC
// ═══════════════════════════════════════
// [Volume histogram code]

// ═══════════════════════════════════════
// MODULE 4 — MULTI-TIMEFRAME DASHBOARD
// ═══════════════════════════════════════
// [MTF table code]

// ═══════════════════════════════════════
// MODULE 5 — SMART ALERT TRIGGER
// ═══════════════════════════════════════
// [Alert condition aggregation]
```

---

## VARIABLE NAMING CONVENTION

Prefix all variables by module to prevent collision:

```
gex_     → GEX level variables
kz_      → Kill zone variables
vp_      → Volume profile variables
mtf_     → Multi-timeframe variables
ma_      → Moving average variables
alert_   → Alert condition variables
```

---

## PERFORMANCE RULES (Pine Script V6)

```
Max objects:   max_lines_count=500, max_boxes_count=500 (hard caps)
Cleanup:       Always clear old drawings before redrawing (prevents limit hit)
bgcolor:       Must be at GLOBAL scope — never inside an if block
talib:         Must be called at GLOBAL scope — result passed into conditional
Loops:         Minimize — Pine runs on every bar, loops compound exponentially
```

---

## THE SINGLE-SLOT RULE

**Morph has 2 indicator slots on the free plan.** One slot = the STIS all-in-one. The second slot = a simple oscillator (RSI, volume) that can't be folded in due to the `overlay=false` requirement.

The all-in-one runs on `overlay=true` (draws on the price chart). Anything that needs its own pane goes in slot 2.

---

## ADDING A MODULE

When Claude needs to add a new module:
1. Add after all existing code (never interleave)
2. Use unique variable prefix for all new variables
3. Add module header comment
4. Test compile before considering complete

*D.I.I | STIS Infrastructure | Pine Script Architecture*
