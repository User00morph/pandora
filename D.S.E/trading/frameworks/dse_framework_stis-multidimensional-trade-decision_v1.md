# D.S.E FRAMEWORK — STIS Multi-Dimensional Trade Decision Matrix
## Sovereign Trading Intelligence System
**Compiled:** 2026-06-11
**Source:** 23 STIS playlist videos (~109K words) + iCloud trading batch (19 files)
**Tier:** OPERATIONAL — load before any live trade session

---

## THE CORE DOCTRINE

STIS does not operate on one axis. Every trade decision is the convergence of **9 simultaneous layers**. A signal on one layer means nothing. Confluence across 3+ layers = qualified setup. Confluence across 5+ layers = high-conviction entry.

> "If you can let go of being right and let go of needing to place the trades yourself, it becomes easy to make a lot of money." — STIS Lesson 5

The matrix below is the operating protocol. Work it top to bottom before every position.

---

## LAYER ACTIVATION MATRIX (Trade-Time Decision Engine)

### DIMENSION 1 — REGIME CLASSIFICATION (IEC Spine)
**Ask:** What is the market doing right now?

| Signal | Regime | STIS Response |
|--------|--------|---------------|
| Uptrend, higher highs/lows, ATH zone | TRENDING | Full size, directional bias |
| Range-bound, choppy, price returning to mean | MEAN-REVERTING | Reduced size, fade extremes |
| Breaking range, conflicting signals | TRANSITIONAL | No position or 25% size max |

**Rule:** Regime determines bias. All subsequent layers filter within it. Never fight the regime.

---

### DIMENSION 2 — GAMMA EXPOSURE MAP (GEX Daily Structure)
**Ask:** Where are market makers forced to act?

**GEX Mechanics (from "Gamma Trading: The Edge You've Been Looking For"):**
- Market makers are the short side of ~99% of all options contracts
- MM's must delta-hedge continuously to stay balanced
- This creates PREDICTABLE buying and selling at specific price levels

| GEX Reading | Market Structure | Trade Implication |
|------------|-----------------|-------------------|
| Large POSITIVE gamma (call wall) | MM's sell rallies, buy dips → PINNED | Range trade. Resistance above. Expect rejection. |
| Large NEGATIVE gamma (put wall) | MM's sell dips AND rallies → EXPANDING | Directional move likely. Fuel exists for breakout. |
| Gamma flip (GEX = 0 level) | MM's neutral → transition point | High volatility inflection. Direction unknown but move incoming. |

**GEX Timing Rule:** Levels near expiration (10-20 DTE) create stronger reactions than far-dated levels. Same dollar level at 10 DTE hits harder than 60 DTE.

**Free tools:** Squeeze Metrics (squeezemetrics.com), Spot Gamma

**Daily GEX Protocol:**
1. Pull net gamma exposure at market open
2. Mark: largest positive gamma level (call wall = resistance)
3. Mark: largest negative gamma level (put wall = support/launcher)
4. Mark: gamma flip level (zero line)
5. Combine with Dimension 1 regime → trade bias locked

---

### DIMENSION 3 — ASSET FILTER (ATH Model + Screening)
**Ask:** Am I trading the right instrument?

**ATH Entry Model (William O'Neill doctrine):**
- Only buy assets at or breaking to new all-time highs
- Any asset capable of reaching ATH is by definition not going to zero
- Only the strongest companies, ETFs, and crypto assets print new ATHs

**ATH Filter Logic:**
```
Is the asset at or near ATH? 
→ YES: eligible. Proceed to Dimension 4.
→ NO: Is it in a confirmed uptrend with ATH within 5-10%?
   → YES: eligible (but smaller size)
   → NO: skip. There are always stronger assets.
```

**For Wheel Strategy specifically:**
- Screen on Finviz: Optionable + Shortable → Volume >2M → Price >$50 → P/E <30 → PEG <2 → Quarter Up → Month Down
- This produces fundamentally sound assets that have temporarily pulled back = ideal CSP entry
- Confirm: W-pattern on chart, old resistance as new support = 3 yeses

---

### DIMENSION 4 — ENTRY TIMING (Order Flow: Context → Location → Confirmation)
**Ask:** Is this the right moment?

**The C/L/C Framework (Volume Profile + Order Flow):**

| Step | What to Do | What to See |
|------|-----------|-------------|
| **Context** | Build the narrative at major structural levels | Daily/weekly inventory position. Are longs trapped? Shorts squeezed? Where is overnight position sitting? |
| **Location** | Identify the outlier zone | Low-volume nodes (price will run through), delta spikes, Point of Control (POC) as magnet |
| **Confirmation** | Wait for absorption + aggression | Absorption = large traders absorbing selling (price holds at level despite pressure). Aggression = volume imbalances, large block trades stepping in |

**Entry only when all 3 present.** Two out of three = wait.

**Combined with ATH model:** ATH tells you WHAT to trade. Order flow tells you WHEN. GEX tells you WHERE levels are. Regime tells you the overall direction.

---

### DIMENSION 5 — PROBABILISTIC SEQUENCING (Markov Matrix)
**Ask:** What is the statistical probability of the next state?

**Markov Logic:** Given current state (regime + GEX reading + IV percentile), what are the probable next states?

**Application in STIS:**
- Do not predict. Assign probabilities.
- "What is the probability this setup produces a winning trade given this regime + GEX configuration?"
- Size position proportional to probability weight, not conviction or emotion
- The Markov Matrix is not a chart pattern — it is historical state transition data

**Connection to Expectancy (from "The Math of Winning in Trading"):**
- Positive expectancy at sufficient frequency = guaranteed profitability over time
- The Markov Matrix gives you the probability numerator
- Expectancy formula: `(Win% × Avg Win) − (Loss% × Avg Loss)`
- 70% win rate with 1:1 RR = same expectancy as 15% win rate with 8:1 RR
- It is the COMBINATION that creates the edge, not either alone

---

### DIMENSION 6 — POSITION SIZING (Quant Portfolio Engineering)
**Ask:** How much capital should this position receive?

**Quant Portfolio Doctrine (from "How Quants Engineer Portfolios"):**

| Principle | Application |
|-----------|-------------|
| Portfolio = collection of uncorrelated strategies | Never stack correlated positions (e.g., 3 tech longs = 1 position risk-wise) |
| Each strategy layer has a Sharpe Ratio + max drawdown profile | Know the historical max drawdown before risking capital |
| Kelly Criterion or fractional Kelly | Full Kelly = optimal mathematically but psychologically unsurvivable; use 25-50% Kelly |
| Volatility drag compounds against you | A volatile 20% annual return beats a consistent 15% in theory but destroys many traders in practice |

**STIS Position Sizing Protocol:**
```
Step 1: Determine account risk per trade (default: 1-2% of total account)
Step 2: Calculate stop distance from entry (order flow structure, NOT arbitrary $)
Step 3: Size = (Account × Risk%) ÷ Stop Distance
Step 4: If Markov probability >70% for winning → can use 1.5× base size
Step 5: Daily loss limit = 2% account total → if hit, STOP. No exceptions.
```

**The Drawdown Doctrine:** Drawdown tolerance = ceiling for gains. Richard Dennis averaged 100%/year by accepting 50% drawdowns. Warren Buffett averaged 30-40% with smaller drawdowns. Choose your ceiling consciously.

---

### DIMENSION 7 — TRADE STRUCTURE (Options Architecture)
**Ask:** What is the optimal instrument and structure?

**Two STIS Options Modes:**

**Mode A — DIRECTIONAL (Trending Regime)**
- Buy calls/puts on confirmed ATH breakouts
- Long gamma: own options and delta-hedge to profit from large moves
- IV matters: enter in low IV (cheap options) before anticipated expansion

**Mode B — INCOME (Mean-Reverting Regime / Wheel)**
- Sell premium in high-IV environments
- Short gamma: sell time decay into range
- The Wheel Strategy is the core income engine (see Wheel Protocol framework)
- Covered Calls: sell out-of-the-money at resistance levels (20-30% OTM) for 1%/month
- Break-even math: paid $2.50 on $130 stock → real cost basis $127.50, not $130

**IV Regime Selection:**
```
IV Percentile < 25% → Long options (Mode A) — options are cheap
IV Percentile > 75% → Short options (Mode B) — options are expensive, mean-revert
IV Percentile 25-75% → Either mode, conviction-dependent
```

---

### DIMENSION 8 — AUTOMATION STATUS (Execution Layer)
**Ask:** Is this execution automated or manual? If manual, why?

**STIS Automation Stack:**
- **TradingView Pine Script** → custom indicators for all STIS signals (GEX levels, ATH filter, volume profile overlays)
- **Alerts → Webhooks** → remove human from the loop at execution
- **IBKR API** → automated order placement (local method)
- **QuantConnect** → production-grade automation with feedback loop (preferred for live capital)

**Current Phase 1 status:** Semi-automated (Claude Code alerts → manual execution)
**Target Phase 2:** Full webhook automation live

**No-Code AI Path (Project No Code doctrine):**
- AI reads options flow in real-time (dark pool + unusual activity)
- Database built entirely via AI prompting, zero human-written code
- Profit mechanism identification: query database for statistically significant market effects
- Weekly cost: ~$30-50 in API costs; single winning trade = months of access cost covered

---

### DIMENSION 9 — MACRO FILTER (Intelligence Layer)
**Ask:** Is this trade consistent with macro regime?

**Active Macro Checkpoints (June 2026):**
- **SpaceX IPO (June 12):** AVOID. $1.75T valuation at 56x revenue. 90-day lockup waiver = September dump window. Do not hold.
- **Quantum-resistant crypto (XRP/XDC/HBAR):** Infrastructure phase — accumulate on pullbacks
- **Tokenized RWA:** NYSE/NASDAQ/BlackRock rebuilding on blockchain rails. Long thesis confirmed.
- **Federal Reserve captured:** Kevin Warsh (crypto stakes). Clarity Act → July 4 target. Legal floor for crypto locked.
- **Stablecoin thesis:** Every dollar into stablecoin = dollar leaving fiat. US debt monetized through peg.

**ATH Macro Filter:** Apply ATH filter to sectors, not just individual assets. Only trade into the strongest macro themes making new highs.

---

## THE SINGLE-PAGE DECISION TREE (Pre-Trade Checklist)

```
BEFORE ANY POSITION — run this in order:

[ ] D1: Regime classified? Trending / Mean-Rev / Transitional
[ ] D2: GEX map loaded? Resistance / Support / Flip levels marked
[ ] D3: Asset passes ATH filter? Strong fundamentals + uptrend?
[ ] D4: Order flow confirms? Context intact → Location identified → Confirmation present?
[ ] D5: Markov probability assigned? > 55% required minimum
[ ] D6: Position sized correctly? 1-2% risk, stop from structure, not $ amount
[ ] D7: Options structure selected? Directional (low IV) vs Income (high IV)
[ ] D8: Execution method confirmed? Automated alert or manual with discipline
[ ] D9: Macro consistent? Not trading into a macro headwind

ALL 9 GREEN → QUALIFIED SETUP. Enter with confidence.
Any RED → Reduce size or wait. Never override the checklist.
```

---

## MULTI-DIMENSIONAL CONFLUENCE SCORING

Not all confluences are equal. Score before entering:

| Dimension | Score if Aligned |
|-----------|-----------------|
| D1 Regime matches trade direction | +2 |
| D2 GEX level within 0.5% of entry | +2 |
| D3 Asset at/near ATH | +2 |
| D4 All 3 order flow signals present | +3 |
| D5 Markov probability >65% | +2 |
| D6 Risk properly sized | +1 (baseline) |
| D7 IV regime matches structure | +2 |
| D8 Automation active | +1 |
| D9 Macro aligned | +1 |

**Score interpretation:**
- 0-6: Skip — insufficient confluence
- 7-10: Small position — watch for more confirmation
- 11-14: Full position — qualified high-conviction setup
- 15+: Maximum position within account limits

---

## SYSTEM HYGIENE RULES

1. **Never evaluate on a single trade.** Minimum 30-trade sample to assess edge.
2. **100-trade truth test:** Equity curve only reveals itself after 100 trades. Quitting at 10-20 is walking away from real edge.
3. **Never override the daily loss limit.** 2% daily max = the survival rule.
4. **No revenge trades.** Exit stops, log it, close the screen for the day.
5. **Never add to losing position unless pre-planned at entry.**
6. **Never mix time and money risk.** Trading should not consume hours of attention. If it is, the system is not yet automated enough.

---

**Deploy with:** `dse_framework_stis-wheel-income-protocol_v1.md` | `dse_framework_stis-expectancy-validation_v1.md` | `dse_framework_stis-capital-compounding-architecture_v1.md`
**Parent framework:** `dse_framework_stis-master-system_v1.md`
