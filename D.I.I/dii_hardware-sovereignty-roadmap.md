# D.I.I — Hardware Sovereignty Roadmap
## Phased Decentralization | Local AI Infrastructure

**Strategic intent:** Eliminate dependency on big tech API infrastructure by building a sovereign local AI stack as open-source models reach parity with frontier closed models. The AI bubble burst accelerates this — commoditization of frontier capability is inevitable.

---

## CORE PARAMETERS (What Drives Model Performance)

| Parameter | Role | Priority |
|-----------|------|----------|
| **VRAM** | Holds model weights — the hard ceiling | #1 |
| **GPU Architecture** | Compute speed (CUDA cores, tensor cores) | #2 |
| **Memory Bandwidth** | How fast data moves inside the GPU | #3 |
| **System RAM** | CPU inference buffer when no GPU | #4 |
| **NVMe SSD** | Model load speed from disk | #5 |
| **CPU cores + clock** | Orchestration + CPU-only inference | #6 |

**VRAM is the non-negotiable.** Everything else is tuning.

---

## VRAM → MODEL SIZE MAP

| VRAM | Max Model (quantized) | Examples |
|------|----------------------|---------|
| 4 GB | 3B | Phi-3 Mini, Gemma 2B |
| 8 GB | 7B | Llama 3.1 8B, Mistral 7B |
| 12 GB | 13B | Llama 2 13B, CodeLlama 13B |
| 16 GB | 20–30B (Q4) | Mixtral, Llama 3 30B |
| 24 GB | 70B (Q4) | Llama 3.1 70B, Falcon 40B |
| 48 GB | 70B (full) + 130B (Q4) | Frontier-class open models |
| 80 GB+ | 405B+ | Full frontier — sovereign compute |

*Quantization (Q4/Q8) compresses model weights — trades slight quality for massive VRAM savings.*

---

## CURRENT HARDWARE PROFILE

| Component | Spec | Constraint |
|-----------|------|-----------|
| CPU | 1.6 GHz Dual-Core Intel Core i5 | Hard bottleneck — generation: ~1-2 tok/sec |
| RAM | 8 GB 2133 MHz LPDDR3 | Adequate for OS + editor, not inference |
| GPU | None (integrated only) | No VRAM — CPU inference only |
| Storage | Unknown | Upgrade to NVMe if HDD |

**Current capability:** Phi-3 Mini / Gemma 2B max. Anthropic API is the right call now.

---

## PHASED SOVEREIGNTY ROADMAP

### Phase 1 — NOW (Current Machine)
**Strategy:** Use Anthropic API (Claude Sonnet/Opus) for all heavy lifting. Build Pandora OS architecture, agentic layer, file systems. Spend zero on hardware.
- Models: Claude via API
- Tools: Claude Code CLI, VS Code, GitHub
- Cost: Anthropic subscription only

---

### Phase 2 — ENTRY SOVEREIGNTY
**Trigger:** When open-source 13–30B models reach GPT-4 quality (happening now with Llama 4, DeepSeek R2)
**Hardware target:** One of:
- **Mac Mini M4 Pro (24GB unified memory)** — ~$1,300 | Runs 30B quantized cleanly, silent, low power
- **NVIDIA RTX 3090 (24GB VRAM)** — ~$700–900 used | Raw compute king, needs a PC host
- **Mac Mini M4 (16GB)** — ~$800 | Runs 13B well, budget entry

**Capability unlocked:**
- Llama 3.3 70B (Q4), Mistral Large, DeepSeek R1 locally
- Ollama + Open WebUI for local chat interface
- VS Code AI extensions running fully local (Continue.dev)
- No API costs for routine tasks

---

### Phase 3 — STRONG SOVEREIGNTY
**Trigger:** When 70B open models match GPT-4o quality consistently
**Hardware target:** One of:
- **Mac Studio M3 Ultra (192GB unified memory)** — ~$4,000 | Runs 405B quantized, silent, unified stack
- **Custom Linux rig + RTX 4090 (24GB)** — ~$2,500 | Highest raw CUDA performance, modular
- **Dual RTX 3090 (48GB total VRAM)** — ~$1,500 used | Runs 70B full precision

**Capability unlocked:**
- Full 70B models at full precision
- Fine-tuning on Pandora OS data
- Agentic pipelines running 100% local
- Host your own model API endpoint

---

### Phase 4 — FULL DECENTRALIZATION
**Trigger:** Open-source frontier models (405B+) fully released with permissive licensing
**Hardware target:**
- Multi-GPU cluster (4x RTX 4090 = 96GB VRAM) or
- Purpose-built AI server (AMD MI300X, 192GB HBM3)
- Mesh with other sovereign nodes (peer compute network)

**Capability unlocked:**
- Run models equivalent to current GPT-4 / Claude Opus locally
- Host as a sovereign node — offer compute to others
- Full exit from big tech AI infrastructure

---

## OPEN SOURCE MODEL WATCH LIST

Models to track as decentralization accelerates.

| Model | Origin | Strength | License | Status |
|-------|--------|---------|---------|--------|
| Llama 4 | Meta | General frontier | Open weights | Active |
| DeepSeek R2 | China | Reasoning | Open weights | Active |
| Mistral Large | France | Instruction following | Open weights | Active |
| Falcon 2 | UAE | Non-Western origin | Apache 2.0 | Active |
| Gemma 3 | Google | Efficient, small | Open weights | Active |
| Qwen 3 | Alibaba | Multilingual + reasoning | Open weights | Active |
| Command R+ | Cohere | RAG + retrieval | Open weights | Active |

---

## SOVEREIGNTY THESIS

Big tech's AI monopoly rests on three pillars:
1. **Compute** — they own the data centers
2. **Data** — they own the training sets
3. **Distribution** — they own the APIs

Open source breaks all three:
- Compute → consumer GPUs + Apple Silicon close the gap annually
- Data → community datasets, synthetic data, self-supervised learning
- Distribution → local inference, peer networks, sovereign hosting

**The window is 2–4 years.** By 2028, a $2,000 machine will run what costs $20/month via API today. The work Morph is doing now — building Pandora OS, sovereign knowledge architecture, agentic systems — positions ahead of that curve.

---

## OPEN SOURCE REPO INTEGRATION QUEUE

Repos to evaluate for integration with Pandora OS + VS Code agentic layer.
*(Populate as Morph sources repos)*

| Repo | Purpose | Interface | Priority | Status |
|------|---------|-----------|----------|--------|
| — | — | — | — | Pending |

---

*D.I.I Hardware Sovereignty Roadmap | Filed 2026-05-01. Review at each phase trigger.*
