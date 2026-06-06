# SKILL — SMART ALERT SYSTEM
**One Alert, All Conditions, Rich Context Delivered**
**Load when:** Setting up or modifying the trading alert infrastructure.
**Department:** D.I.I + D.S.E | STIS Infrastructure | Alert layer

---

## WHAT THIS IS

One TradingView alert covers every condition in the all-in-one indicator simultaneously. When any condition fires, the alert delivers full context — not just "something happened" but what, where, why, and what to do next.

---

## THE ARCHITECTURE

```pine
// In the Pine Script — the smart alert trigger
alert_message = ""

// Each module contributes to the message
if gex_regime_changed
    alert_message := alert_message + "GEX REGIME: " + gex_state + " | "

if markov_signal_strong
    alert_message := alert_message + "MARKOV: " + str.tostring(markov_signal, "#.##") + "% | "

if price_crosses_level
    alert_message := alert_message + "LEVEL HIT: " + str.tostring(level_price) + " | "

if kill_zone_starting
    alert_message := alert_message + "KILL ZONE: " + session_name + " OPEN | "

// Fire the single alert with all context
if alert_message != ""
    alert(alert_message, alert.freq_once_per_bar_close)
```

---

## THE SETUP PROCESS

```
IN TRADINGVIEW:
1. Click the alarm clock icon (right toolbar)
2. Create alert
3. Condition: select the STIS All-In-One indicator
4. Trigger: "Any alert() function call"
5. Frequency: "Once per bar close" (avoids duplicate alerts)
6. Notifications: select all delivery channels

DELIVERY CHANNELS:
  ✓ Push notification (phone app) — for immediate awareness
  ✓ Email — for record-keeping and review
  ✓ Webhook URL — for automation (Telegram bot, Slack, Discord)
  ✓ Sound — for when chart is open
```

---

## RICH ALERT MESSAGE FORMAT

```
STIS ALERT | EURUSD 1H | 2026-06-04 08:30 UTC
GEX REGIME: TRENDING (below HVL 1.0820) |
MARKOV SIGNAL: +47% BULL |
LEVEL HIT: GEX-2 at 1.0850 |
KILL ZONE: LONDON OPEN |
IEC PHASE: EXPANSION |
ACTION: LONG BIAS — GRADE A SETUP CONDITIONS MET
```

---

## WEBHOOK AUTOMATION

Point the webhook to a Telegram bot endpoint or a Zapier webhook:

```
TELEGRAM SETUP:
  1. Create a Telegram bot via @BotFather
  2. Get the bot token and chat ID
  3. Set webhook URL: https://api.telegram.org/bot[TOKEN]/sendMessage?chat_id=[ID]&text=
  4. TradingView appends the alert message to the URL
  5. Message arrives on Telegram instantly

RESULT: Full STIS context delivered to phone in < 1 second of condition firing.
```

---

## RULES

- One alert only — adding multiple alerts for individual conditions defeats the purpose
- "Once per bar close" prevents multiple alerts on the same bar
- The alert message is the audit trail — include timestamp, asset, and all relevant conditions
- Test the webhook before going live (send a test message)

*D.I.I + D.S.E | STIS Infrastructure | Source: Travis Woo TradingView Tricks video*
