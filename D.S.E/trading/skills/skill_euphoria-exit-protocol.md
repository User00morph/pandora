# SKILL — EUPHORIA EXIT PROTOCOL
**The Only Valid Conditions for Overriding the No-Take-Profit Rule**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  A position has moved 10× or more the initial stop distance AND
            the asset appears to be in historic overbought territory
DEPARTMENT: D.S.E | STIS Execution Layer | Discretionary override
LOADS:      skill_asymmetric-return-design.md (the rule being overridden)
            skill_exit-criteria-protocol.md (pre-defined exit framework)
PRODUCES:   GO / NO-GO verdict on partial exit + recommended exit size
CROSS-REF:  skill_relative-strength-analysis.md (ratio charts confirm euphoria)
            skill_on-chain-fundamental-valuation.md (if crypto asset)
```

---

## WHAT THIS IS

The default STIS rule is: no take profit. Let the stop do all the work. The system is designed for asymmetric returns — unlimited upside, defined downside.

This protocol defines the ONLY conditions under which a partial discretionary exit is justified — when a position has moved so far into historic territory that the conditions for a structural reversal are all present simultaneously.

**This is a rare event. Most traders will never need this skill. Most years, the stop handles all exits.**

---

## THE FIVE EUPHORIA CONDITIONS (ALL must be true)

```
CONDITION 1 — MAGNITUDE
  Position has moved ≥ 10× the initial stop distance from entry
  Example: Stop was 50 pips → position is now 500+ pips in profit
  Example: Stop was $4,000 → position profit is $40,000+
  
CONDITION 2 — HISTORIC TERRITORY
  Asset is at or near all-time highs
  OR: asset is at a level that has historically marked major tops
  NOT: asset is just up a lot from a local low
  
CONDITION 3 — MASS PUBLIC AWARENESS
  The asset is being widely discussed in mainstream media
  Non-traders are asking about it / talking about it
  "Everyone is talking about [asset]" — this is the contrarian signal
  
CONDITION 4 — PARABOLIC PRICE ACTION
  The price chart shows vertical or near-vertical acceleration
  Multiple standard deviations above any reasonable moving average
  The chart "looks like a hockey stick"
  
CONDITION 5 — VALUATION EXTREME (for equities/crypto)
  For crypto: funding rates extremely high (paying > 50% APR to hold longs)
  For equities: PE ratio or price multiple at historic extremes
  For commodities: price meaningfully above the long-term inflation-adjusted trend
```

---

## HISTORICAL EXAMPLES (all five conditions were present)

| Asset | Year | Event |
|---|---|---|
| NASDAQ | 1999-2000 | Tech bubble — 5/5 conditions met |
| Nikkei 225 | 1989 | Japanese bubble — 5/5 conditions met |
| Bitcoin | Dec 2020 | 100% gain in one day / $69k peak — 4/5 met |
| Silver | 1979-1980 | Hunt Brothers corner attempt — 5/5 met |
| Silver | 2025 | Travis Woo's $87 exit — 4/5 met |

---

## THE DECISION PROTOCOL

```
STEP 1: Check all 5 conditions
  Count how many are true: [0-5]

STEP 2: Decision matrix
  5/5: Execute partial exit (high conviction)
  4/5: Consider partial exit (monitor — may still be early)
  3/5: Do not exit — this is just a strong trend
  2/5 or less: Do not exit — normal systematic position

STEP 3: If executing partial exit
  Exit SIZE: 25-50% of the position only (NEVER 100%)
  Keep 50-75% running to capture any further upside
  Move stop aggressively on remaining position
  
STEP 4: Log the discretionary exit with justification
  "Exited [X%] at [price]. Conditions met: [list which 5 conditions]. 
   Remaining [X%] still running with stop at [price]."
```

---

## OUTPUT FORMAT

```
EUPHORIA CHECK — [DATE] [INSTRUMENT]
CONDITIONS MET: [X/5]
  [✓/✗] 1. Magnitude: [X× stop distance]
  [✓/✗] 2. Historic territory: [description]
  [✓/✗] 3. Mass awareness: [evidence]
  [✓/✗] 4. Parabolic action: [yes/no]
  [✓/✗] 5. Valuation extreme: [metric]
  
VERDICT: [PARTIAL EXIT JUSTIFIED / NOT YET — CONTINUE HOLDING]
EXIT PLAN (if justified): [X% at [price], remaining [X%] with stop at [price]]
```

---

## RULES

- NEVER exit 100% — the biggest moves often continue past where euphoria is obvious
- This skill overrides the no-take-profit rule ONLY — all other rules remain
- If even one condition is absent, this is NOT a euphoria exit — let the stop work
- Document every discretionary exit with all five conditions noted

*D.S.E/trading/skills | STIS Execution Layer | Euphoria Override*
