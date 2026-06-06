# SKILL — EDGE DECAY MONITORING
**Detecting When a Live Strategy Is Losing Its Statistical Edge**
**Load when:** Reviewing any live strategy's rolling performance, or after 3+ consecutive losing weeks.
**Department:** D.S.E trading workspace | STIS Strategy Portfolio | Edge monitoring

---

## WHAT THIS IS

A strategy's edge can decay gradually before it completely fails. This skill identifies the early warning signals of decay — so you can pause, investigate, and adapt before a drawdown becomes catastrophic.

---

## THE FIVE DECAY SIGNALS

Run this check monthly on every live strategy:

```
SIGNAL 1 — ROLLING EXPECTANCY DECLINING
  Calculate expectancy over the last 20 trades
  Compare to expectancy over the last 50 trades
  If last-20 is < 50% of last-50 expectancy → YELLOW FLAG

SIGNAL 2 — WIN RATE BELOW HISTORICAL FLOOR
  System historical win rate: [X%] (from backtest)
  Current rolling 30-trade win rate: [X%]
  If current < historical floor - 10pp → YELLOW FLAG
  (e.g., if historical 55%, current 40% → Flag)

SIGNAL 3 — DRAWDOWN EXCEEDING EXPECTED RANGE
  System worst historical month in backtest: [X%]
  Current drawdown: [X%]
  If current drawdown > worst historical month → RED FLAG

SIGNAL 4 — MARKET REGIME MISMATCH
  Run regime-change-detection.md on the instrument
  If a regime shift is detected → determine if the strategy was designed for this regime
  If NOT designed for current regime → ORANGE FLAG (pause until regime resolves)

SIGNAL 5 — PARAMETER DRIFT
  Have the optimal parameters shifted significantly from the deployed parameters?
  Run 200-trial optimization with the last 12 months of data
  If optimal parameters have moved > 30% from deployed → investigate
```

---

## THE FLAG RESPONSE PROTOCOL

```
YELLOW FLAG (1 signal):
  → Continue at HALF SIZE
  → Increase monitoring frequency to weekly
  → Run a fresh walk-forward validation

ORANGE FLAG (2 signals or 1 RED):
  → PAUSE the strategy immediately
  → Move to paper trading only
  → Run full robustness stack check
  → Investigate whether the edge assumption is still valid

RED FLAG (2+ RED signals or fundamental change):
  → RETIRE the strategy from live deployment
  → Archive the strategy with full performance data
  → Return to paper trading gateway (start the lifecycle over)
  → Do not "hope it recovers" — the data decides
```

---

## THE EDGE ASSUMPTION CHECK

Every strategy rests on a fundamental edge assumption. When performance decays, check the assumption:

```
EXAMPLE — Turtle/MTP trend system:
  Edge assumption: "Long-run money supply expansion creates sustained
                   trends in real assets and indices"
  Check: Is M2 still expanding? Are major asset trends intact?
  If YES → edge assumption intact, decay may be temporary
  If NO → edge assumption challenged, reduce or pause

EXAMPLE — Markov state system:
  Edge assumption: "Market states exhibit persistence (stickiness)"
  Check: Is the current transition matrix showing normal stickiness values?
  If stickiness has dropped significantly → regime is more random than usual
  → Reduce Markov signal weight, wait for stickiness to return
```

---

## THE LONG BORING PERIOD DISTINCTION

Not all performance decay is edge decay. Some is **regime-induced temporary drawdown** — the system waiting for its next tail event.

```
EDGE DECAY (genuine problem):
  → Statistical metrics deteriorating across all signals
  → Edge assumption no longer valid
  → Market regime has structurally changed against the strategy
  → Action: pause, investigate, potentially retire

TAIL-EVENT WAITING PERIOD (normal, not a problem):
  → Win rate and expectancy are within historical range
  → The strategy simply hasn't had its big event yet
  → This can last 4-6 months even in a healthy system
  → Action: continue holding, do not intervene
  
FROM THE CRYPTO BOT PORTFOLIO:
  November through January = 4 months of bleeding or flat
  This was NOT edge decay
  February = accounts doubled to new highs
  Traders who exited during Nov-Jan had genuine edge decay (in their discipline)
```

**The critical diagnostic question:** Is the strategy underperforming because the edge is gone, or because the tail event hasn't arrived yet? The 5-signal decay check answers this.

---

## THE MONITORING CALENDAR

```
WEEKLY:   Check rolling 20-trade win rate and expectancy
MONTHLY:  Run the full 5-signal decay check (at monthly audit)
ANNUALLY: Re-run walk-forward validation and parameter optimization
```

*D.S.E/trading/skills | STIS Strategy Portfolio | Edge Decay Detection*
