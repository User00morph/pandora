# SKILL — DAILY RISK BUDGET
**Sovereign Capital Allocation and Daily Risk Tracking**
**Load when:** At the start of every session and after every trade.
**Department:** D.S.E trading workspace | STIS Risk Management | Capital allocation

---

## WHAT THIS IS

The daily risk budget defines the maximum loss allowable in one session. Exceeding it is not permitted regardless of how good the next setup looks. The budget is set before the session opens — not in the heat of trading.

---

## THE BUDGET HIERARCHY

```
WEEKLY BUDGET:    2% of total account equity
  → Set every Sunday during weekly prep

DAILY BUDGET:     Weekly budget ÷ 5
  → Calculated from the weekly budget automatically

SINGLE TRADE MAX: 50% of daily budget
  → No single trade risks more than half the day's allowance

EXAMPLE:
  Account: $50,000
  Weekly budget: $50,000 × 2% = $1,000
  Daily budget:  $1,000 ÷ 5 = $200
  Single trade:  $200 × 50% = $100 maximum risk
```

---

## THE LOSS DAY PROTOCOL

```
IF DAILY BUDGET IS 50% CONSUMED (one losing trade):
  → Reduce to half size on all remaining trades today
  → Extra patience required: only A++ setups from here

IF DAILY BUDGET IS 100% CONSUMED:
  → STOP TRADING for the day
  → Close the platform
  → Do not try to recover losses today

IF WEEKLY BUDGET IS 100% CONSUMED (mid-week):
  → STOP TRADING for the rest of the week
  → Run the weekly review early to understand what happened
  → Do not trade again until Sunday prep is complete
```

---

## THE WIN DAY PROTOCOL

```
IF UP 3× DAILY BUDGET IN ONE SESSION:
  → Optional: stop trading for the day (protect the win)
  → If continuing: only A++ setups, standard size

IF UP 5× DAILY BUDGET IN ONE SESSION:
  → STOP TRADING for the day
  → Exceptional day — protect it
  → The market will create another opportunity tomorrow
```

---

## THE POSITION SIZE CALCULATION

```
STEP 1: What is today's maximum dollar risk?
  Daily budget remaining: $[X]
  This trade's risk fraction: 50% (max) or 25% (conservative)
  Dollar risk for this trade: $[X × fraction]

STEP 2: What is the stop distance?
  Entry price: [X.XXXX]
  Stop price: [X.XXXX]
  Stop distance in pips: [N] pips
  Dollar per pip (instrument): $[X]
  Dollar risk per contract: N pips × $[X/pip]

STEP 3: Maximum contracts:
  Max contracts = Dollar risk ÷ Dollar risk per contract
  Round DOWN (never up) to the nearest whole contract

EXAMPLE:
  Dollar risk: $100
  Stop distance: 20 pips
  Dollar per pip (EUR/USD mini): $1.00
  Dollar risk per contract: 20 × $1 = $20
  Max contracts: $100 ÷ $20 = 5 contracts
```

---

## THE TWO-LAYER RISK ARCHITECTURE

The STIS operates TWO distinct position types with completely different risk postures:

```
LAYER A — INTRADAY TRADING (active management)
  Daily budget:       2% weekly / 5 = the framework above
  Monitoring:         Active — check every kill zone
  Stop management:    Follow position management protocol
  Holding period:     Minutes to hours

LAYER B — SYSTEMATIC TREND POSITIONS (passive management)
  Risk allocation:    Separate "systematic account" (not the intraday budget)
  Monitoring:         Weekly check only (or when systematic alert fires)
  Stop management:    Advance only on new structural highs (automated)
  Holding period:     Weeks to months
  Psychological rule: "Don't look for 365 days" — the tail events come to you
```

**The daily risk budget applies to LAYER A only.** Layer B positions are sized and managed separately, governed by the pyramiding protocol and the paper trading gateway criteria.

Never mix the two layers in the same mental account. They require different psychological postures and different management protocols.

---

## DAILY RISK TRACKER

```
DATE: [YYYY-MM-DD]
Account equity: $[X]
Daily budget:   $[X]
─────────────────────────────────
Trade 1: [instrument] | Risk: $[X] | Result: +/-$[X] | Budget remaining: $[X]
Trade 2: [instrument] | Risk: $[X] | Result: +/-$[X] | Budget remaining: $[X]
─────────────────────────────────
Day total: +/-$[X] | Day result: [PROFIT/LOSS/FLAT]
```

*D.S.E/trading/skills | STIS Risk Management | Daily Capital Allocation*
