# SKILL — CHART ANALYSIS
**Load when: performing technical analysis, reviewing a chart for session bias, or annotating key levels.**
**Department: D.S.E trading workspace.**

---

## PROTOCOL

### STEP 1 — SET UP THE CHART
```
chart_set_symbol(symbol)          — switch to the instrument
chart_set_timeframe(timeframe)    — set the timeframe
```
Wait for load before proceeding.

### STEP 2 — ADD INDICATORS
Use `chart_manage_indicator(action="add", name="[FULL NAME]")`.

Full indicator names (required):
```
"Relative Strength Index"      (not RSI)
"Moving Average Exponential"   (not EMA)
"Moving Average"               (for SMA)
"MACD"
"Bollinger Bands"
"Volume"
"VWAP"
"Average True Range"
```

Customize settings after adding: `indicator_set_inputs(entity_id, inputs)`

### STEP 3 — NAVIGATE
```
chart_scroll_to_date(date)                      — jump to specific date
chart_set_visible_range(from_date, to_date)     — zoom to window
chart_get_visible_range()                       — confirm what is visible
```

### STEP 4 — ANNOTATE
```
draw_shape("horizontal_line", params)    — support/resistance level
draw_shape("trend_line", params)         — channel or trendline (two points required)
draw_shape("text", params)               — annotation
```

Apply STIS layer reading before marking levels. Mark: Asia range boundaries, Weekly highs/lows, IEC phase transitions, Impulse Trap zones.

### STEP 5 — CAPTURE AND ANALYZE
```
capture_screenshot(region="chart")       — screenshot annotated chart
data_get_ohlcv(symbol, timeframe, bars)  — pull recent price data
quote_get(symbol)                        — current real-time price
symbol_info(symbol)                      — exchange, type, session metadata
```

### STEP 6 — REPORT
Structure the analysis output:
```
INSTRUMENT:     [symbol + timeframe]
CURRENT PRICE:  [real-time quote]
WEEKLY CYCLE:   [phase — Accumulation / Expansion / Exhaustion / Trap]
IEC PHASE:      [current phase 1–5]
KEY LEVELS:     [Asia range, weekly highs/lows, order blocks]
BIAS:           [Bullish / Bearish / Neutral — with reasoning]
CONFLUENCE:     [Grade A / B / Stand Aside]
```

### CLEANUP
Remove temporary indicators: `chart_manage_indicator(action="remove", entity_id="[id]")`
Remove temporary drawings: `draw_clear()`

---

*SKILL_CHART_ANALYSIS | D.S.E trading | Pandora OS*
