# SKILL — STIS LAYER SYNTHESIS
**How All Five Layers Work Together — The Complete Integration Map**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  When building any STIS workflow, onboarding a new agent to the trading system,
            or when layers are producing conflicting signals
DEPARTMENT: D.S.E | STIS Master Reference | Architecture map
LOADS:      None — this is the architectural reference loaded alongside other skills
PRODUCES:   Layer alignment score + session grade + position sizing modifier
CROSS-REF:  skill_stis-skill-index.md (navigation)
            skill_morning-session-sequence.md (operational execution of this map)
            skill_grade-a-filter.md (the quality gate that uses this framework)
```

---

## WHAT THIS IS

The STIS has 5 layers. Each layer contributes a different type of intelligence. They don't operate independently — they vote. Understanding how the votes interact is what produces Grade A++ setups.

---

## THE FIVE LAYERS

```
LAYER 1 — FUNDAMENTALS (the mechanical spine)
  Sub-layer 1a: IEC (Institutional Expansion Cycle)
    → What phase is the institutional cycle in?
    → Source: skill_iec-phase-detection.md
    → Output: Phase 1-5 classification + entry validity

  Sub-layer 1b: Options Flow / GEX
    → What are dealers mechanically forced to do?
    → Source: skill_gex-regime-read.md + skill_gex-daily-model.md
    → Output: Regime (trending/mean-reverting) + level stack + daily range

  Sub-layer 1c: Quant / Markov
    → What does the statistical probability say about tomorrow?
    → Source: skill_markov-state-machine.md + skill_markov-signal-generation.md
    → Output: Directional signal + position sizing guidance

LAYER 2 — COLLECTIVE CONSCIOUSNESS (market participants)
  → What is the aggregate psychological state of market participants?
  → Source: skill_poc-trend-filter.md + skill_value-area-protocol.md +
             skill_delta-volume-decode.md + skill_candlestick-reading.md
  → Output: POC bias + VAH/VAL structure + delta pressure read

LAYER 3 — EXTERNAL REALITY (macro forces)
  → What are the external forces (macro, geopolitical, liquidity) doing?
  → Source: skill_macro-field-reading.md + dse_framework_intermarket-chain.md
  → Output: Macro bias (risk-on/off) + M2 context + COT positioning

LAYER 4 — ESOTERIC (cosmic cycles)
  → What do the planetary cycles and metaphysical forces indicate?
  → Source: skill_esoteric-market-reading.md + weekly-astro-prep-protocol.md
  → Output: Weekly favorable/unfavorable windows + cycle phase + Ray dominance

LAYER 5 — OBSERVER (sovereign consciousness)
  → Am I in the Observer position? Can I act from sovereignty?
  → Source: skill_observer-calibration.md + skill_observer-gate.md
  → Output: GO (Observer present) / NO-GO (reactive state)
```

---

## THE VOTING SYSTEM

```
LAYER 5 (Observer) = PREREQUISITE
  If Observer is absent → STOP. No trade. No analysis. Restore first.

LAYER 1 = PRIMARY SIGNAL
  IEC + GEX + Markov all agree → Grade A minimum
  2 of 3 agree → Grade B
  1 of 3 → observation only

LAYER 2 = CONFIRMATION
  POC bias + delta align with Layer 1 signal → +1 grade
  Diverge from Layer 1 → -1 grade

LAYER 3 = CONTEXT FILTER
  Macro aligned → no change
  Macro diverges strongly (e.g., major risk-off + long signal) → reduce size 50%

LAYER 4 = TIMING
  Favorable esoteric day → no change (trade on standard criteria)
  Unfavorable/chaotic day → reduce size 25% or wait for clearest A+ setup only
```

---

## THE GRADE CALCULATION

```
Starting grade: Determined by Layer 1 (A / B / C / Observation)

UPGRADE TRIGGERS:
  Layer 2 confirms → A → A+
  Layer 2 + power cluster → A → A++
  All 5 layers aligned → A++

DOWNGRADE TRIGGERS:
  Layer 3 diverges → -1 grade
  Layer 4 unfavorable → -1 grade
  Layer 5 absent → NO TRADE

MINIMUM TO ENTER: Grade A (all Layer 1 sub-layers aligned)
OPTIMAL ENTRY:   Grade A+ or A++ (Layers 1+2 aligned, 3+4 compatible)
```

---

## THE BASELINE EXPECTATION (what "working correctly" looks like)

A properly functioning STIS produces:
```
Daily win rate:    ~48-52% (not alarming — this is correct)
Monthly win rate:  ~56%
Annual win rate:   ~70-77%
Average R/trade:   +0.3 to +0.5R
Max annual loss:   -10 to -15%
Max annual gain:   +30 to +60%
```

If daily performance looks terrible → this is expected.
If monthly performance is below 50% → monitor, not panic.
If annual performance is below the historical floor → investigate the edge assumption.

The STIS has a 50% win rate with 2:1 R:R as its mechanical foundation. This produces strong positive expectancy even while losing half of all trades. Never confuse a losing day with a broken system.

---

## LAYER LOAD ORDER (each session)

```
1. Layer 5 first (Observer Gate)
2. Layer 1b (VIX/Vanna → GEX regime)
3. Layer 1c (Markov signal)
4. Layer 1a (IEC phase check)
5. Layer 2 (POC, VAH/VAL, delta)
6. Layer 3 (macro — daily check, deep check weekly)
7. Layer 4 (esoteric — weekly Sunday, quick check daily)
```

*D.S.E/trading/skills | STIS Master Reference | Layer Synthesis*
