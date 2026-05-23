# SKILL — Grade A Filter (Todd 7-Criteria)
**Pre-Execution Quality Gate | All 7 criteria required**
**Load when:** Evaluating any potential trade entry. Do not enter without running this filter.

---

## WHAT THIS IS

The Grade A filter is the difference between disciplined execution and reactive gambling. Most setups that look like entries are not Grade A. The filter exists precisely to eliminate the 80% of "almost there" setups that drain accounts. A setup that passes 6 of 7 is not Grade A — it is observation data.

**Rule:** If any single criterion fails → the trade is NOT taken. Log it. Move on.

---

## THE 7 CRITERIA (ALL REQUIRED)

### 1. HTF BIAS CONFIRMED
**Question:** Is there a clear, unambiguous directional bias on the higher timeframe?

- PASS: Daily/4H structure shows clear BOS in entry direction. Price respecting the HTF trend.
- FAIL: HTF is in a range, consolidating, or structure is ambiguous.
- FAIL: HTF bias conflicts with entry direction.

*Note: "I think it's bullish" is not a pass. The bias must be visible and unambiguous.*

---

### 2. AT A KEY LEVEL
**Question:** Is price at a significant institutional reference point?

Valid key levels:
- Previous Day High / Previous Day Low (PDH / PDL)
- Session open / Session high / Session low
- Weekly open / Weekly high / Weekly low
- Order block (significant candle prior to strong move)
- Mitigation block (return to 50% of an impulsive move)
- Supply or demand zone (pine_boxes)
- Equal highs / Equal lows (liquidity pools)
- Round numbers (xx.000, xx.500)

- PASS: Price is within 10-15 pips of a clearly defined level from the above list.
- FAIL: Price is mid-range with no reference level nearby.
- FAIL: The "level" is self-drawn with no structural backing.

---

### 3. MANIPULATION OCCURRED
**Question:** Has there been a sweep / stop hunt / inducement event at or near the key level?

This is the institutional signature. Price must have:
- Swept liquidity above a high (equal highs / PDH / session high) before reversing short, OR
- Swept liquidity below a low (equal lows / PDL / session low) before reversing long

- PASS: Visible wick through the level + close back through = sweep confirmed.
- PASS: Price pushed through level (stop hunt), showed momentum failure, reversed.
- FAIL: Price approached the level and reversed without sweeping — manipulation not confirmed.
- FAIL: "The wick is small so it still counts" — no. Manipulation must be visible.

*This is the Asia Grab mechanic at the intraday level. Institutions fake out retail before delivering.*

---

### 4. EXPANSION ACTIVE (OR IMMINENT)
**Question:** Is price beginning to expand away from the entry level in the trade direction?

- PASS: Candle structure showing momentum in entry direction from the key level.
- PASS: IEC Phase identified as Expansion — price has left the Impulse Trap zone.
- FAIL: Price is still consolidating at the level after the sweep — direction unclear.
- FAIL: Candles are small, wicky, indecisive — expansion has not begun.

*Wait for confirmation. The candle that shows expansion is not the entry — it is the signal that the entry is valid.*

---

### 5. ENTRY IN SWEEP DIRECTION
**Question:** Is the entry direction aligned with where the manipulation moved price, not where it came from?

- If sweep was above the high (ran stops above) → entry is SHORT (down = sweep direction)
- If sweep was below the low (ran stops below) → entry is LONG (up = sweep direction)

- PASS: Entry direction = the direction price returned to after sweeping liquidity.
- FAIL: Entering in the direction of the sweep (chasing price into the liquidity pool).

*This eliminates all "breakout" entries that are actually chasing institutional stop raids.*

---

### 6. CLEAR STOP PLACEMENT
**Question:** Is there an unambiguous logical stop level?

- PASS: Stop is placed beyond the swept level (above the wick for short entries / below the wick for long entries).
- PASS: The stop level is at a structural point — not based on dollar amount.
- FAIL: Stop is arbitrary ("50 pips seems right").
- FAIL: Stop is inside the manipulation zone — price will hit it before delivering.

---

### 7. MINIMUM 1:3 RISK-REWARD
**Question:** Does the take profit target offer at least 3× the risk defined by the stop?

- Identify TP: nearest significant liquidity pool in entry direction (equal highs/lows, PDH/PDL, session extreme)
- Calculate: (TP distance from entry) ÷ (Stop distance from entry) ≥ 3.0
- PASS: R:R ≥ 1:3
- FAIL: R:R < 1:3 — do not adjust the stop to manufacture the ratio. The setup doesn't qualify.

*If the nearest TP only offers 1:2, either there's a better TP further out that's logical, or this is not Grade A.*

---

## QUANT ENHANCEMENT LAYER (8 + 9)

These two criteria are add-ons from the STIS quant stack. They do not replace criteria 1–7 — they UPGRADE a 7/7 pass to Grade A+ or downgrade it to Grade B based on the statistical and mechanical context.

### 8. REGIME ALIGNED
**Question:** Does the regime stack support this trade type?
**Load:** `skill_regime-detection.md` → check all four regime layers

- PASS: Gamma regime aligns (trending = follow, mean-reverting = fade matches trade type)
- PASS: Markov signal is non-zero and in entry direction (signal ≥ +0.10 for long, ≤ -0.10 for short)
- PARTIAL: One layer aligns, one conflicts → Grade B (reduce size)
- FAIL: Gamma regime directly opposes trade type (e.g., trending regime for a fade trade)

*A 7/7 setup in the wrong regime is Grade B at best. Never fight the gamma regime.*

---

### 9. FOOTPRINT CONFIRMS
**Question:** Does the volume footprint support the entry direction?
**Load:** `skill_footprint-read.md` → check delta and imbalance

- PASS: Bar delta confirms direction (green delta on long, red on short)
- PASS: Cumulative session delta aligned with entry direction
- PASS+: Imbalance cluster at or within 5 ticks of entry level (Grade A+ upgrade)
- FAIL: Delta diverging from price (price rising but delta declining = distribution)
- FAIL: Cum delta opposing entry direction

---

## SCORING (UPDATED)

```
Criteria Passed | Grade   | Action
7/7             | A       | Execute (after Observer Gate clear)
7/7 + 8 pass    | A+      | Execute — regime confirmed
7/7 + 8+9 pass  | A++     | Execute — maximum STIS confirmation
7/7 + 9 pass    | A+      | Execute — footprint confirmed
7/7 + 8 fail    | B       | Reduce size 50% — regime conflict
6/7             | —       | Log as observation. Do not execute.
5/7 or fewer    | —       | Log as interesting. Move on.
```

---

## EXECUTION CHECKLIST

```
CORE CRITERIA (all 7 required for any execution):
[ ] 1. HTF bias confirmed — direction is [LONG / SHORT]
[ ] 2. At key level — level is [describe] | GEX level? [yes/no]
[ ] 3. Manipulation occurred — sweep of [describe]
[ ] 4. Expansion active — candle structure shows [describe]
[ ] 5. Entry in sweep direction — entry is [LONG / SHORT], sweep was [direction]
[ ] 6. Clear stop — stop at [price level]
[ ] 7. 1:3 R:R — TP at [price], Stop at [price], R:R = [X:1]

QUANT UPGRADE LAYER:
[ ] 8. Regime aligned — Gamma: [aligned/conflict] | Markov signal: [value/direction]
[ ] 9. Footprint confirms — Delta: [confirms/diverges] | Cluster: [yes/no/at GEX level]

GRADE:       [A++ / A+ / A / B — FAIL — criterion(s) that failed]
MARKOV SIZE: [signal multiplier] × base risk
```

---

## NEAR-MISS LOG FORMAT

When a setup fails the filter, log it — near-misses are the most valuable data:

```
DATE/TIME: [timestamp]
SYMBOL: [pair] | TF: [timeframe]
CRITERIA MET: [X]/9 — failed: [list]
REGIME STATE: Gamma [regime] | Markov [state/signal] | Vol [regime]
WHY IT LOOKED LIKE A TRADE: [honest description]
WHAT ACTUALLY HAPPENED: [fill in after the fact]
LESSON: [what this adds to pattern recognition]
```

---

*D.S.E/trading/skills | Grade A Filter | v2.0 — 2026-05-20 | Pandora OS*
*Core 7 required. No exceptions. Quant layer upgrades grade and sizes position.*
