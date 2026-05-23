# SKILL — TRADINGVIEW OPERATIONS
**Platform Operations Skill | D.S.E/trading/skills/**
**Skill File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: STIS PRD v3 §3 (Platform Architecture)**
**Run: Reference during chart analysis sessions**

---

## PURPOSE

TradingView is the primary chart analysis platform for STIS. It is used for all multi-timeframe analysis, structure identification, pattern recognition, and hypothesis formation. It is NOT used for trade execution (that is MT5). This skill covers the TradingView operations needed to run the dual-layer chart reading and pattern recognition protocols efficiently.

---

## SECTION 1 — WORKSPACE SETUP

### The STIS TradingView Workspace Configuration

```
LAYOUT: Multi-chart layout (recommended: 4-chart grid for one pair)
  Top-left: Daily chart (structural bias)
  Top-right: 4H chart (OB and FVG identification)
  Bottom-left: 1H chart (entry zone refinement)
  Bottom-right: 15M chart (trigger candle identification)

CHART TYPE: Candlestick (not bar, not line — candlestick anatomy is essential)

COLOR SCHEME (recommended for STIS structure reading):
  Bullish candles: White or light green body, no border
  Bearish candles: Black or dark body, no border
  Background: Dark (reduces eye strain during multi-hour sessions)
```

### Essential Indicators to Install

```
VOLUME: Standard volume histogram at the bottom of every chart
  → Essential for Patterns 7 (compression) and 8 (climax reversal)
  → Volume bars color-coded to candle direction (green vol on up candles, red on down)

ATR (Average True Range, period 14): Added to every chart
  → Used for Method 3 stop placement and for gauging "normal" candle size
  → ATR multiplier: the climax candle is confirmed when its body/range is 2x+ ATR(14)

NO OTHER INDICATORS required. The STIS reads price action and structure — not indicators.
```

---

## SECTION 2 — THE STRUCTURE MARKING PROTOCOL

Consistent chart marking is essential. Every chart analysis session applies these marks:

### Step 1 — Daily Chart Marks

```
STRUCTURE LINES (horizontal lines):
Color: WHITE — for key levels
- Previous week high (PWH): dashed white line
- Previous week low (PWL): dashed white line
- Previous day high (PDH): solid white line
- Previous day low (PDL): solid white line
- Weekly open (first candle of the week open price): dotted white line
- Monthly open: dotted white line (thicker)
- Major round numbers (e.g., 150.00 on USD/JPY): thin solid white line

ORDER BLOCKS (rectangles):
Color: BLUE rectangles for BULLISH OBs | RED rectangles for BEARISH OBs
- Mark the full range (high to low) of the last bearish candle before a bullish impulse (bullish OB)
- Mark the full range of the last bullish candle before a bearish impulse (bearish OB)
- Keep only the most recent valid OBs visible (older OBs that have been tested more than twice: delete)

FAIR VALUE GAPS (rectangles):
Color: YELLOW rectangles for FVGs
- Mark between C1 high and C3 low (for bullish FVG) using the 3-candle rule
- Mark the midpoint as a horizontal line through the center of the yellow rectangle
- Note whether the FVG is "open" (unfilled) or "mitigated" (price has entered the zone)

LIQUIDITY POOLS (marked liquidity lines):
Color: ORANGE dotted lines above swing highs, below swing lows
- Mark equal highs (two or more candles with the same or very similar highs)
- Mark equal lows (two or more candles with the same or very similar lows)
- These are the Mutable Cross stop clusters — the sweep targets

TREND LINES (for structure visual reference only):
Color: GREY — use sparingly, only to visualize the trend channel
```

### Step 2 — 4H Chart Marks

Repeat the OB, FVG, and liquidity pool marks specifically for the 4H timeframe. The 4H marks are the entry-level precision zones — smaller and more specific than the daily marks.

### Step 3 — Color Coding System (Consistent)

```
WHITE: Key structural levels (PWH, PDH, weekly open)
BLUE: Bullish order blocks
RED: Bearish order blocks / Breaker blocks
YELLOW: Fair Value Gaps (all FVGs regardless of direction)
ORANGE: Liquidity pools (buy-side above highs, sell-side below lows)
GREEN: Bullish trade entry zones (when a valid setup is identified)
PURPLE: Stop levels (placed when a trade is active)
```

---

## SECTION 3 — THE MULTI-TIMEFRAME NAVIGATION PROTOCOL

Efficient navigation between timeframes during the dual-layer chart reading:

```
KEYBOARD SHORTCUTS (default TradingView — customize if needed):
Timeframe switches:
  D = Daily | W = Weekly | M = Monthly (or use 1D, 1W, 1M in the timeframe bar)
  4H = 4-hour | 1H = 1-hour | 15 = 15-minute | 5 = 5-minute

Zoom shortcuts:
  + = zoom in | - = zoom out
  Alt + Z = fit all data on screen (useful for seeing the full daily structure)

Chart navigation:
  Left arrow = scroll back in time | Right arrow = scroll forward
  Ctrl + click and drag = rubber-band zoom to a specific date range

Drawing tools:
  H = Horizontal line | R = Rectangle (for OBs and FVGs) | T = Text label
  V = Vertical line (for marking key dates — FOMC, NFP, planetary events)
```

---

## SECTION 4 — TRADINGVIEW FOR ESOTERIC LAYER SUPPORT

TradingView has tools that support the esoteric calendar integration:

### Planetary Events on the Chart

```
VERTICAL LINE MARKERS for key dates:
  Color: GOLD/YELLOW lines for major planetary events
  Examples:
  - July 4, 2026: "Mars-Uranus conjunction — MAX VOLATILITY" (bright yellow vertical line)
  - July 20, 2026: "Jupiter-Pluto opposition" (yellow vertical line)
  - August 12-13, 2026: "Eclipse window" (orange vertical line)
  
  Add these at the start of each month using the Vertical Line tool (V)
  This makes the esoteric timing layer visible directly on the price chart
```

### Session Markers

```
SESSION SHADING: Use the "Session & Time" indicator in TradingView to shade:
  Asian session: Blue shade
  London session: Yellow shade
  New York session: Red shade
  
  This makes Pattern 4 (Asian Range Sweep + London Continuation) immediately visible
  The moment London opens within the yellow shaded area is when to watch for the sweep
```

### The COT Data Visualization

```
TradingView has a "CFTC COT Report" indicator (search in the indicator library)
Settings: Select the relevant futures contract (e.g., EUR futures for EUR/USD)
Display: Show Commercial, Large Spec, and Small Spec net positions as lines

This brings the COT data INTO the price chart — the Sovereign can see when positioning extremes
coincide with key price levels (the highest-probability contrarian entries)
```

---

## SECTION 5 — ALERT SYSTEM SETUP

TradingView alerts are the mechanism that allows the Sovereign to monitor setups WITHOUT watching the chart continuously (the Mutable Cross behavior to avoid):

```
HOW TO SET AN ALERT:
Right-click on any price level → "Add Alert at [price]"
OR: Click the Bell icon in the top toolbar → Create Alert

ALERT PARAMETERS:
  Condition: Price crosses [level] | Once
  Notification: Email AND App notification (both — emails are reliable backups)
  Message: Include the pair, direction, and what the alert means
  Example: "GOLD — 4H OB zone reached. Check for hammer at $4,385. Potential entry."

WHEN TO SET ALERTS:
□ When a setup is identified but the entry level is not yet reached
□ When price is approaching a key liquidity pool (sweeping level to watch)
□ At the T1 and T2 profit target levels for active trades
□ At the stop level of an active trade (as a backup to the MT5 stop order)
□ At key dates (set a price-independent reminder) — use "Time & Price" alerts for FOMC/NFP days
```

---

## SECTION 6 — WEEKLY CHART MAINTENANCE

At the start of every Sunday session:

```
□ Delete any OB/FVG/structure marks that have been "used" (tested and broken)
□ Update the previous week's high and low horizontal lines
□ Add new marks for the upcoming week's structure
□ Add vertical line markers for any high-impact data events this week
□ Add vertical line markers for any planetary events this week
□ Confirm the chart layout is clean and current — old marks create visual clutter and confusion
□ Screenshot the weekly structure reading for the session log
```

---

## SECTION 7 — TRADINGVIEW WATCHLIST SETUP

```
ACTIVE PAIRS WATCHLIST (maintained in the left sidebar):
XAU/USD (Gold) — primary watch
USD/JPY — active monitoring
EUR/USD — context / setup watching
GBP/USD — setup watching
DXY — context only (not traded, but read)
US10Y (US 10-Year Yield) — intermarket chain
US30Y (US 30-Year Yield) — structural alarm level
US02Y (US 2-Year Yield) — curve steepener/flattener read
SPX (S&P 500) — risk sentiment context
```

---

## CROSS-REFERENCES
- `skill_dual-layer-chart-reading.md` — the analytical protocol this platform skill supports
- `skill_chart-pattern-recognition.md` — the pattern marking done in TradingView
- `dse_framework_astronomical-trading-calendar.md` — dates to mark as vertical lines
- `skill_mt5-operations.md` — the execution platform (different from TradingView analysis)

---

*skill_tradingview-operations.md | D.S.E/trading/skills/ | STIS Platform Operations Skill*
*Status: v1.0 — active | Reference during all chart analysis sessions.*
