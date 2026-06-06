# SKILL — RELATIVE STRENGTH ANALYSIS
**Using Ratio Charts to Find the Strongest Assets**

```
STATUS:     active
VERSION:    1.0
LOAD WHEN:  Asset selection decisions, portfolio rebalancing, or when identifying
            which instrument has the strongest institutional preference
DEPARTMENT: D.S.E | STIS Layer 1a + Layer 3 | Asset selection
LOADS:      skill_cross-asset-correlation-read.md (for portfolio context)
PRODUCES:   Relative strength ranking of primary instruments + directional bias
CROSS-REF:  skill_uncorrelated-portfolio-architecture.md (portfolio construction)
            skill_inflation-asset-thesis.md (macro context for strength reads)
            skill_poc-trend-filter.md (trend confirmation at instrument level)
```

---

## WHAT THIS IS

Relative strength measures how an asset performs compared to its benchmark — not just in absolute terms. An asset can be rising while losing relative strength (being outpaced by its peers). The strongest relative strength = strongest institutional preference = highest-probability trend continuation.

---

## THE RATIO CHART METHOD

```
Ratio chart = Asset A price / Benchmark price

Plotted over time:
  RISING ratio:  Asset A is outperforming the benchmark
  FALLING ratio: Asset A is underperforming the benchmark
  FLAT ratio:    Moving in lockstep with the benchmark

PRIMARY BENCHMARKS:
  For crypto:      Asset / BTC (e.g., TRX/BTC)
  For equities:    Asset / SPX (e.g., AAPL/SPX)
  For currencies:  Asset / DXY (e.g., EUR/DXY)
  For commodities: Asset / Gold (e.g., Silver/Gold ratio)
```

---

## THE SELECTION RULE

**Only add positions in assets with rising relative strength against their benchmark.**

```
STRONG RELATIVE STRENGTH:
  Ratio making new highs
  Ratio well above its 20-period moving average
  Ratio trend intact for 3+ months
  → High priority — this is where institutional money is flowing

WEAK RELATIVE STRENGTH:
  Ratio making new lows
  Ratio below its 20-period moving average
  Ratio declining even while absolute price rises
  → Avoid or underweight — institutions are rotating out
  
NEUTRAL:
  Ratio flat or oscillating
  → Equal weight — no directional institutional preference
```

---

## THE STIS RELATIVE STRENGTH SCAN

Run weekly during Sunday prep:

```
SCAN ALL PRIMARY INSTRUMENTS:
  
  Instrument     | Benchmark | Ratio 12M | Ratio 1M  | Signal
  ─────────────────────────────────────────────────────────────
  Gold           | DXY       | [up/flat/dn] | [up/flat/dn] | [LONG/PASS/AVOID]
  S&P 500        | World EQ  | [up/flat/dn] | [up/flat/dn] | [LONG/PASS/AVOID]
  Bitcoin        | Gold      | [up/flat/dn] | [up/flat/dn] | [LONG/PASS/AVOID]
  Nikkei         | SPX       | [up/flat/dn] | [up/flat/dn] | [LONG/PASS/AVOID]
  EUR/USD        | DXY       | [up/flat/dn] | [up/flat/dn] | [LONG/PASS/AVOID]

SIGNAL CRITERIA:
  LONG:  Ratio making new highs on 12M AND 1M timeframe
  PASS:  Ratio mixed or consolidating
  AVOID: Ratio making new lows on either timeframe
```

---

## THE TRX EXAMPLE (live application)

```
TRX/BTC ratio: "absolutely demolishing Bitcoin"
  12M performance: TRX up 65% vs. BTC
  Ratio at new highs
  Signal: MAXIMUM INSTITUTIONAL PREFERENCE
  
Action taken: Large long position, aggressive pyramiding
Logic: When an asset is outperforming its market benchmark by this margin,
       institutions are actively preferring it — the flow is structural
```

---

## OUTPUT FORMAT

```
RELATIVE STRENGTH SCAN — [DATE]
─────────────────────────────────────────
TOP RS ASSETS (ratio at new highs):
  1. [Instrument] vs [benchmark]: [X%] outperformance | [N months of strength]
  2. [Instrument] vs [benchmark]: [X%] outperformance | [N months of strength]

WEAKEST RS ASSETS (ratio declining):
  1. [Instrument] vs [benchmark]: [X%] underperformance
  
PORTFOLIO IMPLICATIONS:
  Overweight: [top RS assets]
  Underweight or avoid: [weakest RS assets]
```

*D.S.E/trading/skills | STIS Layer 1a + 3 | Asset Selection*
