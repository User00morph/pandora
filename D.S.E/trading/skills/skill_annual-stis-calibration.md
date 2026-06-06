# SKILL — ANNUAL STIS CALIBRATION
**Year-End Full System Recalibration and Strategic Planning**
**Load when:** December/January — the annual reset and rebuild session.
**Department:** D.S.E trading workspace | STIS System Health | Annual architecture

---

## WHAT THIS IS

Once per year, the entire STIS is audited from first principles. Parameters are re-optimized with the latest year's data. Skills are reviewed and upgraded. The system enters the new year sharper than it left the old one.

---

## THE ANNUAL CALIBRATION SEQUENCE (full day — schedule it)

### PHASE 1 — YEAR PERFORMANCE REVIEW (2 hours)

```
PULL THE FULL YEAR:
  □ Total R earned: [X.XX R]
  □ Win rate (yearly): [X%] — Expected: 70-77%
  □ Account growth: [+/-X%]
  □ Compare to backtest expected distribution:
    Within range → system working correctly
    Below range → investigate
    Above range → investigate (may be taking too much risk or lucky year)

BEST AND WORST:
  □ Best month: [month] | R: [X.XX] | What drove it?
  □ Worst month: [month] | R: [X.XX] | What caused it?
  □ Best trade: [setup type] | Lesson to encode?
  □ Worst trade: [setup type] | Lesson to encode?

PROTOCOL COMPLIANCE REVIEW:
  □ Average checklist score across the year: [X/12]
  □ How many days was the daily budget exceeded? [N] → investigate each
  □ How many stops were widened this year? [N] → this is unacceptable if > 3
```

---

### PHASE 2 — SYSTEM RECALIBRATION (3 hours)

```
PARAMETER UPDATE:
  □ Run MTP portfolio backtest with last year's data added
  □ Re-run 200-trial optimization with the new dataset
  □ Check: did the optimal parameter range shift?
  □ If shifted > 20% → update parameters
  □ If stable → no change needed (stability = robustness confirmed)

MARKOV MATRIX UPDATE:
  □ Re-run the Markov state machine on all instruments with full 2025 data
  □ Calculate new transition probabilities including last year's regimes
  □ Update the signal calibration table with new signal-to-size thresholds

LAYER ACCURACY REPORT:
  □ For each layer: what was the accuracy rate over the full year?
  □ Which layer produced the most false signals?
  □ What single change would most improve that layer's accuracy?
```

---

### PHASE 3 — SKILL LIBRARY UPDATE (2 hours)

```
REVIEW EVERY SKILL FILE:
  □ Is the information still current? (market structure changes, new tools)
  □ Are there concepts from the year's trading that aren't captured in a skill?
  □ Are there any skills that were never used? (archive or merge)
  □ Are there new concepts from research that should become skills?

PRIORITY UPGRADES FROM THE YEAR:
  → List the 3-5 most impactful skill improvements identified
  → Make all changes in this session
  → Update the skill version notes
```

---

### PHASE 4 — STRATEGIC PLANNING (1 hour)

```
NEW YEAR OBJECTIVES:
  □ Capital target by end of year (realistic, based on system distribution)
  □ Any new instruments to add to the universe?
  □ Any autonomous trading goals? (paper trading gateway → live)
  □ AI trading firm development goals for the year

ALBEDO PHASE GATE REVIEW:
  □ Can I articulate forex mechanics from first principles? [Yes/No]
  □ Can I identify structure on live chart? [Yes/No]
  □ Can I name dominant Ray? [Yes/No]
  □ Can I calculate correct position size from scratch? [Yes/No]
  □ All yes → Consider advancing from Nigredo to Albedo phase
```

---

## THE ANNUAL CALIBRATION LOG ENTRY

```
YEAR: [YYYY]
SYSTEM HEALTH: [Excellent/Good/Needs attention]
PERFORMANCE: [X% account growth | X.XX avg R | X% win rate]
VS. EXPECTED: [Above/Within/Below distribution]
PARAMETERS UPDATED: [Yes/No + details]
MATRIX UPDATED: [Yes/No]
SKILLS UPDATED: [N skills revised]
STRATEGIC PRIORITIES FOR [YYYY+1]: [list]
ALBEDO READINESS: [X/6 criteria met]
```

*D.S.E/trading/skills | STIS System Health | Annual Architecture*
