# D.R.D DECODE — Trading: Small Cap Screening + Risk Scaling Fundamentals
**Stage 3–4 | Deconstruction → Reconstruction**
**Date:** 2026-06-11
**Sources:** 2 videos — Jun 10 (Russell 2000 small caps) + Jun 11 (risk/scaling fundamentals)
**Decoded by:** D.R.D pipeline | Extends: `drd_decode_quant-options-ai-trading-stack_v1.md`
**Routes to:** D.S.E trading operations / STIS PRD

---

## SOVEREIGN VERDICT

These two videos add two missing layers to the existing STIS + quant stack:

1. **Equity screening methodology** — how to find asymmetric small cap positions using institutional-grade fundamental filters. The existing stack is mechanics (IEC, GEX, order flow). This adds the *selection layer* — how to identify what to trade before the chart is even opened.

2. **Risk scaling doctrine** — the mathematical proof that account size is irrelevant to process. The setup is the same at $1K and $1M. Only lot size changes. This resolves the psychological scaling problem.

These are not new frameworks — they are the **pre-trade and meta-trade layers** that belong above and around the STIS mechanical spine.

---

## SECTION 1 — SMALL CAP SCREENING: THE INSTITUTIONAL METHOD

### Core Principle (ESTABLISHED — institutional floor sourced)
> "Dig where nobody else is digging."

The edge in small caps is **asymmetric attention**. Mega cap tech is over-covered, over-traded, over-priced. The Russell 2000 is under-covered. Institutional floor process: run numbers on thousands of small caps → filter by fundamental velocity → identify what the market hasn't priced in yet.

### Screening Filters (INFERRED from examples — pattern is consistent across all 5 picks)

| Filter | Threshold | Rationale |
|--------|-----------|-----------|
| EPS growth (forward) | 100%+ (ideally 200–500%) | Market tends to underprice acceleration |
| Revenue growth | 40%+ YoY | Confirms EPS isn't a one-time accounting event |
| EBITDA expansion | Directionally up | Operating leverage confirmation |
| Valuation | Low P/E relative to growth | Cheap relative to trajectory = mispriced |
| Sector | Institutional tailwind sector | AI supply chain, healthcare, fintech, energy |

### The 5 Picks (Jun 10) — As Fundamental Case Studies

| Ticker | Sector | Edge | Key Numbers |
|--------|--------|------|-------------|
| I-Core Holdings | Semiconductor supply chain (fluid/gas delivery) | AI chip demand = infrastructure demand. Plumbing inside chip machines. | EPS +500%, Rev $1.2B |
| PAR Pacific | Oil refining (Hawaii/Pacific NW) | Regional moat, EBITDA 10M→91M in one year. 4x earnings. | EBITDA +810% |
| Oscar Health | Tech-driven health insurance | Membership +56%, Rev +52%, medical costs declining while revenue grows | 3.2M members, $4.65B rev |
| Flywire | Global payments (education/healthcare/travel) | Three defensive sectors, EBITDA +81%, forward EPS +220% | Rev +41% |
| United Natural Foods | Wholesale food distribution (Whole Foods supplier) | "Boring businesses with numbers like these never stay cheap long" | EPS +262% |

### Pandora Integration — STIS Pre-Session Screening Layer
The existing STIS stack tells you *how* price moves (IEC structure, GEX levels, order flow). This adds *what* to put in the watchlist. For equities/small caps:

```
SCREENING SEQUENCE:
1. Universe filter: Russell 2000 → apply EPS/revenue/EBITDA velocity thresholds
2. Sector filter: institutional tailwind sectors only (AI supply chain, fintech, health)
3. Valuation check: P/E relative to growth trajectory
4. Chart entry: THEN apply IEC + GEX framework for timing
```

**Note:** These 5 picks are live as of Jun 10, 2026. Run current fundamentals before acting.

---

## SECTION 2 — RISK SCALING DOCTRINE

### The Core Insight (ESTABLISHED — demonstrated mathematically)
> "The only thing that changes as you scale is your lot size. The setup is identical."

Most traders psychologically break when account size grows because they attach emotional weight to dollar amounts. The doctrine: **look at the setup, not the number**. The setup doesn't know what account size it's attached to.

### The Math Model

| Account Size | Risk % | Risk $ | RR | Return $ |
|---|---|---|---|---|
| $1,000 | 10% | $100 | 1:4 | $400 |
| $10,000 | 10% | $1,000 | 1:4 | $4,000 |
| $100,000 | 10% | $10,000 | 1:4 | $40,000 |
| $1,000,000 | 10% | $100,000 | 1:4 | $400,000 |

2 trades at 1:4 on $1M = $800K return. 3 trades = $1.2M. Math is invariant.

### Operating Parameters
- **Risk per trade:** 10% (acknowledged as high risk — appropriate for high-conviction setups)
- **Reward target:** 1:3 to 1:4 minimum
- **Frequency:** 1–2 setups per week (not every day — quality over frequency)
- **Evaluation criteria:** Was it a good setup? Not: did it win?

### The Consistency Principle (ESTABLISHED)
> "People that are consistent take the same trades, the same setups, every single time."

Scaling is not a skill. Consistency is the skill. Once the setup is repeatable at small size, the only scaling variable is position size. Everything else is held constant. This is the mechanical proof that process > outcome.

### Pandora Integration — STIS Risk Management Layer
Extends the existing STIS mechanical spine with explicit risk doctrine:

```
STIS RISK PROTOCOL (encoding):
- Risk unit: 10% per qualifying setup
- Qualification threshold: IEC structure confirmed + GEX level confluence
- RR minimum: 1:3 before entry
- Frequency gate: max 1-2 setups/week — no forced trades
- Scaling rule: only lot size changes, setup criteria unchanged at any account size
- Evaluation rule: judge setup quality, not P&L outcome
```

---

## CONFIDENCE TIERS

| Claim | Tier | Basis |
|-------|------|-------|
| Institutional small cap screening methodology | ESTABLISHED | Sourced from stated H1 floor experience, consistent with known institutional process |
| 5 stock fundamentals (EPS/rev figures) | PROBABLE | Stated figures, unverified — check current data before acting |
| Risk scaling math | ESTABLISHED | Mathematical — invariant |
| 10% risk per trade | PROBABLE | Creator's personal approach — high for most frameworks, appropriate for high-conviction |
| 1–2 setups/week frequency | ESTABLISHED | Consistent with quality-over-frequency doctrine across multiple sources |

---

## DEPLOY TO

| Department | What to add |
|---|---|
| D.S.E — STIS | Small cap screening sequence as pre-session layer. Risk protocol encoding. |
| D.S.E — trading ref | 5 live picks logged with date and fundamentals for tracking |
| STIS PRD | Risk module update: 10% / 1:3-4 / 1-2x weekly |

---

*drd_decode_trading-small-caps-risk-fundamentals_v1.md | D.R.D | Pandora OS*
*"D.R.D is the front door. Nothing enters untested."*
