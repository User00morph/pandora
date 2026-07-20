# RAW EXTRACT — Local AI Hardware Setup Clip (Strix Halo / llama.cpp)

## Source Metadata
- **Title:** Unknown (short-form clip, no title metadata — local file)
- **Source file:** fbc59f206cfc4a0c8772cfff1a417395.MP4 (local download, not YouTube)
- **Duration:** 1:48
- **Extracted:** 2026-06-20
- **Extraction method:** Whisper (local, model=base) — no captions available, local file
- **Domain:** tech-decentralization / local-ai-infrastructure
- **Creator context:** References building "medical reasoning" local AI systems — appears to be from a technical/medical-AI-adjacent channel, identity otherwise unconfirmed.

## Transcript
A lot of people have been asking that we get the medical reasoning to work on local AI,
or even how to develop local AI. And if I were in your shoes, here's what I would do to
develop my own local AI system. So the first thing you're going to need is either a GPU
or an integrated GPU CPU system. **The three main options are Strix Halo, an Nvidia graphics
card, or Apple Silicon.** They all have trade-offs. I've found the Strix Halo to be a really
good price point for the value you get from it.

The next thing you're going to need to do is install something like **llama.cpp** — what
llama.cpp does is it allows you to run the local language models on your system. For something
like the Strix Halo, you can get a **Qwen 3.6 35B parameter model to run at about 75 tokens
per second**, which is more than fast enough. And then you're going to download that model,
either from Hugging Face or another repo if you want. And you're going to have to set up your
llama.cpp to function with that in the best way possible. I use **MTP (multi-token prediction)**,
which allows you to get more tokens per second without diminishing accuracy.

And then you connect it to whatever system you want to connect it to. So what llama.cpp does
is it opens up an endpoint that you can use either with Claude Code, Pi, OpenCode, Hermes, or
OpenClaw — dealer's choice, whatever kind of agent harness system you want to use. And then you
start working with it.

So if you're more coding inclined, then the **Qwen 3.6 27B parameter model** does better, but
it runs much slower. So it's all up to what you want. Again, the models that are open-weight
aren't as good as frontier models if you're using them for coding. If you're using them for
language-based tasks or agentic tool use, then they are very good, and I don't notice a
difference, to be honest.

---
*RAW — lightweight D.R.D pass applied below given short, single-source, how-to nature of content.*
