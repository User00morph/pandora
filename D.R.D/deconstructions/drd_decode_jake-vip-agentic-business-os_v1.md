# DRD DECODE — Jake VIP Sessions: Agentic Business OS
**Stages 3-4 | Deconstruction + Reconstruction**
**Date:** 2026-06-06
**Source:** Jake VIP Sessions 1, 3, 4, 5, AT5, VIP7 (25 docs + transcript)
**Raw catalog:** `research/tech-decentralization/drd_research_jake-vip-sessions-raw-catalog_2026-06-06.md`
**Deploy targets:** D.I.I (primary) | D.S.E (primary) | D.S.C (secondary) | Pandora OS meta-upgrade

---

## STAGE 3 — DECONSTRUCTION

### SECTION A — D.I.I (Agentic Architecture + Sovereignty)

---

**[ESTABLISHED] FINDING A1 — ICM = Pandora OS Architecture Independently Validated**

The Interpretable Context Methodology (ICM) — folder-structure-as-agent-intelligence — was developed independently by Jake and published as a MIT-licensed paper (Model Workspace Protocol / MWP). Pandora OS uses the same architecture. Two independent practitioners arrived at identical conclusions through different paths. This validates Pandora's core design.

Key ICM principles (cross-verified with Pandora):
- Everything is a file (Unix 1972 / Thompson + Ritchie)
- Small composable tools (Parnas 1972 modularity)
- Folder = agent identity: when a Claude session reads a folder's CLAUDE.md, it becomes that agent
- The folder structure IS the orchestration — not code
- 5 layers: Identity → Routing → Contract → Reference → Working artifacts

**Pandora OS confirmation:** L0-L4 context hygiene system = ICM's 5-layer architecture. UPHQ client's agents spontaneously generated 200+ ICM-style markdown files after reading the paper — proving agents can recognize and reproduce this structure. Morph's OS already operates at this level.

**Confidence:** ESTABLISHED (independent convergence + UPHQ case evidence)

---

**[ESTABLISHED] FINDING A2 — 60/30/10 Architecture Rule**

60% of any AI-augmented workflow is traditional code/files/deterministic logic. 30% is rule-based or database-driven. 10% is where AI judgment lives. Most workflow design errors invert this ratio — putting 90% of the bet on AI judgment where deterministic logic should be.

The "opinion layer" lives in the 30% (rule-based). The AI executes within it. This is where Pandora's skills and workflow files operate.

**Confidence:** PROBABLE (documented through multiple client engagements, logically sound)

---

**[PROBABLE] FINDING A3 — Effort-to-Output Ladder (L1/L2/L3)**

Every automatable workflow sits on a ladder:
- **L1 / Manual hand-off** — human moves data, runs script, uploads file. Zero or minimal engineering. Right for: low volume, judgment required, data quality unreliable, workflow not yet proven stable.
- **L2 / Light scripts + structured prompts** — templates, structured prompts, simple scripts, folder structures. Most real workflows live here. Right for: workflow runs often, steps are stable, describable.
- **L3 / Custom pipelines** — custom code, integrated services, multi-agent orchestration. Justified at scale or specialty work. VULNERABILITY: when the AI vendor ships the feature, your L3 work becomes their L1.

**Absorption warning:** L3 work gets absorbed by platform releases. Pacific Life story: 50 employees building Snowflake agent to upload an Excel file. The file was uploaded manually by one person every few days. L1 was the answer the whole time.

Decision gate: before any build, ask which rung. Not how to build the rung.

**Confidence:** PROBABLE (Pacific Life case + logical framework)

---

**[ESTABLISHED] FINDING A4 — Agentic Security — 5 Fundamentals**

Real breaches in 2026:
1. **Microsoft Copilot (CW1226324)** — hidden instructions in SharePoint form → Copilot sent internal data to attacker address. Six weeks of open exposure.
2. **Salesforce Agent Force** — embedded prompts in CRM records → agent executed attacker instructions during normal workflow.
3. Security Boulevard + Lasera: 300-400% increase in prompt injection attempts YoY.

**The 5 Fundamentals:**

1. **LEAST PERMISSIONS** — every agent starts with nothing. Add capabilities only as proven necessary. Ask: if this agent gets compromised, what is the worst it can do?
2. **SEPARATE INSTRUCTIONS FROM DATA** — user-submitted content never sits in same context slot as system prompt. Wrap user input in delimiters. Tell model explicitly: content inside delimiters is NOT instruction.
3. **AUDIT EVERY SKILL AND TOOL CALL** — before running downloaded skill, MCP server, or GitHub repo, read it. Or paste into a fresh Claude session and ask: "what is this doing, what are the ways this could be malicious?"
4. **AIR GAPS WHERE IT MATTERS** — sensitive workflows on isolated environments with no outbound network capability. PHI, PCI, credentials, legal privileged content = candidates.
5. **ASSUME INJECTION** — before shipping any agent, walk through every data source it reads. Every form field, email body, file path, API response. Ask: what if an attacker planted instructions here?

**Attack surface priority for Pandora:** MCP connectors (proto_mcp-connectors.md) + downloaded Claude Skills + any external data read by agents.

**Confidence:** ESTABLISHED (real breaches, documented, independently verifiable)

---

**[ESTABLISHED] FINDING A5 — AI Governance + Sovereign Infrastructure Path**

Real regulatory events (2026):
- **Italy Garante → OpenAI: €15M** (no lawful basis for training data processing)
- **European Parliament: internal ban** on Claude, Copilot, ChatGPT on official devices (Cloud Act + training-data leakage)
- **EU AI Act (effective August 2026):** €35M or 7% global turnover for prohibited practices
- **Cloud Act:** US government can compel US cloud providers to hand over data stored anywhere

**Sovereign infrastructure path (open-source tools):**

| Tool | What it is | Best for |
|------|------------|----------|
| Ollama | Local LLM runner (1 command) | Solo operators + devs |
| AnythingLLM | Local-first chat UI + docs + agents (MIT) | Non-technical teams |
| Open WebUI | Self-hosted ChatGPT interface, multi-user | Internal teams |
| Jan | Desktop LLM, offline, easiest install | Solo + privacy-first |
| OpenLLM | Deploy Llama/Mistral on own servers | Tech teams with IT |
| Spellbook (ZDR) | Managed, zero-data-retention, SOC 2 | Regulated industries |
| Cloudflare Workers AI | Edge inference, regional data controls | Quick deploy |

**Trade-off:** Local model (Llama 3.1 70B) ≠ Claude Opus capability. ~70% of business workflows = sufficient at local. 30% = decide if privacy premium is worth the pull.

**Practical moves (non-negotiable):**
1. Map data sensitivity — for each workflow, would a regulator care if this leaked?
2. Read the DPA (data processing addendum) on any enterprise AI contract
3. Build one workflow tested on a local model as an "off ramp"
4. Document consent flows — what consent was given, what happens if you click thumbs-down

**Connects to:** D.I.I sovereignty roadmap (hardware decentralization Phase 2)

**Confidence:** ESTABLISHED (law + real fines, independently verifiable)

---

**[PROBABLE] FINDING A6 — One Agent, Many Personalities (Multi-Tenant Architecture)**

The correct architecture for serving multiple clients/contexts from one agent:

**Build one really good agent. Give each tenant their own system prompt + onboarding packet (a folder that defines their voice, tools, data, escalation rules).**

Do NOT build per-tenant runtimes unless three triggers are met:
1. **Revenue gate:** ~$10K MRR per tenant (below = unit economics fight you)
2. **Regulated buyer:** government, defense, PHI healthcare (requires runtime-layer isolation, not just data-layer)
3. **Vendor lock fear:** key customer paying for independence from model provider

**Do NOT fork the codebase.** One codebase, two deploy modes (multi-tenant / per-tenant), toggled by configuration flag. Fork costs a year of maintenance. Config flag costs one week.

**Pandora OS application:** 12 departments = 12 personalities on one Claude operator. Each department's ref card + context file = the "system prompt and onboarding packet" for that personality. This is already the Pandora architecture.

**Confidence:** PROBABLE (logical + Pandora already validates this pattern)

---

**[ESTABLISHED] FINDING A7 — UPHQ Vibe-Coded Software Audit Protocol**

Real client: Australian SaaS (construction contract management). Built with AI agents (OpenClaw). Used Claude + $10-15K API spend over 2 months. 200+ markdown files spontaneously generated by agents after reading ICM paper.

**What was found (pre-audit):**
- 8 major security exploits (4 rated CRITICAL)
- State machine issues (actions allowed that should be blocked)
- Key handling issues
- Tenant isolation failures (logged-in user could pivot to full access)
- Routes accepting privileged commands from any caller
- **Unsupervised cron job** — agents set up GitHub Actions to update code every 2 hours. Had been running for 2 months (360 runs). He never knew.

**Pattern:** Agents build routes and schemas correctly. Agents SKIP runtime validation and permission checks that a human engineer would add by habit. Architecture looks complete. Hardening hasn't landed.

**Phased fix order (tracks where lawsuits land):**
1. Pause cron — stop new code landing on unfixed audit findings
2. Top 4 critical security fixes first
3. Financial code review line-by-line (payments, escrow, claims)
4. Validation + isolation across all routes
5. Load test before scale

**Business framing:** Written audit = sales asset. Enterprise clients: "we used AI to build this, and we had a third party run a full security review. Here's the report." Insurers write cyber liability policies when audit exists. Investors stop flinching.

**The opportunity:** Thousands of businesses vibe-coding software, about to go to market, no idea what's in their codebase. One curious attacker away from catastrophe.

**Confidence:** ESTABLISHED (real engagement, documented, real numbers)

---

**[PROBABLE] FINDING A8 — Multi-Agent = Folder Navigation in Disguise**

The most common over-engineering pattern in current AI work: building LangGraph/CrewAI/AutoGen orchestration for workflows that could be folder navigation.

**Before (heavy):** transcription agent → summarization agent → animation agent. Wired with LangGraph. State management, handoffs, error recovery. 6 weeks to build.

**After (ICM):** one folder with subfolders (raw audio / transcripts / scripts / animations). Each subfolder has CLAUDE.md. Fresh Claude session reads folder, walks through steps. Built in 4 hours.

**When the heavy version is ACTUALLY justified:**
- Autonomous workflow at scale, no human in the loop, real budget pressure on token efficiency
- Strict isolation between steps for security/compliance reasons
- Engineering capacity to maintain orchestration layer through model upgrades
- Cost of being wrong at any step is high enough that explicit handoff contracts pay for themselves

Most workflows fail at least 2 of those tests.

**Confidence:** ESTABLISHED (validated by Pandora OS's own architecture)

---

### SECTION B — D.S.E (Sovereign Business Acquisition + Architecture)

---

**[ESTABLISHED] FINDING B1 — Content-to-Client Pipeline (5 Phases)**

Documented results: Jake, 200 → 48,000 YouTube subscribers (Jan–May 2026, zero ads). 3 enterprise contracts from CTOs watching content. Alex (music studio) found Jake at midnight waiting for a mix to bounce. Eric became a client mid-session watching the pipeline operate.

**5 Phases:**

**Phase 1 — Prove You Can Think** (Week 1-4, $0)
Create 10-15 short videos demonstrating perspective on industry problems. NOT selling. Showing how you think. Content types: common industry mistake + why + fix; tool everyone uses badly + better approach; result you got + exact steps; expensive competitor service + teach it free; controversial opinion + plain reasoning.

**Phase 2 — Let the Algorithm Work** (Week 2-8, $0)
Algorithm matches content to people who care about that topic. Help it by being specific. "AI tips for business" = no one. "3 things luxury cleaners get wrong about pricing" = luxury cleaners. Watch for: "I have this exact problem" comments, DMs asking for help, shares from industry insiders, followers who match ideal client profile. Do not optimize for view count.

**Phase 3 — Create a Place to Go Deeper** (Week 4-8, $0-97/mo)
Community layer where attention can land. Options: free Discord, free Skool, low-cost paid tier ($27-97/mo). Two functions: people get more value + trust your judgment; you hear their real problems in their own words (tells you what to sell).

**Phase 4 — The Inbound Flip** (Week 6-12, $0)
Stop reaching out. Start responding. Signs: DMs asking about services before you mention them, "how do I work with you?" questions, references to specific things you taught. Response = not a sales pitch. "Tell me what's going on. Let me see if I can help."

**Phase 5 — The Offer** (Ongoing)
Three tiers:
- Tier 1: Package (folder structure + prompts + workflow) — $500-2K one-time — solopreneurs
- Tier 2: Service (audit + build + train) — $5K-15K — small-to-mid companies
- Tier 3: Retainer (ongoing + revenue share) — $7,500+/mo — real budgets

**Confidence:** ESTABLISHED (documented results, corroborated by transcript)

---

**[ESTABLISHED] FINDING B2 — Show Your Work (4 Moves)**

**4 moves:**
1. **One channel, posted consistently** — choice of channel matters less than commitment. Pick one.
2. **Post the work as it actually looks** — actual build, folder structure, the mistake you made yesterday, the fix. Not polished. Polished = what competitors post. No one reads it.
3. **Take a position strong enough to repel** — position everyone agrees with attracts no one. Counter-narratives travel.
4. **Stop measuring virality** — watch conversion, not impressions. One CTO finding the right video > 100,000 views from people who won't hire you.

**Book:** "Show Your Work" — Austin Kleon.

**Confidence:** ESTABLISHED (Jake's own documented results corroborate)

---

**[PROBABLE] FINDING B3 — Software in Service vs. SaaS**

**SaaS:** sells the software. Product = the tool. Moat = feature depth + integrations + switching cost. Problem: most SaaS features are becoming standard AI capabilities. Moats thinning.

**Software in Service:** sells the process. Product = method, judgment, operating procedure. Software = rails that deliver the process. Competitor lifting the rails still doesn't have the process. Rails = commodity. Process = durable.

**Works when:** you have a methodology refined over years of specific work, encodable in a structured workflow, customers care about outcome not tool, market for methodology > market for specific tool implementation.

**Doesn't work when:** selling pure technical capability anyone can verify and reproduce, customers buying for tool features specifically, methodology generic enough to be written down in a weekend.

**Pandora OS is Software in Service.** The 12 departments = the methodology. Claude = the rails.

**Confidence:** PROBABLE (compelling thesis, early validation, Pandora validates the model)

---

**[PROBABLE] FINDING B4 — Second-Order Problems Framework**

Most pitches sell the win. Premium goes to people who name the problems that emerge AFTER the win is real.

**Framework in 3 lines:**
> "This capability will work."
> "When it does, here are the 3 problems that emerge."
> "Here are the solutions I'd implement before those problems hit."

**Worked example (Austin + director):** Autonomous coding for SREs. Instead of "this will ship 10x more code" → named the problem: specs are the bottleneck → named the solution: run multiple Claude Code instances in parallel against same spec, pick best output, feed diff into others, iterate. Director's head exploded. Austin answered the second-order problem before the director finished forming it.

**Pilot-first sales move:** Don't pitch enterprise transformation. Pitch transforming a team of 10 better than anyone has, faster than anyone has, for less than anyone has. Then scale. Math: 10 people × 10 hrs/wk saved × 52 wks × $80/hr = $416K/yr. Pilot pays for itself in 30 days.

**Confidence:** PROBABLE (one documented case, logical framework, widely applicable)

---

**[PROBABLE] FINDING B5 — Productionize Your Opinion**

Technical pipelines absorb into the next platform release. Judgment, operating procedures, specific decision trees = durable.

**4-year test:** Before committing serious build effort, ask — will this be a feature in Claude/Codex in 4 years? If yes, build on top of it, not into it. If no, build it.

**Absorbs (4 years):** document summarization, standard API integrations, basic agent orchestration, lead enrichment, scheduling, first-pass content generation, code generation for common patterns, support triage.

**Stays durable:** your deal evaluation decision tree, your client triage method, your hiring pattern recognition, your build vs. buy vs. wait decision framework, your years of domain pattern recognition, the relationships + reach-out order, the way you communicate hard things, your POV on what matters in your field.

**4-step encoding mechanic:**
1. Write it down (ugly first draft, ship anyway)
2. Make it reproducible (folder structure, templates, prompts, decision trees)
3. Teach it to a person first (if a smart human can't follow it, AI can't either — teaching exposes gaps)
4. Encode it (AI layer applies opinion to fresh inputs, you review + refine)

**Jarvis frame:** Jarvis is only useful because Tony Stark has strong opinions. Jarvis without strong opinions = chatbot. Morph's sovereign frameworks = the opinions. Pandora OS = Jarvis.

**Confidence:** PROBABLE (logical, validated by Pandora's own design)

---

**[PROBABLE] FINDING B6 — AI Company vs. Company That Uses AI**

**AI company:** competes on model performance, cost per token, inference speed. Needs to be ahead on technical curve every quarter. Raises venture money to subsidize losses. Dies when the next frontier lab ships the next thing.

**Company that uses AI:** competes on outcome, brand, customer relationship. Model under the hood = interchangeable. If Anthropic raises prices, swap to Google. Customer never knew or cared which model responded. Brand + outcome = the moat.

**Implication:** don't architect so that swapping Claude for Gemini for Llama would break everything. One-day refactor = protected from both cloning and pricing arguments simultaneously.

**Confidence:** PROBABLE (logical, documented cases, widely applicable)

---

**[PROBABLE] FINDING B7 — Framing Layer > Feature Parity**

Bette Nesmith Graham (1956): single mother, secretary at Texas Bank and Trust. Mixed white tempera paint in kitchen blender, put in nail polish bottle, called it "Mistake Out." Sold to Gillette for $47.5M in 1979. Product was paint. Everyone else selling paint. Hers was a productivity tool for typists.

The framing layer (brand, design, positioning, the specific way a product feels) = what a clone can't easily reproduce. A clone can copy features in a weekend. Reproducing the feel takes a year and they still won't get it right.

**Compete on framing, not on the model.** Pandora OS framing: sovereign intelligence operating system, not "AI assistant with folders."

**Confidence:** PROBABLE (Bette Nesmith example = ESTABLISHED; application to AI market = PROBABLE)

---

**[ESTABLISHED] FINDING B8 — Nobody Wants the Drill (Jobs-to-be-done)**

Academic framework (Harvard Business School + Clayton Christensen lineage). Customers hire products to do a job. The job is a transformation, not a feature.

**3 steps:**
1. Name the job — what transformation does the customer actually hire this for?
2. Find the alternatives — what are they doing today to get this job done, even imperfectly?
3. Build the smallest thing that does the job better — not most impressive, smallest

**For transformation domains** (tarot, coaching, spiritual practice, healing, philosophy, ritual): the moment of self-recognition is the value. The product is the ritual. The app is the delivery mechanism. Technology stack = almost irrelevant; pick fastest to ship.

**Soft service reframe:** software inside the service, not service as wrapper around software. AI is the tool the practitioner uses to serve more clients. The service is the product.

**Confidence:** ESTABLISHED (academic framework, widely documented, decades of validation)

---

**[PROBABLE] FINDING B9 — Partnership Playbook**

**2 paths:**

**Path 1 — Unique / first-mover:** needs genuine technical edge or real speed advantage. First-mover windows close in months. Works in niche verticals bigger players haven't prioritized.

**Path 2 — Copy and move markets:** proven model from one region, run it in lower-barrier region (LATAM, international markets outside top 5). Pattern recurs: build → platform buys you.

**Durable margins (AI partnership):**
- **Compliance:** translate AI capabilities into audit-ready documentation. Slow, tedious, relationship-based. Frontier companies won't do at scale. Compounds because each engagement makes the next easier.
- **Workforce enablement:** training humans to use the tools. Distinct from selling tools. Gets more valuable as tools get cheaper — adoption is the bottleneck.

**Barriers:** $100K-500K committed book before Anthropic/OpenAI treat you as serious partner. Formal certification tiers (AWS, Azure, Google Cloud). Exclusive contract clauses (read carefully). Reseller gross margin = 15-25% on pure resale. Money is in attached services.

**Confidence:** PROBABLE (practitioner observations + logical, some documented cases)

---

**[ESTABLISHED] FINDING B10 — Emerge Methodology (300 Sites, 2 Days)**

When to run this:
- Contract size justifies the burn ($30K-60K average, single conversion pays run 10x over)
- Audience is enumerable (named attendee list + company names)
- Personal touch is the differentiator (voice, brand, how you think)
- Can hand the artifact off in person

**4-stage workflow:**
1. **Scrape attendee list** → CSV/markdown, one row per company
2. **Markdown per company** → agent research pass (Gartner style): business model, revenue mechanics, pain points, recent news, leadership signals. Each company = own folder + research markdown
3. **Generate HTML** → one file per company, CSS inline, JavaScript inline. Same structure across all; variable: brand color palette, pain points, relevant case studies, calendar link tied to that company in CRM
4. **Push to GitHub Pages** → GitHub CLI (`gh`) automates publish. Each company = own repo. URL handed to prospect in person.

**Failure modes (documented):**
- Google flagged some sites as phishing (had logo replicas) → use brand-adjacent colors, not actual logos; or host on own domain
- Token overrun (estimated 3M, came in at 7M) → budget 2-3x estimate
- Site without conversation = just a website → script: "I built you a site. You can keep it whether or not we work together. I wanted to show you what we'd do in the first 30 days."

**Confidence:** ESTABLISHED (Jake ran it, 300 sites, documented failures)

---

**[PROBABLE] FINDING B11 — Reusable Workflows: 3-Layer Portability**

**Layer A — Platform-level reference:** files that apply across every project on the same stack. Voice and style rules, naming conventions, default folder layout, logging setup. One shared folder. All projects reference it. Edit once = update everywhere.

**Layer B — Domain-level reference:** files for a cluster of projects but not all. Group by domain. Projects in same domain pull from same domain folder.

**Layer C — Workspace-level reference:** project-specific files. Don't travel. Die with the project.

**Versioning:** every platform-level file carries version number + short changelog at top. Workspaces pin to a version OR read latest. Breaking change = changelog tells you what to check.

**Pandora OS application:** L0-L2 context files = Layer A (platform). Department context files = Layer B (domain). Working artifacts in `research/` = Layer C (workspace).

**Confidence:** PROBABLE (logical, directly maps to Pandora's existing architecture)

---

### SECTION C — PANDORA OS META-UPGRADE

---

**[ESTABLISHED] META A — Pandora OS IS an ICM**

Pandora OS and ICM arrived at identical architecture independently. Key terminological mappings:

| ICM term | Pandora OS equivalent |
|----------|----------------------|
| CLAUDE.md | pandora.md + CLAUDE.md + ref_[dept].md |
| 5 ICM layers | L0-L4 context hygiene system |
| Folder = agent identity | Department folder = department agent |
| Platform-level reference | shared/skills/ + shared/protocols/ |
| Domain-level reference | D.*/context.md + D.*/workflow/ |
| Workspace-level reference | D.*/research/ + working artifacts |
| ICM developer | Morph (architect) |
| ICM operator | Claude (executor) |
| Short-lived ICM | Session protocol (archive artifacts, don't accumulate state) |

**Upgrade implication:** Pandora OS should explicitly acknowledge this convergence. The architecture is validated. Jake's published ICM research (MIT-licensed MWP paper on GitHub) provides external documentation for what Pandora already does.

---

**[PROBABLE] META B — Short-Lived ICM Principle → Already in Pandora**

Long-lived ICMs accumulate complexity. Drift hides in corners. Same pattern as a Claude chat muddled after 50 turns. Fix: shorter sessions with cleaner restart boundaries.

Pandora already has this in session log protocol (DONE / DECIDED / NEXT). Reinforce: working artifacts go to `research/` after sessions. Templates and skills are the only things that travel forward. State does not.

---

## STAGE 4 — RECONSTRUCTION

### Frameworks Extracted for Deployment

**Deploy to D.I.I:**
- Agentic Security 5-Pillar Protocol (A4)
- Effort-to-Output Ladder (A3)
- AI Governance Sovereign Infrastructure Path (A5)
- Multi-Agent = Folder Navigation (A8)
- One Agent Many Personalities (A6)
- UPHQ Audit Protocol (A7)
- ICM validation + 60/30/10 (A1 + A2)

**Deploy to D.S.E:**
- Content-to-Client Pipeline 5 Phases (B1)
- Show Your Work 4 Moves (B2)
- Software in Service vs. SaaS (B3)
- Second-Order Problems Framework + Pilot-First (B4)
- Productionize Your Opinion (B5)
- Framing Layer doctrine (B7)
- Jobs-to-be-done / Nobody Wants the Drill (B8)
- Emerge Methodology (B10)

**Deploy to D.S.C:**
- Effort-to-Output Ladder (A3)
- 60/30/10 rule (A2)
- Jobs-to-be-done lens for new projects (B8)
- When to Build Software: 4-stage sequence (A1-adjacent)

**Deploy to Pandora OS meta (CLAUDE.md / pandora.md):**
- ICM validation + nomenclature alignment (META A)
- Short-lived ICM principle reinforcement (META B)

---

### Confidence Summary

| Tier | Findings |
|------|----------|
| ESTABLISHED | A1, A4, A5, A7, A8, B1, B2, B8, B10 |
| PROBABLE | A2, A3, A6, B3, B4, B5, B6, B7, B9, B11, META A, META B |
| HELD | EdubaWare (in development), YC % (verify independently) |

---

**Stage 5 briefs:** `drd_brief_dii_agentic-framework-icm-security_v1.md` | `drd_brief_dse_sovereign-business-pipeline-stack_v1.md`
