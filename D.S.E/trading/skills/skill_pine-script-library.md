# SKILL — Pine Script Library
**STIS TradingView Indicator Reference | What Exists, What It Does, When to Load**
**Load when:** Setting up TradingView for a session, building a new Pine Script, or deciding which indicators to have on chart.
**Department:** D.S.E trading workspace | STIS Tool Layer
**File location:** `~/Desktop/Pandora/tools/pine-scripts/`

---

## WHAT THIS IS

A reference card for every Pine Script built in the STIS library. Each indicator has a defined role, pane placement, and loading conditions. Use this to configure TradingView correctly before any session.

**Installation:** In TradingView → Pine Script Editor → paste file content → Save → Add to Chart

---

## THE STIS PINE SCRIPT STACK

### LAYER 1 — PRICE CHART (overlay=true)

#### `monday_gold_box.pine` — IEC Weekly Range Box
**Status:** Complete | **Version:** v1
**What it does:** Draws the Monday high/low range as a box on the price chart. The Monday range = Phase 1–2 of the IEC (accumulation + manipulation). Tuesday–Thursday expansion = Phase 3. Box breach confirms directional bias.
**When to have on chart:** Every session (forex + indices). Always on.
**Key read:** Which direction did price breach the Monday box? That is the directional bias for the week.
**Layer:** L1 Mechanical (IEC)

---

#### `volume_footprint_overlay_v1.pine` — POC / VAH / VAL on Price Chart
**Status:** Complete | **Version:** v1
**What it does:** Draws three horizontal lines on the price chart:
- POC (yellow) — highest volume price level in the rolling window
- VAH (aqua) — value area high (top 70% volume band)
- VAL (orange) — value area low (bottom 70% volume band)
- Value area fill (blue) — shows fair value zone
- Labels: price levels annotated at right edge
- Background tint: green when above VAH (premium), orange when below VAL (discount)
**When to have on chart:** Any chart analysis session where order flow context is needed.
**Key read:** Is price inside the value area (range) or outside (premium/discount)?
**Layer:** L1 Mechanical (Order Flow)
**Companion:** Pair with `volume_footprint_v1.pine` in a separate pane

---

### LAYER 2 — SEPARATE PANE (overlay=false)

#### `volume_footprint_v1.pine` — Volume Delta + Imbalance Detection
**Status:** Complete | **Version:** v1
**What it does:**
- Delta histogram (green/red bars) — buy vol minus sell vol per bar
- Cumulative session delta line — who is winning the session
- Imbalance markers (◆) — bars where buy or sell vol dominated by 3:1+
- Cluster detection (◆ CLUSTER label) — 3+ consecutive imbalanced bars
- Stats table (top left): buy vol, sell vol, net delta, bar delta%, imbalance status
- Background tint: session directional tint
**When to have on chart:** Whenever evaluating an entry setup or running the Grade A filter.
**Key read:** Is delta confirming price direction? Are there imbalance clusters at key levels?
**Layer:** L1 Mechanical (Order Flow X-ray)
**Companion:** Pair with `volume_footprint_overlay_v1.pine` on price chart

---

#### `markov_state_matrix.pine` — Hedge Fund State Transition Matrix
**Status:** Complete | **Version:** v1
**What it does:**
- Classifies current market state: Bull / Sideways / Bear (based on 20-day cumulative return)
- Calculates full 3×3 transition probability matrix from historical data
- Displays stickiness (diagonal probability — how likely state persists)
- Generates signal = P(bull tomorrow) - P(bear tomorrow)
- Signal line with threshold zones (+0.20 / -0.20)
- Stats table: current state, cumulative return%, signal, bias, stickiness
- Background tint: state color
**When to have on chart:** Run on the primary instrument before each session, leave as reference.
**Key read:** Current state + signal magnitude = statistical bias and sizing modifier.
**Layer:** L1c Quant (Markov)
**Companion:** Use with `skill_markov-state-read.md`

---

#### `gex_levels_v1.pine` — GEX Key Level Overlay
**Status:** Complete | **Version:** v1
**What it does:**
- Draws all computed GEX levels as horizontal lines on the price chart
- HVL (yellow dashed) — gamma flip point; above = positive gamma, below = negative
- Call Wall (green solid) — ceiling where dealer buying peaks above spot
- Put Wall (red solid) — floor where dealer selling peaks below spot
- Max Gamma (purple dotted) — strongest price magnet regardless of direction
- Volatility Trigger (white) — ATM reference
- Gamma regime background: green tint (positive) / red tint (negative)
- Right-edge labels for each level
**When to have on chart:** Every session — load AFTER running `gex_engine.py --pine` to get today's levels. Paste auto-generated Pine output into TradingView.
**Key read:** Is spot above or below HVL? Where are the walls relative to your trade target?
**Layer:** L1b GEX/Options
**Data source:** `tools/gex-engine/gex_engine.py --symbol SPY --pine` (or QQQ/GLD/FXE)
**Workflow:** `python3 tools/gex-engine/gex_engine.py --symbol SPY --pine` → copy output → paste into TradingView → update input values

---

#### `regime_detector.pine` — ATR Volatility Regime Classifier
**Status:** Complete | **Version:** v1
**What it does:**
- ATR% (ATR as % of close) measured against a 50-day rolling baseline
- Ratio = current ATR% / baseline ATR% — compares today to normal
- Regime classification in 5 bands:
  - **COMPRESSION** (<0.50x) — coiling, Phase 1 Accumulation, positive gamma expected
  - **LOW VOL** (0.50–0.75x) — positive gamma likely, fades valid
  - **NORMAL** (0.75–1.25x) — baseline; gamma regime depends on GEX engine read
  - **ELEVATED** (1.25–2.00x) — approaching expansion, gamma flip watch zone
  - **EXPANSION** (≥2.00x) — negative gamma likely, trend mode, no fades
- Background tint per regime (gray/teal/blue/orange/red)
- Table: ATR%, baseline, ratio, GEX hint, IEC phase hint
- Alerts on regime transitions
**When to have on chart:** Every session (daily or H4). Add to BOTTOM PANE alongside Markov.
**Key read:** Ratio ≥ 2.0x = expansion regime confirmed. Ratio < 0.75x = coiling / accumulation.
**GEX integration:** EXPANSION regime cross-validates negative gamma from `gex_engine.py`. COMPRESSION cross-validates positive gamma.
**Layer:** L1b/L1c Volatility Regime

---

#### `vanna_vix_bias.pine` — VIX Vanna Direction Indicator
**Status:** Complete | **Version:** v1
**What it does:**
- Pulls VIX directly via `request.security("CBOE:VIX")` — works on any chart symbol
- Compares VIX to its 5-day SMA to classify Vanna direction
- 3-day ROC (rate of change) for signal strength
- Vanna signal scale: +2 (strong tailwind) → +1 → 0 (neutral) → −1 → −2 (strong headwind)
  - +2: VIX below SMA AND ROC < −5% (accelerating decline = strong mechanical long drift)
  - +1: VIX below SMA (dealer excess hedge → invisible buy pressure)
  - 0: VIX flat within ±0.5pt neutral band (gamma is dominant force)
  - −1: VIX above SMA (dealer underhedged → invisible sell pressure)
  - −2: VIX above SMA AND ROC > +5% (accelerating rise = strong mechanical headwind)
- Histogram of Vanna signal + VIX/SMA lines + neutral band fill
- Table: bias label, VIX, SMA, direction arrow, ROC%, implication, trade note
- Alerts on Vanna regime transitions
**When to have on chart:** Every session. Separate pane. Run on SPY, GLD, or any instrument.
**Key read:** Signal ≥ +1 = long tailwind active. Treat as invisible buyer behind every dip.
**GEX integration:** Vanna signal output matches `get_gex_brief()` `vanna_signal` field from `gex_engine.py`. Use both together to confirm direction.
**Forex application:** Vanna is a macro force — VIX rising triggers risk-off flows affecting ALL pairs. SPY negative gamma + Vanna −2 = maximum trending environment in forex too.
**Layer:** L1b GEX/Vanna

---

#### `iec_phase_overlay.pine` — IEC 5-Phase Algorithmic Overlay
**Status:** Complete | **Version:** v1
**What it does:**
- Classifies current IEC phase on any instrument using algorithmic detection
- Phase 1 (Accumulation): ATR < 0.75x baseline + price inside Donchian range → gray background
- Phase 2 (Impulse Trap): Price swept above/below range but closed back inside + no expansion ATR → orange background
- Phase 3 (Expansion): ATR > 1.25x baseline + directional breakout → green background
- Phase 4 (Exhaustion): Post-expansion, ATR declining + RSI divergence → red background
- Phase 5 (Mitigation): ATR returned low after expansion, price back in range → purple background
- Phase transition labels printed at each change (P1/P2/P3/P4/P5)
- Table: phase name, action directive, ATR ratio, range position, trap detection, momentum divergence
- Optional Donchian range midline display
- Alerts on every phase transition
**Important caveat:** Algorithmic estimate only. IEC is a discretionary chart-reading skill. Use as a visual prompt — if the indicator disagrees with your reading, trust the chart.
**When to have on chart:** During chart analysis and entry evaluation. Overlay on price chart.
**Key read:** Phase 2 orange flash = trap forming, prepare Grade A setup. Phase 3 green = enter or wait for 50% retracement. Phase 4 red = exits only.
**Companion:** Use with `skill_iec-phase-detection.md` for discretionary confirmation.
**Layer:** L1 Structural (IEC)

---

## RECOMMENDED CHART LAYOUTS

### LAYOUT A — FULL STIS SESSION (main chart)
```
TOP PANE (main price chart):
  → Candlesticks
  → iec_phase_overlay.pine (IEC phase background + transition labels)
  → monday_gold_box.pine (IEC weekly range)
  → volume_footprint_overlay_v1.pine (POC / VAH / VAL)
  → gex_levels_v1.pine (HVL / Call Wall / Put Wall — update daily via gex_engine.py)
  → [Your EMA stack if used]
  → [Your institutional levels / order blocks]

MIDDLE PANE (medium height):
  → volume_footprint_v1.pine (delta histogram + cumulative delta)

LOWER PANE (medium):
  → vanna_vix_bias.pine (Vanna direction + VIX trend)

BOTTOM PANE (small):
  → markov_state_matrix.pine (state + signal reference)
  → regime_detector.pine (ATR regime — can share pane by reducing height)
```

### LAYOUT B — QUICK SESSION (morning brief only)
```
TOP PANE:
  → Candlesticks
  → monday_gold_box.pine

LOWER PANE:
  → vanna_vix_bias.pine

BOTTOM PANE:
  → markov_state_matrix.pine
```

### LAYOUT C — ORDER FLOW DEEP DIVE
```
TOP PANE:
  → Candlesticks
  → volume_footprint_overlay_v1.pine

MIDDLE PANE:
  → volume_footprint_v1.pine (large — delta focus)
```

### LAYOUT D — REGIME CLASSIFICATION ONLY
```
Used when running the Step 2 GEX regime read (no chart analysis needed yet)
TOP PANE:
  → Candlesticks (minimal, timeframe: D or H4)
  → gex_levels_v1.pine

MIDDLE PANE:
  → vanna_vix_bias.pine

BOTTOM PANE:
  → regime_detector.pine
```

---

## PINE SCRIPT ROADMAP

| Script | Status | Priority | What It Adds |
|--------|--------|----------|-------------|
| `monday_gold_box.pine` | ✅ COMPLETE | — | IEC weekly range |
| `markov_state_matrix.pine` | ✅ COMPLETE | — | Quant state matrix |
| `volume_footprint_v1.pine` | ✅ COMPLETE | — | Delta histogram + imbalances |
| `volume_footprint_overlay_v1.pine` | ✅ COMPLETE | — | POC/VAH/VAL on price chart |
| `gex_levels_v1.pine` | ✅ COMPLETE | — | GEX levels overlay — run gex_engine.py --pine daily |
| `regime_detector.pine` | ✅ COMPLETE | — | ATR volatility regime + IEC/GEX cross-reference |
| `vanna_vix_bias.pine` | ✅ COMPLETE | — | VIX Vanna signal −2/+2 + dealer mechanic read |
| `iec_phase_overlay.pine` | ✅ COMPLETE | — | IEC 5-phase overlay — P1–P5 background tint + labels + trap detection |

---

## BUILD NOTES

**When adding a new Pine Script to the library:**
1. Write the script to `tools/pine-scripts/[name].pine`
2. Add entry to this skill file (above table + layout recommendations)
3. Update STIS PRD (tool inventory section)
4. Create or update the companion skill file (`skill_[name]-read.md`)
5. Update `context_trading.md` file inventory

**Walk-Forward Testing Protocol (before any strategy goes live):**
1. Set optimization lookback to 60 bars
2. Set out-of-sample test to 20 bars
3. Run across 3 non-overlapping periods minimum
4. Only accept strategy if edge persists in ALL out-of-sample windows
5. See `skill_regime-detection.md` for regime-specific validation

---

*D.S.E/trading/skills | STIS Pine Script Library | Pandora OS*
*All scripts: ~/Desktop/Pandora/tools/pine-scripts/*
