# SKILL — Regime Detection
**Market Regime Classification | Three-Layer Protocol**
**Load when:** Beginning any session, calibrating position sizing, evaluating strategy appropriateness, or when market behavior seems inconsistent with current read.
**Connects:** `skill_iec-phase-detection.md`, `skill_gex-regime-read.md`, `skill_markov-state-read.md`
**Department:** D.S.E trading workspace | STIS Cross-Layer

---

## WHAT THIS IS

A trading strategy that works in one regime will fail in another. The Regime Detection skill classifies the current market environment across three independent layers before any trade decision is made. The three layers operate at different timescales and use different detection mechanisms — when they align, conviction is maximized.

**Three layers:**

| Layer | Timescale | What It Measures | Skill |
|-------|-----------|-----------------|-------|
| **IEC Phase** | Weekly/Daily | Structural expansion phase | `skill_iec-phase-detection.md` |
| **Gamma Regime** | Intraday/Daily | Options dealer force field | `skill_gex-regime-read.md` |
| **Markov State** | Daily (20-day rolling) | Statistical probability of state persistence | `skill_markov-state-read.md` |
| **Volatility Regime** | Rolling | ATR percentile — trending or mean-reverting environment | (this skill) |

---

## REGIME CLASSIFICATION PROTOCOL

### LAYER 1 — IEC STRUCTURAL PHASE

Run `skill_iec-phase-detection.md` or check `tools/iec-scanner/iec_scanner.py`

```
PHASE 1 — ACCUMULATION:   Range. Wait. No directional trades.
PHASE 2 — IMPULSE TRAP:   False move opposite to true direction. Do not chase.
PHASE 3 — EXPANSION:      Trend trade. Maximum conviction. Full size eligible.
PHASE 4 — RETRACEMENT:    Pullback within Phase 3. Re-entry opportunity.
PHASE 5 — REVERSAL:       Trend ending. Reduce/exit. Watch for new Phase 1.
```

**IEC Regime Output:** `IEC: Phase [N] — [name] | Bias: [long/short/wait]`

---

### LAYER 2 — GAMMA REGIME

Run `skill_gex-regime-read.md`

```
POSITIVE GAMMA (above HVL): Mean-reverting. Fade strategy.
NEGATIVE GAMMA (below HVL): Trending. Follow strategy.
```

**Gamma Regime Output:** `GEX: [mean-reverting/trending] | HVL [level] | Vanna [tailwind/headwind/neutral]`

---

### LAYER 3 — MARKOV STATE

Run `skill_markov-state-read.md` or check the `markov_state_matrix.pine` indicator

```
BULL STATE (20-day return ≥ +5%):     Long bias | stickiness [X]%
SIDEWAYS STATE (-5% to +5%):          Neutral | no directional edge
BEAR STATE (20-day return ≤ -5%):     Short bias | stickiness [X]%

SIGNAL: P(bull tomorrow) - P(bear tomorrow)
  Positive signal = long bias (size proportional to magnitude)
  Negative signal = short bias
  Near zero = no edge — observe only
```

**Markov Output:** `Markov: [BULL/SIDEWAYS/BEAR] | Signal: [+X.XX / -X.XX] | Stickiness: [X]%`

---

### LAYER 4 — VOLATILITY REGIME

Manual calculation or Pine Script:
```
ATR percentile over 100 bars:
  ATR > 80th percentile:   HIGH VOLATILITY REGIME
    → Trend strategies favored
    → Wider stops required
    → Momentum setups valid
    → Mean-reversion setups HIGH RISK

  ATR < 20th percentile:   LOW VOLATILITY REGIME
    → Mean-reversion strategies favored
    → Tighter stops possible
    → Range-bound setups valid
    → Breakout setups HIGH RISK (often false)

  ATR 20th–80th:           NORMAL VOLATILITY REGIME
    → Both strategy types have edge
    → Use IEC + Gamma to determine appropriate approach
```

**Vol Regime Output:** `Vol: [HIGH/NORMAL/LOW] | ATR [value] at [percentile] percentile`

---

## REGIME ALIGNMENT MATRIX

Cross-reference all four layers. The more aligned, the higher the conviction.

```
MAXIMUM CONVICTION (all 4 aligned):
  IEC Phase 3 (Expansion)
  + Gamma Trending (Negative GEX / below HVL)
  + Markov Bull State (high stickiness, positive signal)
  + Vol High Percentile
  = FOLLOW THE TREND | Grade A+ | Full size eligible

HIGH CONVICTION (3 aligned):
  IEC Phase 3 + Gamma Trending + Markov Bull = strong long environment
  IEC Phase 3 + Gamma Trending + Vol High = trend confirmation
  = TRADE DIRECTION | Grade A | Standard size

MODERATE CONVICTION (2 aligned):
  IEC Phase 3 + Gamma Mean-Reverting = structural expansion but options are dampening
  → Expect slower, choppier expansion. Wait for deeper pullback before entry.
  → Reduce size. Grade B only.

LOW CONVICTION (regimes conflict):
  IEC Phase 3 (Expansion) + Gamma Mean-Reverting (above HVL) + Markov Sideways
  = Structural desire to trend but options market dampening moves
  → OBSERVE ONLY. Wait for regime alignment.

NO TRADE:
  IEC Phase 1 (Accumulation) + any other regime
  → Structural range. No directional edge. Map only.

  Markov Signal near zero (±0.05)
  → Statistical dead zone. No probability edge. Reduce or flat.
```

---

## REGIME CONFLICT RESOLUTION

When layers disagree, use this priority hierarchy:

```
PRIORITY 1 — IEC Phase
  The structural phase is the foundation. If Phase 1 (accumulation),
  nothing else matters — no trade regardless of other signals.

PRIORITY 2 — Gamma Regime
  The intraday force field. If you are fighting the gamma regime,
  you are fighting mechanical dealer forces. Avoid.

PRIORITY 3 — Markov State
  Statistical backdrop. Use for position sizing and holding time.
  Strong signal = full size and hold. Weak signal = reduced size, quicker exit.

PRIORITY 4 — Volatility Regime
  Determines strategy type (trend vs mean-reversion). Use to calibrate stop width.
```

---

## REGIME CHANGE DETECTION

Watch for these signals that a regime shift is occurring:

```
IEC PHASE TRANSITION SIGNALS:
  Phase 1 → 2: Strong move opposite to accumulation bias (Impulse Trap forming)
  Phase 2 → 3: Price reclaims accumulation range + ADX begins rising
  Phase 3 → 4: ADX retreating, ATR contracting, first lower high
  Phase 4 → 5: Lower high + lower low + DI flip

GAMMA REGIME FLIP SIGNALS:
  Transition: Price crosses the HVL level
  Confirmation: 2 consecutive closes on new side of HVL
  Warning: Do not assume flip on first cross — false crosses are common

MARKOV STATE TRANSITION SIGNALS:
  20-day cumulative return crosses ±5% threshold
  Signal flips sign (positive → negative or vice versa)
  Stickiness score drops below 50% (state instability)

VOLATILITY REGIME TRANSITION SIGNALS:
  ATR crosses 80th or 20th percentile (use 3-day SMA of ATR to reduce noise)
```

---

## SESSION REGIME LOG FORMAT

```
─────────────────────────────────────────────────────
REGIME DETECTION — [DATE] [SESSION]
─────────────────────────────────────────────────────
IEC PHASE:       Phase [N] — [name] | Bias: [direction/wait]
GAMMA REGIME:    [mean-reverting/trending] | HVL: [level]
VANNA:           [tailwind/headwind/neutral] | VIX: [level/direction]
MARKOV STATE:    [BULL/SIDEWAYS/BEAR] | Signal: [X.XX] | Stick: [X]%
VOL REGIME:      [HIGH/NORMAL/LOW] | ATR: [X.X] at [N]th pct

ALIGNMENT:       [MAXIMUM/HIGH/MODERATE/LOW/NONE]
DOMINANT FORCE:  [what is running the show today]
SESSION POSTURE: [TREND LONG / TREND SHORT / FADE / OBSERVE / NO TRADE]
STRATEGY TYPE:   [trend / mean-reversion / wait]
─────────────────────────────────────────────────────
```

---

## REGIME ADAPTATION RULES

**Positive gamma + Markov Bull + IEC Phase 4 (retracement):**
Wait for the retracement to complete near a GEX level. The gamma regime will pin price and create the clean re-entry. This is the ideal Grade A re-entry scenario.

**Negative gamma + Markov Bear + IEC Phase 3 (expansion):**
All three systems saying trend — maximum conviction scenario. The dealer mechanics are amplifying every move. Do not fade. Trail stops wide. This is the 400-500pt NQ drop scenario.

**IEC Phase 3 + Positive Gamma conflict:**
Structural desire to expand but options market dampening it. Common during "grind up" periods where price is above HVL. Reduce position size and expect slower, choppier expansion. Take profits at GEX levels rather than holding for extended targets.

---

*D.S.E/trading/skills | STIS Regime Classification | Pandora OS*
*Cross-links: skill_iec-phase-detection.md | skill_gex-regime-read.md | skill_markov-state-read.md*
