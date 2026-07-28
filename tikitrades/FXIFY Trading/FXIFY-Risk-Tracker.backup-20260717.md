# FXIFY Risk Tracker

_Converted from `FXIFY-Risk-Tracker.backup-20260717.xlsx` — source workbook is the system of record; this file is a readable snapshot for transfer/extraction._

## How to Use

**FXIFY Risk Tracker — Gold & GBP/JPY**
Tracks daily-loss room and max-drawdown room for each FXIFY account so you know your cushion before you trade.

1. Each trading day, open the 200K Log (and 100K Log once that account is live).
2. Add ONE new row at the bottom with today's Date and current Balance.
3. Everything else calculates automatically: daily loss used/room, drawdown used/room, and a Status flag.
4. Check the Summary for a one-glance view of both accounts before you place a trade.
5. If Status says STOP or CAUTION, don't open new risk that day — see the trading plan doc for the rule.

**Rules built in (FXIFY One-Phase, from fxify.com):**
- Daily loss limit: 3% of the prior day's balance (day 1 uses the starting balance).
- Max drawdown: 6% trailing below the highest balance ever reached on that account.

## Config

| Account | Initial Balance | Daily Loss % | Daily Loss Limit $ | Max Drawdown % | Max Drawdown Limit $ | Risk % per Trade | High-Water Mark |
|---|---|---|---|---|---|---|---|
| 200K (Phase 1) | $200,000.00 | 3.0% | $6,000.00 | 6.0% | $12,000.00 | 2.0% | $201,178.33 |
| 100K (not started) | $100,000.00 | 3.0% | $3,000.00 | 6.0% | $6,000.00 | 2.0% | $100,000.00 |

Source: FXIFY One-Phase program rules — fxify.com / tradingfinder.com/props/fxify/rules (3% daily, 6% trailing drawdown).

HWM = highest equity peak ever (FXIFY dashboard). Daily loss limit = 3% of PREVIOUS DAY balance (FXIFY definition), computed per-row in the logs.

## Summary (as of latest logged entry)

| Account | As Of | Balance | Daily Loss Room $ | Daily Loss Room % | Drawdown Room $ | Drawdown Room % | Status |
|---|---|---|---|---|---|---|---|
| 200K (Phase 1) | 2026-07-16 | $196,164.57 | $4,980.77 | 84.2% | $6,986.24 | 58.2% | OK |
| 100K | - | - | - | - | - | - | - |

## 200K Log (Phase 1)

| Date | Balance | Day Start Bal. | Daily P&L $ | Daily Loss Limit $ | Daily Loss Used $ | Daily Loss Used % | Daily Room Left $ | Peak Balance | Max DD Limit $ | DD Used $ | DD Used % | DD Room Left $ | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026-07-15 | $197,096.70 | $200,000.00 | $-2,903.30 | $6,000.00 | $2,903.30 | 48.4% | $3,096.70 | $201,178.33 | $12,000.00 | $4,081.63 | 34.0% | $7,918.37 | STOP - ONE LOSS FROM DAILY BREACH |
| 2026-07-16 | $196,164.57 | $197,096.70 | $-932.13 | $5,912.90 | $932.13 | 15.8% | $4,980.77 | $201,178.33 | $12,000.00 | $5,013.76 | 41.8% | $6,986.24 | OK |

### 200K Log (Phase 1) — Notes

- **2026-07-15**: Baseline EOD balance from FXIFY dashboard ('Previous Day'). Daily figures on this row not meaningful - earlier days unlogged.
- **2026-07-16**: Per FXIFY dashboard 11:42 CT: daily -$932.13 of $5,912.90 (15.76%); max loss $5,013.76 of $12,000 (41.78%); HWM $201,178.33. Two overlapping XAUUSD sells 15:17+15:21 server time.

## 100K Log

_Not started — no rows logged yet. Same columns as the 200K Log once trading begins: Date, Balance, Day Start Balance, Daily P&L $, Daily Loss Limit $, Daily Loss Used $, Daily Loss Used %, Daily Room Left $, Peak Balance, Max Drawdown Limit $, Drawdown Used $, Drawdown Used %, Drawdown Room Left $, Status, Notes._

