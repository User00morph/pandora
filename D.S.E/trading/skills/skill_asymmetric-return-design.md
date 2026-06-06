# SKILL — ASYMMETRIC RETURN DESIGN
**No Take Profit + Stop Loss = Unbounded Upside + Defined Downside**
**Load when:** Designing any systematic strategy or reviewing exit architecture.
**Department:** D.S.E trading workspace | STIS System Design

---

## WHAT THIS IS

The structural reason systematic long-biased trading outperforms discretionary trading over time: unlimited upside combined with strictly defined downside. Capping profits is the primary reason most traders underperform their own systems.

---

## THE MATH

```
Maximum loss per trade:    1× stop distance (defined, finite)
Maximum gain per trade:    UNLIMITED (no take profit)

A trade with a stop at -$4,000 and no take profit:
  If it loses:     -$4,000
  If it wins:      +$4,000 / +$40,000 / +$400,000 — no ceiling
```

The Silver example from Travis Woo:
- Initial stop: $4,000 (12% from entry at $34)
- Price reached $109 (21 months later)
- Profit: $75,000 on a $4,000 risk
- Risk:Reward achieved: 18.75:1

A system with a 45% win rate and 18:1 R:R on winners produces massive positive expectancy even while losing more than half its trades.

---

## WHY TAKE PROFITS DESTROY SYSTEMS

| With take profit | Without take profit |
|---|---|
| Caps winners at 2-3R | Winners can run to 20R, 50R, 100R |
| Requires being right about target | Requires only knowing when to stop |
| Optimizes for win rate | Optimizes for expectancy |
| Misses the compounders | Captures the compounders |

"Why would you ever want to sell? You only want to sell for protection."

---

## THE EUPHORIA EXCEPTION

The ONLY condition that justifies a discretionary partial exit:
1. Price has moved 10-20× the initial stop distance
2. The asset is making historic new highs (all-time high territory)
3. Mass public awareness (everyone talking about it)
4. Parabolic price action — vertical move

Historical examples: NASDAQ 1999, Nikkei 1989, Bitcoin 2020-21, Silver Hunt Brothers 1970s.

**Even then: partial exit only. Not full close. The trend may continue.**

---

## THE REVERSE PARETO DISTRIBUTION

The asymmetric design produces a specific performance shape: **lose most of the time, make all the money in rare tail events.**

From the 27-bot crypto portfolio:
- Most days, weeks, months = small losses or flat
- Occasional days = massive gains (e.g., $60k in a single day)
- The annual result: strongly positive

This is the opposite of what people expect. Most people want to "win consistently." The asymmetric design deliberately accepts consistent small losses in exchange for occasional enormous wins. The math is on this side — you only lose 1× your stop, but you can win 20× it.

**The psychological prescription:** "The best thing you can do is not look at it for 365 days." Active monitoring of a tail-event system creates anxiety that leads to premature exits — exactly when the position is about to produce its biggest win.

---

## THE STRUCTURAL DESIGN

```
ENTRY SIGNAL:    System-defined (new N-day high or structural breakout)
STOP LOSS:       ATR-based, advances only on new structural highs
TAKE PROFIT:     NONE (except euphoria override above)
EXIT SIGNAL:     Stop loss hit only
```

---

## THE LEVERAGE AMPLIFICATION

The asymmetric design becomes more powerful with leverage because:
- The unlimited upside scales with leverage
- The maximum downside is still capped at the stop loss × contracts

At 2× leverage: the potential 20:1 winner becomes a 40:1 winner. The loss on any single trade only doubles (still defined and finite). This is why the no-take-profit principle and leverage calibration must be designed together — see `skill_leverage-calibration-dial.md` for the full tradeoff.

---

## RULES

- Default position: no take profit on any systematic trade
- The stop loss is the only risk management tool needed
- Cutting winners early is the primary cause of underperformance vs. the system's backtest
- The asymmetric design only works at scale — it requires holding through drawdowns that feel catastrophic on a daily basis

*D.S.E/trading/skills | STIS System Design | Source: Travis Woo Full Trading Education video + MTP Backtesting video*
