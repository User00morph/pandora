# SKILL — REPLAY PRACTICE
**Load when: drilling mechanical execution, testing pattern recognition, or practicing STIS framework application on historical data.**
**Department: D.S.E trading workspace.**

---

## PROTOCOL

### STEP 1 — SETUP
```
chart_set_symbol(symbol)            — set the instrument
chart_set_timeframe(timeframe)      — set the trading timeframe
replay_start(date)                  — enter replay mode at the starting date
chart_manage_indicator(...)         — add required indicators
capture_screenshot()                — document the starting state
```

Choose a starting date where context is available: start 2–3 bars before the session open to see the full pre-session structure.

### STEP 2 — PRE-TRADE ANALYSIS
Before stepping any bars, run the CF-51 checklist from `skill_sovereign-trading-intelligence.md`:
```
[ ] Asia range mapped (data from prior session)
[ ] Session timing valid
[ ] EMA stack configuration
[ ] IEC phase identifiable
[ ] Entry signal present or being watched for
```

Document the initial read and bias before the market moves.

### STEP 3 — STEP THROUGH BARS
```
replay_step(bars=5)       — advance 5 bars at a time during scanning
replay_step(bars=1)       — advance 1 bar at a time near setup
replay_autoplay(speed=1)  — continuous play for trending phases
replay_status()           — check current date and position
```

Narrate each significant move as it prints:
- IEC phase transitions
- Session cascade triggers
- Impulse Trap confirmations
- Expansion confirmations
- Three-Hit completions

### STEP 4 — EXECUTE PRACTICE TRADES
When a Grade A setup triggers:
```
replay_trade(action="buy")    — long entry
replay_trade(action="sell")   — short entry
replay_status()               — confirm position opened, note entry price
```

When exit condition triggers (Three-Hit, ADR ceiling, Two-Hour Clock):
```
replay_trade(action="close")
replay_status()               — record P&L and exit reason
```

### STEP 5 — SESSION REVIEW
```
replay_status()                           — final P&L summary
capture_screenshot(region="chart")        — document final chart state
replay_stop()                             — exit replay mode
```

**Review report:**
```
DATE PRACTICED:    [historical date]
INSTRUMENT:        [symbol + timeframe]
TRADES TAKEN:      [count]
WIN / LOSS:        [record]
NET P&L:           [amount]
SETUPS IDENTIFIED: [what was seen, graded correctly]
MISSES:            [setups present but not taken — why]
EXECUTION ERRORS:  [entries taken without full confluence]
LESSON:            [one sentence — what this session reinforced or corrected]
```

File in: `D.S.E/trading/research/[date]_replay-review_[instrument].md`

---

## STIS SKILL FOCUS OPTIONS

Structure replay sessions around specific framework layers:

| Focus | What to Practice |
|-------|-----------------|
| IMA / IEC phases | Identifying each phase in real time before it completes |
| Asia Grab | Finding the 2am–4am sweep and reading direction from it |
| Weekly cycle | Entering Tuesday pullback, exiting before Friday trap |
| Three-Hit | Identifying exhaustion signals before reversal confirms |
| Observer state | Practicing detachment — exiting at the Two-Hour Clock without hesitation |

---

*SKILL_REPLAY_PRACTICE | D.S.E trading | Pandora OS*
