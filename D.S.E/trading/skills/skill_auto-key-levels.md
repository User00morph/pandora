# SKILL — AUTO KEY LEVELS
**Automatic Level Drawing — Never Manually Redraw Again**
**Load when:** Setting up chart analysis or reviewing the active level stack.
**Department:** D.S.E trading workspace | STIS Layer 1 + 2 | Level infrastructure

---

## WHAT THIS IS

Key levels — previous day/week/month highs and lows, OHLC, session extremes — are drawn automatically by the Pine Script and update as the chart moves. No manual drawing. No stale lines. Every session start, the levels are fresh.

---

## THE AUTO-LEVEL STACK

```
DAILY LEVELS (reset every 00:00 UTC):
  PDH  — Previous Day High
  PDL  — Previous Day Low
  PDO  — Previous Day Open
  PDC  — Previous Day Close

WEEKLY LEVELS (reset every Sunday 00:00 UTC):
  PWH  — Previous Week High
  PWL  — Previous Week Low
  PWO  — Previous Week Open

MONTHLY LEVELS (reset every 1st of month):
  PMH  — Previous Month High
  PML  — Previous Month Low

SESSION LEVELS (Asia reference for London/NY):
  Asia High    — Highest price during Asia session
  Asia Low     — Lowest price during Asia session
  Asia Range   — The width of the Asia range (defines breakout range)
```

---

## WHY THESE LEVELS MATTER IN THE STIS

```
PDH / PDL:     The most watched institutional reference levels
               Price above PDH = continuation signal
               Price below PDL = breakdown signal

PWH / PWL:     The weekly range — defines whether we're trending or ranging
               Outside PWH = weekly breakout (bull)
               Outside PWL = weekly breakdown (bear)

Asia High/Low: The "manipulation" reference for London kill zone
               London break of Asia High = liquidity sweep or genuine breakout
               Return below Asia Low = reversal setup
```

---

## THE LEVEL CONFLUENCE RULE

When a GEX level, a volume profile POC, and a prior day high/low all cluster within 10 pips of each other → that cluster is a Grade A++ level. Price will respect it with maximum force.

```
PDH 1.0850 + GEX-1 at 1.0847 + VAH at 1.0853 = POWER CLUSTER
```

Seek power clusters in the morning prep. Trade at power clusters, not at isolated levels.

---

## PINE SCRIPT IMPLEMENTATION

```pine
// Previous day levels — auto-calculated
[pd_high, pd_low, pd_open, pd_close] = request.security(
    syminfo.tickerid, "D",
    [high[1], low[1], open[1], close[1]]
)

line.new(bar_index, pd_high, bar_index + 100, pd_high,
    color=color.red, style=line.style_dashed, width=1)
label.new(bar_index, pd_high, "PDH", textcolor=color.red)
```

---

## RULES

- All auto-levels extend 100 bars to the right (future projection) — do not manually extend
- When price enters a power cluster, downsize entry and tighten stop (multiple forces = potential reversal or acceleration)
- Auto-levels are reference — they don't trigger entries alone; use grade-a-filter

*D.S.E/trading/skills | STIS Layer 1+2 | Auto Key Levels*
