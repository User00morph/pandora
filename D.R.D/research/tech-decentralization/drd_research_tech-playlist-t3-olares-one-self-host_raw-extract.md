# RAW EXTRACT — Olares One: Run AI Locally + Self-Host Everything

## Source Metadata
- **Title:** Olares One: Run AI Locally + Self-Host Everything
- **Duration:** 20:24
- **URL:** https://youtu.be/tTB8spzgdzM
- **Video ID:** tTB8spzgdzM
- **Tier:** 3 (Pandora Tech Playlist)
- **Extracted:** 2026-06-20
- **Domain:** tech-decentralization / local-ai-infrastructure / home-server
- **Disclosure noted by source:** Creator received free Olares One hardware from the company (sponsored content, not cash) — flag bias accordingly.

## Transcript (timestamped, condensed)
[00:00:00] Olares (formerly TerminusOS, renamed ~1 year ago) — open-source personal cloud OS, self-hosting platform. Desktop-like browser UI, taskbar on left side.
[00:02:13] Unifies local files, synced devices, and NAS shares into one file manager interface.
[00:04:14] App store ("market") — every app installs in a couple clicks, no command line or config files. **Built on Kubernetes** under the hood (user doesn't need to know this).
[00:05:44] Security model: every app runs in its own sandbox, isolated from other apps and the system — one compromised app can't affect others or the data.
[00:06:00] Remote access via unified "Olares ID" login + secure URL. Client app "Larapass" works cross-platform (PC/Mac/tablet/phone/browser extension).
[00:06:23] **Caveat — currently requires internet for authentication** (no true offline-first auth yet, though team says it's in development).

### Olares One Hardware (the appliance itself)
[00:06:56] Launching on Kickstarter early December, **$2,999** (campaign price; $50 refundable deposit gets $200 off; shipping ~January 2026). Specs subject to change (pre-production/Kickstarter caveat).
[00:07:47] **Specs:** Intel Core Ultra 9 275HX (24-core, 5.4GHz max turbo), **96GB DDR5 RAM**, 2TB NVMe, **RTX 5090 Mobile (24GB VRAM)** — VRAM matches a desktop RTX 4090, in a mobile form factor.
[00:08:50] Physical: cube design, ~320×197×55mm, under 23 dB idle (very quiet per creator, no formal measurement tool used).
[00:09:24] I/O: barrel jack (330W PSU), Thunderbolt 5, HDMI 2.1, USB-A, 2.5GbE ethernet, Wi-Fi 7, Bluetooth 5.4. No monitor/keyboard needed for daily operation — managed entirely via browser/app.

### Performance claims (creator's own testing, ~2 weeks)
[00:11:19] Text generation on GPT-OSS-20B: ~125-130 tokens/sec using optimized frameworks.
[00:11:39] Image generation (ComfyUI + Qwen image models): 4 unique 1024×1024 images in 30 seconds.
[00:12:05] Video generation (WAN 2.2 image-to-video): ~7 minutes for a few-second clip; GPU maxed, temps reached upper-80s°C; fan noise described as quieter/less annoying than the creator's laptop fans.
[00:13:41] GPU allocation modes: dedicate full GPU to one app, OR memory-slice VRAM across multiple apps simultaneously, OR time-share (apps take turns with full GPU).
[00:14:26] Also runs Steam Headless (game streaming via Proton — ~80% of Steam's top 100 games), full Windows VM accessible via RDP for occasional Windows-only software needs, self-hosted Mattermost (private Slack alternative).

### Funding/credibility context
[00:19:17] Company has secured **$45M Series A funding**, partnering with established manufacturers for production. Software is open source under **AGPL 3.0** (auditable).
[00:20:03] Olares software itself can be installed on your own existing Linux system for free, to test before buying dedicated hardware.

---
*RAW — not yet passed through full D.R.D deconstruction. Confidence tiering applied in decode file given sponsored-hardware disclosure and pre-production/Kickstarter specs.*
