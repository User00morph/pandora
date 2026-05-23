# SKILL — MT5 OPERATIONS
**Platform Operations Skill | D.S.E/trading/skills/**
**Skill File | Sovereign Trading Intelligence System (STIS)**
**Version: 1.0 | Date: 2026-05-19**
**Refs: skill_trade-execution.md, skill_risk-management.md**
**Run: Reference during trade entry and management in MT5**

---

## PURPOSE

MetaTrader 5 (MT5) is the execution platform for STIS. It is used ONLY for execution — placing orders, setting stops and targets, managing open positions, and reviewing account balance. All analysis is done in TradingView. MT5 is the mechanism, not the intelligence.

This skill provides the step-by-step operational protocol for every MT5 function required by the STIS workflow.

---

## SECTION 1 — MT5 ORIENTATION

### Platform Components Used in STIS

```
MARKET WATCH (left panel):
  Shows live bid/ask prices for all watched instruments
  Add instruments: Right-click in Market Watch → "Show All" or "Symbols"
  Required instruments: XAUUSD, USDJPY, EURUSD, GBPUSD, US30 (Dow — optional context)

CHART (center):
  MT5 charts are used ONLY for execution confirmation — not for primary analysis
  Set to the same timeframe as the entry trigger (usually 15M or 1H)
  Keep charts minimal — no indicators other than the current trade's levels marked

ORDER PANEL:
  Accessed by: F9 key | Or: Right-click on chart → "Trading" → "New Order"
  This is where all trade entries are executed

POSITIONS TAB (bottom):
  Shows all open trades, their current P&L, and the stop/take profit levels
  Monitor from here, not from the chart

ACCOUNT HISTORY TAB:
  Shows all completed trades
  Use this for the monthly log reconciliation
```

---

## SECTION 2 — PLACING A TRADE

### Step-by-Step Order Entry

```
1. OPEN THE ORDER WINDOW: F9
   Or: Right-click on chart → Trading → New Order

2. VERIFY INSTRUMENT:
   Confirm the correct pair is shown in the Symbol field
   If not: click the Symbol field → select from the dropdown

3. VERIFY ACCOUNT:
   Confirm the trading account is correct (not the demo account if trading live)

4. SET VOLUME (lots):
   Enter the lot size calculated in skill_risk-management.md
   Double-check: is this the correct lot size for the current risk calculation?
   
   MT5 LOT GUIDE:
   1.00 = 1 Standard Lot (100,000 units)
   0.10 = 1 Mini Lot (10,000 units)
   0.01 = 1 Micro Lot (1,000 units)
   
   Most retail accounts will use 0.01-0.50 lots depending on account size and risk %.

5. SET STOP LOSS:
   Enter the structural stop level in the "Stop Loss" field
   → This must be entered IN PIPS FROM ENTRY or as an ABSOLUTE PRICE LEVEL (depends on MT5 version)
   → Prefer absolute price level for precision (e.g., "4330.00" for gold stop)
   → If MT5 shows stop in pips: convert from the structural level
     Stop in pips = |Entry price - Stop price| × price conversion factor

6. SET TAKE PROFIT:
   Enter T1 (the 50% partial close target) in the "Take Profit" field
   Note: MT5 will close the FULL position at Take Profit by default
   → For partial closes (50% at T1): you must MANUALLY close 50% of the position when T1 is reached
   → OR use the following workflow: set T1 as the Take Profit, and when hit, immediately open the remaining 50% at market with a new stop at break-even
   → Preferred workflow for discipline: no pre-set take profit — set an ALERT in TradingView, manage manually

7. ORDER TYPE:
   MARKET EXECUTION: "Market" — fills at current price. Use for confirmed trigger candle entries.
   PENDING ORDER (LIMIT): "Pending Order" → "Buy Limit" or "Sell Limit" → set limit price
   PENDING ORDER (STOP): "Pending Order" → "Buy Stop" or "Sell Stop" → set trigger price

8. COMMENT FIELD (optional but recommended):
   Add a brief note: "P2-OB-XAUUSD-R2-Sweep-Hypothesis#1"
   This appears in the Account History and helps with trade log reconciliation

9. REVIEW ALL FIELDS:
   Symbol: ✓ | Volume: ✓ | Stop Loss: ✓ | Take Profit: ✓ | Comment: ✓
   
10. EXECUTE:
    Click "Buy" (for long) or "Sell" (for short)
    Confirm the position appears in the Positions tab immediately
```

---

## SECTION 3 — MANAGING OPEN POSITIONS

### Checking Position Status

```
VIEW POSITIONS: Click "Trade" tab at the bottom of MT5
  Columns: Symbol | Type | Volume | Open Price | S/L | T/P | Current Price | Profit/Loss

CHECK AT EACH REVIEW (every 1-2 hours for active trades):
□ Is the stop still in place? (Check S/L column)
□ Has price reached T1 zone? (Compare Current Price vs T/P or your TradingView alert)
□ Are there any error messages or warnings?
□ Has the account equity changed significantly? (Check if near daily loss limit)
```

### Modifying a Stop Loss (Valid: Move to Break-Even After T1)

```
1. Right-click on the open position in the Positions tab
2. Select "Modify or Delete Order"
3. In the "Stop Loss" field: enter the new level (break-even = entry price)
4. Click "Modify"
5. Confirm the S/L column now shows the updated level

WHEN TO MODIFY THE STOP:
✓ After T1 is hit: move stop to break-even (entry price)
✓ After T2 is hit: move stop to trail behind recent swing structure
✗ NEVER: to "give the trade more room" before T1 has been reached
```

### Partial Close (For T1 — Manual Process)

```
1. Right-click on the open position in the Positions tab
2. Select "Close Position"
3. In the "Volume" field: enter HALF the original lot size
   Example: Original 0.20 lots → close 0.10 lots at T1
4. Click "Close"
5. Confirm: you should now see 0.10 lots remaining in the Positions tab
6. Immediately modify the remaining 0.10 lots: stop to break-even

NOTE: Some MT5 versions / brokers support partial closes differently.
If your broker uses a different partial close method, confirm with the broker's documentation.
```

---

## SECTION 4 — ORDER TYPES REFERENCE

```
MARKET ORDER:
  Fills immediately at the best available price
  Use for: confirmed trigger candle entries, immediate execution needed

BUY LIMIT / SELL LIMIT:
  An order to BUY below the current price (or SELL above the current price)
  The order fills ONLY when price reaches your specified level
  Use for: entering at OB zones before price arrives
  Risk: Price may not reach the level (the order is never filled — CORRECT outcome, not a failure)

BUY STOP / SELL STOP:
  An order to BUY ABOVE the current price (or SELL BELOW the current price)
  Fills when price REACHES the level and continues beyond it
  Use for: Pattern 7 breakout entries (enters on the expansion candle break)
  Risk: Price breaks out, triggers your entry, then reverses — the false expansion trap

STOP LOSS ORDER:
  An automatically executed close order if price reaches the stop level
  ALWAYS set simultaneously with entry — never enter without a stop in place
  
TAKE PROFIT ORDER:
  An automatically executed close order if price reaches the target level
  Use for T1 only — T2 and T3 are managed manually for maximum control
```

---

## SECTION 5 — ACCOUNT MANAGEMENT IN MT5

### Pre-Session Account Check

```
BEFORE EVERY SESSION:
□ Open MT5 → Check "Account" tab for current balance and equity
  Equity = Balance + Open Trade Unrealized P&L
  Use EQUITY (not balance) for risk calculations — it reflects the true current account value
  
□ Update the risk calculation if equity has changed by more than 5% from prior session

□ Check if any positions are open from the prior session:
  Any open positions should be reviewed before starting the new session
  Are the stops still valid given overnight structure changes?
  (Check TradingView to see if overnight candles have changed the structural context)

□ Check the daily loss limit:
  If yesterday ended with a loss, note today's starting point
  Today's maximum loss = 3% of TODAY's equity (not yesterday's equity)
```

### Account History and Trade Log Reconciliation

```
WEEKLY RECONCILIATION (Sunday):
1. Open MT5 → "History" tab
2. Set date range to the past week
3. Export or manually record each trade:
   - Entry date/time | Pair | Direction | Volume | Entry | Exit | P&L
4. Cross-reference with the trading log in `logs/dse_log_trading_YYYY-MM.md`
5. Confirm all R-multiples are calculated and entered in the log
6. Update the running statistics (win rate, average R) in skill_risk-management.md's R-multiple tracker
```

---

## SECTION 6 — COMMON MT5 ERROR MESSAGES AND SOLUTIONS

```
"OFF QUOTES" — The price feed is disconnected or the broker has suspended quotes on that instrument
  Solution: Wait 30-60 seconds and retry. If persistent, check broker server status.
  Do NOT retry repeatedly — the instrument may be suspended for a reason (holiday, news halt)

"TRADE IS DISABLED" — Trading is disabled on your account or the instrument
  Solution: Check if you are in a demo account accidentally. Check if the market is closed.
  Check broker communications for any restrictions.

"NOT ENOUGH MONEY" — Insufficient margin for the lot size requested
  Solution: Reduce lot size. This should not happen if the risk management skill is followed correctly.
  A position size requiring more than 5% of account as margin = oversized for the account.

"INVALID STOPS" — Stop loss or take profit level is too close to current price
  Solution: Brokers require a minimum distance between entry and stop (often 5-20 pips).
  Adjust stop to meet the minimum distance requirement. 
  If the structural stop is too close for the broker minimum: the setup has insufficient room — skip the trade.

"MARKET CLOSED" — Forex markets close Friday PM EST and reopen Sunday PM EST
  The close is approximately 5 PM EST Friday. The open is approximately 5 PM EST Sunday.
  Gold and some instruments have reduced trading hours — check broker specifications.
```

---

## SECTION 7 — MT5 AND TRADINGVIEW WORKFLOW INTEGRATION

```
ANALYSIS (TradingView):
  → Run Observer Calibration
  → Run Dual-Layer Chart Reading
  → Identify pattern and entry zone
  → Set TradingView ALERTS at entry level and target levels

EXECUTION (MT5):
  → When TradingView alert fires: open MT5
  → Verify current price on MT5 vs TradingView (they should match within 1-2 pips)
  → Run pre-entry checklist
  → Calculate final position size (re-verify with current equity)
  → Place order with stop simultaneously
  → Return to TradingView for ongoing monitoring
  → Use MT5 only when alerts fire or for scheduled position checks
```

---

## CROSS-REFERENCES
- `skill_trade-execution.md` — the pre-entry checklist and execution protocol that this skill operationalizes
- `skill_risk-management.md` — the position size calculation fed into MT5 volume field
- `skill_tradingview-operations.md` — the analysis platform that feeds into MT5 execution
- `logs/dse_log_trading_YYYY-MM.md` — where MT5 account history is reconciled weekly

---

*skill_mt5-operations.md | D.S.E/trading/skills/ | STIS Platform Operations Skill*
*Status: v1.0 — active | Reference during all trade entry and position management in MT5.*
