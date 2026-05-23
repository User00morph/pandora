# PRD — SOVEREIGN TRADING INTELLIGENCE SYSTEM (STIS)
**Product Requirements Document | v5 | Sovereign GEX Engine + Full Quant Integration**
**Date Updated: 2026-05-20**
**Supersedes:** v4 (IEC mechanical spine + Earik Beann astro tools)

---

## 0. WHAT CHANGED FROM v4

v4 operationalized Layers 1 and 4 with the IEC scanner, Earik Beann tools, Schumann proxy, and unified P.M.I.B. L1b and L1c were registered as layers but marked pending — no sovereign tools existed for them yet.

v5 closes those gaps entirely and expands the system:

**New in v5:**

- **Sovereign GEX Engine** — `tools/gex-engine/gex_engine.py` — self-contained Python tool. Computes Gamma Exposure from free yfinance options chain data using the SpotGamma formula (publicly documented). No paid provider dependency. Covers SPY, QQQ, GLD (XAU), FXE (EUR), FXB (GBP), FXY (JPY), UUP (DXY). L1b is now fully operational.
- **PMIB L1b Integration** — `pmib.py` now includes the GEX layer automatically. Gamma signal + Vanna signal feed directly into the L5 coherence score. `--no-gex` and `--gex-symbol` flags added.
- **Forex GEX Proxy Protocol** — currency ETFs (FXE/FXB/FXY/UUP) used as options-chain proxies for forex pairs. Tier 1 (SPY macro regime) + Tier 2 (pair-specific ETF) + Tier 3 (what not to use) — full protocol in `skill_gex-regime-read.md`.
- **GEX Levels Pine Script** — `gex_levels_v1.pine` — auto-generated Pine Script overlay from `gex_engine.py --pine`. HVL / Call Wall / Put Wall / Max Gamma / Volatility Trigger drawn on chart with gamma regime background tint.
- **Volume Footprint Pine Scripts** — `volume_footprint_v1.pine` (delta histogram + imbalance) + `volume_footprint_overlay_v1.pine` (POC / VAH / VAL) — free Bookmap equivalent.
- **Grade A Filter v2.0** — 7 core criteria → 9 criteria. Added Criterion 8 (Regime Aligned: GEX + Markov) and Criterion 9 (Footprint Confirms: delta + cluster at level). New tier: Grade A++ when both quant criteria met.
- **Skill expansion** — 11 skills in v4 → 20+ skills. New: `skill_gex-regime-read.md` (with full forex protocol), `skill_regime-detection.md`, `skill_markov-state-read.md`, `skill_footprint-read.md`, `skill_pine-script-library.md`.
- **Agent stack** — two new agents: `agent_gex-analyst.md` (L1b gamma regime brief) and `agent_regime-detection.md` (cross-layer IEC + GEX + Markov + Vol classification).
- **Quant archive** — `D.S.E/trading/quant/` now logging daily GEX session maps across all 7 symbols. First session: 2026-05-20. Walk-forward validation dataset begins here.
- **Daily session sequence v3** — updated to 7 steps with Step 2 now being GEX regime classification before any chart opens. Step 3 is the full PMIB (now includes L1b automatically).

---

## 0a. LINEAGE

| Version | Date | Core Addition |
|---|---|---|
| v1 | 2026-02 | Original STIS blueprint |
| v2 | 2026-03 | 5-Layer stack locked. Forex as primary instrument. |
| v3 | 2026-04-09 | Bailey esoteric integration. Seven Rays, Three Crosses, Observer Flip. |
| v4 | 2026-05-19 | IEC mechanical spine. Earik Beann tools. Schumann proxy. P.M.I.B. |
| **v5** | **2026-05-20** | **Sovereign GEX Engine. Quant integration. Full skill + Pine Script stack.** |

---

## 1. PROJECT OVERVIEW

**Project Name:** Sovereign Trading Intelligence System (STIS)
**One-Sentence Description:** A continuously evolving trading intelligence architecture within Pandora OS that fuses institutional mechanics (IEC), dealer gamma dynamics (GEX), statistical regime probability (Markov), planetary cycles (Earik Beann), geomagnetic field state (Schumann proxy), the Bailey esoteric framework, and observer sovereignty into a complete system for engaging forex and adjacent markets from the Observer position.
**Owner:** Morph
**Primary Home:** D.S.E (with D.I.I, D.O.M, D.P.S.A, D.R.D as structural co-owners)
**Primary Instrument:** **FOREX** (locked — see §3)
**Mechanical Spine:** IEC (Institutional Expansion Cycle) — `drd_decode_institutional-market-architecture_v1.md`
**Quant Spine:** GEX + Markov — `drd_decode_quant-options-ai-trading-stack_v1.md`
**Metaphysical Spine:** Alice Bailey, *Esoteric Astrology* — `drd_decode_bailey-esoteric-astrology.md`

---

## 2. PROBLEM STATEMENT

Markets are the largest live data stream of collective human consciousness on earth. Every candlestick is an aggregate wave-function of the internal states of everyone interacting with that instrument at that moment. Most traders either become the wave (emotional reactivity) or pretend the wave doesn't contain consciousness (mechanical indicator-worship). Neither reads what is actually there.

v5 adds the dealer mechanical layer — the invisible force operating beneath all price delivery. Market makers maintaining delta neutrality create the same "liquidity" the IEC describes, but the mechanism is options gamma, not predatory smart money. GEX is the formula that makes that force quantifiable. Markov gives the statistical probability scaffolding for how long any regime persists. Together with the existing four layers, STIS now reads the market from seven simultaneous vantage points before a single chart is opened.

---

## 3. FOREX IS THE PRIMARY INSTRUMENT (LOCKED)

Forex is chosen not as a preference but as the instrument most aligned with STIS doctrine:

| Reason | Detail |
|---|---|
| **Collective consciousness of nations** | Every forex pair is the relative internal state of two national/monetary fields — the purest macro-consciousness reading available |
| **Liquidity / continuity** | $7.5T daily volume, 24/5 — the field is always alive |
| **No single-stock specific risk** | Removes corporate-event noise so what remains is collective sentiment, macro forces, and cyclic law |
| **Natural fit for Rays + Crosses** | Each major currency carries a distinguishable ray-signature readable once the framework is internalized |
| **GEX proxy coverage** | Currency ETFs (FXE, FXB, FXY, UUP, GLD) provide options chain data that translates directly to forex pair mechanics |

Other instruments (indices, commodities, crypto) are not excluded — they enter via the same doctrinal lens after forex fluency is established. SPY/QQQ are now actively tracked as the macro gamma regime context for all forex positions.

---

## 4. THE FIVE-LAYER INTELLIGENCE STACK (v5)

```
┌───────────────────────────────────────────────────────────────────┐
│  LAYER 5 — QUANTUM FIELD / OBSERVER SOVEREIGNTY                  │
│  Science: Science of the Self (the Observer Flip)                │
│  Purpose: The reversal. Trading from the Aries→Pisces wheel.     │
│  Skills:  skill_observer-gate.md, skill_observer-calibration.md  │
│  Artifacts: dse_framework_observer-flip-trading.md               │
│             dse_framework_great-reversal-doctrine.md             │
│             dse_framework_aries-pisces-wheel.md                  │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 4 — ESOTERIC ASTROLOGY & CYCLIC LAW                       │
│  Science: Science of Triangles + Science of Destiny              │
│  Purpose: Seven Rays, Three Crosses, planetary cycles,           │
│           declination turning points, intraday aspect triggers.  │
│  Spine:   drd_decode_earik-beann-astrotrader_v1.md               │
│  Tools:   declination_system.py, aspect_scanner.py               │
│  Skills:  skill_esoteric-market-reading.md (weekly),             │
│           skill_macro-field-reading.md (weekly),                 │
│           skill_session-calibration-triad.md (every session)     │
│  Artifacts: dse_framework_rays-crosses-markets.md                │
│             dse_framework_rays-currency-signatures.md (living)   │
│             dse_framework_astronomical-trading-calendar.md       │
│             dse_framework_crisis-polarization-sweep.md           │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 3 — EXTERNAL REALITY FIELD                                │
│  Science: Science of the Rays (expressed in macro forces)        │
│  Purpose: Central banks, COT, geopolitics, macro data,           │
│           intermarket chain, power architecture.                 │
│  Skills:  skill_macro-field-reading.md, skill_dual-layer-        │
│           chart-reading.md                                       │
│  Artifacts: dse_framework_power-architecture-decode.md           │
│             dse_framework_institutional-data-intelligence.md     │
│             dse_framework_intermarket-chain.md                   │
│             dse_framework_central-bank-doctrine.md               │
│             dse_framework_banking-data-streams.md                │
│             dse_framework_macro-narrative-reading.md             │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 2 — COLLECTIVE CONSCIOUSNESS (PRICE ACTION + EM FIELD)    │
│  Science: Psychological-astrological (participant consciousness) │
│  Purpose: Candlesticks as aggregate internal state mirror.       │
│           Kp index / solar wind as quantified field-state proxy. │
│  Tool:    schumann_resonance.py (NOAA SWPC — live)               │
│  Skills:  skill_candlestick-reading.md,                          │
│           skill_chart-pattern-recognition.md,                    │
│           skill_liquidity-engineering.md                         │
│  Artifacts: dse_framework_collective-consciousness-price.md      │
│             dse_framework_candlestick-as-mirror.md               │
│             dse_archive_pattern-library.md                       │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 1 — SOVEREIGN FUNDAMENTALS / IEC MECHANICS                │
│  Science: (Prima materia — institutional price delivery)         │
│  Purpose: IEC 5-phase cycle, market structure, order flow,       │
│           Monday Gold Box, risk management.                      │
│  Spine:   drd_decode_institutional-market-architecture_v1.md     │
│  Tools:   iec_scanner.py, monday_gold_box.pine                   │
│  Skills:  skill_iec-phase-detection.md, skill_chart-read-5-layer │
│           skill_footprint-read.md, skill_risk-management.md,     │
│           skill_trade-execution.md, skill_trade-management.md    │
│  Pine:    monday_gold_box.pine, volume_footprint_v1.pine,        │
│           volume_footprint_overlay_v1.pine                       │
│  Artifacts: dse_framework_market-structure.md (+ 5 siblings)     │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 1b — GEX / OPTIONS MECHANICS (OPERATIONAL v5)             │
│  Science: (Dealer delta hedging as intraday mechanical force)    │
│  Purpose: Gamma regime (positive/negative), HVL detection,       │
│           Call Wall / Put Wall / Max Gamma, Vanna/Charm,         │
│           Zero-DTE weight + directional lean, forex ETF proxy.  │
│  Spine:   drd_decode_quant-options-ai-trading-stack_v1.md        │
│  Tool:    gex_engine.py — SOVEREIGN (free, no paid API)          │
│           Formula: GEX = Gamma × OI × 100 × Spot² × 0.01        │
│           HVL = cumulative GEX zero crossing                     │
│           Covers: SPY, QQQ, GLD, FXE, FXB, FXY, UUP             │
│  Pine:    gex_levels_v1.pine (auto-generated from --pine flag)   │
│  Skills:  skill_gex-regime-read.md (with forex proxy protocol),  │
│           skill_regime-detection.md                              │
│  Agents:  agent_gex-analyst.md                                   │
│  Archive: D.S.E/trading/quant/ (daily GEX session maps)          │
│  Artifact: dse_framework_gex-options-mechanics.md                │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 1c — QUANT / MARKOV STATE (OPERATIONAL v5)                │
│  Science: (Statistical regime probability — hedge fund method)   │
│  Purpose: 3-state Markov chain (Bull/Sideways/Bear),             │
│           transition matrix, stickiness, position sizing signal. │
│           Signal = P(bull tomorrow) − P(bear tomorrow)           │
│  Spine:   drd_decode_quant-options-ai-trading-stack_v1.md        │
│  Pine:    markov_state_matrix.pine (3×3 live transition matrix)  │
│  Skills:  skill_markov-state-read.md, skill_regime-detection.md  │
│  Agents:  agent_regime-detection.md                              │
│  Artifact: dse_framework_gex-options-mechanics.md (linked)       │
└───────────────────────────────────────────────────────────────────┘
```

---

## 5. THE FIVE SCIENCES → STACK MAPPING

| Bailey's Science | STIS Layer | What It Does in the System |
|---|---|---|
| **Science of Triangles** | L4 | Reads three-way relationships: ray / constellation / planet — and trader / field / price. Every trade has a triangle. |
| **Science of the Rays** | L3–L4 | Identifies which of the Seven Rays is dominant in a macro regime or a currency's behavior. |
| **Science of Destiny** | L4 | Timing — Crisis→Polarization→Sweep as the cyclic law that replaces random walk. |
| **Science of the Self** | L5 | The Observer Flip. Who is watching, and from which wheel? |
| **Psychological-astrological Science** | L2 | Candlesticks as mirror of aggregate internal state — the retail becomes the price; the sovereign reads it. |

L1/L1b/L1c is the *prima materia* — the mechanical and statistical soil none of the sciences can skip but none are specifically about.

---

## 6. THE SEVEN RAYS AS MARKET ENERGY SIGNATURES

The Seven Rays are the foundational energies expressed through every chart, currency, and macro regime. Before reading any chart, ask: *which ray is currently expressing here?*

| Ray | Keynote | Market Signature | Currency / Regime Expression |
|---|---|---|---|
| **R1 — Will / Power** | "I assert the fact." | Impulsive, directional, policy-driven force moves. Terminal: destruction of the old trend. | USD in Fed-driven regimes; JPY interventions; central-bank shock moves |
| **R2 — Love / Wisdom** | "The Word of incarnation." | Accumulative, liquidity-building, range-consolidation that holds participants. Attractive force. | EUR as reserve/anchor; Gold as risk-off love-wisdom mirror |
| **R3 — Active Intelligence** | "Purpose itself am I." | Fast adaptive, algorithmic, opportunistic, complex. | Algorithmic-dominated pairs; GBP's cross-rate complexity |
| **R4 — Harmony through Conflict** | "Two merge with one." | Conflict → resolution. Violent swings ending in equilibrium. | AUD, NZD (risk/commodity tension); oil-driven CAD conflicts |
| **R5 — Concrete Science** | "Three minds unite." | Precision, structural levels holding exactly; science of form. | CHF (precision), structural levels obeyed cleanly |
| **R6 — Idealism / Devotion** | "I see the goal." | Narrative-devotional, one-directional moves, believer rallies and capitulations. | Narrative-driven moves; memetic momentum |
| **R7 — Ceremonial Order / Ritual** | "The highest and the lowest meet." | Rhythm, ritual, cyclical repetition, session-opens, fix-times, rollover. | London/NY/Tokyo opens; month-end / quarter-end flows |

**Current dominant Ray (2026-05):** R6 (Neptune in Aries) + R7 (Uranus in Gemini).
Living log: `dse_framework_rays-currency-signatures.md` — update every session.

---

## 7. THE THREE CROSSES — PARTICIPANT CONSCIOUSNESS STAGES

| Cross | Signs | Participant Stage | How They Show Up In Price |
|---|---|---|---|
| **Mutable Cross — Personality** | Gemini, Virgo, Sagittarius, Pisces | The retail/reactive participant. Moved by every news item. Becomes the pattern. | Wick-chasers, stop-runs, liquidity pools, noise that creates ranges |
| **Fixed Cross — Soul** | Taurus, Leo, Scorpio, Aquarius | The disciplined participant. Has a system but is still inside the chart. | Trend-followers, structural-level respecters, smart money flows defining range |
| **Cardinal Cross — Spirit** | Aries, Cancer, Libra, Capricorn | The Observer. Initiates from outside the chart. Uses the field, is not used by it. | Visible as the *absence* at extremes — lack of participation when others are in full expression |

The Sovereign's job is not to predict where the Mutable Cross will capitulate — it is to stand on the Cardinal Cross and read the whole wheel from above.

**Practical read of any candlestick:**
- The wick = Mutable reaction
- The body direction = Fixed commitment
- The session close / structural pivot = Cardinal decision

---

## 8. ORTHODOX vs ESOTERIC RULERS — DUAL-LAYER CHART READING

Every chart must be read twice.

1. **Orthodox read** (L1+L2+L3): standard market mechanics, order flow, macro data — the retail/institutional consensus read.
2. **Esoteric read** (L4+L5): once the orthodox read is in, what does the ray / cross / cycle-position say — the Observer read.

A trade is only taken when both reads agree, or when the esoteric read contradicts the orthodox read with sufficient authority that the Sovereign is consciously stepping off consensus. The second case is rare and requires Observer calibration logging.

---

## 9. SACRED vs NON-SACRED PLANETS → TRANSMUTING vs REACTIVE FORCE

| Force Type | In The Market | Sovereign Response |
|---|---|---|
| **Transmuting (Sacred)** | Shifts in *how the market thinks* — regime changes, monetary doctrine shifts, structural rewrites | Fed pivot, new central-bank mandate | Update the doctrine. Old charts partially lose meaning. |
| **Reactive (Non-Sacred)** | Pressure inside an existing regime — data prints, emotional swings, momentum bursts | NFP, CPI, sentiment squeezes | Trade the reaction, do not mistake it for transmutation. |

The catastrophic error is mistaking a non-sacred reactive event for a sacred transmuting one, or vice versa.

---

## 10. THE OBSERVER FLIP — METAPHYSICAL FOUNDATION OF LAYER 5

```
RETAIL / REACTIVE WHEEL (Pisces → Aries)
price moves → emotion arises → position taken → confirmation-seeking →
becoming the pattern → capitulation → re-entry from emotion → cycle repeats

SOVEREIGN / OBSERVER WHEEL (Aries → Pisces)
calibration (Observer position) → ray/cross/cycle read → hypothesis from the field →
conditions specified → price meets the conditions OR not → position or no-position →
outcome dissolved back into the field → no residue → calibration resumes
```

STIS will only trade from the second wheel. The Observer Calibration Protocol (`skill_observer-calibration.md`) is the ritual technology that enforces this. It is run before every session. It is non-negotiable.

---

## 11. CRISIS → POLARIZATION → SWEEP — THE CYCLIC LAW OF THE MARKET

| Phase | Market Expression | Sovereign Action |
|---|---|---|
| **Crisis** | Volatility expansion, consensus breaks, narrative incoherence, liquidity gaps | Do not trade. Observe. Note which ray is ending its expression. |
| **Polarization** | A new dominant side emerges. Structure reforms. A new ray begins to express. | Calibrate to the new ray. Begin to map the new field. |
| **Sweep forward** | Trend. The field expresses the new ray unimpeded. Edge lives here. | Trade with the sweep from the Observer position — not ahead of it, not chasing it. |

**Current cycle phase (2026-05):** Late Sweep approaching Crisis (July window). Key date: July 4 Mars-Uranus conjunction.

---

## 12. REINTERPRETED SUN / MOON / RISING FOR TRADE TIMING

| Element | What To Read |
|---|---|
| **Sun of the session** | What is the present problem the market is trying to solve today? |
| **Rising of the session** | What is actually being brought forward beneath the headline? |
| **Moon of the session** | What is the dead-form narrative everyone is still trading that has already expired? |

Run this triad at the start of every session via `skill_session-calibration-triad.md`.

---

## 13. THE COMPLETE TOOL STACK (v5)

### Primary Daily Commands

```bash
# Full PMIB — run first, every session (all layers including L1b GEX)
cd tools/declination-system && python3 pmib.py

# L1b GEX — detailed read + save to quant/
cd tools/gex-engine && python3 gex_engine.py --symbol SPY --save
cd tools/gex-engine && python3 gex_engine.py --symbol GLD --save

# L1a IEC — mechanical phase scan
cd tools/iec-scanner && python3 iec_scanner.py

# Unified launcher
python3 tools/stis.py all
```

### Tool Reference

| Tool | Layer | Purpose | Key Flags |
|---|---|---|---|
| `pmib.py` | ALL | Unified daily brief — all layers in one command | `--brief` `--no-gex` `--gex-symbol` `--location` `--json` |
| `gex_engine.py` | L1b | Sovereign GEX — gamma regime, HVL, key levels | `--symbol` `--days` `--all` `--save` `--pine` `--json` |
| `iec_scanner.py` | L1a | IEC phase scan across 10 instruments | `--symbol` `--timeframe` `--json` |
| `declination_system.py` | L4 | DS formula, 6-month turning point forecast | `--today` `--months` `--chart` `--json` |
| `aspect_scanner.py` | L4 | Applying aspects, ASC/MC trigger schedule, T-squares | `--date` `--location` `--orb` |
| `schumann_resonance.py` | L2 | Live NOAA Kp + solar wind | `--watch` `--history` `--json` |
| `stis.py` | ALL | Unified launcher | `brief` `report` `iec` `ds` `aspects` `kp` `all` |

### GEX Engine — Symbol Coverage

| Symbol | Proxy For | Type |
|---|---|---|
| SPY | S&P 500 — macro gamma regime | Index |
| QQQ | Nasdaq 100 — tech/risk appetite | Index |
| GLD | XAU/USD — Gold | Direct commodity |
| FXE | EUR/USD | Currency ETF (direct) |
| FXB | GBP/USD | Currency ETF (direct) |
| FXY | USD/JPY | Currency ETF (inverted) |
| UUP | DXY / Dollar Index | Currency ETF (direct) |

### Pine Script Stack

| Script | Layer | Purpose | Update Frequency |
|---|---|---|---|
| `monday_gold_box.pine` | L1a | Weekly IEC range box | Static — permanent on chart |
| `gex_levels_v1.pine` | L1b | HVL / Call Wall / Put Wall overlay | Daily — run `gex_engine.py --pine` |
| `volume_footprint_v1.pine` | L1a | Delta histogram + imbalance detection | Static — always on chart |
| `volume_footprint_overlay_v1.pine` | L1a | POC / VAH / VAL on price chart | Static — always on chart |
| `markov_state_matrix.pine` | L1c | 3×3 transition matrix + signal | Static — reference pane |

### Recommended Chart Layout (Full STIS)

```
TOP PANE (price chart):
  → Candlesticks
  → monday_gold_box.pine
  → gex_levels_v1.pine (update daily from gex_engine.py --pine)
  → volume_footprint_overlay_v1.pine

MIDDLE PANE:
  → volume_footprint_v1.pine

BOTTOM PANE:
  → markov_state_matrix.pine
```

---

## 14. COMPLETE SKILL STACK (v5)

| Category | Skill | When |
|---|---|---|
| **Session gates** | `skill_observer-gate.md` | Every session — before anything |
| | `skill_observer-calibration.md` | Every session — non-negotiable |
| **Regime classification** | `skill_gex-regime-read.md` | Step 2 — before any chart opens |
| | `skill_regime-detection.md` | Cross-layer IEC + GEX + Markov + Vol |
| | `skill_markov-state-read.md` | Step 2 alongside GEX |
| **Chart analysis** | `skill_iec-phase-detection.md` | IEC 5-phase identification |
| | `skill_chart-read-5-layer.md` | Per-instrument analysis sequence |
| | `skill_dual-layer-chart-reading.md` | Every chart analysis session |
| | `skill_candlestick-reading.md` | Every entry evaluation |
| | `skill_chart-pattern-recognition.md` | Chart analysis |
| | `skill_liquidity-engineering.md` | Mapping institutional order zones |
| **Order flow** | `skill_footprint-read.md` | Entry evaluation — Grade A criteria 9 |
| **Trade execution** | `skill_grade-a-filter.md` v2.0 | 9-criteria pre-trade gate |
| | `skill_risk-management.md` | Before every trade — non-negotiable |
| | `skill_trade-execution.md` | Every trade entry and exit |
| | `skill_trade-management.md` | Position management after entry |
| **Esoteric** | `skill_esoteric-market-reading.md` | Weekly (Sunday) |
| | `skill_macro-field-reading.md` | Weekly (Sunday) |
| | `skill_session-calibration-triad.md` | Phase 4 of observer calibration |
| | `skill_morning-brief-protocol.md` | Step 5 — full 7-step brief |
| **Reference** | `skill_pine-script-library.md` | TradingView setup |
| | `skill_mt5-operations.md` | MT5 execution |
| | `skill_tradingview-operations.md` | TradingView analysis |

---

## 15. GRADE A FILTER — v2.0 (9 CRITERIA)

All 9 must be assessed before any trade. Core 7 must pass. Quant criteria determine grade tier.

| # | Criterion | Source Layer | Notes |
|---|---|---|---|
| 1 | HTF bias confirmed | L1 — market structure | Higher timeframe direction unambiguous |
| 2 | At a key level | L1 — OB / FVG / liquidity | GEX walls qualify as institutional levels |
| 3 | IEC phase aligned | L1a — IEC scanner | Phase 3/4 for trend; Phase 1 for range |
| 4 | Macro / Ray aligned | L3 + L4 | Dominant Ray + cycle phase supports direction |
| 5 | Clean structure | L2 — price action | No overlapping structures, clear swing |
| 6 | Entry trigger present | L2 — candlestick | Valid entry candle pattern confirmed |
| 7 | Risk:Reward ≥ 2:1 | L1 — risk management | Minimum threshold; 3:1+ preferred |
| 8 | Regime aligned | L1b + L1c | GEX regime supports trade type; Markov signal ≥ ±0.10 |
| 9 | Footprint confirms | L1a — order flow | Delta + cumulative delta alignment; cluster at level = A++ |

**Grade tiers:**
- **A++** — criteria 1–7 + 8 + 9
- **A+** — criteria 1–7 + one of (8 or 9)
- **A** — criteria 1–7 met
- **B** — criteria 1–7 met with regime conflict (reduce size 50%)
- **No trade** — any of 1–7 fails

---

## 16. AGENT STACK (v5)

| Agent | File | Function |
|---|---|---|
| Trading Analyst | `agent_trading-analyst.md` | Core session analysis + execution |
| GEX Analyst | `agent_gex-analyst.md` | L1b — gamma regime read, GEX level map, Vanna/Charm |
| Regime Detection | `agent_regime-detection.md` | Cross-layer: IEC + GEX + Markov + Vol classification |

---

## 17. DECISION ARCHITECTURE (v5)

```
┌──────────────────────────────────────────────────────────────────┐
│  STEP 0 — OBSERVER GATE (2 min)                                  │
│    skill_observer-gate.md                                        │
│    Is the Observer present? If not: log blocked. Stop.           │
├──────────────────────────────────────────────────────────────────┤
│  STEP 1 — OBSERVER CALIBRATION (10-15 min)                       │
│    skill_observer-calibration.md                                 │
│    Run full pre-session protocol. Confirm Observer position.     │
├──────────────────────────────────────────────────────────────────┤
│  STEP 2 — REGIME CLASSIFICATION (5-7 min)              ← NEW v5 │
│    python3 gex_engine.py --symbol SPY [+ pair ETFs]              │
│    skill_gex-regime-read.md + skill_markov-state-read.md         │
│    Gamma regime (above/below HVL)? Vanna direction?              │
│    Markov state + signal on primary instrument?                  │
│    → SESSION POSTURE set before any chart opens.                 │
│    → --pine flag generates TradingView levels for the session    │
├──────────────────────────────────────────────────────────────────┤
│  STEP 3 — FULL PMIB (2 min)                            ← NEW v5 │
│    python3 pmib.py                                               │
│    Outputs L1b GEX + L2 Schumann + L4 DS + L4 Aspects           │
│    + L5 coherence score (now includes gamma + Vanna signals)     │
│    DS turning point zone? Applying aspects? Kp state?            │
├──────────────────────────────────────────────────────────────────┤
│  STEP 4 — BANKING DATA + INTERMARKET CHECK (3 min)               │
│    dse_framework_banking-data-streams.md                         │
│    dse_framework_intermarket-chain.md                            │
│    DXY direction? Yield move overnight? Gold / risk sentiment?   │
├──────────────────────────────────────────────────────────────────┤
│  STEP 5 — MORNING BRIEF (10-15 min)                              │
│    skill_morning-brief-protocol.md (v2)                          │
│    Per-instrument analysis on watchlist. Sun/Rising/Moon triad.  │
│    Grade A filter (9-criteria) on any forming setups.            │
├──────────────────────────────────────────────────────────────────┤
│  STEP 6 — HYPOTHESIS + CHECKLIST (if trade forming)              │
│    dse_framework_observer-flip-trading.md                        │
│    Write hypothesis as Ray-expression + IEC phase statement.     │
│    Run 9-criteria Grade A checklist. Apply Markov size modifier. │
│    Enter only if all core criteria met. Observer maintained.     │
├──────────────────────────────────────────────────────────────────┤
│  STEP 7 — POST-SESSION LOG                                       │
│    File session entry: D.S.E/trading/logs/dse_log_YYYY-MM.md    │
│    File P.M.I.B: D.S.E/trading/logs/pmib/YYYY-MM-DD_pmib.md     │
│    File GEX map: D.S.E/trading/quant/ (if --save used)          │
│    Observer residue check. Hypothesis result filed.              │
│    Result dissolves back into field. No residue.                 │
└──────────────────────────────────────────────────────────────────┘
```

---

## 18. TRADE DECISION LOG — v5 TEMPLATE

```markdown
## Trade #[N] — [YYYY-MM-DD] — [Pair] — [Direction]

**Hypothesis:**
"This is an R[_] expression on [pair] during [cycle phase] of [regime],
supported by [Layer 3 confirmation] and confirmed by [Layer 1-2 entry trigger]."

**REGIME CONTEXT (L1b/L1c):**
- GEX Symbol: [SPY/GLD/FXE/etc]
- Gamma Regime: [POSITIVE mean-reverting / NEGATIVE trending]
- HVL: [level] | Spot [above/below] HVL
- Call Wall: [level] | Put Wall: [level]
- Markov Signal: [value] | State: [BULL/SIDEWAYS/BEAR] | Stickiness: [%]
- Sizing multiplier: [×]

**PMIB CONTEXT (L2/L4/L5):**
- Coherence Score: [/100] | Grade: [A/B/C/D]
- Kp: [value] | DS: [value] [zone]
- Dominant aspect: [planet/planet aspect orb applying/separating]

**ESOTERIC CONTEXT (L4):**
- Dominant Ray: [R1-R7] — reasoning: ...
- Cycle phase: [Crisis / Polarization / Sweep]
- Session Sun (present problem): ...
- Session Rising (actual field): ...
- Session Moon (dead narrative): ...

**PRE-TRADE DATA:**
- Account equity at entry: $___
- Risk %: ___% | Risk $: $___
- Lot size: ___

**ENTRY:** [level] | Type: [Limit/Market/Stop] | Candle: [type + TF] | Time: [EST]
**STOP:** [level] | Distance: [pips] | Type: [Structural/OB-FVG/ATR]
**TARGETS:** T1 (2:1): [_] | T2 (3:1): [_] | T3 (trail): [structure-trailing]

**Grade A Score:** [__/9] | Grade: [A++ / A+ / A / B / No trade]
- Dual-Layer Convergence: [__/10] | Esoteric: [__/5] | Orthodox: [__/5]

---

**OUTCOME:**
- T1 reached: [ ] Yes [_] [ ] No | T2: [ ] Yes [_] [ ] No
- Final exit: [level] at [time] | Reason: [stop/T1/T2/trail/valid early]
- P&L: $[___] | R-multiple: [___]R

**POST-TRADE ASSESSMENT:**
- Ray read correct: [ ] Yes [ ] No
- Cycle phase correct: [ ] Yes [ ] No
- Regime read correct: [ ] Yes [ ] No
- Hypothesis result: [ ] Confirmed [ ] Invalidated [ ] Refined

**If refined:** "[What the setup was actually showing — how to recognize it next time]"

**Observer residue check:** [ ] Clean | [ ] Named: ___ and released
**Pattern library update:** [ ] Win / [ ] Loss at [R] | Pattern #[N]
**Ray library update:** [ ] Yes — [summary] | [ ] No
```

---

## 19. ARCHITECTURE — FILE STRUCTURE (v5)

```
Desktop/Pandora/
│
├── tools/
│   ├── stis.py                              — Unified STIS launcher
│   ├── gex-engine/                          — NEW v5
│   │   └── gex_engine.py                   — L1b: Sovereign GEX Engine
│   ├── declination-system/
│   │   ├── pmib.py                          — P.M.I.B (run daily — now includes L1b)
│   │   ├── declination_system.py            — L4: DS turning point forecast
│   │   ├── aspect_scanner.py                — L4: Intraday aspect triggers
│   │   └── schumann_resonance.py            — L2: Kp/solar wind field state
│   ├── iec-scanner/
│   │   └── iec_scanner.py                   — L1a: IEC phase scanner (10 instruments)
│   └── pine-scripts/
│       ├── monday_gold_box.pine             — L1a: IEC weekly range box
│       ├── gex_levels_v1.pine              — L1b: GEX level overlay (update daily)
│       ├── volume_footprint_v1.pine        — L1a: Delta histogram + imbalance
│       ├── volume_footprint_overlay_v1.pine — L1a: POC / VAH / VAL
│       └── markov_state_matrix.pine        — L1c: 3×3 transition matrix
│
├── D.S.E/trading/
│   ├── context_trading.md                  — Living context (update every session)
│   ├── fundamentals/                       — L1 (6 files including GEX framework)
│   ├── collective-consciousness/           — L2 (3 files)
│   ├── external-reality/                  — L3 (6 files)
│   ├── esoteric/                          — L4 (7 files)
│   ├── observer/                          — L5 (3 files)
│   ├── skills/                            — 20+ skill files
│   ├── quant/                             — L1c daily Markov + L1b GEX session maps
│   │   └── YYYY-MM-DD_gex-session-map_[symbol].md  (7 symbols per session)
│   ├── options/                           — L1b daily GEX Pine output
│   ├── research/
│   │   └── 2026-05-19_dse_intelligence_current-field.md
│   └── logs/
│       ├── dse_log_trading_2026-05.md     — Active session + trade log
│       └── pmib/                          — Daily P.M.I.B session files
│
├── .claude/agents/
│   ├── agent_trading-analyst.md
│   ├── agent_gex-analyst.md               — NEW v5
│   └── agent_regime-detection.md          — NEW v5
│
└── D.S.C/
    └── dsc_prd_sovereign-trading-intelligence_v5.md  ← THIS FILE
```

---

## 20. PHASED BUILD PLAN (v5 STATUS)

### PHASE 1 — NIGREDO (Prima Materia)
**Status: COMPLETE**
All files built. Full infrastructure operational. No live trades placed yet.

### PHASE 2 — ALBEDO (Technical Mastery — paper trading)
**Status: NOT STARTED — GATE PENDING**
Gate requires all 9 checks:
```
□ Can articulate how any forex pair works from first principles (L1)
□ Can identify market structure (HH/HL, BOS, CHoCH, inducement) on a live chart
□ Can identify liquidity pools, OBs, and FVGs on a live chart
□ Can calculate correct position size for any given stop distance and account size
□ Can name the dominant Ray in the current macro environment
□ Can state current cycle phase (Crisis/Polarization/Sweep) with reasoning
□ Has run Observer Calibration Protocol for 5 consecutive sessions
□ Has written at least 5 hypothesis statements in the correct format
□ Has logged at least 10 observed patterns in the pattern library
```
When all 9 are checked: Phase 2 begins — paper trading with full 5-layer protocol.

### PHASE 3 — CITRINITAS (Esoteric Layer mastery)
**Status: NOT STARTED**
Can perform dual-layer read (orthodox + esoteric) on any chart without reference material.

### PHASE 4 — CITRINITAS DEEP (Observer Layer mastery)
**Status: NOT STARTED**
Can pre-calibrate and post-calibrate a session. Can detect slippage to Pisces→Aries wheel in real time.

### PHASE 5 — RUBEDO (Live Integration)
**Status: NOT STARTED**
Ray-expression hypothesis library compounding. Full system running on live or micro positions.

---

## 21. CROSS-DEPARTMENT INTEGRATION

| Department | Role |
|---|---|
| **D.S.C** | Houses this PRD. Tracks STIS as active build. Approves phase gates. |
| **D.S.E** | Primary home. All trading artifacts live under `D.S.E/trading/`. |
| **D.R.D** | Decoded all spine documents. Any further source research goes through D.R.D. |
| **D.O.M** | Owns the Observer Calibration ritual (L5). Cycles and ritual-design support L4. |
| **D.P.S.A** | Holds Morph's natal context — used only to inform individual calibration, not market predictions. |
| **D.I.I** | Sovereign tool builds (gex_engine.py, iec_scanner.py, pmib.py) live in the tools stack. |
| **D.S.S** | Empirical validation of ray-expression hypotheses; walk-forward statistical rigor. |

---

## 22. SUCCESS CRITERIA (v5)

1. Morph can articulate market mechanics and GEX dealer dynamics from first principles (L1/L1b).
2. Morph can read a naked forex chart and articulate what the collective consciousness of participants is doing (L2).
3. Morph can identify the dominant Ray expressing in a macro regime (L3–L4).
4. Morph can perform a dual-layer (orthodox + esoteric) read on any forex chart without reference material (L4).
5. Morph can classify the current cycle phase (Crisis / Polarization / Sweep) for any pair on any timeframe (L4).
6. Morph can state the current gamma regime (positive/negative), identify HVL, and translate it to a session posture before opening a chart (L1b).
7. Morph runs the Observer Calibration protocol pre- and post-session and can detect slippage back to the Pisces→Aries wheel (L5).
8. Every trade logged uses the v5 template including Ray-expression hypothesis and GEX regime context.
9. The quant archive (`D.S.E/trading/quant/`) has 20+ daily GEX sessions logged — sufficient for walk-forward correlation.
10. The esoteric layer is not philosophy-decoration — it produces decisions the orthodox layer alone would not produce.

---

## 23. KILL CONDITIONS

- If the esoteric layer detaches from price action and becomes pure cosmology → recalibrate down to fundamentals.
- If the orthodox layer dominates and L4/L5 become decorative → stop trading until Observer Flip protocol is re-established.
- If a trade is ever taken to *prove* the esoteric framework → stop. That is the Mutable Cross running the Sovereign.
- If GEX levels are treated as exact price targets rather than mechanical zones → recalibrate. Currency ETF chains are thinner than index chains.
- If complexity of the system exceeds Morph's ability to run it fluently in 30 minutes → simplify without abandoning the spine.
- If capital deployment pressure begins to influence the reading → stop deployment. Return to paper or micro.
- If a genuinely better framework for the same purpose is discovered → absorb it via D.R.D, don't compete with it.

---

## 24. REFERENCES (v5)

**Sovereign tool stack:**
- `tools/gex-engine/gex_engine.py` — Sovereign GEX Engine (L1b)
- `tools/declination-system/pmib.py` — Unified P.M.I.B (all layers)
- `tools/iec-scanner/iec_scanner.py` — IEC phase scanner (L1a)

**Decoded spines:**
- `D.R.D/research/trading-systems/drd_decode_quant-options-ai-trading-stack_v1.md` — L1b/L1c spine
- `research-deconstruction /markdown/drd_decode_institutional-market-architecture_v1.md` — L1a spine
- `research-deconstruction /markdown/drd_decode_earik-beann-astrotrader_v1.md` — L4 spine
- `research-deconstruction /markdown/drd_decode_bailey-esoteric-astrology.md` — L4/L5 meta-spine

**Living files (update every session):**
- `D.S.E/trading/context_trading.md` — master routing file
- `D.S.E/trading/logs/dse_log_trading_YYYY-MM.md` — active trade journal
- `D.S.E/trading/fundamentals/dse_framework_rays-currency-signatures.md` — Ray library

---

## 25. OPERATING DOCTRINE (v5 — ONE PAGE)

> The market is the aggregate internal state of everyone participating in it.
> Every candlestick is a mirror; every price is a vote from the collective.
> Seven Rays are expressing through every chart at every moment.
> Three Crosses are moving through every participant.
> The Mutable Cross *becomes* the price. The Fixed Cross *uses* the price. The Cardinal Cross *reads* the price from outside it.
> The retail trader travels Pisces → Aries: pulled by circumstance, becoming the pattern.
> The Sovereign reverses the wheel, Aries → Pisces: initiates from the Observer position, dissolves the form.
> Crisis → Polarization → Sweep is the law beneath all cycles.
> Every chart is read twice: orthodox and esoteric. Both reads must agree, or the Observer is consciously stepping off consensus.
> Beneath the chart is a force field of dealer gamma. The HVL is the regime boundary. Above it, price is pinned. Below it, price trends violently. Know which side you are on before a single position is opened.
> The Markov state is the statistical ground — it tells you the probability of tomorrow's regime from the pattern of all prior transitions. It does not predict; it informs sizing.
> The Schumann proxy is the collective nervous system meter. When it storms, the crowd becomes irrational — stand aside or reduce dramatically.
> Run `python3 pmib.py` before every session. It synthesizes all layers. It is the session opening act.
> A sacred force transmutes the regime. A non-sacred force pressurizes it. Mistaking one for the other is the catastrophic error.
> The Sun of a session is its present problem. The Rising is its actual field. The Moon is its dead narrative. Read all three before the first trade.
> Every trade dissolves back into the field. No residue. Calibration resumes.
> This is STIS.

---

*dsc_prd_sovereign-trading-intelligence_v5.md | Pandora OS | D.S.C*
*Status: ACTIVE — v5 full stack operational. Nigredo complete. Albedo gate pending.*
*Prior versions: v1 (blueprint) → v2 (5-layer stack) → v3 (Bailey esoteric) → v4 (IEC + Earik Beann tools) → v5 (Sovereign GEX Engine + full quant integration)*
