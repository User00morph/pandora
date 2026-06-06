# SKILL — TRADINGVIEW FREE STACK
**Replicating $270/Month Paid Features for Free via Pine Script**
**Load when:** Setting up or upgrading the TradingView environment.
**Department:** D.I.I + D.S.E | STIS Infrastructure | Chart platform

---

## WHAT THIS IS

TradingView's free plan limits you to 2 indicator slots. Pine Script removes that limit entirely — package unlimited indicator logic into one slot. Every paid feature is a function. Functions live inside one file.

---

## THE TEN REPLICABLE FEATURES

| Paid Feature | Pine Script Equivalent | Value |
|---|---|---|
| Multiple indicators | Package all into one script | $270/mo feature unlocked |
| Multi-chart layout | Multi-timeframe dashboard table | 4-chart view on 1 chart |
| Premium screener | Pine Script screener module | Multi-asset condition scan |
| Anchored VWAP | Calculate from user-defined moment | Event-relative price context |
| Volume Profile / POC | Horizontal volume histogram | Highest-traded price levels |
| Higher timeframe levels | HTF data overlaid on LTF | HTF context without switching |
| Auto key levels | Script calculates daily/weekly OHLC | Never redraw levels manually |
| Session kill zones | Shaded boxes by session hours | Visual timing + kill zone overlay |
| Smart alerts | One alert, all conditions | Unlimited effective alerts |
| Multi-symbol screener | Scan multiple assets | Premium screener equivalent |

---

## THE BUILD PROCESS

```
1. Paste the one-shot prompt into Claude Code terminal
2. Answer the onboarding questions:
   - Which features to include (modular selection)
   - Asset preferences
   - Color scheme
   - Moving average periods
   - Session timing (UTC offset)
3. Claude generates the Pine Script
4. Claude installs it directly via TradingView MCP
5. One alert set up to cover all conditions
6. Done — full stack in < 5 minutes
```

---

## THE MAINTENANCE MODEL

Once installed: zero maintenance. The script auto-updates key levels. The alert auto-fires on conditions. When adding a feature, tell Claude in natural language → it modifies the script and reinstalls.

**Cost: $0/month. Build time: 5 minutes. Replaces: $270/month plan.**

---

## LIMITATIONS (honest)

- Anchored VWAP: functional but visual presentation differs from paid version
- Screener: runs on current chart data, not real-time cross-asset stream
- Session highlighting: accurate but requires correct UTC offset input

*D.I.I + D.S.E | STIS Infrastructure | Source: Travis Woo TradingView Tricks video*
