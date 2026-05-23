# SKILL — CANDLESTICK READING
**Layer 2 Skill | D.S.E/trading/skills/**
**Skill File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: dse_framework_candlestick-as-mirror.md, dse_archive_pattern-library.md**
**Run: At every entry evaluation — reading the trigger candle(s)**

---

## PURPOSE

This skill provides the rapid, precise protocol for reading individual candles and short candle sequences. It is the micro-level tool — used at the 15M and 1H timeframes to identify the entry trigger signal within a valid setup already identified by the dual-layer chart reading skill.

A valid hypothesis + valid structure + wrong candle read = a missed or mistimed entry.
A valid hypothesis + valid structure + correct candle read = the precision that improves R:R.

---

## THE FOUR QUESTIONS OF EVERY CANDLE

Before labeling any candle, answer the four questions from `dse_framework_candlestick-as-mirror.md`:

```
WHERE did price OPEN? (The prior session's unresolved state)
WHERE did price TRY to go? (The full range of the session's attempt)
WHERE did price ULTIMATELY GO? (The close — the decision that was held)
WHO WON? (Body vs wick comparison — who has more of the candle?)
```

These four questions tell you everything. The named patterns are just shorthand for the most common combinations of answers.

---

## SECTION 1 — RAPID CANDLE CLASSIFICATION

### BODY ASSESSMENT (seconds)

```
BODY SIZE:
Large body (> 60% of total candle range): Strong conviction — one side dominated
Small body (< 30% of total range): Indecision — fight ended close to where it started
Doji (body < 10% of range): Maximum indecision — neither side won

BODY DIRECTION:
Bullish body (close > open): Buyers won the session
Bearish body (close < open): Sellers won the session

BODY LOCATION:
Body in upper 50% of range: Bullish pressure even if bearish body (failed to close lower)
Body in lower 50% of range: Bearish pressure even if bullish body (failed to close higher)
```

### WICK ASSESSMENT (seconds)

```
UPPER WICK:
None or tiny: Price did not test meaningfully higher — bullish territory uncontested
Normal: Price tested higher, some resistance
Long (> 30% of total range): Price rejected HARD from upper wick level — bearish signal above
Very long (> 50% of total range): Maximum rejection — the overhead level is defended by force

LOWER WICK:
None or tiny: Price did not test lower — bearish territory uncontested
Long: Price tested lower, buyers stepped in at lower wick level — bullish signal below
Very long: Maximum rejection of lower prices — the lower level is defended by force

THE PIN BAR RULE (from dse_framework_candlestick-as-mirror.md):
Lower wick 2x+ the body and upper wick = HAMMER = bullish rejection
Upper wick 2x+ the body and lower wick = SHOOTING STAR = bearish rejection
The location of the pin bar is MORE IMPORTANT than the pin bar itself:
- Hammer at an OB or FVG or key support = high probability reversal signal
- Hammer in the middle of a range = noise
```

---

## SECTION 2 — THE TRIGGER CANDLE DICTIONARY

These are the primary candles used as entry triggers in the STIS. Each must occur at a VALID LEVEL to qualify as a trigger.

### BULLISH TRIGGERS

**HAMMER** (or pin bar low)
```
Structure: Small body at top, long lower wick (2x+ body length)
Body color: Either — bullish preferred but not required
What it means: Price swept lows (swept Mutable Cross stops), then buyers recovered completely
Trigger condition: Must occur at OB zone / FVG zone / key support level in discount zone
Entry: Buy on close or next candle open
Stop: Below the lower wick (below where price was rejected)
Target: Next liquidity pool above (previous high / FVG / OB)
```

**BULLISH ENGULFING**
```
Structure: Large bullish candle completely "engulfs" the prior bearish candle's body
The bullish candle must open at or below the prior candle's close AND close above its open
What it means: Sellers' entire session was reversed by buyers — complete dominance shift
Trigger condition: At OB zone / key support / after a sweep of lows
Entry: On close of the engulfing candle
Stop: Below the low of the engulfing candle (or the prior candle's low if lower)
Note: The larger the engulfing, the stronger the signal
```

**MORNING STAR** (3-candle sequence)
```
Structure: (1) Bearish candle → (2) Small indecision candle (doji or spinning top, ideally with gap) → (3) Large bullish candle closing > 50% into Candle 1's body
What it means: The Crisis (C1 bearish), the Polarization (C2 indecision), and the Sweep initiation (C3 bullish) — the full cycle in 3 candles
Trigger condition: Must occur at key support, OB, or after a significant downtrend
Entry: On close of Candle 3
Stop: Below the low of Candle 2 (the Polarization candle)
```

**BULLISH MARUBOZU**
```
Structure: Large bullish candle with NO wicks (or very small wicks — < 5% of body)
What it means: Buyers dominated the ENTIRE session — no test of lower prices was sustained
Context: R1 Will expression — a decisive assertion. The move IS the message.
Entry: This candle is often a BOS candle — the signal is already past. Wait for the pullback to the OB this candle created, rather than chasing.
```

**INSIDE BAR BREAKOUT (bullish)**
```
Structure: A small candle completely inside the prior candle's range, followed by a bullish break above the inside bar high
What it means: Polarization (the inside bar) followed by Sweep initiation (the break)
Trigger condition: The inside bar should be within a valid OB zone or after a liquidity sweep
Entry: On break and close above the inside bar high
Stop: Below the inside bar low
Note: The inside bar is R3 compression storing R1 energy. The breakout direction = the R1 assertion.
```

---

### BEARISH TRIGGERS

**SHOOTING STAR** (or pin bar high)
```
Structure: Small body at bottom, long upper wick (2x+ body length)
What it means: Price swept highs (swept Mutable Cross buy stops), then sellers recovered completely
Trigger condition: At OB zone (now Breaker) / FVG zone / key resistance in premium zone
Entry: Sell on close or next candle open
Stop: Above the upper wick
Target: Next liquidity pool below
```

**BEARISH ENGULFING**
```
Structure: Large bearish candle completely engulfs the prior bullish candle's body
What it means: Buyers' entire session reversed by sellers — complete dominance shift
Trigger condition: At Breaker zone / key resistance / after a sweep of highs
Entry: On close of the engulfing candle
Stop: Above the high of the engulfing candle
```

**EVENING STAR** (3-candle sequence)
```
Structure: (1) Bullish candle → (2) Small indecision → (3) Large bearish candle closing > 50% into Candle 1's body
The bearish cycle in 3 candles
Trigger condition: At key resistance, after a significant uptrend / Breaker zone
Entry: On close of Candle 3
Stop: Above the high of Candle 2
```

**THREE BLACK CROWS**
```
Structure: Three consecutive bearish candles, each with similar size and each closing near its low
What it means: Sustained, institutional selling pressure — no Mutable Cross reaction recoveries
Context: R1 bearish force — not a single event but a sustained assertion
Entry: After the third crow closes, on the next candle's open (if at a valid level)
Note: Do not chase three black crows that have already extended far from the key level
```

---

## SECTION 3 — SEQUENCE READING (Candle Groups)

Individual candles provide the trigger. The sequence provides the context.

### THE BUILDUP SEQUENCE (Pre-Move Compression)
```
[Normal candle] [Normal candle] [Smaller] [Smaller] [Tiny inside bar]
                                                          ↓
                                                    THE EXPANSION CANDLE
```
When you see progressively smaller candles: STOP anticipating, start watching. The expansion is imminent. The direction of the expansion = the trade direction. Do NOT enter before the expansion candle closes.

**The false expansion warning:** If the "expansion" candle closes back inside the compression range = not real. Wait for the second candle to confirm.

---

### THE CLIMAX SEQUENCE (Reversal Warning)
```
[Normal trend candles] [Larger] [Larger] [CLIMAX — largest candle of entire series, on highest volume]
                                                         ↓
                                                   [RECOVERY CANDLE — smaller, opposite color]
```
The Volume Climax Reversal (Pattern 8 from `dse_archive_pattern-library.md`). The climax candle = R4 maximum conflict expressing in one moment. The recovery candle = the R1/R2 beginning.

**Entry:** On the close of the recovery candle. Stop: below the wick of the climax candle.

---

### THE INSTITUTIONAL MOVE SEQUENCE
```
[Large body candle] [Small retracement candles — 2-3 candles]
       ↑ BOS                     ↑ OB zone is here
                                         [Next large body candle in same direction]
```
When you see a strong impulse followed by 2-3 small-bodied corrective candles that do NOT fill the prior impulse's body: this is the institutional continuation setup. The small corrective candles are the Fixed Cross adding at better levels. The next impulse will be of similar or greater size.

---

### THE REJECTION SEQUENCE (The Cardinal Cross Tells Its Story)
```
[Setup candle enters the OB zone]
      ↑ long lower wick forms (Cardinal Cross is here)
[Small candle] (brief hesitation)
[Impulse candle in the direction of the OB] (Cardinal Cross confirmed — entry)
```
Three candles: the probe → the pause → the decision. This is the most reliable OB return entry sequence. The probe tests the OB (the pin bar). The pause confirms the Cardinals are defending. The impulse confirms the direction.

---

## SECTION 4 — VOLUME INTEGRATION

Volume amplifies or weakens every candle signal:

```
CANDLE + HIGH VOLUME:
  Bullish engulfing + high volume = maximum conviction reversal
  Bearish candle breaking support + high volume = real break (not a sweep)
  Pin bar + high volume = institutional participation at this level (strong signal)

CANDLE + LOW VOLUME:
  Any candle + unusually low volume = treat as noise until confirmed
  A BOS on low volume = possible inducement (Fixed Cross trap)
  Inside bar + very low volume = deepest compression = strongest expansion incoming

VOLUME AND THE SWEEP:
  Liquidity sweep candle + spike volume → immediate recovery = the sweep worked
  Liquidity sweep candle + spike volume → continuation = real break, not a sweep
  The volume on the recovery candle must be comparable to the sweep candle to confirm Cardinal Cross defense
```

---

## SECTION 5 — THE 5-SECOND CANDLE SCAN

In live markets, candles are forming in real time. The rapid assessment:

```
1. WHAT IS THE BODY DOING? → Large/small? Bullish/bearish? In upper/lower half?
2. WHAT ARE THE WICKS SAYING? → Which side is being rejected?
3. IS THIS AT A VALID LEVEL? → OB? FVG? Key structure? Yes = signal. No = noise.
4. WHAT WAS THE PRIOR CANDLE? → Opposite? → Engulfing sequence. Same? → Momentum.
5. DOES THIS MATCH THE HYPOTHESIS TRIGGER? → If yes: execute. If not: wait.
```

The 5-second scan does not replace the full analysis. It is for the moment when the entry trigger fires and a decision must be made quickly.

---

## SECTION 6 — CANDLE FAILURES TO WATCH FOR

Not every candle is a signal. These are patterns that look like signals but are not:

```
FALSE SIGNAL 1 — THE WICK TRAP
  Long wick forms at a key level → but closes as a bearish body
  This is NOT a hammer — the close tells the truth. The wick tested support, found it, then was rejected.
  → Interpretation: The level tested lower and the recovery was incomplete. Weakness at this level.

FALSE SIGNAL 2 — THE OUTSIDE BAR CONFUSION
  An "outside bar" (ranges wider than the prior candle in BOTH directions) is a conflict candle, not a direction candle
  The close matters: if it closes bullish (near the high of its range), treat as tentatively bullish
  If closes near the middle → R4 maximum conflict, no clear signal

FALSE SIGNAL 3 — THE GAP FILL CANDLE
  A candle that gaps at open and then reverses to fill the gap is NOT a reversal signal
  It is a gap fill — the market is simply filling the imbalance. Wait for the candle AFTER the gap fill.

FALSE SIGNAL 4 — THE PRE-NEWS PINBAR
  A pin bar forming in the 30-60 minutes before a major data release
  This is NOT a genuine Cardinal Cross signal — it is positioning/stop-hunting before news
  Never enter on a trigger candle that forms within 1 hour of a major economic release
```

---

## CROSS-REFERENCES
- `dse_framework_candlestick-as-mirror.md` — the framework this skill operationalizes
- `dse_archive_pattern-library.md` — the patterns that these candles form within
- `dse_framework_order-flow-mechanics.md` — the liquidity mechanics each candle expresses
- `skill_dual-layer-chart-reading.md` — Phase 2E uses this skill for entry trigger identification
- `skill_chart-pattern-recognition.md` (pending) — how these candles combine into multi-candle patterns

---

*skill_candlestick-reading.md | D.S.E/trading/skills/ | STIS Layer 2 Operational Skill*
*Status: v1.0 — active | Applied at every entry evaluation.*
