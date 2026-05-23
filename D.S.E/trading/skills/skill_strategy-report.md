# SKILL — STRATEGY PERFORMANCE REPORT
**Load when: reviewing backtest results, evaluating a Pine Script strategy, or auditing edge quality before live deployment.**
**Department: D.S.E trading workspace.**

---

## PROTOCOL

### STEP 1 — GATHER DATA
```
data_get_strategy_results()     — overall metrics (net profit, win rate, profit factor, etc.)
data_get_trades(max=20)         — individual trade list
data_get_equity()               — equity curve data points
chart_get_state()               — symbol, timeframe, active studies
symbol_info(symbol)             — metadata for context
```

### STEP 2 — CAPTURE VISUALS
```
capture_screenshot(region="chart")              — chart with strategy overlay
capture_screenshot(region="strategy_tester")    — Strategy Tester panel
```

### STEP 3 — ANALYZE

**Profitability metrics:**
```
Net Profit and % return
Total Trades and Win Rate
Profit Factor (target > 1.5 — below 1.2 = fundamental edge problem)
Average Trade ($ and %)
```

**Risk metrics:**
```
Max Drawdown ($ and %)
Max Consecutive Losses
Worst single trade
```

**Reward architecture:**
```
Average Winner vs Average Loser (reward:risk ratio)
Long vs Short performance breakdown
Time in market
```

**Equity curve assessment:**
```
Smooth and upward-sloping? Or jagged and inconsistent?
Extended drawdown periods? How long, how deep?
Front-loaded or back-loaded? (recent performance ≠ historical edge)
```

### STEP 4 — STIS EDGE AUDIT

Cross-reference the strategy logic against the STIS frameworks:

| STIS Layer | Audit Question |
|-----------|----------------|
| IMA / IEC | Does the strategy enter during Phase 3 (Expansion), not Phase 2 (Trap)? |
| Session cascade | Are entries aligned with London or NY delivery windows? |
| Liquidity | Does the strategy avoid entering ON the sweep? Does it wait for rejection? |
| CF-51 | How many of the 5 gates does the strategy mechanically encode? |
| Saaja | Does the strategy filter by COT? Does it avoid trading into extreme collective belief? |

### STEP 5 — GENERATE REPORT

```
## STRATEGY REPORT: [Name]
**Symbol:** [symbol] | **Timeframe:** [tf] | **Period:** [date range]

### Summary
[2-sentence performance overview]

### Key Metrics
| Metric             | Value |
|--------------------|-------|
| Net Profit         |       |
| Win Rate           |       |
| Profit Factor      |       |
| Max Drawdown       |       |
| Avg Trade          |       |
| Reward:Risk        |       |

### STIS Edge Assessment
[Which layers are mechanically encoded? Which are absent?]

### Strengths
- [bullet points]

### Weaknesses
- [bullet points]

### Recommendations
- [specific, actionable improvements tied to STIS gaps]
```

### DIAGNOSTIC RULES

| Condition | Diagnosis | Recommendation |
|-----------|-----------|---------------|
| Win rate < 50%, profit factor > 1.5 | Good edge, poor entry precision | Tighten entry timing to CF-51 gate 5 |
| Max drawdown > 20% | Position sizing or stop architecture problem | Reduce size, widen stop to order block |
| Profit factor < 1.2 | Weak or absent edge | Strategy needs fundamental rebuild against STIS framework |
| Few total trades | Overfitted or over-filtered | Widen lookback or loosen entry criteria |
| Front-loaded equity | Historical edge not present in recent market structure | Re-evaluate which IEC phase the strategy is targeting |

---

*SKILL_STRATEGY_REPORT | D.S.E trading | Pandora OS*
