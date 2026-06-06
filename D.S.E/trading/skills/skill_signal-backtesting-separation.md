# SKILL — SIGNAL-BACKTESTING TOOL SEPARATION
**Using the Right Tool for Each Job in the Trading Stack**
**Load when:** Building or reviewing the STIS technology infrastructure.
**Department:** D.I.I + D.S.E | STIS Infrastructure | Tool architecture

---

## WHAT THIS IS

TradingView and a portfolio backtesting engine (MTP, Python, etc.) serve different purposes. Conflating them — using TradingView for backtesting or expecting the backtester to generate live signals — is a category error that produces inferior results from both tools.

---

## THE SEPARATION PRINCIPLE

```
TRADINGVIEW:
  Primary function:     Real-time signal generation
  Secondary function:   Visual chart analysis
  Tertiary function:    Alert delivery (webhooks, email, app notifications)
  Backtest capability:  Single-asset only, limited parameter optimization
  NOT for:             Portfolio-level backtesting, multi-asset optimization

PORTFOLIO BACKTESTER (MTP / Python / custom):
  Primary function:     Multi-asset backtesting
  Secondary function:   Parameter optimization (200-300 trials)
  Tertiary function:    Walk-forward validation
  NOT for:             Live signal generation, chart visualization, alerts
```

---

## THE WORKFLOW

```
DESIGN PHASE:
  1. Portfolio backtester → Find robust parameters
  2. Portfolio backtester → Validate (walk-forward, multi-asset, median params)
  3. Portfolio backtester → Set performance expectations

SIGNAL PHASE:
  4. TradingView → Load the validated parameters into the indicator
  5. TradingView → Monitor live charts for signals
  6. TradingView → Set alerts for signal triggers

EXECUTION PHASE:
  7. Brokerage platform → Execute the trades when alert fires
  8. Trade log → Record every execution

REVIEW PHASE:
  9. Portfolio backtester → Re-run quarterly with updated data
  10. Compare live performance to backtested distribution
```

---

## WHY THE SEPARATION MATTERS

TradingView single-asset backtest limitations:
- Cannot test whether parameters generalize across multiple assets simultaneously
- Cannot run 200+ trials efficiently
- Cannot produce portfolio-level equity curves
- Cannot run walk-forward optimization

Portfolio backtester limitations:
- Cannot show signals on live charts
- Cannot send real-time alerts
- Cannot integrate with brokerage execution systems

Each tool does ONE thing extremely well. Force either tool to do the other's job → mediocre results from both.

---

## THE STIS TOOL STACK

| Layer | Tool | Function |
|---|---|---|
| Backtesting | MTP / Python custom | Multi-asset optimization and validation |
| Signal generation | TradingView | Live chart signals and alerts |
| GEX data | gex_engine.py | Options chain data and level generation |
| Execution | MT5 / Broker platform | Order placement and management |
| Logging | Pandora trade log | Session records and performance tracking |

---

## RULES

- Never use TradingView backtesting results as the primary validation for a system
- Never try to replicate portfolio-level analysis in TradingView — use the right tool
- The indicator on TradingView and the backtesting engine must use identical parameter values — sync them after every optimization run

*D.I.I + D.S.E | STIS Infrastructure | Source: Travis Woo MTP Backtesting video*
