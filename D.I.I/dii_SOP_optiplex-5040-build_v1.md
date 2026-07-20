# D.I.I — OPTIPLEX 5040 "VAULT" BUILD
## SOP — Homelab Cloud Core + AI Services Node
**Date:** 2026-07-18
**Status:** ACTIVE — execute in phase order
**Machine:** Dell OptiPlex 5040 MT (mfg 2015-11, service tag DX5B082)
**Role:** Single-box cloud core per revised 2-server topology (2026-07-18) — Tailscale hub, Nextcloud, Gitea, Qdrant, Open WebUI, Ollama GPU 3B, Whisper, embeddings, Restic source.

---

## WHAT THIS IS

The 5040 absorbs both the "Vault" and "Engine" roles after OptiPlex #2 was demoted to parts donor (2026-07-18). Three transplants go into this one box, then it becomes the always-on Ubuntu server hosting the entire self-hosted service stack. The HP Envy (Node 4) handles 7B–8B heavy inference separately; the CyberPower becomes "The Archive" (backup target) after donating its GPU here.

**Parts inbound:**
| Part | Source | Destination |
|------|--------|-------------|
| DDR3L RAM sticks | OptiPlex #2 (twin board — guaranteed compatible) | DIMM slots, matched pair for dual-channel |
| Intel E1G42ETBLK dual-port NIC (82576, PCIe x4, full-height) | OptiPlex #2 | Spare PCIe slot (x16-wired-x4) |
| GTX 1050 2GB (75W, slot-powered — 240W PSU OK) | CyberPower Tower | PCIe x16 slot |

---

## PHASE 0 — PARTS HARVEST + VERIFICATION (before any software)

- [x] Pull DDR3L sticks from OptiPlex #2 — **CONFIRMED 2026-07-18: 3×4GB PC3L = 12GB.** Seat all three: two in the matched-color slot pair (DIMM1/DIMM2), third in either remaining slot (flex mode)
- [ ] Pull Intel E1G42ETBLK NIC from OptiPlex #2 (full-height bracket already correct for MT chassis)
- [ ] Pull GTX 1050 from CyberPower Tower
- [ ] Open 5040: record existing RAM (capacity/speed) and storage (SSD vs HDD, capacity)
- [ ] **GATE — storage:** if the 5040 has a spinning HDD, acquire a SATA SSD (500GB class, ~$30–40) before OS install. An always-on server hosting Nextcloud/Gitea/Qdrant on a 2015 HDD is a reliability and speed liability. Models + Nextcloud data can overflow to the HDD as a second volume.
- [ ] Install RAM: matched pair in the correct slots for dual-channel (check board silkscreen — pair same-color slots)
- [ ] Install GTX 1050 in the x16 slot; NIC in the open x4 slot
- [ ] POST check: enter BIOS (F2) — verify full RAM recognized, boot order, SATA mode AHCI
- [ ] BIOS housekeeping: set **AC Power Recovery = Power On** (server survives outages), disable unneeded boot devices
- [ ] Confirm CPU model in BIOS while there (expected i5-6500 4C/4T)

---

## PHASE 1 — OS INSTALL (headless server base)

- [ ] Ubuntu Server 24.04 LTS — flash USB installer (from MacBook: `balenaEtcher` or `dd`)
- [ ] Install to SSD; hostname: `vault`; enable **OpenSSH server** during install; no desktop environment
- [ ] Router: DHCP reservation for the onboard NIC's MAC (static local IP)
- [ ] First boot: `sudo apt update && sudo apt upgrade -y`
- [ ] SSH in from MacBook, confirm headless access, then disconnect monitor/keyboard
- [ ] `sudo apt install unattended-upgrades` — security patches automatic
- [ ] Verify all 3 Ethernet ports visible: `ip link` (onboard + 2× NIC). Onboard carries the LAN; the Intel pair stays dark until LAG/router duty is designed — do not configure yet.

---

## PHASE 2 — BASE LAYER (network + runtime)

- [ ] **Tailscale:** `curl -fsSL https://tailscale.com/install.sh | sh` → `sudo tailscale up` — this box is the hub; add MacBook + phone to the tailnet
- [ ] **Docker:** official convenience script or apt repo; add user to `docker` group
- [ ] **NVIDIA driver:** `sudo ubuntu-drivers install` — GTX 1050 is Pascal; the 570/580 branch is the last to support it, so pin that branch and hold it if newer branches drop Pascal
- [ ] Verify: `nvidia-smi` shows GTX 1050, 2GB
- [ ] **NVIDIA Container Toolkit:** install + `sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker`
- [ ] Verify GPU in Docker: `docker run --rm --gpus all ubuntu nvidia-smi`

---

## PHASE 3 — AI SERVICES

- [ ] **Ollama** (native install, not container — simpler GPU path): `curl -fsSL https://ollama.com/install.sh | sh`
- [ ] Bind to network: systemd override `OLLAMA_HOST=0.0.0.0` — reachable over LAN + tailnet
- [ ] Pull the 2GB-VRAM-fit stack: `llama3.2:3b` (partial offload OK), `llama3.2:1b`, `nomic-embed-text`
- [ ] Benchmark: `ollama run llama3.2:3b --verbose` — record tok/s in memory core
- [ ] **Whisper:** `faster-whisper` (CTranslate2, CUDA) — `small` model fits 2GB VRAM; wrap as a service or use the `speaches` (ex-faster-whisper-server) container with `--gpus all`
- [ ] **Qdrant:** Docker container, persistent volume
- [ ] **Open WebUI:** Docker container → connect to local Ollama; later federate the Envy's Ollama as a second connection. Create Morph admin + family accounts (mom's devices reach it over Tailscale)

---

## PHASE 4 — CLOUD SERVICES

- [ ] **Nextcloud:** Docker (AIO or compose w/ Postgres) — data directory on the larger volume
- [ ] **Gitea:** Docker container, persistent volume — migrate Pandora repos/backups in
- [ ] Access rule: everything over **Tailscale only** — no ports opened to the internet (sovereignty + attack-surface rule from the 5-pillar security protocol)
- [ ] Document every service: port, volume path, compose file location — one `docker-compose.yml` per service under `/opt/stacks/`

---

## PHASE 5 — BACKUP LAYER (The Archive)

- [ ] CyberPower (post-GPU-donation): boots headless, wired LAN, wake-on-LAN enabled in its BIOS
- [ ] **Restic** on the 5040 → repository on the Archive (SSH/SFTP target)
- [ ] Schedule: cron/systemd-timer — WoL packet wakes Archive → restic backup (Nextcloud data, Gitea, Qdrant snapshots, compose files) → Archive shuts down (95W chip too hungry for 24/7)
- [ ] Verify a restore, not just a backup — pull one file back before calling this done

---

## PHASE 6 — COMMAND-LAYER WIRING

- [ ] MacBook Claude Code → 5040 Ollama via **OLLMCP** (MCP bridge) — local free tier for drafts/summaries/embeddings
- [ ] Pipeline law: Whisper + 3B/8B local models do extraction/drafts free → Anthropic API only for final synthesis
- [ ] When Node 4 (Envy) is built: add its Ollama endpoint to Open WebUI + OLLMCP — fleet tiers: 5040 = instant/small, Envy = fast/medium, API = frontier
- [ ] Update `dii_memory-core.md` with benchmarks + endpoints; update ref card session log

---

## COMPLETION CRITERIA

The build is DONE when: SSH + Tailscale reachable headless · `nvidia-smi` clean · Ollama answering over LAN from the MacBook · Open WebUI serving accounts · Nextcloud + Gitea live · one verified Restic restore from the Archive.

---

*dii_SOP_optiplex-5040-build_v1.md | D.I.I | Pandora OS*
*"The machine serves the sovereign."*
