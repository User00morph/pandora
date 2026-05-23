# SKILL — GEX Regime Read
**Gamma Exposure Daily Classification | Pre-Session Protocol**
**Load when:** Opening any trading session BEFORE looking at any chart. Run after Observer Gate, before chart analysis.
**Department:** D.S.E trading workspace | STIS Layer 1b
**Source decoded:** `drd_decode_quant-options-ai-trading-stack_v1.md`
**Framework:** `dse_framework_gex-options-mechanics.md`

---

## WHAT THIS IS

The GEX Regime Read is a three-question pre-session protocol that classifies the intraday mechanical force field before any chart analysis begins. It answers: what is the dominant invisible force operating in the market today, and which direction is it pushing?

The three forces are:
- **Gamma** — are dealers dampening or amplifying every move?
- **Vanna** — is VIX creating a mechanical tailwind or headwind?
- **Charm** — where will afternoon gravitational pull land?

These are not predictions. They are mechanical forces derived from the options positioning of market makers. They are as reliable as gravity.

**Where to get GEX data (Sovereign — no paid provider needed):**
```
python3 tools/gex-engine/gex_engine.py --symbol SPY    # S&P macro regime
python3 tools/gex-engine/gex_engine.py --symbol GLD    # XAU/USD direct
python3 tools/gex-engine/gex_engine.py --symbol FXE    # EUR/USD proxy
python3 tools/gex-engine/gex_engine.py --symbol FXY    # USD/JPY proxy (inverted)
python3 tools/gex-engine/gex_engine.py --symbol FXB    # GBP/USD proxy
python3 tools/gex-engine/gex_engine.py --symbol UUP    # DXY proxy
```
Add `--save` to log to quant/ and `--pine` to generate TradingView levels.

---

## THE THREE-QUESTION PROTOCOL

Run this sequence every session before touching a chart.

---

### QUESTION 1 — GAMMA REGIME

**Ask:** Is price above or below the HVL (High Volatility Level)?

```
HVL = the strike where gamma flips from positive to negative

ABOVE HVL:
  Dealers are LONG gamma
  Effect: they FADE every move (sell rallies, buy dips)
  Market behavior: MEAN-REVERTING — tight ranges, failed breakouts,
                   rubber-band wicks, slow grinding
  Trade approach:  FADE extensions | take profits quickly | never chase
  Structure read:  Expect consolidation, ranging, price pinned near HVL

BELOW HVL:
  Dealers are SHORT gamma
  Effect: they AMPLIFY every move (buy rallies, sell dips)
  Market behavior: TRENDING/ACCELERATING — strong trends,
                   large ranges, 400-500pt drops possible
  Trade approach:  Follow continuation | wait for pullback confirmation
                   Do NOT fade — you are fighting a mechanical force
  Structure read:  Expect trend continuation, wide ranges, strong momentum
```

**Log:** `Gamma Regime: [mean-reverting / trending] | Price [above/below] HVL [level]`

---

### QUESTION 2 — VANNA DIRECTION

**Ask:** Which direction is VIX moving?

```
First thing each morning: check VIX chart (TradingView: VIX or CBOE:VIX)
Look for: 5-day trend direction, not just today's tick

VIX DECLINING:
  Implied volatility decreasing → dealer delta recalculates lower
  Dealers have EXCESS hedge → they BUY underlying to rebalance
  Effect: MECHANICAL LONG TAILWIND (invisible buyer in background)
  The "mystery drift higher with no catalyst" = Vanna
  Read: Long bias baked in. Fades against the up drift fail repeatedly.

VIX RISING:
  Implied volatility increasing → dealer delta recalculates higher
  Dealers are UNDERHEDGED → they SELL underlying to rebalance
  Effect: MECHANICAL SHORT HEADWIND (invisible seller in background)
  Read: Caution on longs. Every rally has mechanical selling pressure behind it.
  Rallies feel weak, fade fast, no follow-through.

VIX FLAT (±0.5 over 3 days):
  Vanna is neutral. Gamma regime is the dominant force.
  No additional directional mechanic operating.
```

**Log:** `Vanna: VIX [declining/rising/flat] → [long tailwind / short headwind / neutral]`

---

### QUESTION 3 — KEY LEVEL MAP

**Build the daily GEX level stack (pre-session):**

```
From your GEX data source, identify and log:

CALL RESISTANCE (0DTE):  [level] ← session ceiling
HVL (0DTE):             [level] ← REGIME BOUNDARY (answer to Q1)
PUT SUPPORT (0DTE):     [level] ← session floor
GEX 1:                  [level] ← strongest magnetic strike
GEX 2:                  [level]
GEX 3:                  [level]
GAMMA WALL:             [level] ← single largest positive gamma (weekly)

DOMINANT GREEK TODAY:
  Check which Greek is most active:
  → Major options expiry today? → Charm dominant (afternoon pull to nearest level)
  → VIX moving >1 pt? → Vanna dominant (directional drift regardless of structure)
  → Neither? → Gamma dominant (regime determines behavior)
```

**Log:** `Key levels: [fill in stack] | Dominant Greek: [Gamma/Vanna/Charm]`

---

## DAILY REGIME OUTPUT FORMAT

```
─────────────────────────────────────────────
GEX REGIME READ — [DATE] [SESSION]
─────────────────────────────────────────────
GAMMA REGIME:   [mean-reverting / trending]
  Price:        [above/below] HVL [level]
  
VANNA BIAS:     [long tailwind / short headwind / neutral]
  VIX:          [level] | [declining/rising/flat] [N-day trend]

LEVEL STACK:
  Call Res:     [level]
  HVL 0DTE:     [level]  ← regime boundary
  GEX 1:        [level]
  GEX 2:        [level]
  GEX 3:        [level]
  Put Sup:      [level]
  Gamma Wall:   [level]

DOMINANT GREEK: [Gamma / Vanna / Charm / mixed]
DAILY RANGE:    [put support] → [call resistance]
SESSION POSTURE:[fade / follow / observe]
─────────────────────────────────────────────
```

---

## FOREX APPLICATION PROTOCOL

Forex pairs have no public options OI — GEX cannot be computed directly on EUR/USD or USD/JPY. Apply it via three tiers:

### Tier 1 — SPY as Macro Force Field (applies to ALL forex pairs)
```
SPY NEGATIVE GAMMA (below HVL):
  → Equity vol amplified → risk-off flows activate
  → USD/JPY: carry unwind accelerates — JPY strengthens
  → EUR/USD: inverse DXY — dollar can trend hard
  → GBP/USD: widest ranges — no mean-reversion bets
  → Gold: negative gamma on SPY often coincides with GLD sweep

SPY POSITIVE GAMMA (above HVL):
  → Equity vol suppressed → risk-on drift supported
  → USD/JPY: carry stable — higher levels defendable
  → EUR/USD: slow grind, tight ranges — fade extensions
  → GBP/USD: range-bound behavior — use walls as targets
```
**Current check: Run SPY first, every session. The equity gamma regime is your global macro backdrop.**

### Tier 2 — Currency ETF Proxies (pair-specific)
```
Pair        ETF    Command                            Inversion?
XAU/USD     GLD    gex_engine.py --symbol GLD         Direct (1:1)
EUR/USD     FXE    gex_engine.py --symbol FXE         Direct (FXE ≈ EUR/USD × 100)
GBP/USD     FXB    gex_engine.py --symbol FXB         Direct (FXB ≈ GBP/USD × 100)
USD/JPY     FXY    gex_engine.py --symbol FXY         INVERTED (FXY up = USD/JPY down)
DXY         UUP    gex_engine.py --symbol UUP         Direct
```

**Reading currency ETF GEX in forex terms:**
- FXE Call Wall 109 = EUR/USD resistance at ~1.09
- FXE Put Wall 105 = EUR/USD support at ~1.05
- FXY Call Wall = USD/JPY floor (JPY cannot strengthen beyond this today)
- FXY Put Wall = USD/JPY ceiling (if FXY breaks this, USD/JPY rises)
- Net GEX negative on FXE = put-heavy options chain = bearish ETF structure

**Important caveat:** Currency ETF options are thinner than equity index options. The GEX numbers are smaller and the HVL detection is less reliable. Use as directional confirmation, not as a primary regime classifier.

### Tier 3 — What Doesn't Apply to Forex
```
❌ 0DTE analysis — currency ETFs rarely have same-day expiry
❌ Charm intraday timing — less meaningful on thin chains
❌ Precise GEX level targets — use as approximate zone, not exact strike
✓ Gamma regime direction (above/below HVL) — use this
✓ Call Wall / Put Wall as approximate range boundaries — use this
✓ SPY negative gamma = trending environment in ALL pairs — always use this
```

### Forex GEX Daily Protocol
```
STEP 1: python3 gex_engine.py --symbol SPY
         → Set macro backdrop (negative = trending/vol, positive = range/quiet)

STEP 2: python3 gex_engine.py --symbol [ETF for your pair]
         → Get pair-specific range and regime

STEP 3: Cross-reference ETF GEX walls with your STIS chart analysis levels
         → GEX wall aligns with OB/FVG = Grade A++ level
         → GEX wall contradicts chart structure = reduce confidence

STEP 4: Log regime in session record
         → "SPY -gamma | FXE +gamma | CW 109 / PW 105 | Pair range 1.05–1.09"
```

---

## INTEGRATION WITH STIS STACK

**How GEX regime changes what you do in other skills:**

| GEX Output | Changes This Skill |
|------------|-------------------|
| Gamma = mean-reverting | `skill_grade-a-filter.md`: Criterion 1 (HTF bias) can be softer — range trades valid |
| Gamma = trending | `skill_grade-a-filter.md`: Bias must be unambiguous — trend only, no fades |
| Vanna = long tailwind | `skill_liquidity-engineering.md`: Equal lows sweep + reversal = Grade A long |
| Vanna = short headwind | `skill_liquidity-engineering.md`: Equal highs sweep + reversal = Grade A short |
| Price at GEX level | Adds to criterion 2 (At a key level) — GEX levels qualify as institutional levels |
| Dominant = Charm | Watch for afternoon close near the nearest GEX level (gravity pull) |

**Integration with IEC (skill_iec-phase-detection.md):**
```
IEC Phase 3 (Expansion) + Gamma Trending (Negative GEX) = maximum conviction trend entry
IEC Phase 1 (Accumulation) + Gamma Mean-Reverting (Positive GEX) = range confirmed, no breakout
IEC Phase 2 (Impulse Trap) + Vanna Headwind = trap confirmed — do NOT chase the false move
```

---

## RULES

- Run this AFTER the Observer Gate (skill_observer-gate.md), BEFORE any chart
- Never trade a fade in negative gamma (below HVL) — you are fighting a mechanical amplifier
- Never hold through a Vanna move against you — it is mechanical and does not reverse without VIX reversing
- Log the GEX regime every session, even no-trade sessions — regime classification is research data
- GEX levels are TARGETS, not entries — build trade narrative from structure, use GEX to set exits

---

*D.S.E/trading/skills | STIS Layer 1b | GEX Regime Protocol | Pandora OS*
*Framework: dse_framework_gex-options-mechanics.md | Source: drd_decode_quant-options-ai-trading-stack_v1.md*
