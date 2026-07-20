# RAW EXTRACT — Turning an Old Laptop into a Home Server! (2026)

## Source Metadata
- **Title:** Turning an Old Laptop into a Home Server! (2026)
- **Channel:** Tech by Matt
- **Duration:** 32:31
- **URL:** https://youtu.be/46T4cDQBkDs
- **Video ID:** 46T4cDQBkDs
- **Tier:** 3 (Pandora Tech Playlist)
- **Extracted:** 2026-06-20
- **Domain:** tech-decentralization / home-server / local-ai-infrastructure

## Transcript (timestamped, condensed — full walkthrough)
[00:00:00] Demonstrates converting a 7-year-old laptop (8th gen Intel i3-8130U dual-core, 8GB DDR4, 1TB 5400RPM HDD) into a home server.
[00:01:18] Swaps failing mechanical HDD for SSD. Recommends SSD over HDD; 256GB minimum workable.
[00:02:35] States 8GB RAM is adequate for basic server applications — don't upgrade RAM until you know you need it.
[00:02:56] Comparable used hardware available for ~$50 on eBay.
[00:03:12] Flashes Ubuntu Server ISO to USB via Balena Etcher.
[00:05:22] Walks through Ubuntu Server install: language, keyboard, default install type, network (DHCP auto-detected), no proxy, default mirror, storage (skips LVM — "adds complication we don't need right now"), profile/username/password, skip Ubuntu Pro, **install OpenSSH server** (critical for headless management), skip extra snap packages.
[00:08:32] Notes IPv4 address assigned (192.168.0.141) — must be recorded for remote access.
[00:08:44] For laptops specifically: edits `/etc/systemd/logind.conf` to ignore lid-close suspend (`HandleLidSwitch=ignore`, etc.) so the server keeps running with the lid closed.
[00:09:52] Connects via SSH from main PC (`ssh username@server-ip`).
[00:10:36] Runs `sudo apt update` then `sudo apt upgrade`, then reboots.
[00:11:36] Installs **CasaOS** — web GUI for managing apps/services without command line — via one curl command from casaos.io.
[00:12:33] Accesses CasaOS via browser at the server's IP. Dashboard shows CPU/RAM/storage/network stats.
[00:13:18] Creates shared network folders directly from CasaOS file manager — accessible from any PC on the network via SMB-style path.
[00:15:34] Installs **Jellyfin** (one-click via CasaOS app store) — self-hosted media server, alternative to Plex.
[00:17:33] Demonstrates transcoding bottleneck: software (CPU-only) transcoding chokes the dual-core CPU at 100%. Fix: enable **Intel QuickSync hardware acceleration** in Jellyfin (works because CPU is 7th-gen Intel or newer with iGPU) — drops CPU usage to ~45% for the same playback.
[00:19:47] Installs **Immich** (photo backup, "without machine learning" variant worked when the main one didn't) — self-hosted alternative to iCloud/Google Photos. Sets up mobile app sync; phone must be on same network to back up (can be automated).
[00:23:33] Installs **Crafty Controller** (Minecraft server manager) via CasaOS app store. Spins up a Fabric Minecraft server in a few clicks; sets RAM allocation (2GB min/4GB max).
[00:26:01] For remote friend access without port-forwarding: uses **playit.gg** (free tunnel service) — creates a sharable address, traffic routes through playit.gg, no ports exposed to the internet. Described as "much safer and more secure" than port forwarding.
[00:30:07] Total time invested: "maybe an hour or two." Total hardware cost if buying used: ~$50-400 depending on specs.
[00:30:51] Recommends also looking into: **Pi-hole** (network-wide ad blocking) and **Tailscale** (free remote access/VPN — "access your server easily, freely, and remotely from anywhere in the world").
[00:31:38] Closing rule of thumb: use old hardware you already have until you hit real hardware limitations, then plan a purpose-built server.

---
*RAW — passed through lightweight D.R.D pass below given narrow, single-source, how-to nature of content (tutorial, not contested claims).*
