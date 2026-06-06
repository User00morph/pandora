# SKILL — POC TREND FILTER
**Session Point of Control as the Binary Trend Classifier**
**Load when:** Establishing directional bias for any trading session.
**Department:** D.S.E trading workspace | STIS Layer 2 (Collective Consciousness)

---

## WHAT THIS IS

The simplest and most reliable trend filter in the STIS stack. The prior session's POC (Point of Control — the highest volume price level) determines directional bias for the current session. "If the market is trading above the POC, we're in an uptrend. If it's below, we're in a downtrend. It really is that simple."

---

## THE RULE

```
Price ABOVE prior session POC → LONG BIAS
Price BELOW prior session POC → SHORT BIAS
Price AT prior session POC → NEUTRAL — wait for resolution
```

The session hierarchy for POC reference:
1. **Asia session POC** → reference for London session bias
2. **London session POC** → reference for New York session bias
3. **Prior day POC** → reference for full day bias

---

## WHY IT WORKS

The POC is the price level where institutions did the MOST business during that session. It represents their collective cost basis for that period. Institutions will defend this level — they want to protect their filled orders. Price above the POC means the session's collective institutional position is in profit. Price below means it's in drawdown.

This is why the POC acts as a magnet, a support/resistance, and a trend anchor — not because of "S/R" but because of institutional cost basis psychology.

---

## CONFLUENCE AMPLIFIERS

The POC filter becomes Grade A++ when combined with:

| Confluence | What it adds |
|---|---|
| GEX regime aligned | Mechanical force confirms structural bias |
| IEC phase aligned | Institutional cycle confirms directional read |
| Markov signal aligned | Statistical probability confirms direction |
| ATR trend indicator aligned | Momentum confirms structure |

**Three-way confluence (POC + GEX + IEC):** Maximum conviction. Full size.

---

## MORNING PREP PROTOCOL

```
1. Identify Asia session POC from prior session
2. Note London session POC
3. Mark yesterday's full-session POC
4. Check current price relative to all three
5. Log: "Price [above/below] Asia POC [level] | London POC [level]"
6. Set bias: [long / short / neutral] for session
```

---

## RULES

- POC filter sets the BIAS — not the entry
- Never trade against a clear POC bias unless all other layers strongly disagree
- When price is within 5 ticks of the POC, bias is neutral — wait for resolution

*D.S.E/trading/skills | STIS Layer 2 | POC Trend Filter | Source: Travis Woo Volume Profile video*
