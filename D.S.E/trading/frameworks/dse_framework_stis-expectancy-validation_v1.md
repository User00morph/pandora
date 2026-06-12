# D.S.E FRAMEWORK — STIS Expectancy-First System Design & Validation Protocol
**Compiled:** 2026-06-11
**Source:** "The Math of Winning in Trading" + "How I Develop Trading Strategies: Permutation Tests" + "How Quants Engineer Portfolios" + Full Trading Education (21K words)
**Tier:** CORE DOCTRINE — load before designing any new STIS strategy

---

## THE FUNDAMENTAL LAW

> "Trading is not a prediction problem. It is a math problem."

Every STIS strategy starts with a single question: **What is the expectancy?**

Not: "Does this look good on a chart?"
Not: "What is the win rate?"
Not: "What is the profit factor?"
**Only: What is the expectancy per trade, net of real costs?**

---

## THE EXPECTANCY FORMULA

```
Expectancy = (Win% × Average Win) − (Loss% × Average Loss)
```

**Rules:**
- If expectancy is POSITIVE: profitable system. Deploy and repeat at scale.
- If expectancy is NEGATIVE: unprofitable system. Do not trade it, regardless of how it looks.
- Win rate alone means nothing. R-multiple alone means nothing. Only the combination matters.

**The Trade-Off Matrix (there is no perfect system):**

| System Profile | Win% | R-Multiple | Expectancy/Trade |
|---------------|------|-----------|-----------------|
| High win rate, low reward | 70% | 1R | ~$400 |
| Low win rate, high reward | 15% | 8R | ~$1,200 |
| Balanced | 50% | 2.5R | ~$1,250 |
| Day trading average (real data) | ~45% | 0.8R | Negative |

> "15% win rate and 70% win rate can produce nearly identical expectancy. Stop chasing win rate."

**The hidden cost — real expectancy vs paper expectancy:**
```
Paper Expectancy: calculated from backtest (ignores transaction costs)
Real Expectancy = Paper Expectancy − (Spread + Commission + Slippage) per trade
```
A system can show positive paper expectancy and still lose money live. Always calculate real costs.

---

## THE VARIANCE DOCTRINE (Why Traders Quit Too Early)

**The 100-Trade Truth Test:**

An edge does not reveal itself in 10-20 trades. The equity curve is noise in the early phase. Only after ~100 trades does the true expectancy manifest.

```
Trades 1-20: Could look like anything. Do not evaluate.
Trades 20-50: Starting to signal direction. Still high variance.
Trades 50-100: Pattern of expectancy becoming reliable.
Trades 100+: Statistical truth appears. Now you know.
```

**The Dropout Trap:** Traders quit at trade 15 when the curve is going sideways or slightly down. They may be walking away from a perfectly valid +$400/trade expectancy system that simply hasn't manifested through the noise yet.

**The Variance Rule:** Set a minimum sample (100 trades) before declaring a system valid or invalid. Paper trade the full 100 if needed.

**Richard Dennis standard:** Grew $400 to $200M averaging ~100%/year by accepting 50% drawdowns. The willingness to hold through variance was the edge. Most people cannot stomach it — that tolerance is tradeable in itself.

---

## THE 4-STEP PERMUTATION VALIDATION PROTOCOL

**Rule:** No new STIS strategy goes live with real capital without passing all 4 steps.

### Step 1 — IN-SAMPLE OPTIMIZATION
**What it is:** Optimize strategy parameters on historical data (e.g., backtest a Donchian breakout on SPY 2020-2024)
**Goal:** Find parameters that maximize objective function (Sharpe, profit factor, etc.)
**Warning:** This step alone proves nothing. ANY parameters optimized on the same data they are tested on will look good.

### Step 2 — MONTE CARLO PERMUTATION TEST (The Null Hypothesis Destroyer)
**What it is:** Take the same historical price data → randomly permute (scramble) the bar sequence → re-run the same optimization on the permuted data
**Purpose:** Scrambled data destroys any real market structure. If strategy still performs well on scrambled data, the edge is an artifact of curve-fitting — not a real market effect.
**Protocol:**
```
1. Optimize strategy on real data → record objective function score (e.g., Sharpe 1.8)
2. Generate 200+ permutations of the same price data
3. Optimize strategy on each permutation → record each score
4. Count: how often does the permutation score exceed the real data score?
5. If <5% of permutations beat real data → REAL EDGE EXISTS (95% confidence)
6. If >5% of permutations beat real data → CURVE-FIT ARTIFACT → redesign
```

**The Conceptual Test:** If your strategy relies on a property the permutation algorithm destroys (trend, momentum, mean-reversion), and it still outperforms 200 scrambled versions — that is genuine signal.

### Step 3 — WALK-FORWARD TEST
**What it is:** Split data into rolling in-sample / out-of-sample windows. Optimize on in-sample. Test on out-of-sample. Roll forward.
**Purpose:** Confirms edge holds on data the strategy was not optimized on.
**Protocol:**
```
Example: 4 years of data
Window 1: Optimize on Year 1-2 → test on Year 3
Window 2: Optimize on Year 1-3 → test on Year 4
Window 3: Optimize on Year 2-4 → test on Year 5 (or current live data)
```
**Threshold:** Out-of-sample performance should be within 50-70% of in-sample performance. If it collapses to near-zero, the strategy is overfit.

### Step 4 — WALK-FORWARD MONTE CARLO PERMUTATION TEST
**What it is:** Combine Steps 2 and 3. Run permutation test on each walk-forward window.
**Purpose:** The gold standard. Confirms the strategy holds up under both: (a) out-of-sample time and (b) random data null hypothesis testing simultaneously.
**Threshold:** Strategy must pass permutation test in each walk-forward window, not just the aggregate.

---

## THE FULL STRATEGY DEPLOYMENT LADDER

Before any new STIS setup goes live with real capital:

```
[ ] Step 1: Build hypothesis (Pine Script or Python)
[ ] Step 2: MTP backtest — minimum 2 years data, 7 markets tested
[ ] Step 3: Pass Monte Carlo permutation test (200+ iterations, <5% null)
[ ] Step 4: Pass walk-forward test (3+ windows, <50% degradation)
[ ] Step 5: Pass walk-forward Monte Carlo (gold standard)
[ ] Step 6: Paper trade 30 days — does live behavior match backtest?
[ ] Step 7: Deploy at micro-size (0.25% account risk per trade)
[ ] Step 8: After 30 consecutive trades within backtest parameters → scale to standard size
[ ] Step 9: Ongoing permutation test every 6 months to confirm edge persists
```

**Never skip steps.** Each step has a specific failure mode it catches. Skipping any step means a specific failure mode remains uncaught.

---

## THE MTP BACKTESTING TOOL (STIS Standard)

**Identified from playlist:** "New MTP Backtesting Tool Is Cooking" + "MTP Backtesting Software Tutorial"

**MTP capabilities:**
- Multi-asset: 7 markets, data back to 1965
- 200 trial Monte Carlo simulation suite
- Anti-overfitting protocol: takes median of top 20 (not the best) trial results
- Drawdown projection (Monte Carlo distribution of outcomes)

**The Median-of-Top-20 Rule:** Standard backtesting takes the best parameters. MTP takes the MEDIAN of the top 20 parameter sets. This prevents the single-scenario cherry-pick that makes backtests look better than they are.

**Drawdown projection:** Monte Carlo provides a distribution of possible outcomes. You don't just see "average drawdown = 15%" — you see "95th percentile drawdown = 30%." Design for the 95th percentile, not the average.

---

## SYSTEM DESIGN ANTI-PATTERNS (What Kills Expectancy)

| Anti-Pattern | Why it Kills Edge |
|-------------|------------------|
| Optimizing win rate at expense of R-multiple | Negative expectancy despite "feeling like you win more" |
| Testing on same data used to optimize | 100% data mining bias — edge is illusion |
| Not including spread/slippage in cost | Real expectancy always lower than paper |
| Quitting before 100-trade sample | Walking away from real edge during noise phase |
| Day trading without automation | Competing against Renaissance-tier algorithms with 20+ years of advantage |
| Adding complexity without permutation testing | Complexity + no validation = curve-fit labyrinth |
| Sizing based on conviction not math | Kelly formula exists for a reason |

**Day Trading Verdict (from Full Trading Education):**
- Brokers' 7-year data: essentially everyone loses money day trading
- Why: commissions compound against you; competing against Renaissance Technologies algorithms (20+ years old) plus newer neural network systems
- "Even if you win day trading, you created a job where you're sitting at a screen, stressed out, missing life." — STIS Lesson
- The correct alternative: systematic position trading + the Wheel = no time spent, compounding works

---

## EXPECTANCY + REGIME INTEGRATION

Expectancy is not static across regime. The same system has different expectancy in trending vs. mean-reverting regimes.

**Protocol:**
```
For each strategy: segment backtest results by regime (IEC: Trending / Mean-Rev / Transitional)
→ Calculate expectancy in each regime separately
→ Only deploy strategy in the regime where its expectancy is positive
→ Turn strategy OFF in other regimes
```

This is why the IEC Spine is foundational. Not just for trade bias — but for turning strategies on and off.

**Example application:**
- Wheel Strategy: highest expectancy in Mean-Reverting + high-IV regime
- ATH Breakout: highest expectancy in Trending + expanding GEX regime
- Neither works optimally in Transitional regime → reduce/pause all strategies

---

## PORTFOLIO EXPECTANCY (Not Just Trade Expectancy)

**The Quant Portfolio Layer:**

Individual trade expectancy is not enough. Portfolio expectancy accounts for:
1. **Correlation between strategies** — if 3 strategies all fail together (correlated), the combined drawdown is brutal
2. **Strategy capacity** — some edges exist only at small size
3. **Volatility drag** — geometric compounding punishes volatile equity curves

**Volatility Drag Formula:**
```
Geometric Mean ≈ Arithmetic Mean − (Variance ÷ 2)
A system with 20% avg return + 30% volatility:
Geometric return ≈ 20% − (0.09 ÷ 2) = 15.5%
A system with 20% avg return + 10% volatility:
Geometric return ≈ 20% − (0.01 ÷ 2) = 19.5%
→ SAME average return, very different actual wealth accumulation
```

**Implication:** A smooth, slightly lower return beats a higher, volatile return in actual account growth. The STIS stack is designed to have uncorrelated layers for exactly this reason.

**STIS Layer Correlation Design:**
- Wheel Strategy (income) ← uncorrelated to → ATH Breakout (momentum)
- Crypto Edge Pro ← partially correlated to → broad crypto macro layer
- MTP backtest layers ← tested for correlation before combining

**The target:** Portfolio Sharpe > 1.5. Individual strategies can be Sharpe 0.8-1.0. Combined + uncorrelated → portfolio Sharpe lifts.

---

**Deploy with:** `dse_framework_stis-multidimensional-trade-decision_v1.md` | `dse_framework_stis-capital-compounding-architecture_v1.md`
**Parent framework:** `dse_framework_stis-master-system_v1.md`
