# SOVEREIGN HARDWARE STACK — PRESENTATION BRIEF
**Filed:** D.I.I — Infinite Intelligence / Techgnosis
**Prepared for:** Father presentation
**Date:** 2026-05-20
**Status:** Active

---

## THE CORE ARGUMENT

Every device connected to a cloud service is a dependency on an institution.
Every model running locally is compute you own.
Every piece of sovereign hardware is infrastructure that cannot be revoked.

This brief lays out the hardware roadmap to move our compute stack
toward full sovereignty — starting with what we have, ending with
what unlocks the full local AI capability tier.

---

## PRESENTATION SUMMARY — THE FIVE POINTS

**1. The actual bottleneck, quantified:**

| Component | Current (MacBook Air 2019) | What's missing |
|---|---|---|
| RAM | 8GB | Models need to fit fully in memory to run at all |
| GPU | None — integrated only | No VRAM = no GPU-accelerated inference |
| Practical ceiling | 3B–4B models, CPU-only, slow | Real local AI work needs 30B+ |

**2. Mac Mini vs. NVIDIA — resolved, not an open debate.** A real counter-argument exists: NVIDIA GPU rigs (RTX 5090, ~$8,000–10,000 full build) can beat Apple unified memory on raw speed-per-dollar. The recommendation still stands at **Mac Mini M4 Pro 48GB (~$1,929–2,099)**:
- The NVIDIA path costs 4–5x more for a speed advantage that matters most running many parallel model instances simultaneously — not this household's use case
- It requires building and maintaining a full PC (PSU, cooling, drivers) — a single point of failure for a shared resource, not a hobby rig
- Silent, low power draw — running 24/7 in a home, not a server room
- The ~$6–8K cost gap is better spent on the enterprise build-out itself (LLC formation, operating runway) than marginal inference speed

**3. What the price actually buys — unified memory:** traditional computers split CPU/GPU memory — models load into RAM then transfer to VRAM, with a hard size ceiling. On the M4 Pro, RAM and GPU memory are the *same pool*. The full 48GB is available to a model with no transfer overhead — this is what lets one consumer machine in this price range run **70B-parameter open-source models**, the frontier-adjacent tier, fully offline, permanently, no monthly fee.

**4. Cost-of-ownership math:** the equivalent compute via cloud API credits runs $200–500/month depending on usage. The machine pays for itself in **under 10 months**, then every inference afterward is free.

**5. The redirected-labor argument:** with this hardware live, development work currently sent overseas can be done locally instead — with direct oversight, faster iteration, and someone who understands the architecture underneath the tools, not just surface-level usage.

---

## SECTION 1 — CURRENT HARDWARE INVENTORY

### MacBook Air (2019 — Intel)
| Spec | Detail |
|------|--------|
| Model | MacBook Air 8,1 |
| Chip | Intel Core i5 (dual-core, Intel UHD 617) |
| RAM | 8GB |
| AI Capability | CPU-only inference — limited to 3B–4B models |
| Status | Active daily driver |

**What it can run locally (via Ollama) RIGHT NOW:**
| Model | Size | Speed | Use Case |
|-------|------|-------|----------|
| Llama 3.2 3B | ~2GB | Fast | General chat, quick tasks |
| Phi-3.5 Mini 3.8B | ~2.3GB | Fast | Reasoning, coding assistance |
| Gemma 2 2B | ~1.5GB | Very fast | Lightweight summarization |
| Mistral 7B Q4 | ~4.5GB | Slow | Edge of what this machine handles |

7B models and above are impractical on this machine — too slow for real use.
This machine remains the portable layer. The Mac Mini becomes the sovereign compute core.

---

### CyberPower Tower — Node 2 (Lightweight Always-On)
| Spec | Detail |
|------|--------|
| Motherboard | Gigabyte GA-78LMT-S2 (AM3+) |
| CPU | AMD FX-4300 Quad-Core @ ~3.8GHz (Bulldozer, 2012-era) |
| GPU | NVIDIA GeForce GTX 1050 — **2GB VRAM** (CUDA capable) |
| RAM | 16GB DDR3 |
| Cooler | DeepCool CPU cooler + Corsair case fans |
| OS | Windows 10 Home 64-bit (Build 19045) — fresh wipe |
| AI Capability | 1B–2B models GPU-accelerated | 7B CPU-only (slow) |
| Status | **Cleaned + wiped — ready to activate** |
| Confirmed via | dxdiag screenshots — 2026-06-09 |

**Role in the stack — recalibrated:**
The GTX 1050's 2GB VRAM is the hard ceiling. GPU-accelerated inference is limited to
1B–2B models. 7B+ models would run CPU-only on the FX-4300 — too slow for real use.

This machine is a **lightweight always-on utility node**, not a primary inference node.
Best use: Auset's fast routing tasks, summarization, classification, lightweight
automation — tasks where 1B–2B model quality is sufficient and speed matters.
For reasoning depth, Claude API remains primary until Mac Mini M4 Pro arrives.

**What runs well (GPU-accelerated):**
| Model | VRAM | Speed |
|-------|------|-------|
| Llama 3.2 1B Q4 | ~1GB | Fast |
| Gemma 2B Q4 | ~1.5GB | Good |
| Phi-3 Mini 3.8B Q4 | ~2.3GB | Offloads to CPU — marginal |

**Mac Mini M4 Pro 48GB remains the primary acquisition target.**
This node handles lightweight/always-on load. Mac Mini handles 70B frontier inference.

---

### Node 2 — SERVER BUILD-OUT PLAN
**Filed:** 2026-06-20 | **Status:** Planned — not yet executed

**Goal:** Convert the CyberPower Tower from a desktop machine into a true always-on server — headless, network-reachable, reliable. This also doubles as the working prototype for the self-hosted private infrastructure service being pitched to D.S.E clients (Dr. Nwosu engagement).

**OS decision — RESOLVED via D.R.D pass 2026-06-20 (see `drd_research_proxmox-home-lab-clip_raw-extract.md`):**

The Windows-vs-Linux framing was a false binary. **Proxmox VE** — a free, Type-1 hypervisor — resolves it: install Proxmox as the base layer, then run Windows (for TradingView Desktop) and Linux containers (for Ollama, Open WebUI, n8n) as separate isolated VMs/containers on the same physical tower simultaneously. No either/or tradeoff.

| Layer | Role |
|-------|------|
| Proxmox VE (bare metal) | Type-1 hypervisor, $0 licensing, community edition |
| Windows VM | TradingView Desktop, LM Studio GUI |
| Linux container/VM (LXC or KVM) | Ollama (headless server), Open WebUI, n8n |
| Built-in backup (vzdump) | One-click backup of the whole stack — confirmed Proxmox feature |

**Tradeoff to confirm before committing:** virtualization overhead. The FX-4300/GTX 1050 are already the hard compute ceiling — running multiple VMs on top of already-limited hardware costs some headroom versus running one OS bare-metal. GPU passthrough to a VM (needed for Ollama to use the GTX 1050 inside a container) also needs verification — not all consumer GPUs/motherboards support clean passthrough. **Action before executing:** confirm GPU passthrough viability on the Gigabyte GA-78LMT-S2 board before wiping to Proxmox.

**Required additions for server-grade reliability:**
- [ ] **UPS (battery backup)** — currently missing. A server that loses power mid-write or reboots randomly isn't reliable. Acquire before going always-on.
- [ ] **Static local IP** (DHCP reservation on router) — so other devices on the network can find it consistently
- [ ] **Remote access layer** — **updated 2026-06-20 via D.R.D pass** (`drd_decode_tech-playlist-tier3-home-server-hardware_v1.md`): **Tailscale** is the better fit over WireGuard-from-scratch or playit.gg — free, self-hosted-spirit (built on WireGuard under the hood), general-purpose (not gaming-specific like playit.gg), and explicitly avoids opening ports to the internet
- [ ] **Headless operation confirmed** — SSH (Linux) or RDP (Windows) access verified before disconnecting monitor for daily use
- [x] **CasaOS vs. Proxmox — RESOLVED 2026-06-20: Proxmox.** TradingView Desktop is confirmed to run on the tower, which requires a Windows VM — CasaOS (bare-metal, no virtualization) can't support that. Proxmox is the final call.

**GPU passthrough — concrete steps (logged 2026-06-20, sourced from current Proxmox documentation/community):**

Key clarification: TradingView (Windows VM) needs **no GPU access at all** — only the Ollama/AI workload does. This means GPU sharing only needs to target the **Linux LXC container**, not the Windows VM — LXC-based GPU sharing is simpler than full VM passthrough, and multiple LXC containers can share the GPU concurrently (a VM would get exclusive lock on it instead).

**The real risk:** IOMMU support needs both CPU and motherboard chipset support. The FX-4300 (Piledriver/Vishera) is on the supported side of AMD's "Bulldozer-and-newer" cutoff for AMD-Vi — but the Gigabyte GA-78LMT-S2 is a budget AM3+ board from that era, and budget boards from this generation frequently don't expose IOMMU as a BIOS option even when the CPU supports it. **This is the actual unknown, not the CPU.**

1. **Check BIOS for an AMD-Vi / IOMMU option** (do this FIRST, before anything else — determines if the rest is possible)
2. If present, enable it
3. After Proxmox install: add `amd_iommu=on iommu=pt` to `GRUB_CMDLINE_LINUX_DEFAULT`, run `update-grub`, reboot
4. Verify: `dmesg | grep -i iommu` + check `/sys/kernel/iommu_groups/*/devices/` for the GTX 1050 sitting in a clean group by itself
5. Install NVIDIA driver on the **Proxmox host**, then expose `/dev/nvidia*` into the LXC container (Resources tab or `/etc/pve/lxc/<id>.conf`) — no VM-level passthrough needed for this
6. Windows VM (TradingView): no GPU config needed — standard virtual display is sufficient

**If BIOS has no IOMMU option at all:** GPU passthrough to any container/VM is impossible. Fallback: run Ollama directly on the Proxmox host (not virtualized) to retain GPU access, or accept CPU-only inference in the container. Given the GTX 1050's 2GB VRAM already caps things at 1B-2B models, CPU-only isn't a major capability loss — the tower stays a lightweight utility node regardless of outcome.

**What it serves once live:**
- Ollama API endpoint — other devices (MacBook, phone) query it over the local network
- Open WebUI — private ChatGPT-style frontend, accessible network-wide
- File storage / NAS role — Pandora OS backups, decoded research archive
- n8n (self-hosted automation) — replaces Zapier MCP dependency, keeps the sovereignty thesis intact
- TradingView Desktop (if Windows retained) — 24/7 chart monitoring for STIS, independent of AI workload

**⚠️ HIPAA caveat — directly relevant to the Dr. Nwosu engagement:**
The Dr. Nwosu outreach email promises her practice "full HIPAA-compliant private data sovereignty." This CyberTower — a 2012-era consumer tower in a residence — does **not** meet HIPAA technical safeguards as a server (encryption at rest, access controls, audit logging, infrastructure-level compliance). It is the correct R&D/prototype rig to develop and test the self-hosting methodology on. If the Dr. Nwosu engagement reaches the point of actually hosting patient data, that requires its own dedicated, compliant deployment — not this specific box. Do not represent this tower as the client-facing HIPAA solution.

---

### Dell USB-C DisplayLink Dock (4K)
| Spec | Detail |
|------|--------|
| Brand | Dell |
| Connectivity | USB-C |
| Display | DisplayLink 4K Plug and Display |
| Ports | 3x USB-A, audio jack |
| Status | In inventory — ready to deploy |

**Use:** Connects MacBook Air to external displays now.
Once Mac Mini arrives — extends its port options for multi-display or USB routing.

---

## SECTION 2 — RECOMMENDED ACQUISITION

**Tension resolved 2026-06-20 (see `drd_decode_tech-playlist-tier3-home-server-hardware_v1.md`):** an experienced multi-machine local-AI operator argues NVIDIA GPU rigs (e.g., RTX 5090, ~$8,000-10,000 full build) beat Apple unified memory on raw stability and speed-per-dollar. This is real, opinion-tier (not a controlled benchmark), from someone running comparable infrastructure — but it doesn't change the recommendation for this household's use case. **Decision: Mac Mini M4 Pro 48GB stands.** Reasoning:
- The NVIDIA path is ~4-5x the cost ($8K-10K vs ~$2K) for a speed advantage that matters most for the operator's specific workload (running 4+ parallel agentic model instances simultaneously) — not the Pandora use case (one primary local inference node)
- The NVIDIA path requires building and maintaining a full PC (PSU, cooling, drivers, Windows/Linux config) — added complexity and a single point of failure for a household-shared resource, not a personal hobby rig
- Mac Mini's silence and low power draw matter for a machine running 24/7 in a home, not a dedicated server room
- The cost gap (~$6-8K) is capital better spent elsewhere in the enterprise build-out (LLC formation, retainer runway, business credit) than on marginal inference speed
This is the version to present as a settled recommendation, not an open debate.

**Internal tracking note — not part of father presentation:** **Olares One** (Kickstarter, ~$2,999, shipping ~Jan 2026) is the first found appliance combining self-hosting OS (Kubernetes-based, NAS-like) AND serious local AI hardware (RTX 5090 Mobile 24GB VRAM, 96GB RAM) in one box — the "combined NAS+AI" category previously concluded not to exist as a single product. Pre-production/crowdfunding risk — track, don't buy yet. Its software (Olares OS, AGPL 3.0 open source) can be tested for free on existing hardware (e.g., the CyberTower) before deciding whether the appliance itself is worth it.

**Model selection note for whatever hardware is acquired:** prioritize MoE-architecture models (e.g., Qwen 3.6 35B-class, ~3B active params) over same-size dense models — one operator's benchmarking showed ~70 tok/s vs. ~10 tok/s for a dense model of similar total size, on identical hardware. This affects which models to pull first once any local rig is live, independent of which hardware path is chosen.

### Mac Mini M4 Pro — 48GB Unified Memory

This is the sovereign compute core. One machine. No GPU dependency.
No cloud required. Every major open-source model runs locally.

| Spec | Detail |
|------|--------|
| Chip | Apple M4 Pro |
| CPU | 14-core (10 performance + 4 efficiency) |
| GPU | 20-core Apple GPU |
| Neural Engine | 16-core |
| Memory | 48GB unified memory |
| Memory Bandwidth | 273 GB/s |
| Storage | 512GB SSD (upgradeable at purchase to 1TB/2TB) |
| Ports | 3x Thunderbolt 4, 2x USB-A, HDMI 2.1, Ethernet, SD card |

**Why unified memory matters for AI:**
Traditional computers split CPU and GPU memory. Models load into RAM
then transfer to VRAM — slow, with a size ceiling.
On M4 Pro, RAM and GPU memory are the same pool.
48GB is available to the model in full. No transfer overhead.
This is architecturally closer to how the brain routes information —
unified, not fragmented across buses.

---

## SECTION 3 — WHAT THE MAC MINI M4 PRO 48GB RUNS LOCALLY

All models run through **Ollama** — open source, no cloud, no subscription.
Models are downloaded once and run entirely offline.

| Model | Parameters | RAM Required | Capability Tier |
|-------|-----------|-------------|----------------|
| Llama 3.2 3B | 3B | ~2GB | Fast assistant, lightweight tasks |
| Phi-4 Mini | 3.8B | ~2.3GB | Strong reasoning in small package |
| Gemma 3 4B | 4B | ~2.5GB | Google's compact sovereign model |
| Llama 3.1 8B | 8B | ~5GB | Strong general intelligence |
| Mistral 7B | 7B | ~4.5GB | Fast, efficient, excellent instruction |
| Gemma 3 12B | 12B | ~7GB | Mid-tier with strong multilingual |
| Phi-4 14B | 14B | ~9GB | Microsoft's best small reasoning model |
| Qwen 2.5 14B | 14B | ~9GB | Strong coder, multilingual |
| DeepSeek R1 Distill 14B | 14B | ~9GB | Deep reasoning, math, logic |
| Gemma 3 27B | 27B | ~16GB | High-quality large model |
| Qwen 2.5 32B | 32B | ~20GB | Near-GPT-4 level on benchmarks |
| DeepSeek R1 Distill 32B | 32B | ~20GB | Elite local reasoning model |
| **Llama 3.3 70B** | **70B** | **~40GB** | **Flagship — near frontier quality** |
| **DeepSeek R1 70B** | **70B** | **~40GB** | **Best local reasoning model available** |

The 70B models are the sovereign frontier. At 48GB unified memory,
the M4 Pro is one of the only consumer machines that can run them at full Q4 quantization.
This is capability that costs $20–200/month in API fees — running free, locally, permanently.

**Claude (this instance)** continues to run via API for complex synthesis tasks.
The local models handle: drafts, research passes, code generation, summarization,
classification, and any task where data sovereignty is required
(no content leaves the device).

---

## SECTION 4 — SOVEREIGN DECENTRALIZATION STRATEGY

```
INSTITUTIONAL LAYER (what we're reducing dependency on)
├── OpenAI API (GPT-4 / ChatGPT)     → replaced by local 70B models
├── Google Cloud / Gemini API         → replaced by local Gemma 3 27B/70B
├── Anthropic API (Claude)            → retained for frontier synthesis only
└── Any cloud compute subscription    → replaced by owned hardware

SOVEREIGN LAYER (what we already own + what we're adding)
├── Mac Mini M4 Pro 48GB       [ACQUIRE] → Primary compute core — 70B models
├── MacBook Air 2019 8GB       [OWNED]   → Portable node — API + small models
├── HP All-in-One 24-ct2024    [OWNED]   → Always-on node — 7B–13B via Ryzen AI
├── Dell USB-C DisplayLink Dock [OWNED]  → Peripheral and display routing hub
└── Local ethernet network               → All nodes query Mac Mini Ollama server
```

**Phase 1 — NOW (before Mac Mini):**
Install Ollama on the HP All-in-One (Windows 11 — one download, one install).
Pull Llama 3.1 8B and Phi-4 14B. Sovereign local AI is operational today.
Clean the CyberPower PC fans. Assess CPU/RAM/PSU for upgrade viability.

**Phase 2 — Mac Mini acquisition:**
Install Ollama on Mac Mini. Pull Llama 3.3 70B + DeepSeek R1 32B.
Run Ollama as a server (`OLLAMA_HOST=0.0.0.0 ollama serve`).
Every device on the local network queries the Mac Mini — one brain, many access points.
HP All-in-One stays as the backup/secondary node running lighter models.

**Phase 3 — CyberPower upgrade (if viable):**
Confirm PCIe slot open + PSU wattage sufficient (need 450W+ for RTX 4060 Ti).
Add RTX 4060 Ti 16GB (~$380). Now a Windows CUDA node running 13B models.
Three sovereign inference nodes. Zero cloud dependency for routine AI work.

---

## SECTION 5 — PRICING & SOURCING

### Mac Mini M4 Pro 48GB / 1TB

| Vendor | Price | Notes |
|--------|-------|-------|
| Apple (retail) | $2,099 | MSRP — baseline |
| B&H Photo | ~$1,929–1,999 | Authorized reseller — currently $100–170 off |
| Apple Refurbished Store | ~$1,700–1,800 | Certified refurb — 1-year warranty, same return policy |
| Apple Education | ~10–15% off retail | Requires .edu email or student/faculty verification |
| Adorama | ~$1,999 | Authorized — competitive with B&H |

**Recommended path:**
1. Check Apple Refurbished Store first — highest savings, same quality guarantee
2. If refurb is out of stock (inventory moves fast), buy from B&H Photo
3. If eligible for education pricing, use Apple Education store directly

**Fallback gate — logged 2026-06-20:** if combined funding (Dr. Nwosu retainer + father's contribution) reaches ~$1,300 but not the full ~$1,929-2,099, buy the **Mac Mini M4 Pro 24GB (~$1,300)** now rather than waiting. Same chip, same machine, lower memory ceiling — caps at ~30B models (Qwen 2.5 32B "near-GPT-4 level," DeepSeek R1 Distill 32B, Gemma 3 27B) instead of the 70B frontier tier. Real capability, not a consolation prize. Upgrade path later: sell/repurpose the 24GB unit when funding allows the 48GB (or higher) tier, rather than treating 24GB as a permanent ceiling.

**Storage note:** 512GB base is sufficient if an external SSD is added.
A 2TB Samsung T9 NVMe external (~$130) stores all downloaded models
and keeps the internal SSD clean for the OS and active files.

---

## TOTAL SOVEREIGN STACK COST (ESTIMATED)

| Item | Cost |
|------|------|
| Mac Mini M4 Pro 48GB / 512GB (refurb or B&H) | ~$1,929 |
| 2TB External SSD for model storage (optional) | ~$130 |
| USB-C cable for Dell dock → Mac Mini | ~$15 |
| **Total** | **~$2,074** |

Already owned and deployable: Dell dock, HP display, CyberPower PC, MacBook Air.

---

## CLOSING ARGUMENT

The cloud is convenient. It is not sovereign.
Every API call is a record. Every subscription is a dependency.
Every model that runs locally is compute that belongs to us —
permanently, without a monthly bill, without data exposure,
without institutional permission.

The Mac Mini M4 Pro 48GB at $2,000 is not a consumer purchase.
It is infrastructure. The equivalent compute in cloud credits
costs $200–500/month depending on model and usage.
The machine pays for itself within 10 months.
After that, every inference is free.

This is the foundation of the sovereign computing layer.

---

*dii_blueprint_sovereign-hardware-stack_v1.md | D.I.I | Pandora OS*
*"Technology fused with divine stewardship — the machine serves the sovereign."*
