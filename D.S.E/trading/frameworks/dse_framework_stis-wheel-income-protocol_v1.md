# D.S.E FRAMEWORK — STIS Wheel Income Protocol
## Sovereign Trading Intelligence System — Options Income Engine
**Compiled:** 2026-06-11
**Source:** "The Wheel Options Strategy I Will Use For Life" + Gamma Trading + AI Options videos
**Tier:** OPERATIONAL — the core monthly income generation protocol

---

## THE DOCTRINE

> "For the well-educated options trader, selling premiums is our bread and butter. Stop solely trading direction. Start letting time work for you."

The Wheel is not a gamble or a speculation. It is a systematic income protocol that generates cash flow on fundamentally sound assets regardless of market direction — through time decay mechanics.

**The three-phase loop:**
1. Get paid to wait to buy at your price (CSP)
2. Get paid while you hold (Covered Calls + dividends)
3. Get paid when you sell (CC assignment at higher price)
→ Repeat. The wealth wheel cranks.

---

## PREREQUISITE: THE WHEEL MINDSET

- Never wheel a stock you would not want to own
- This is NOT a way to create job income — trading generates variable returns, not stable monthly checks
- The Wheel is designed to multiply existing capital, not replace earned income
- Operate from security: if you lose the capital in this position, you are still okay financially
- Day trading = gambling addiction loop. The Wheel = sovereignty through time + discipline

---

## STEP 1 — WHEEL STOCK SELECTION (Finviz Screen Protocol)

**Objective:** Find fundamentally sound, liquid stocks on temporary pullback

**Finviz Screening Sequence:**

| Filter | Setting | Rationale |
|--------|---------|-----------|
| Optionable + Shortable | Yes | Ensures liquid options chain |
| Average Volume | >2,000,000 | Ensures option market liquidity |
| Price | >$50 | Filters low-cap instability |
| P/E Ratio | <30 | Ensures fair price vs earnings |
| PEG Ratio | <2 (target <1.5) | Identifies growth potential at fair price |
| Performance (Quarter) | Positive | Stock is fundamentally strong |
| Performance (Month) | Negative | Stock is temporarily on sale |

**Result:** 10-15 candidates max. Then manual review.

**Manual Review Criteria:**
1. Do I understand this business and want to own it?
2. Does it pay dividends? (bonus — stacks on top of premium income)
3. Is there a technical W-pattern on the chart? (double bottom = 3 confirmed price yeses)
4. Has old resistance become new support? (breakout → retest → hold = structural confirmation)
5. Is there an upcoming catalyst I need to avoid? (earnings, FDA, Fed announcement = skip week)

**The EOG Standard (reference example):**
- Fundamental sound: natural gas company, dividend, rising energy demand thesis
- Chart pattern: double bottom at $130 → bounced twice → old ceiling became new floor
- Entry point: stock pulled back to the exact support zone → perfect CSP candidate

---

## STEP 2 — SELL THE CASH-SECURED PUT (CSP)

**Objective:** Get paid to promise to buy the stock at your price

**CSP Parameters:**

| Parameter | Target | Notes |
|-----------|--------|-------|
| Expiration | 30-45 DTE | Sweet spot for theta decay. 35 DTE = ideal. |
| Strike Price | At or below technical support | The price you would genuinely want to buy the stock |
| Premium Target | ≥1% of cash requirement | $250 premium on $13,000 cash = 1.9% — ideal |
| Bid-Ask Spread | Split the spread | If bid $2.40 / ask $2.60 → place limit at $2.50 |

**CSP Math Protocol:**
```
Cash Requirement = Strike Price × 100 (per contract)
Premium Collected = (Bid + Ask) ÷ 2 × 100
Premium % = Premium Collected ÷ Cash Requirement × 100
Target: ≥1.0% — if below 0.5%, skip and find better stock
```

**Break-even Calculation:**
```
Real Break-Even = Strike Price − Premium per Share
Example: $130 strike − $2.50 premium = $127.50 actual break-even
You already own it cheaper than anyone who just bought the stock
```

**The Two Outcomes (both are fine):**

| Outcome | What Happens | Response |
|---------|-------------|----------|
| Stock stays above strike (≥66% probability) | Keep premium. CSP expires worthless. | Run Step 2 again next month |
| Stock falls below strike (≤34% probability) | Get assigned 100 shares at strike price | Move to Step 3 — this is a good outcome |

**Probability Check (using Thinkorswim or any broker):**
- Move price slice to break-even → confirms probability of staying profitable
- Move price slice to strike → confirms probability of assignment
- 66% premium keep / 34% assignment = typical target ratio at 30-35 DTE
- If probability of assignment >50% → strike is too deep in-the-money, move it out

---

## STEP 3 — SELL THE COVERED CALL (CC)

**Objective:** Generate income on owned stock while holding; get paid on the way out

**When to enter Step 3:** Upon assignment from CSP. Now own 100 shares at strike price.

**CC Parameters:**

| Parameter | Target | Notes |
|-----------|--------|-------|
| Expiration | 30-45 DTE (same cycle) | Same theta sweet spot |
| Strike Price | Above resistance zone | Where stock is statistically unlikely to go |
| Premium Target | ≥0.5-1% of stock price | Aiming for consistent 10% annualized added yield |
| Select strike | 15-20% probability of assignment | OTM means you keep premium most months |

**CC Math Protocol:**
```
Stock cost basis: $130 (assigned from CSP)
CC premium: $1.25 on $130 stock = 0.96% for the month
Annualized: ~10% additional yield on top of stock appreciation + dividends
Maximum gain if called away: ($150 − $130) + $1.25 = $21.25/share = $2,125/contract
```

**The Two Outcomes (both are fine):**

| Outcome | What Happens | Response |
|---------|-------------|----------|
| Stock stays below CC strike (≥80% probability) | Keep premium. CC expires worthless. | Write another CC next month |
| Stock rises above CC strike (≤20% probability) | Stock called away at strike | Keep premium + capital gains from assignment price to CC strike. Go back to Step 1. |

**If Called Away:**
- You made: (CC strike − CSP strike) + CC premium + CSP premium + any dividends
- This is a winning outcome
- Simply restart the wheel from Step 1 — find next stock, repeat

---

## THE COMPOUNDING MATH (Why This Works)

**Consistent execution at 1%/month on owned positions:**
```
10 CC cycles/year (not all 12 are possible) × ~1% each = ~10% additional yield
+ Dividend income (if applicable) = +2-4%
+ Capital appreciation on the underlying = variable
Total: baseline 10-15% yield floor on owned positions, before appreciation
```

**The Wheel Compounding Effect:**
- January: $13,000 cash → CSP → collect $250 (1.9%)
- Month 2 (if assigned): $13,000 tied up in stock → CC → collect $125 (0.96%)
- Month 3: stock called away at $150 → capital gain $2,000 + premiums → repeat with $15,375+
- Every cycle: lower cost basis, higher actual yield

---

## SECRET SAUCE — PROTECTION LAYER (Managing Assignment Risk)

**What if the stock keeps dropping after assignment?**

**Step 1:** Remember — you ran the screen for a fundamentally sound stock. The business is real.

**Step 2:** Continue selling covered calls at or below your cost basis to lower it further.

**Step 3:** Calculate "managed" cost basis after all premium collected.
```
Assigned at $130
Collected $2.50 CSP premium → real basis $127.50
Collected $1.25 CC month 1 → real basis $126.25
Collected $1.25 CC month 2 → real basis $125.00
Two months of CCs at 0.96%/month → still own a stock worth perhaps $120 but basis is $125
Gap shrinks with every cycle
```

**Step 4:** If stock fundamentally deteriorates (earnings collapse, sector disruption) → exit at small loss. The premium collected over months softens the blow.

**The Core Protection:** You selected a stock you would genuinely be comfortable owning long-term. Assignment is not a disaster — it is the designed alternative outcome.

---

## WHEEL + GEX INTEGRATION (STIS Enhancement)

**Standard Wheel:** Select CSP strike at technical support
**STIS Wheel Enhancement:** Select CSP strike at largest GEX put wall

| Why | Mechanics |
|-----|-----------|
| Put wall = large negative gamma concentration | MM must buy shares to hedge when price approaches → creates real buying support |
| GEX levels near expiration react most strongly | 30 DTE CSP aligns with 10-20 DTE GEX reaction window |
| Confirms technical support with structural support | Double confirmation = higher probability of holding |

**Protocol:**
1. Run Finviz screen → identify candidate
2. Check GEX chart on candidate → find largest put wall below current price
3. Set CSP strike AT the put wall level (or 1 strike above)
4. The market maker's hedging forces become your support buffer

---

## ACCOUNT REQUIREMENTS

| Strategy | Minimum Capital | Account Type |
|----------|----------------|-------------|
| 1 CSP contract on $50 stock | $5,000 (cash-secured) | Cash or IRA |
| 1 CSP contract on $130 stock | $13,000 (cash-secured) | Cash or IRA |
| Margin account | 50% of above | Margin account |
| Diversified Wheel (3-4 positions) | $30,000-$50,000 | Recommended minimum |

**STIS Phase 1 protocol:** Start with 1 position. Prove the system over 10+ cycles. Scale only after consistent execution demonstrated.

---

## THE WHEEL TRADE LOG (Hygiene)

For every Wheel cycle, log:

| Field | Track |
|-------|-------|
| Stock | Ticker + entry date |
| CSP strike + expiration | Exact contract |
| Premium collected | Dollar amount + % of cash req |
| Outcome (premium kept or assigned) | Result |
| If assigned: CC strike + expiration | Next contract |
| CC premium collected | Dollar amount + % |
| Total yield for cycle | All premiums ÷ initial cash |
| Cumulative cost basis | Lowering with each cycle |

**Minimum sample for assessment:** 10 full Wheel cycles before evaluating strategy performance.

---

**Deploy with:** `dse_framework_stis-multidimensional-trade-decision_v1.md`
**Parent framework:** `dse_framework_stis-master-system_v1.md`
