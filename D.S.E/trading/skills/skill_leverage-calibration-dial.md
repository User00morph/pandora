# SKILL — LEVERAGE CALIBRATION DIAL
**The Explicit Tradeoff Between Leverage, Returns, and Drawdown**
**Load when:** Setting position sizing for any systematic strategy, reviewing leverage levels.
**Department:** D.S.E trading workspace | STIS Position Sizing | Leverage management

---

## WHAT THIS IS

Leverage is not a risk — it is a dial with a known, calibratable tradeoff. Every increment of leverage produces a corresponding increment of both returns AND drawdown. This relationship is explicit and predictable. The skill is knowing where your dial belongs.

---

## THE TRADEOFF FORMULA

```
APPROXIMATE RELATIONSHIP (for trend-following systems):
  Doubling leverage → doubles average winning year returns
  Doubling leverage → doubles max drawdown

Example from backtest:
  100% equity → avg winning year: 47% | max drawdown: 47%
  200% equity → avg winning year: 100% | max drawdown: 76%
  (Note: not exactly double at high leverage due to path dependency)
```

---

## THE CALIBRATION PROCESS

```
STEP 1: Identify your psychological max drawdown tolerance
  Ask: "At what drawdown level would I abandon this system?"
  Be honest. Most people say 30% but feel sick at 15%.
  Test: imagine your $100k account at $70k — how do you feel?
  If sick → your real tolerance is probably 15-20%, not 30%.

STEP 2: Find the leverage level where max drawdown = your tolerance
  Run the backtest at multiple leverage levels
  Find the level where max drawdown ≈ your honest answer from Step 1
  That is your leverage setting

STEP 3: Verify the expected return at that leverage level
  Is the average winning year still meaningful?
  At your chosen leverage: is the expected Kalmar ratio acceptable?
  If not → reconsider whether this system is worth trading at your risk tolerance

STEP 4: Lock it in
  This is now a fixed parameter — not adjusted based on current market conditions
  Never increase leverage because the system is "on a hot streak"
  Never decrease leverage because the system is "in a drawdown" (that's the worst time)
```

---

## THE PSYCHOLOGICAL TOLERANCE TEST

Before going live, run a simulation:
- Take the backtest's worst historical drawdown at your chosen leverage
- Open your brokerage account and imagine that dollar amount gone
- Hold that image for 60 seconds
- If you can do that without your gut clenching → proceed
- If you can't → reduce leverage until you can

---

## THE "JUICE THE RETURNS" PRINCIPLE

If current returns feel too low → increase leverage ONE increment at a time.
If current drawdowns feel too severe → decrease leverage ONE increment at a time.

Never make large leverage changes. The account compounds — a small leverage change has large long-run effects.

---

## RULES

- Leverage is set during calm periods — never adjusted during drawdowns or hot streaks
- The max drawdown you can handle psychologically is the binding constraint — not the mathematical maximum
- Doubling leverage does NOT double risk if the system is fundamentally robust — it doubles the amplitude

*D.S.E/trading/skills | STIS Position Sizing | Source: Travis Woo MTP Backtesting video*
