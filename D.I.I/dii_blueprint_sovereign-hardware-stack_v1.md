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

### HP All-in-One 24-ct2024 (Next Gen AI PC)
| Spec | Detail |
|------|--------|
| Model | HP All-in-One 24-ct2024 — Product ID: 85UG7AA#ABA |
| Case | CyberPower C Series tower housing |
| Display | 23.8" built-in screen |
| Processor | AMD Ryzen AI 5 (built-in NPU — Neural Processing Unit) |
| Graphics | Gigabyte AMD Radeon discrete GPU |
| Cooler | DeepCool CPU cooler + Corsair case fans |
| OS | Windows 10 Home / Windows 11 |
| AI Capability | 7B–13B models via Ollama (CPU + NPU + AMD Radeon) |
| Status | In inventory — needs compressed air cleaning before use |

**Immediate action required:** Dust buildup on fans is severe.
Run compressed air through all fans before powering on — thermal throttling
or fan failure risk if used in current condition.

**This is a capable sovereign compute node — already owned.**
The AMD Ryzen AI 5 has a dedicated NPU (AMD XDNA architecture) built into the chip.
The discrete Gigabyte AMD Radeon GPU adds GPU-accelerated inference via ROCm on Linux
or DirectML on Windows — faster than CPU-only inference.

**To confirm:** Exact GPU model (Radeon RX series?), RAM amount, and storage size.
Run `dxdiag` on Windows or open Task Manager → Performance to see these numbers.

**Role in the stack:** Always-on local AI node. Run Ollama server on this machine.
Any device on the local network queries it — one brain, multiple access points.
No cloud. No subscription. Low power draw (~90W max).

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
