# HARDWARE OPTIONS — FOR FATHER PRESENTATION
**Filed:** D.I.I | **Date:** 2026-06-20 | **Status:** Draft — for email/presentation use
**Purpose:** Establish current hardware situation, lay out upgrade tiers with specs/pricing/ROI, and explain what the upgrade actually enables beyond just "running AI" — local server + data storage capability.

---

## PART 1 — CURRENT HARDWARE SITUATION

### MacBook Air (2019 — daily driver, the actual bottleneck)

| Spec | Detail |
|---|---|
| Model | MacBook Air 8,1 |
| Chip | Intel Core i5, dual-core, Intel UHD 617 (integrated graphics — no dedicated GPU) |
| RAM | 8GB |
| AI capability right now | CPU-only inference, 3B-4B models max, slow |

**What this means concretely:** this machine cannot run any real local AI model. No GPU means no VRAM, which means no model can be GPU-accelerated — everything runs on the CPU alone, which is slow and caps out at small, low-capability models. This is the actual bottleneck, not a vague complaint.

### CyberPower Tower (already owned — separate track, not part of this ask)

| Spec | Detail |
|---|---|
| CPU | AMD FX-4300 Quad-Core (2012-era) |
| GPU | NVIDIA GTX 1050 — 2GB VRAM |
| RAM | 16GB DDR3 |
| Role | Lightweight always-on server — TradingView monitoring + light AI routing tasks. Already owned, $0 cost, being converted into a home server separately from this hardware ask. |

This machine stays in the stack regardless of what happens with the laptop upgrade — it's not competing with this ask, it's a separate, already-funded track.

---

## PART 2 — THE UPGRADE OPTIONS

All three tiers below are the **same chip family (Apple M4 Pro)** in the **same machine (Mac Mini)** — the only thing that changes is how much unified memory it has, which determines the size of AI model it can run.

| Tier | Price | Memory | Model ceiling | What that ceiling means |
|---|---|---|---|---|
| **24GB** | ~$1,300 | 24GB unified | ~30B parameters | Qwen 2.5 32B ("near-GPT-4 level" on benchmarks), DeepSeek R1 Distill 32B, Gemma 3 27B — strong, real capability |
| **48GB** (primary target) | ~$1,929-2,099 (refurb ~$1,700-1,800) | 48GB unified | **70B parameters** | Llama 3.3 70B, DeepSeek R1 70B — frontier-class open-source models, full Q4 quantization |
| **Above 48GB — Mac Studio** | ~$2,800-4,000+ depending on configuration | 64GB-192GB+ unified | 70B at full precision, up to 400B+ quantized | Multi-year-out tier — fine-tuning capability, running multiple large models simultaneously, hosting a model API endpoint for others to query |

**Why 48GB is the target, not 24GB or Mac Studio:** 48GB is the cheapest tier that crosses into the actual frontier-model range (70B). 24GB is real capability but stops one tier short of that. Mac Studio crosses into capability that isn't needed yet — it's the right machine for a later phase (multi-model hosting, fine-tuning), not this one.

---

## PART 3 — PRICE-TO-CAPABILITY AND ROI

| Tier | One-time cost | Equivalent cloud AI cost | Break-even point |
|---|---|---|---|
| 24GB | ~$1,300 | ~$100-200/month for comparable usage | ~7-13 months |
| 48GB | ~$1,929-2,099 | ~$200-500/month for comparable usage | **Under 10 months** |
| Mac Studio (64GB+) | ~$2,800-4,000+ | $500+/month for comparable usage | ~6-8 months, but capability exceeds current need |

After the break-even point, every single inference — every AI query, every model run — costs **$0** going forward, permanently, with no subscription. This is the direct counter to "why not just keep paying for cloud AI": the math crosses over in under a year, and after that the machine is pure savings for as long as it's used.

---

## PART 4 — WHAT THIS UPGRADE ACTUALLY ENABLES: NOT JUST AI, A FULL LOCAL SERVER

This is the part that matters beyond raw AI horsepower. The Mac Mini doesn't just run AI models — once it's live, it becomes a **second always-on node** in the household's infrastructure, alongside the CyberTower, doing two additional things:

**1. Data storage.** The Mac Mini has Thunderbolt 4 ports — fast enough to attach a large external SSD (e.g., 2TB, ~$130) and use it as real storage: every downloaded AI model, every backup of Pandora's work, every piece of decoded research, all stored locally, under direct control, with no monthly cloud storage fee.

**2. Serving other devices on the network.** Once Ollama (the software that runs AI models) is installed on the Mac Mini and set to run as a server, every other device in the house — the MacBook, a phone, anything on the network — can query it directly over the local network. One machine becomes "the brain," and everything else becomes a thin client accessing it. This is the same pattern used by serious self-hosted AI setups: one capable always-on machine, many devices accessing it remotely.

**Put together with the CyberTower:** the household ends up with two complementary always-on nodes — the CyberTower handles trading monitoring and lightweight routing tasks, the Mac Mini handles serious AI compute and fast storage. Neither competes with the other; they're two different tiers of the same sovereign infrastructure, both already owned or being acquired, both running locally, with zero ongoing cloud dependency for the work that matters most.

---

*dii_doc_father-hardware-options-comparison_v1.md | D.I.I | Pandora OS*
