# SKILL — MONTHLY SYSTEM AUDIT
**End-of-Month Full STIS Health Check and Calibration**
**Load when:** Last day of every month before creating the next month's log file.
**Department:** D.S.E trading workspace | STIS System Health | Monthly calibration

---

## WHAT THIS IS

The monthly audit checks that every layer of the STIS is still functioning as designed — the backtest assumptions are holding, the layer reads are calibrated, and the system is evolving correctly. Each month produces one strategic upgrade.

---

## THE MONTHLY AUDIT SEQUENCE

### SECTION 1 — PERFORMANCE vs. DISTRIBUTION (20 min)

```
Pull this month's trade data:
  □ Win rate: [X%] — Expected: 54-56% (monthly wins)
  □ Average R per trade: [X.XX R] — Expected: positive
  □ Largest win: [X.XX R] | Largest loss: [-1.0 R always]
  □ Month result: +/- [X% of account]

Compare to expected distribution (from backtest):
  □ Is this month within the historical distribution?
    Average winning month in backtest: +4-6%
    Average losing month in backtest: -2 to -3%
  □ If outside distribution: investigate (not panic)
```

---

### SECTION 2 — LAYER ACCURACY AUDIT (30 min)

```
Review each layer's reads from this month:

LAYER 1b (GEX):
  □ How often did the GEX regime correctly predict intraday behavior?
  □ Were there false regime signals? What caused them?
  □ Is the GEX engine data still fresh? (re-run calibration if needed)

LAYER 1c (Markov):
  □ How often did the Markov signal align with actual state?
  □ Were there regime change events that shifted the matrix?
  □ Update the transition matrix with last month's data → new signal table

LAYER 2 (Volume/POC):
  □ Did POC levels hold as expected?
  □ Were value area breakouts reliable signals this month?
  □ Any anomalies in delta reads?

LAYER 3 (Macro):
  □ Is the macro intelligence document still current?
  □ Any structural changes in DXY, yields, COT since last update?
  → Update dse_intelligence_current-field.md if needed

LAYER 4 (Esoteric):
  □ Were the weekly astro forecasts accurate in identifying high/low volatility days?
  □ Did cycle phase predictions match price behavior?
  → Log accuracy rate for the esoteric layer
```

---

### SECTION 3 — PROTOCOL COMPLIANCE (15 min)

```
Pull all pre-trade checklists from this month:
  □ Average checklist score: [X/12]
  □ Which questions failed most often? → These are the weak links
  □ Were any stops widened this month? → Investigate each one
  □ Were any budgets exceeded? → Investigate each one

COMPLIANCE GRADES:
  All 12/12: A — Full protocol discipline
  10-11/12:  B — Minor slippage, acceptable
  8-9/12:    C — Recurring deviations — add a rule to address
  Below 8:   F — Structural protocol issue — rebuild discipline layer
```

---

### SECTION 4 — STRATEGIC UPGRADE (10 min)

Every month identifies ONE strategic upgrade to the STIS:

```
CANDIDATES FOR UPGRADE:
  → A layer that produced the most false signals this month
  → A protocol step that was consistently skipped (and why)
  → A skill file that needs updated parameters or new information
  → A new concept from the Travis Woo library that should be integrated

THIS MONTH'S UPGRADE:
  Problem: [identified issue]
  Skill to update: [file path]
  Change: [specific update]
  → Make the change before creating next month's log
```

---

### SECTION 5 — NEXT MONTH SETUP (5 min)

```
□ Create new log file: dse_log_trading_[YYYY-MM].md
□ Update context_trading.md system status section
□ Run walk-forward check on primary instrument (monthly cadence)
□ Set next month's risk parameters based on account equity
□ Log the strategic upgrade in the system change record
```

*D.S.E/trading/skills | STIS System Health | Monthly Calibration*
