# PRD — SOVEREIGN TRADING INTELLIGENCE SYSTEM (STIS)
**Product Requirements Document | v4 | Mechanical Spine + Astro Tool Stack**
**Date Updated: 2026-05-19**
**Supersedes:** v3 (Bailey esoteric integration) — adds the IEC mechanical spine, Earik Beann astro tools, Schumann proxy, and P.M.I.B unified brief.

---

## 0. WHAT CHANGED FROM v3

v3 grounded the architecture on Bailey's *Esoteric Astrology* and locked the Five-Layer Intelligence Stack. v4 does not replace that framework — it **operationalizes** it with concrete tools and decoded research for Layers 1 and 4.

Specifically, v4 adds:

- **L1 Mechanical Spine** — the `drd_decode_institutional-market-architecture_v1.md` file is now the authoritative L1 doctrine, integrating Nathan Banks' IEC (Institutional Expansion Cycle), Kim BTS market structure methodology, and Todd's 6M Candle Setup
- **IEC Cycle Scanner** — `tools/iec-scanner/iec_scanner.py` — automated phase detection across 10 instruments (ADX, ATR, Bollinger heuristics)
- **Pine Script Monday Gold Box** — `tools/pine-scripts/monday_gold_box.pine` — TradingView indicator for IEC weekly range (zero-cost Nathan Banks template equivalent)
- **L4 Astro Tool Stack** — three working Python tools implementing Earik Beann's methodology:
  - `declination_system.py` — DS formula, 6-month turning point forecast
  - `aspect_scanner.py` — applying/separating aspects, intraday ASC/MC trigger schedule
  - `schumann_resonance.py` — NOAA SWPC Kp + solar wind as L2 Collective Consciousness proxy
- **P.M.I.B** — `pmib.py` — single-command Pre-Market Intelligence Brief integrating all layers
- **Decision Architecture Stage 0** updated — `python3 pmib.py` is now the session opener
- **Trade Decision Log** updated — adds IEC phase, DS forecast, active aspects, Kp state fields

---

## 0a. WHAT CHANGED FROM v2 (preserved from v3)

v2 established the 5-Layer Intelligence Stack and locked Forex as the primary instrument. v3 re-grounded it on Alice Bailey's *Esoteric Astrology*. That full record is in `dsc_prd_sovereign-trading-intelligence_v3.md` §0.

---

## 1. PROJECT OVERVIEW

**Project Name:** Sovereign Trading Intelligence System (STIS)
**One-Sentence Description:** A continuously evolving trading intelligence architecture within Pandora OS that fuses institutional market mechanics (IEC), planetary cycles (Earik Beann), geomagnetic field state (Schumann proxy), the Bailey esoteric framework, and observer sovereignty into a complete system for engaging forex (and adjacent markets) from the Observer position rather than the reactive personality.
**Owner:** Morph
**Primary Home:** D.S.E (with D.I.I, D.O.M, D.P.S.A, D.R.D as structural co-owners)
**Primary Instrument:** **FOREX** (locked — see §3)
**Metaphysical Spine:** Alice Bailey, *Esoteric Astrology* — decoded in `drd_decode_bailey-esoteric-astrology.md`
**Mechanical Spine:** IEC (Institutional Expansion Cycle) — decoded in `drd_decode_institutional-market-architecture_v1.md`

---

## 2. PROBLEM STATEMENT

Markets are the largest live data stream of collective human consciousness on earth. Every candlestick is an aggregate wave-function of the internal states of everyone interacting with that instrument at that moment. Most traders either become the wave (emotional reactivity) or pretend the wave doesn't contain consciousness (mechanical indicator-worship). Neither reads what is actually there.

v4 operationalizes the reading: the IEC gives the mechanical scaffolding of institutional price delivery (how price moves); the Earik Beann tools give the planetary timing backbone (when price is most likely to turn); the Schumann proxy gives the collective field state (whether the crowd's nervous system is calm or disturbed); and the Bailey framework gives the metaphysical ground from which all of this is observed. The P.M.I.B synthesizes all four into one pre-session brief.

---

## 3. FOREX IS THE PRIMARY INSTRUMENT (LOCKED)

*Unchanged from v3. Full rationale in `dsc_prd_sovereign-trading-intelligence_v3.md` §3.*

---

## 4. THE FIVE-LAYER INTELLIGENCE STACK (v4)

```
┌───────────────────────────────────────────────────────────────────┐
│  LAYER 5 — QUANTUM FIELD / OBSERVER SOVEREIGNTY                  │
│  Science: Science of the Self (the Observer Flip)                │
│  Purpose: The reversal. Trading from the Aries→Pisces wheel.     │
│  Skill:   skill_observer-calibration.md                          │
│  Artifact: dse_framework_observer-flip-trading.md                │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 4 — ESOTERIC ASTROLOGY & CYCLIC LAW                       │
│  Science: Science of Triangles + Science of Destiny              │
│  Purpose: Seven Rays, Three Crosses, planetary cycles,           │
│           declination turning points, intraday aspect triggers.  │
│  Spine:   drd_decode_earik-beann-astrotrader_v1.md               │
│  Tools:   declination_system.py, aspect_scanner.py               │
│  Artifact: dse_framework_rays-crosses-markets.md                 │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 3 — EXTERNAL REALITY FIELD                                │
│  Science: Science of the Rays (expressed in macro forces)        │
│  Purpose: Central banks, geopolitics, macro data, narrative.     │
│  Skill:   skill_macro-field-reading.md                           │
│  Artifact: dse_framework_external-reality-field.md               │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 2 — COLLECTIVE CONSCIOUSNESS (PRICE ACTION + EM FIELD)    │
│  Science: Psychological-astrological (participant consciousness) │
│  Purpose: Candlesticks as aggregate internal state mirror.       │
│           Kp index / solar wind as quantified field-state proxy. │
│  Tool:    schumann_resonance.py (NOAA SWPC — live)               │
│  Artifact: dse_framework_collective-consciousness-price.md       │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 1 — SOVEREIGN FUNDAMENTALS / IEC MECHANICS                │
│  Science: (Prima materia — institutional price delivery)         │
│  Purpose: IEC 5-phase cycle, market structure, order flow,       │
│           Monday Gold Box, Todd 6M setup, Kim BTS methodology.   │
│  Spine:   drd_decode_institutional-market-architecture_v1.md     │
│  Tools:   iec_scanner.py, monday_gold_box.pine                   │
│  Artifact: dse_framework_market-structure.md (+ siblings)        │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 1b — GEX / OPTIONS MECHANICS (NEW 2026-05-20)             │
│  Science: (Dealer delta hedging as intraday mechanical force)    │
│  Purpose: Gamma regime (positive/negative), HVL, GEX levels,    │
│           Vanna/VIX mechanic, Options Greeks as market forces.   │
│  Spine:   drd_decode_quant-options-ai-trading-stack_v1.md        │
│  Tools:   (external GEX data provider — pending selection)       │
│  Artifact: dse_framework_gex-options-mechanics.md                │
├───────────────────────────────────────────────────────────────────┤
│  LAYER 1c — QUANT / MARKOV STATE (NEW 2026-05-20)                │
│  Science: (Statistical regime probability — hedge fund method)   │
│  Purpose: 3-state Markov chain, transition matrix, stickiness,   │
│           signal = P(bull) - P(bear), position sizing by signal. │
│  Spine:   drd_decode_quant-options-ai-trading-stack_v1.md        │
│  Tools:   markov_state_matrix.pine (TradingView)                 │
│  Artifact: dse_framework_gex-options-mechanics.md (linked)       │
└───────────────────────────────────────────────────────────────────┘
```

---

## 5–12. UNCHANGED FROM v3

*Sections 5–12 (Five Sciences mapping, Seven Rays, Three Crosses, Orthodox vs Esoteric, Sacred vs Non-Sacred, Observer Flip, Crisis→Polarization→Sweep, Sun/Moon/Rising) are unchanged from v3. See `dsc_prd_sovereign-trading-intelligence_v3.md` §§5–12.*

---

## 13. L1 MECHANICAL SPINE — IEC FRAMEWORK

The `drd_decode_institutional-market-architecture_v1.md` is the primary L1 reference. It contains the complete decoded frameworks of:

| Teacher | Framework | Core Concept |
|---------|-----------|-------------|
| Nathan Banks (@tradewithbanks) | IEC — Institutional Expansion Cycle | 5-phase model: Accumulation → Manipulation → Expansion → Retracement → Reversal |
| Kim (IC4XCLEARLY) | BTS — Build To Structure | Zone-to-zone price delivery, market structure markup, weekly workflow |
| Todd (IC4XCLEARLY) | 6M Candle Setup | Monthly candle analysis, Power of 3 (AMD), Grade A criteria for institutional entries |

**IEC Phase Reference:**

| Phase | Name | Characteristics | Action |
|-------|------|----------------|--------|
| 1 | Accumulation | Low ADX, ATR flat, BB squeeze, range-bound | Wait |
| 2 | Manipulation | False breakout / stop hunt opposing true direction | Caution — wick trap |
| 3 | Expansion | ADX >25, ATR expanding, conviction close outside range | Trade the move |
| 4 | Retracement | 38–62% fib pullback, ADX retreating, ATR contracting | Entry zone for Phase 3 continuation |
| 5 | Reversal | DI flip, new structure break, new cycle begins | Flip bias |

**Monday Gold Box (IEC weekly application):**
- Monday range = Phase 1–2 (accumulation + manipulation)
- Tuesday–Thursday expansion = Phase 3
- Box breach = directional bias confirmation
- Pine Script: `tools/pine-scripts/monday_gold_box.pine`
- Scanner: `tools/iec-scanner/iec_scanner.py`

---

## 14. L2 COLLECTIVE CONSCIOUSNESS — SCHUMANN PROXY

The Schumann Resonance (~7.83 Hz fundamental) correlates with collective nervous system coherence. Direct SR monitoring requires hardware. NOAA SWPC provides the best available proxy through real-time geomagnetic data.

**Tool:** `tools/declination-system/schumann_resonance.py`

| Kp Index | Field State | STIS L2 State | Trading Action |
|----------|-------------|---------------|----------------|
| 0–2 | Quiet | Calm collective field | Full size, trend-following favored |
| 3–4 | Unsettled | Elevated EM noise | Reduce size 20–30%, tighter stops |
| 5–6 | Storm | Geomagnetic storm | Minimum size, expect sharp reversals |
| 7+ | Severe storm | Extreme disturbance | Stand completely aside |

**Solar wind precursor:** Speed >450 km/s or Bz < −5 nT → Kp escalation likely within 30–60 min. Watch for upgrade.

---

## 15. TOOL STACK (v4)

All tools in `~/Desktop/Pandora/tools/`.

### Primary Daily Command
```bash
python3 tools/declination-system/pmib.py
```
Runs the full Pre-Market Intelligence Brief in ~15 seconds. Combines L1+L2+L4.

### Individual Tools

| Tool | File | Layer | Purpose | Key Flags |
|------|------|-------|---------|-----------|
| **P.M.I.B** | `declination-system/pmib.py` | L1+L2+L4+L5 | Unified pre-session brief | `--brief` `--tomorrow` `--location` `--json` |
| **Declination System** | `declination-system/declination_system.py` | L4 | DS = 6×Mer+5×Ven+4×Ear+3×Mar+2×Jup+1×Sat. 6-month turning point forecast. | `--today` `--months N` `--chart` `--json` |
| **Aspect Scanner** | `declination-system/aspect_scanner.py` | L4 | Applying/separating aspects, ASC/MC trigger schedule, T-squares | `--date` `--location` `--orb` `--time` |
| **Schumann Proxy** | `declination-system/schumann_resonance.py` | L2 | Live NOAA Kp + solar wind. L2 field state. | `--watch` `--history` `--json` |
| **IEC Scanner** | `iec-scanner/iec_scanner.py` | L1 | 10-instrument IEC phase scan (ADX, ATR, BB heuristics) | `--symbol` `--timeframe` `--json` |
| **Monday Gold Box** | `pine-scripts/monday_gold_box.pine` | L1 | TradingView Pine Script — weekly IEC range box | (paste into TradingView) |
| **Markov State Matrix** | `pine-scripts/markov_state_matrix.pine` | L1c | 3×3 hedge fund transition probability matrix live on chart — quant state + signal | (paste into TradingView) |
| **Unified Launcher** | `stis.py` | ALL | `brief` `report` `ds` `aspects` `kp` `iec` `all` | — |

### Unified launcher
```bash
python3 tools/stis.py brief    # one-line status
python3 tools/stis.py report   # full P.M.I.B
python3 tools/stis.py iec      # IEC scan all instruments
python3 tools/stis.py all      # run everything
```

---

## 16. DECISION ARCHITECTURE (v4)

```
┌──────────────────────────────────────────────────────────────────┐
│  STAGE 0 — CALIBRATION                                           │
│    RUN: python3 pmib.py              (L1+L2+L4 automated)        │
│    Observer position check                     (L5)              │
│    Session Sun/Rising/Moon triad                (L4)              │
│    IEC phase check on target instrument         (L1 — iec_scanner)│
│    Kp state check                               (L2 — schumann)  │
│    DS position + next turning point             (L4 — decl sys)  │
│    Active aspects + today's trigger times       (L4 — asp scanner)│
├──────────────────────────────────────────────────────────────────┤
│  STAGE 1 — INPUT                                                 │
│    Macro / data feed (L3)                                         │
│    Price action (L2)                                              │
│    IEC phase + structure (L1)                                     │
├──────────────────────────────────────────────────────────────────┤
│  STAGE 2 — SYNTHESIS (DUAL-LAYER READ)                           │
│    Orthodox read (L1+L2+L3): IEC phase, structure, momentum       │
│    Esoteric read: dominant Ray, DS zone, applying aspects (L4)    │
│    L2 modifier: Kp state — adjust confidence accordingly          │
│    Agreement check. Contradiction → Observer Flip protocol (L5)  │
├──────────────────────────────────────────────────────────────────┤
│  STAGE 3 — DECISION                                              │
│    Take / Don't take. If take: hypothesis written as             │
│    Ray-expression + IEC phase statement.                          │
├──────────────────────────────────────────────────────────────────┤
│  STAGE 4 — EXECUTION                                             │
│    Risk first (L1). Entry, stop, target. Observer maintained.    │
├──────────────────────────────────────────────────────────────────┤
│  STAGE 5 — POST-TRADE                                            │
│    Outcome logged in Trade Decision Log v4 template.             │
│    Observer Flip recalibration. Hypothesis result filed.         │
│    Result dissolves back into field. No residue.                 │
└──────────────────────────────────────────────────────────────────┘
```

---

## 17. TRADE DECISION LOG (v4 TEMPLATE)

```markdown
## Trade / Consideration — [YYYY-MM-DD HH:MM UTC]
**Pair:** [e.g. EURUSD]
**Session:** [Asia / London / NY]
**IEC Phase:** [1 Accumulation / 2 Manipulation / 3 Expansion / 4 Retracement / 5 Reversal]
**DS Reading:** [value] — [TOP ZONE / BOTTOM ZONE / NEUTRAL]  Next turn: [date] [type]
**Active Aspects:** [e.g. Moon/Jupiter trine 0.3° APPLYING] or None
**Kp State:** [QUIET / UNSETTLED / STORM] — Kp=[value]
**Cycle phase:** [Crisis / Polarization / Sweep]
**Dominant Ray:** [R1–R7] — reasoning: ...
**Cross position:** [Mutable / Fixed / Cardinal dominant]
**Orthodox read:** ...
**Esoteric read:** ...
**Agreement?:** [Yes / No — if No, Observer Flip protocol ran: ...]
**Session triad:**
  - Sun (present problem): ...
  - Rising (actual field): ...
  - Moon (dead narrative): ...
**Hypothesis:** "This is an R_ expression on [pair] in IEC Phase [N], [cycle phase] of [regime]."
**Decision:** [Taken / Not taken]
**Risk:** ...
**Entry / Stop / Target:** ...
**Outcome:** ...
**Hypothesis result:** [Confirmed / Invalidated / Refined → new statement]
**Observer residue check:** [Clean / Residue detected → recalibration note]
```

---

## 18. ARCHITECTURE — FILE STRUCTURE (v4)

```
Desktop/Pandora/
│
├── tools/
│   ├── stis.py                              — Unified STIS launcher
│   ├── declination-system/
│   │   ├── pmib.py                          — P.M.I.B (run this daily)
│   │   ├── declination_system.py            — L4: DS turning point forecast
│   │   ├── aspect_scanner.py                — L4: Intraday aspect triggers
│   │   ├── schumann_resonance.py            — L2: Kp/solar wind field state
│   │   └── README.md
│   ├── iec-scanner/
│   │   └── iec_scanner.py                   — L1: IEC phase scanner
│   └── pine-scripts/
│       ├── monday_gold_box.pine             — L1: TradingView Monday box
│       └── markov_state_matrix.pine         — L1c: Hedge fund 3×3 Markov transition matrix (NEW 2026-05-20)
│
├── research-deconstruction /markdown/
│   ├── drd_decode_institutional-market-architecture_v1.md  ← L1 SPINE
│   ├── drd_decode_earik-beann-astrotrader_v1.md            ← L4 SPINE
│   └── drd_decode_bailey-esoteric-astrology.md             ← L4/L5 META SPINE
│
└── D.S.C/
    └── dsc_prd_sovereign-trading-intelligence_v4.md        ← THIS FILE
```

*Full D.S.E/trading/ structure unchanged from v3 §15.*

---

## 19–22. UNCHANGED FROM v3

*Sections on Phased Build Plan, Cross-Department Integration, Success Criteria, Kill Conditions — see `dsc_prd_sovereign-trading-intelligence_v3.md` §§16–19.*

---

## 23. REFERENCES (v4)

**Mechanical Spine (L1 — new in v4):**
- `research-deconstruction /markdown/drd_decode_institutional-market-architecture_v1.md`

**Astro Tool Spine (L4 — new in v4):**
- `research-deconstruction /markdown/drd_decode_earik-beann-astrotrader_v1.md`

**Metaphysical Spine (L4/L5 — from v3):**
- `research-deconstruction /markdown/drd_decode_bailey-esoteric-astrology.md`

**OS files:**
- `pandora.md` — master context
- `D.S.C/dsc_prd_sovereign-trading-intelligence_v3.md` — prior version
- `D.S.E/Context.md`, `D.I.I/Context.md`, `D.O.M/context.md`, `D.P.S.A/context.md`

---

## 24. OPERATING DOCTRINE (v4 — ONE PAGE)

> The market is the aggregate internal state of everyone participating in it.
> Every candlestick is a mirror; every price is a vote from the collective.
> Seven Rays are expressing through every chart at every moment.
> Three Crosses are moving through every participant.
> The Mutable Cross *becomes* the price. The Fixed Cross *uses* the price. The Cardinal Cross *reads* the price from outside it.
> The retail trader travels Pisces → Aries: pulled by circumstance, becoming the pattern.
> The Sovereign reverses the wheel, Aries → Pisces: initiates from the Observer position, dissolves the form.
> Crisis → Polarization → Sweep is the law beneath all cycles.
> Every chart is read twice: orthodox and esoteric. Both reads must agree, or the Observer is consciously stepping off consensus.
> IEC Phases are the mechanical skeleton: Accumulation, Manipulation, Expansion, Retracement, Reversal. The Sovereign knows which phase is active before entering.
> The Declination System shows the planetary tide. When DS is in the top zone, the tide is running toward a top — the Sovereign reads it, not fights it.
> The aspects are the timing mechanism. Applying aspects build energy. The ASC/MC trigger fires it. T-squares define the price target.
> The Kp index is the collective nervous system meter. When it storms, the crowd becomes irrational — stand aside or reduce dramatically.
> Run `python3 pmib.py` before every session. It synthesizes the field. It is the session opening act.
> A sacred force transmutes the regime. A non-sacred force pressurizes it. Mistaking one for the other is the catastrophic error.
> The Sun of a session is its present problem. The Rising is its actual field. The Moon is its dead narrative. Read all three before the first trade.
> Every trade dissolves back into the field. No residue. Calibration resumes.
> This is STIS.

---

*dsc_prd_sovereign-trading-intelligence_v4.md | Pandora OS | D.S.C*
*Status: ACTIVE — v4 tool stack operational. L1 + L2 + L4 tools live. L3 macro-field and L5 Observer skills pending build.*
