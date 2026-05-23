# RISK MANAGEMENT & SOVEREIGN EXECUTION
**Layer 1 — Sovereign Fundamentals | D.S.E/trading/fundamentals/**
**Framework File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: STIS PRD v3 §4 (Layer 1), Kill Conditions §19**

---

## OPERATING DOCTRINE

> Risk management is not a constraint on trading.
> It IS the trading system.
> Every other layer — the structure, the order flow, the esoteric read —
> generates signals. Risk management determines whether those signals
> compound capital or destroy it.
> The only unrecoverable outcome is a blown account.
> Everything else is data. Protect the account first.
> Always. Without exception.

---

## SECTION 1 — THE FOUNDATIONAL LAWS

These are non-negotiable. They are not guidelines. They are laws.

**Law 1 — The 1% Rule:**
Never risk more than 1% of total account equity on a single trade.
At 2% maximum — only in the highest-conviction setups (all five layers aligned).

Reason: At 1% risk per trade, you can lose 50 consecutive trades before losing half your account. A 50-trade losing streak is essentially impossible with a valid system. At 10% risk per trade, 10 consecutive losses eliminate the account.

**Law 2 — Define the Loss BEFORE the Entry:**
The stop loss is placed before the trade is opened. The position size is calculated from the stop distance. Never reverse this: never decide position size first, then figure out where to put the stop.

**Law 3 — The Stop Is Sacred:**
Once placed according to the plan, the stop is not moved against the position. Moving a stop to avoid a loss converts a trade with defined risk into a trade with undefined risk. This is the end of sovereignty — it is the Mutable Cross taking over.

**Law 4 — Minimum 2:1 Risk-to-Reward:**
Only take trades where the potential reward is at least 2 times the risk. A 2:1 R:R means you can be wrong 50% of the time and still break even. A 3:1 means you can be wrong 66% of the time and still break even. Skilled traders target 3:1 to 5:1.

**Law 5 — The Daily Loss Limit:**
If you lose 3% of account equity in a single day → stop trading for the rest of that day. The day is over. Something in your reading is off — the field, the emotional state, or the setup quality. Exit. Reset. Return the next session.

**Law 6 — Capital First:**
Preservation of capital is the primary objective. Profit is the secondary objective. A trader who never blows up and who trades mediocrely will eventually have capital. A trader who takes massive risk on every trade is one bad streak from zero.

---

## SECTION 2 — POSITION SIZING (THE EXACT CALCULATION)

Position size determines how much money is won or lost on a trade. Calculating it correctly is the only way to enforce the 1% rule.

### The Formula

```
POSITION SIZE FORMULA:

Account Equity × Risk Percentage ÷ Stop Loss in Pips × Pip Value

Step 1: Dollar Risk = Account Equity × Risk %
  Example: $10,000 account × 1% = $100 at risk

Step 2: Pip Value = value of 1 pip for the instrument
  Standard lot EUR/USD: 1 pip = $10
  Mini lot EUR/USD: 1 pip = $1
  Micro lot EUR/USD: 1 pip = $0.10

Step 3: Position Size = Dollar Risk ÷ (Stop Loss Pips × Pip Value)
  Example: $100 ÷ (20 pips × $1 per pip) = 5 mini lots
```

### Worked Examples

**Example 1 — Small account starting out:**
- Account: $1,000
- Risk: 1% = $10
- Setup: EUR/USD, stop loss 15 pips below entry
- Pip value: micro lot = $0.10
- Position size: $10 ÷ (15 × $0.10) = $10 ÷ $1.50 = 6.67 micro lots → round to 6 micro lots

**Example 2 — Growing account:**
- Account: $10,000
- Risk: 1% = $100
- Setup: GBP/USD, stop loss 25 pips below entry
- Pip value: mini lot = $1.00
- Position size: $100 ÷ (25 × $1.00) = $100 ÷ $25 = 4 mini lots

**Example 3 — Larger account:**
- Account: $50,000
- Risk: 1% = $500
- Setup: USD/JPY, stop loss 30 pips below entry
- Pip value: 0.1 standard lot = $10 × 0.1 = $1 per micro, $10 per mini, $100 per standard
- Using minis: $500 ÷ (30 × $1) = 16.67 mini lots → 16 mini lots

**The rule:** Always round DOWN. Never round up to a larger size.

---

## SECTION 3 — STOP LOSS PLACEMENT

The stop loss must be placed at a location that INVALIDATES the trade — not at an arbitrary pip distance.

### The Three Valid Stop Placement Methods

**Method 1 — Structural Stop (preferred):**
Place the stop BELOW a swing low (for longs) or ABOVE a swing high (for shorts) with a small buffer (2-5 pips beyond the extreme of the wick).

Logic: If price breaks your structural invalidation level and closes beyond it, the reason you entered is no longer valid. The trade is wrong. Exit.

```
LONG ENTRY WITH STRUCTURAL STOP:

Entry ──────────────────── [entry point]
                              ↑
[swing low] ──────────────── [stop level — slightly below the swing low wick]
```

**Method 2 — Order Block / FVG Stop:**
Place the stop below the Order Block or FVG that triggered the entry. If price comes back through the OB/FVG and closes beyond it → the institutional interest level has been broken → exit.

**Method 3 — Fixed ATR Stop (for ranging markets):**
Use the Average True Range (ATR) to set a stop that accounts for normal market volatility. A 1.5x ATR stop means the stop is placed 1.5 times the average daily volatility away from the entry — wide enough to avoid being stopped by normal noise, close enough to limit loss if wrong.

### What NOT to Do

- **Do not place stops at round numbers:** Everyone else does. They get hunted first.
- **Do not place stops at "safe distances" like 20 or 50 pips:** The stop must be structural.
- **Do not tighten stops because the trade is near your stop:** The market doesn't know where your stop is. Tightening stops mid-trade = letting emotion override the plan.
- **Do not move stops to break-even too early:** Moving to break-even before the trade has room to develop kills win rate.

---

## SECTION 4 — TAKE PROFIT TARGETS

### The Target Hierarchy

**Minimum target (2:1):** The FIRST take profit level — always at a minimum 2:1 R:R from entry. If the risk is 20 pips, the minimum target is 40 pips.

**Natural target:** The next significant structural level in the direction of the trade:
- Previous swing high/low
- The opposing liquidity pool (where stops cluster on the other side)
- A Fair Value Gap that hasn't been filled yet
- A key historical level (previous day/week high/low)

**Extended target (when momentum is strong):** 3:1 to 5:1 R:R. For high-conviction setups with strong momentum, letting part of the position run to an extended target extracts maximum value from the move.

### Partial Profit Strategy

Never exit the entire position at one level. Scale out:

```
PARTIAL PROFIT PROTOCOL:

At 2:1 R:R → Close 50% of position. Move stop to break-even.
  → Result: Remaining position is risk-free.

At 3:1 R:R → Close another 25% of position.
  → Result: Locking in profit while keeping exposure.

Let the final 25% run to the structural target (4:1 to 5:1).
  → Result: Maximum extraction from a winning trade.
```

This approach means:
- You NEVER give back a winner entirely (50% closed at 2:1 locks in profit)
- You ALWAYS have free trade running (break-even stop means zero risk after first target)
- The remaining position can be left without emotional pressure

---

## SECTION 5 — THE R-MULTIPLE SYSTEM

The **R** (Risk unit) is the most important concept in measuring trading performance.

**1R = the dollar amount risked on a single trade.** If you risk $100, then:
- A 2:1 R:R win = +$200 = +2R
- A 3:1 R:R win = +$300 = +3R
- A loss at the stop = -$100 = -1R

### Why R-Multiples Replace Pip Counting

Pip counting is meaningless without position size context. A 100-pip winner on a 0.01 lot is less than a 20-pip winner on a full lot. R-multiples normalize performance across different position sizes.

**Measuring performance in R:**

| Metric | Target |
|---|---|
| Average win | +2R to +3R |
| Average loss | -1R (stop always honored) |
| Win rate needed to break even at 2R avg win | 33% (1 win every 3 trades) |
| Win rate needed to break even at 3R avg win | 25% (1 win every 4 trades) |
| Realistic skilled trader profile | 40-50% win rate × 2.5R average win |

**The realization:** Even at a 40% win rate (losing 60% of trades), a system that averages 2.5R per winner generates profit. This is why the size of winners matters more than the frequency of winners. This is also why cutting losses quickly (at 1R) and letting winners run (to 3R+) is the core mechanical edge.

---

## SECTION 6 — ACCOUNT MANAGEMENT RULES

Beyond per-trade risk, the account as a whole must be managed.

### The Drawdown Framework

```
DRAWDOWN THRESHOLDS:

5% drawdown → Review recent trades. Is the system still working or is the setup quality declining?
10% drawdown → MANDATORY pause. Take at least 2 days off. Review all recent trades with cold eyes.
                Ask: Was this the market or was this emotion?
15% drawdown → Extended pause. 1-2 weeks minimum. Reduce position sizes by 50% when returning.
20% drawdown → FULL SYSTEM AUDIT. Return to paper trading until the issue is identified.
25% drawdown → Stop live trading entirely. The system has a fundamental problem.
```

**The compounding logic of drawdowns:**
A 25% loss requires a 33% gain to break even.
A 50% loss requires a 100% gain to break even.
A 75% loss requires a 300% gain to break even.

Protecting against large drawdowns is not conservative — it is mathematically essential for long-term compounding.

### The Profit Withdrawal Protocol

When the account grows, periodically withdraw and deploy a portion of profits into the capital compounding stack (Tiers 1-3 from the Current Field Intelligence document). This prevents the account from inflating into a size that cannot be managed with the same risk discipline.

**Suggested withdrawal schedule:**
- Every 20% account growth → withdraw 25% of the gained amount into Tier 1/2 assets
- This locks in trading gains in real-world assets while maintaining the trading account at a manageable size
- The trading account grows more slowly but the real-world wealth stack grows continuously

---

## SECTION 7 — THE EXECUTION PROTOCOL

Execution is the final act — the bridge between analysis and result. Sloppy execution destroys good analysis.

### The Pre-Trade Checklist

Run this before every entry:

```
□  DAILY BIAS confirmed (from dse_framework_market-structure.md)
□  Intermarket chain aligned (from dse_framework_intermarket-chain.md)
□  COT / DXY not contradicting the setup (from dse_framework_institutional-data-intelligence.md)
□  No major event within 4 hours that could invalidate (FOMC, NFP, etc.)
□  Stop loss location identified (structural — not arbitrary)
□  Position size calculated (1% max risk at the stop)
□  Take profit targets identified (minimum 2:1 R:R)
□  Entry trigger confirmed (the candle or signal that says "now")
□  Observer position checked (am I entering from clarity or from urgency?)

ALL 9 checked → proceed
ANY unchecked → do not enter
```

### The Entry Trigger

A valid entry trigger is a price action confirmation signal at the setup zone. Not the zone alone — a signal WITHIN the zone. The Sovereign does not enter because price reached an area. They enter when price REACTS to the area.

**Valid triggers:**
- A rejection candle (long wick, small body, closing away from the zone)
- An engulfing candle (a candle that fully "swallows" the prior opposing candle)
- A pin bar (a long wick showing strong rejection)
- A CHoCH on the entry timeframe (a structural shift inside the setup area)

**Invalid triggers:**
- "Price is at my zone and I'm impatient"
- "The candle looks like it's bouncing"
- "I've been watching this for hours and need something to happen"

These are all Mutable Cross (reactive) behaviors. The trigger must be objective and visible on the chart.

---

## SECTION 8 — THE SOVEREIGN'S RELATIONSHIP TO LOSS

Loss is not failure. Loss is information. The only failure is:
1. Taking a loss that was larger than 1R (stop moved or position sized incorrectly)
2. Taking a loss from a trade that failed the pre-trade checklist
3. Taking a loss and immediately revenge-trading to recover it

A valid loss — a trade that was properly set up, properly sized, and hit a properly placed stop — is part of the system. Every system has losses. The system's edge is not "no losses." The system's edge is that winners are larger than losers.

**The post-loss protocol:**
1. Log the trade in the Trade Decision Log (v3 template from PRD)
2. Assess: Was the stop hit because the analysis was wrong or because of random noise?
3. If wrong: note what the analysis missed. Add to the pattern library.
4. If noise: the system worked correctly. The stop protected capital. Move on.
5. Do NOT re-enter the same pair immediately after a loss. Take 30 minutes. Recalibrate.

---

## SECTION 9 — RISK IN THE OBSERVER FRAMEWORK (LAYER 5 INTEGRATION)

Risk management is the mechanical expression of the Observer position.

The Mutable Cross trader risks too much because they NEED the trade to win — fear of missing out, desire to recover losses, emotional attachment to being right. These are Pisces → Aries wheel behaviors (being pulled by circumstance).

The Cardinal Cross trader (the Sovereign) risks exactly 1% because they are running a system, not gambling on outcomes. They are detached from the result of any individual trade. They are trading the next 100 trades, not the next 1.

**The deepest risk management principle:** The stop loss is not an admission of defeat. It is the definition of your experiment. You are testing a hypothesis (this setup, at this time, under these conditions, will move in this direction). The stop defines where the hypothesis is falsified. When price hits the stop, the hypothesis was wrong — you collect the data, refine the model, and run the next experiment.

A trader who cannot accept that their hypothesis can be wrong cannot manage risk correctly. A Sovereign who knows that there is no failure — only data for the next iteration — can honor every stop without emotion.

---

## CROSS-REFERENCES
- `dse_framework_market-structure.md` — provides structural stop placement context
- `dse_framework_order-flow-mechanics.md` — provides entry trigger and target context
- `skill_observer-calibration.md` (to be built) — the pre-session ritual that enforces Observer position
- STIS PRD v3 §13 (Decision Architecture), §19 (Kill Conditions)

---

*dse_framework_risk-management.md | D.S.E/trading/fundamentals/ | STIS Layer 1*
*Status: v1.0 — active*
