# L4 VALIDATION LEDGER — DECLINATION SYSTEM vs MARKET TURNS
**Filed:** 2026-07-07 | **Tool:** `tools/astro_backtest.py` (PRD v6 build #9)
**Method:** DS turning points (ephem-computed, Beann weights) vs price swing turns (±10 trading days), scored against 1,000-permutation random baseline.
**Valid until:** standing result — supersede only with a pre-registered re-test.

## RESULTS

| Test | Instrument | Window | Tolerance | Real hit | Random base | p-value | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | SPY | 10y | ±5d | 10.9% | 12.4% | 0.760 | NO EDGE |
| 2 | GLD | 10y | ±5d | 8.0% | 12.3% | 0.984 | NO EDGE (worse than random) |
| 3 | SPY | 10y | ±7d, DS extremes 20% tails (book's claim) | 8.6% | 11.6% | 0.929 | NO EDGE |
| 4 | GLD | 10y | ±7d, DS extremes 20% tails | 10.4% | 11.6% | 0.772 | NO EDGE |

## RULING (per PRD v6 §9)

The composite Declination System, as decoded and weighted, has **no timing edge** on SPY or GLD over the last decade. Four tests including the book's own strongest claim (extremes) all fall at or below the random baseline.

- **Directional/timing authority: SUSPENDED.** No trade sizing, timing, or entry decision may cite the DS.
- **Retained roles:** L4 remains context/state architecture (Observer discipline, cycle language, session triad) — those need no statistical defense.
- **Future re-tests must be PRE-REGISTERED** (write the parameterization and prediction *before* running) — scanning parameters until something passes is data mining, and a p-value found by search is not a p-value. Candidate pre-registered re-tests, in order: (1) per-planet applying aspects (aspect_scanner) vs intraday range expansion, not swing turns; (2) heliocentric vs geocentric DS variant; (3) instrument-specific weights via walk-forward split only.
- **Transmutation:** this is the first time the OS has converted esoteric doctrine into a falsifiable number. The result is not a loss — it is the system working exactly as v6 designed it. The dual-ledger (§9) continues collecting live-session evidence independently of this historical test.

*"There is no failure — only transmutation, with a sample size."*
