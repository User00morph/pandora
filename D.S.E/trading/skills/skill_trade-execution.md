# SKILL — TRADE EXECUTION
**Layer 1 Skill | D.S.E/trading/skills/**
**Skill File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: dse_framework_risk-management.md, skill_risk-management.md, STIS PRD v3 §14**
**Run: At every trade entry and trade management decision**

---

## PURPOSE

The Observer Calibration, dual-layer reading, pattern recognition, and risk management skills bring the Sovereign to the threshold of the trade. This skill covers what happens AT the threshold: the physical and mental execution protocol for entering, managing, and exiting positions correctly.

Correct execution is not speed — it is the calm, sequential application of the protocol under real-time conditions.

---

## SECTION 1 — PRE-ENTRY CHECKLIST (2 minutes)

Before placing any order, complete this checklist IN SEQUENCE:

```
□ 1. OBSERVER CALIBRATION was run today: [ ] Yes → proceed | [ ] No → run it before this trade
□ 2. DUAL-LAYER READING was completed for this pair: [ ] Yes → proceed | [ ] No → complete it
□ 3. HYPOTHESIS is fully written (all 6 components): [ ] Yes → proceed | [ ] No → do not enter
□ 4. CONVERGENCE SCORE is ≥ 6: Score: ___ → [ ] ≥ 6 proceed | [ ] < 6 do not enter
□ 5. RISK CALCULATION is complete: Risk %: ___ | Lots: ___ | Stop level: ___
□ 6. TARGET LEVELS are identified: T1: ___ | T2: ___ | T3: trailing
□ 7. R:R RATIO is ≥ 2:1: Ratio: ___:1 → [ ] ≥ 2:1 proceed | [ ] < 2:1 do not enter
□ 8. NO HIGH-IMPACT DATA within 4 hours: [ ] Confirmed | [ ] Event at ___ — abort or defer
□ 9. DAILY LOSS LIMIT not reached: Today's P&L: $___  | [ ] Limit not reached | [ ] Limit reached — stop
□ 10. OBSERVER POSITION CONFIRMED: Am I still on the Aries → Pisces wheel? [ ] Yes → enter | [ ] No → recalibrate first

ALL 10 CONFIRMED? 
→ YES: Proceed to entry execution
→ NO to any: STOP. Resolve the unchecked item or do not enter.
```

---

## SECTION 2 — ENTRY EXECUTION

### Types of Entry Orders

**LIMIT ORDER (preferred)**
```
Use when: Price has not yet reached the entry zone, and you want to enter at a specific level.
Example: Gold is at $4,420, but the OB zone is $4,380-$4,410. You place a limit BUY at $4,390.
Advantage: Ensures you enter at the correct level with the correct R:R.
Risk: Price may not reach your level (the move starts before your order is filled).
The Sovereign rule: A missed entry because price didn't reach the limit = the correct outcome. 
Never chase. The next setup will appear.
```

**MARKET ORDER (when trigger confirms)**
```
Use when: The trigger candle has formed AND closed at the entry zone, and you want immediate execution.
Example: A hammer closes at the 4H OB zone. You enter on the open of the next candle at market.
Advantage: Guaranteed fill.
Risk: Slippage — especially around major data events (another reason to avoid entering within 1 hour of news).
```

**STOP ORDER (for pattern 7 — compression + expansion breakouts)**
```
Use when: Waiting for a breakout above/below a level to confirm the expansion direction.
Example: Inside bar compression at $4,430. Place a buy stop at $4,435 (just above the inside bar high).
Advantage: Automatically enters when the expansion occurs, even if you're not watching.
Risk: Can be triggered by a false expansion and then reversed — always set the stop immediately upon fill.
```

### Entry Execution Sequence

```
1. CONFIRM the trigger signal (from skill_candlestick-reading.md): 
   Pattern + level + trigger candle = all three confirmed
   
2. CALCULATE lot size one more time (from skill_risk-management.md):
   This is not optional redundancy — prices move between hypothesis formation and execution.
   Recalculate if entry level has shifted more than 5 pips from the original calculation.

3. SET ENTRY ORDER:
   Order type: [Limit / Market / Stop]
   Direction: [Buy / Sell]
   Price: _________
   Lot size: _________ lots
   
4. SET STOP LOSS (simultaneously with entry — NEVER enter without a stop already placed):
   Stop: _________ (from risk management calculation)
   Confirm stop is at the STRUCTURAL level (not a round number proximity, not an arbitrary level)
   
5. SET TAKE PROFIT (initial target only):
   T1: _________ (50% of position at 2:1 target)
   Note: T2 and T3 are managed DURING the trade, not pre-set (prices shift; pre-set T2 limits may be suboptimal)

6. CONFIRM ORDER DETAILS before executing:
   Direction matches hypothesis? [ ] Yes
   Lot size matches risk calculation? [ ] Yes
   Stop at the structural level? [ ] Yes
   T1 at ≥ 2:1? [ ] Yes
   → EXECUTE
```

---

## SECTION 3 — TRADE MANAGEMENT

Once in a position, the trade management protocol begins. This is where most psychological slippage occurs. The rules are strict.

### The Watching Protocol
```
AFTER ENTRY:
→ Set your stop. Set your T1 target alert.
→ CLOSE the chart.

Do not watch the trade real-time tick by tick.
Watching the trade tick by tick IS the Mutable Cross behavior.
The stop protects you. The target alert will notify you.
Check the chart every 1-2 hours maximum for active trades — not every 5 minutes.
```

### When Price Moves TO the Stop
```
The stop is hit.
The experiment is complete.
DO NOT:
  □ Move the stop to "give it more room"
  □ Add to the position ("averaging down") 
  □ Place a new trade in the same direction immediately ("getting my money back")

DO:
  □ Accept the fill. The experiment is complete.
  □ Run the post-trade Observer Calibration Protocol (from skill_observer-calibration.md)
  □ Log the trade in the monthly log
  □ Wait. The next setup will appear.
```

### When Price Moves TO the First Target (T1)
```
T1 alert fires.
Execute the partial close:
→ Close 50% of the position at T1
→ Move the stop to break-even on the remaining 50% (entry price, not the original structural stop)
→ Set T2 alert at the 3:1 level
→ The trade is now "risk-free" on the remaining 50% — it cannot produce a net loss
```

### When Price Moves TO the Second Target (T2)
```
T2 alert fires.
Execute the partial close:
→ Close 25% of the position at T2 (half of the remaining 50%)
→ Now 25% of the original position remains
→ Begin the trailing stop protocol on this 25%:
   Trail stop behind the most recent 4H or 1H SWING LOW (for longs) / SWING HIGH (for shorts)
   Move the trailing stop UP each time a new swing low forms (for longs)
   Exit when the trailing stop is hit — or when the cycle phase changes (Sweep exhaustion signals)
```

### When Price Moves Against the Position (Before Stop)
```
Price is moving against you but has NOT hit the stop.
DO NOTHING. 
The stop defines the experiment's boundary. 
As long as price has not hit the stop, the experiment is still running.
DO NOT:
  □ Close early because "it's not working"
  □ Add more to "average your entry better"
  □ Move the stop closer to reduce current mark-to-market loss
  □ Check news to rationalize closing the trade
```

---

## SECTION 4 — TRADE EXIT PROTOCOLS

Beyond the automatic stop and target protocols, there are valid reasons to exit a trade before either is reached:

### Valid Early Exit Conditions
```
□ A significant Ray transition occurs that invalidates the hypothesis
  Example: Entry was based on R2 accumulation thesis. A surprise geopolitical event shifts to R4 Crisis.
  The Ray that supported the hypothesis has changed. The thesis is no longer valid. EXIT.
  
□ The cycle phase changes materially
  Example: Entry was in a confirmed Sweep phase. A large unexpected BOS in the opposite direction 
  signals possible CHoCH and transition to Polarization or Crisis. EXIT.
  
□ A major data release produces a new structural reality
  Example: A surprise FOMC emergency meeting changes the rate trajectory fundamentally.
  The Layer 3 confirmation that supported the entry is now reversed. EXIT.

□ A KILL CONDITION is triggered (from skill_observer-calibration.md):
  Two consecutive losses at stop → Three failed entries at same level → Observer position lost
  EXIT all positions, run post-trade calibration, assess before re-entering.
```

### INVALID Early Exit Conditions (do not exit for these reasons)
```
✗ "The trade is in profit and I'm worried it will reverse"
   → Trust the system. Let T1 be the profit-taking trigger, not anxiety.
   
✗ "It's been X hours and the trade hasn't moved"
   → Time is not a valid exit condition. Structure is. Let the stop or target trigger.
   
✗ "I just had a feeling it won't work"
   → Feelings are Mutable Cross. The Observer executes the hypothesis, not the feeling.
   
✗ "The news just said [X] and I'm worried"
   → News should have been assessed in the hypothesis. If the news was anticipated, hold.
     If the news is genuinely regime-changing: use the valid early exit protocol above.
```

---

## SECTION 5 — POST-TRADE PROTOCOL

After every trade closes (whether at stop, target, or valid early exit):

**Within 5 minutes of close:**
```
□ Name any emotional residue: "I feel [___] because [___]."
□ Was the stop honored? [ ] Yes (system worked) | [ ] No (rule break — note why)
□ Was position sizing correct? [ ] Yes | [ ] No — correction for next trade: ___
□ Was the entry trigger valid? [ ] Yes | [ ] No — what was the false signal?
```

**Within 30 minutes of close:**
```
Hypothesis assessment (from skill_observer-calibration.md POST-TRADE Section):
□ Was the Ray read correct? What confirmed or contradicted it?
□ Was the cycle phase read correct?
□ Was the entry trigger valid in retrospect?
□ Hypothesis result: [ ] Confirmed [ ] Invalidated [ ] Refined
   If refined: write the refined hypothesis for reference
```

**Log entry:**
Complete the trade log entry in `logs/dse_log_trading_YYYY-MM.md` (see that file for the format).

**The Dissolution:**
Read the Great Reversal Dissolution ritual (from `dse_framework_great-reversal-doctrine.md`):
> "This trade is complete. Its outcome is data. The data has been logged.
> I release the result back into the field.
> The next session begins from the same foundation.
> The Observer remains."

---

## SECTION 6 — THE EXECUTION SUMMARY CARD

The condensed version for a fully internalized protocol:

```
BEFORE: 10-point checklist ALL green → position size calculated → orders set
ENTRY: Limit / Market / Stop order → Stop set SIMULTANEOUSLY → T1 alert set
DURING: DO NOT WATCH tick by tick → check 1-2x per hour maximum
AT T1: Close 50% → Move stop to break-even → Set T2 alert
AT T2: Close 25% → Trail remaining 25% behind structure
AT STOP: Accept → Post-trade calibration → Log → Dissolve → Next session
EARLY EXIT (valid only): Ray/phase change → regime data → kill condition triggered
POST-TRADE (always): Name residue → Assess hypothesis → Log → Dissolve
```

---

## CROSS-REFERENCES
- `skill_observer-calibration.md` — must run before entry; post-trade protocol used after every trade
- `skill_risk-management.md` — provides the position size calculation for entry
- `skill_dual-layer-chart-reading.md` — provides the hypothesis and convergence score
- `skill_candlestick-reading.md` — provides the entry trigger identification
- `dse_framework_observer-flip-trading.md` — the Four Modes of Slippage (watch during trade management)
- `dse_framework_great-reversal-doctrine.md` — the Dissolution ritual used post-trade
- `logs/dse_log_trading_YYYY-MM.md` — where the trade record is created

---

*skill_trade-execution.md | D.S.E/trading/skills/ | STIS Layer 1 Operational Skill*
*Status: v1.0 — active | Applied at every trade entry, management, and exit.*
