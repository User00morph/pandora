# WF STAGE 1 — SETUP
## D.TRD — Trading | First-time / one-time intake

**Trigger:** Run once before any live session. Re-run only if Tiki's capital, broker, or risk rules change.

## STAGE CONTRACT

1. Open `_config/trd_config_tiki-profile.md`. If any required field is blank, ask Tiki directly — do not assume.
2. Required fields before this stage is complete:
   - Capital allocated to trading
   - Broker / platform
   - Asset class (stocks, options, futures, crypto)
   - Timeframe (day trading — confirm hours she can actually watch the market)
   - Risk per trade (max % of capital risked on a single position)
   - Experience level (beginner vs. experienced — changes how much strategy complexity is appropriate)
3. Once filled in, confirm the profile back to Tiki in plain language before moving to Stage 2.
4. Update `ref_trd.md` Active State table: mark profile as filled in.

**Exit condition:** Profile complete and confirmed. Do not proceed to Stage 2 (live sessions) otherwise.
