# RAW EXTRACT — Context Engineering in 29 Minutes: Complete Course

## Source Metadata
- **Title:** Context Engineering in 29 Minutes: Complete Course
- **URL:** https://www.youtube.com/watch?v=-h9VVJIqtvA
- **Tier:** 1
- **Extracted:** 2026-06-09
- **Domain:** tech-decentralization / agentic-systems
- **Playlist:** Pandora Tech Playlist — PLWKcfqsabTLUxfC7OFs7UZ8EIJ6hjY_M8
- **Word Count:** ~6782

## Transcript (timestamped)

[00:00:00] If you've been building AI agents,
[00:00:01] you've probably noticed something. Your
[00:00:03] agent works fine for the first few
[00:00:05] steps. It picks the right tools, reasons
[00:00:07] clearly, and stays on track. But
[00:00:08] somewhere around step 15 or 20, it
[00:00:11] starts getting a little sloppy. It
[00:00:12] forgets what you asked for, calls tools
[00:00:14] that don't make sense, or starts
[00:00:16] producing low-quality outputs. And most
[00:00:18] people's first assumption is that the
[00:00:19] model is the problem, but it's usually
[00:00:21] not. It's more often what the model is
[00:00:23] seeing. Organizing what the model sees
[00:00:25] is called context engineering, and it's
[00:00:27] quickly becoming one of the most
[00:00:29] important skills for anyone working in
[00:00:30] this space. I'm Marina,
[00:00:32] >> [music]
[00:00:32] >> a senior applied scientist at Twitch
[00:00:33] working on Gen AI. I went through dozens
[00:00:35] of sources for this video, engineering
[00:00:37] blogs, talks from conferences, academic
[00:00:39] papers, and practitioner reports, and
[00:00:41] distilled all of the best practices I
[00:00:43] can find into this one video. Here's
[00:00:45] what we'll cover. First, what context
[00:00:47] engineering is and why agents
[00:00:48] specifically need it. Then, the four
[00:00:50] core strategies that you need to know.
[00:00:52] After that, the ways agents fail when
[00:00:54] context goes wrong and how to prevent
[00:00:55] it. And finally, we'll compare how
[00:00:57] platforms like Claude Code, ChatGPT, and
[00:00:59] Manifold each approach this differently.
[00:01:01] [music] All right, let's start by
[00:01:02] actually defining what we're talking
[00:01:04] about. You've definitely heard of prompt
[00:01:06] engineering. That's the skill of writing
[00:01:07] good instructions for an LLM, like
[00:01:09] phrasing things clearly, giving good
[00:01:11] examples, and telling the model what
[00:01:12] role to play. And that works great when
[00:01:14] you're having a conversation with
[00:01:15] ChatGPT. But when you move from chatbots
[00:01:18] to agents, prompt engineering stops
[00:01:20] being enough. And the reason is pretty
[00:01:21] simple. An agent doesn't just answer one
[00:01:23] question. It takes actions like browsing
[00:01:25] the web, calling APIs, writing code, and
[00:01:28] running commands.
[00:01:29] >> [music]
[00:01:29] >> And it does all of this autonomously,
[00:01:31] step after step, sometimes for dozens of
[00:01:33] steps. Every single one of those steps
[00:01:35] produces output that gets added to the
[00:01:37] model's context. And that context is
[00:01:39] finite. So, context engineering is the
[00:01:40] discipline of designing the entire
[00:01:42] information system around the model, not
[00:01:44] just that initial instruction, but
[00:01:46] everything the model sees at every step.
[00:01:48] The system prompt, tool definitions, the
[00:01:50] results from previous calls,
[00:01:51] conversation history, and more.
[00:01:53] Anthropic's engineering team defines it
[00:01:55] like this. Context is the set of tokens
[00:01:57] included when you sample from an LLM,
[00:01:59] and context engineering is optimizing
[00:02:01] the utility of those tokens to
[00:02:02] consistently achieve a desired outcome.
[00:02:05] So, basically, it's making sure your
[00:02:06] agency is the right information in the
[00:02:08] right format at the right time.
[00:02:09] Anthropic actually describes context
[00:02:11] engineering as the natural progression
[00:02:12] of prompt engineering. It includes
[00:02:14] everything prompt engineering does, like
[00:02:16] clear instructions, good examples, and
[00:02:18] structured formatting, but it adds a
[00:02:20] whole layer on top, managing tools,
[00:02:22] external data, message history, memory
[00:02:24] systems, and dynamic state. You can
[00:02:26] think of prompt engineering as a subset
[00:02:28] of context engineering. Getting good at
[00:02:29] context engineering matters right now
[00:02:31] because agent adoption is accelerating
[00:02:33] really, really fast. Gartner projects
[00:02:35] that 40% of enterprise applications will
[00:02:37] integrate task-specific AI agents by the
[00:02:40] end of 2026, up from less than 5% in
[00:02:42] 2025. Teams that figure out context
[00:02:44] engineering are the ones whose agents
[00:02:46] will actually work reliably. This is
[00:02:47] because agents move us from static
[00:02:49] prompts and rag pipelines to a dynamic
[00:02:51] system. Now, every tool call, retrieved
[00:02:53] document, and decision the agent makes
[00:02:55] gets packed into a context window that's
[00:02:57] filling up with operations the user
[00:02:59] never explicitly asked for. And context
[00:03:01] has a fixed size, which is a problem if
[00:03:03] it's filling up with a bunch of random
[00:03:05] stuff. LangChain has a nice analogy for
[00:03:07] this. Think of an LLM as a new kind of
[00:03:09] operating system. The model itself is
[00:03:11] the CPU. It does the [music] thinking.
[00:03:13] And the context window is RAM, the
[00:03:15] working memory where everything the
[00:03:16] model can currently see and reason about
[00:03:18] lives. Just like your computer slows
[00:03:20] down when RAM fills up, your agent's
[00:03:22] reasoning degrades when your context
[00:03:23] window gets crowded. This is called
[00:03:25] context drop. Chroma published a really
[00:03:27] important study where they evaluated 18
[00:03:29] frontier models, GPT-4.1, Claude-4,
[00:03:32] Gemini-2.5, Gwen-3, and others. What
[00:03:35] they found is that every single model's
[00:03:37] performance degrades as input length
[00:03:39] increases, [music]
[00:03:40] even well below the stated context
[00:03:42] window limit. A model with a 200K token
[00:03:44] window might start showing significant
[00:03:46] degradation at 50K tokens. The decline
[00:03:48] is continuous, not like a sudden cliff.
[00:03:50] Anthropic also talks about this in their
[00:03:51] engineering blog, confirming that
[00:03:53] context degradation is a gradient.
[00:03:55] [music] The technical reason has to do
[00:03:57] with how transformers work. Every token
[00:03:59] attends to every [music] other token,
[00:04:01] creating n squared pairwise
[00:04:03] relationships. As the context grows, the
[00:04:05] model's ability to capture all those
[00:04:07] relationships get stretched thinner
[00:04:08] [music] and thinner. It's like asking a
[00:04:10] person to keep track of an increasingly
[00:04:12] large number of things simultaneously.
[00:04:14] At some point stuff gets dropped.
[00:04:15] There's also a well-studied phenomenon
[00:04:17] called lost in the middle. A research
[00:04:18] team found that LLMs exhibit a U-shaped
[00:04:21] attention curve. They remember
[00:04:22] information at the beginning of the
[00:04:24] context well and at the end well, but
[00:04:26] information in the middle gets missed.
[00:04:27] [music] The team measured a 30-plus
[00:04:29] percentage point drop in accuracy when
[00:04:31] relevant information moved from the
[00:04:33] beginning of the context to the middle.
[00:04:34] So, you can think about what that means
[00:04:36] for an agent whose original instructions
[00:04:38] are buried under 50,000 tokens of tool
[00:04:40] outputs. Those instructions effectively
[00:04:42] disappear. So, we know the context
[00:04:44] window is finite and degrades as it
[00:04:45] fills. But, what's actually competing
[00:04:48] for that space? There are basically
[00:04:49] seven categories of information in an
[00:04:51] agent's context window. First, the
[00:04:53] system prompt. This is the agent's
[00:04:55] identity,
[00:04:56] >> [music]
[00:04:56] >> its behavioral rules, control flow
[00:04:58] logic, and instructions for how it
[00:04:59] should approach different types of
[00:05:00] tasks. In an agent, this isn't just
[00:05:03] like, "You are a helpful assistant." It
[00:05:05] can define the entire architecture of
[00:05:07] how the agent operates. [music] Next, we
[00:05:09] have tool definitions. Every tool the
[00:05:11] agent could potentially call needs a
[00:05:13] schema in the context describing what it
[00:05:15] does, what parameters it takes, and when
[00:05:17] to use it. Then, we have the results of
[00:05:19] those tool calls. Every time the agent
[00:05:21] calls a tool, the result gets added to
[00:05:23] the context. A web page retrieval might
[00:05:25] be 5 to 10,000 tokens. A file read could
[00:05:27] also be similar. Fourth, [music] we have
[00:05:29] retrieved knowledge from rag. These are
[00:05:31] documents pulled from vector databases,
[00:05:33] search results, or API responses.
[00:05:36] Anything the agent or the system
[00:05:38] retrieves to inform the agent's
[00:05:39] decisions. [music] Fifth, conversation
[00:05:41] history. The full transcript of
[00:05:43] everything that's happened in the
[00:05:44] session, including the user's messages,
[00:05:46] the agent's responses, its reasoning,
[00:05:49] and its prior decision. This grows
[00:05:51] linearly with every turn. Sixth, memory.
[00:05:53] Both short-term memory from the current
[00:05:55] session and long-term memory from
[00:05:57] previous sessions. That [music] would be
[00:05:58] things like user preferences, prior task
[00:06:00] outcomes, and learned patterns. And
[00:06:02] finally, agent state. This is the
[00:06:04] agent's current plan, its to-do list,
[00:06:06] >> [music]
[00:06:07] >> progress markers, and scratchpad notes.
[00:06:09] All of that meta information that helps
[00:06:11] the agent track where it is in a
[00:06:12] multi-step task. [music] So, now we know
[00:06:14] what the problem is. The rest of this
[00:06:16] video is all about how to effectively
[00:06:18] make that context work well together.
[00:06:20] But even with perfect context
[00:06:21] engineering, [music] we're still going
[00:06:22] to benefit from a model that's built for
[00:06:24] this kind of work. Kimi just released
[00:06:26] K2.6, an open-source LLM that hit
[00:06:29] state-of-the-art on SweBench Pro. The
[00:06:30] reason it's relevant here is that it was
[00:06:32] built for this exact kind of agentic
[00:06:34] problem that we've been talking about.
[00:06:35] [music]
[00:06:36] Their team demonstrated it on a task
[00:06:37] where an agent ran autonomously for 13
[00:06:40] hours, made over 1,000 tool calls,
[00:06:42] modified 4,000 lines of code, and nearly
[00:06:45] tripled throughput on a code base
[00:06:47] already optimized.
[00:06:48] >> [music]
[00:06:48] >> It did all that while being
[00:06:49] significantly more cost-effective,
[00:06:51] especially for long-horizon agentic
[00:06:52] tasks. [music] K2.6 reaches the same
[00:06:55] outcomes in about 35 fewer steps than
[00:06:57] the previous version. Fewer unnecessary
[00:06:58] tool calls means less junk in the
[00:07:00] context window, [music] which means the
[00:07:01] model stays sharp for even longer. They
[00:07:03] also have an agent swarm where you can
[00:07:05] spin up 300 sub-agents in parallel. Each
[00:07:07] one gets its own clean context window,
[00:07:09] does focused work, and reports [music]
[00:07:11] back. We'll talk more about these
[00:07:12] strategies and how to implement them
[00:07:13] next. And the product is the full stack.
[00:07:15] Kimi Code is a CLI agent like Claude
[00:07:17] Code. They've got a website builder with
[00:07:19] solid front-end design and slide
[00:07:20] generation. [music] Plus, K2.6 is
[00:07:22] open-source if you want to run it
[00:07:24] locally. I'll link Kimi in the
[00:07:25] description if you want to check it out.
[00:07:26] Thanks to Kimi for sponsoring this
[00:07:28] video. Now, [music] let's start talking
[00:07:29] about how to effectively engineer our
[00:07:31] context. How do you decide what goes in,
[00:07:33] what stays out, and what gets
[00:07:34] compressed? LangChain published a widely
[00:07:36] cited framework that organizes every
[00:07:38] context engineering technique into four
[00:07:40] categories: write, select, compress, and
[00:07:43] isolate. Once you're familiar with these
[00:07:45] four buckets, every technique you
[00:07:47] encounter will fit into one of them,
[00:07:49] more or less. Let me walk through each
[00:07:50] one. The first strategy is write, and
[00:07:53] the problem it solves is really simple.
[00:07:55] Agents forget things. When an agent's
[00:07:57] context fills up and gets compacted,
[00:07:59] which we'll talk about more later, it
[00:08:00] loses information. And if the agent
[00:08:02] didn't write anything down before that
[00:08:04] happened, that information is just gone.
[00:08:06] So, write means giving the agent ways to
[00:08:08] persist information outside the context
[00:08:10] window. There are a few forms this
[00:08:12] takes. The first is scratch pads. This
[00:08:14] is literally giving the agent a tool
[00:08:16] that lets it take notes during a task.
[00:08:17] It can jot down intermediate findings,
[00:08:20] track decisions it made, or save
[00:08:21] information it knows it'll need later.
[00:08:23] Anthropic built something called the
[00:08:24] think tool, which gives Claude a
[00:08:26] dedicated workspace for working through
[00:08:28] these kinds of problems. On one
[00:08:29] benchmark, this improved performance by
[00:08:31] 54% on certain tasks. The second form is
[00:08:34] rules files, which are a kind of
[00:08:36] persistent procedural memory. If you've
[00:08:38] used Claude code, you've probably seen
[00:08:40] claude.md. These are instructions that
[00:08:41] get loaded at the start of every agent
[00:08:43] session. Basically, the agent's standing
[00:08:45] orders. They define things like the
[00:08:47] project structure, its conventions, how
[00:08:49] to run tests, and what to be careful
[00:08:51] about. The agent reads them every time
[00:08:53] it starts up, so it never forgets the
[00:08:54] fundamentals. The third form is memory
[00:08:56] extraction, which is the agent saving
[00:08:58] facts, user preferences, or learned
[00:09:00] patterns so it can retrieve them across
[00:09:02] sessions. It's a file-based system that
[00:09:04] lets the agent store and consult
[00:09:05] information that lives outside the
[00:09:07] context window entirely. But, writing
[00:09:09] things down only helps if the agent
[00:09:11] pulls the right stuff back in at the
[00:09:13] right time. That's the second strategy,
[00:09:15] select. The core idea is simple. Don't
[00:09:17] give the agent everything, give it what
[00:09:19] it needs for this step. An agent with
[00:09:21] access to dozens of tools, a large
[00:09:23] knowledge base, and several sessions of
[00:09:25] conversation history can't load all of
[00:09:27] that into the context at once. So,
[00:09:29] something has to decide what's relevant
[00:09:31] right now. And the key question is, what
[00:09:33] makes that decision? In traditional rag,
[00:09:35] the system makes it. The user asks a
[00:09:37] question, you retrieve some documents,
[00:09:40] you stuff them into the prompt, and
[00:09:41] you're done. It's a static pipeline
[00:09:42] where the model has no say in what gets
[00:09:44] pulled in. Agentic rag flips this
[00:09:46] around. Now, the agent itself decides
[00:09:49] what to search for, what tools to use,
[00:09:51] how to refine its queries, and when it
[00:09:52] has enough information. It's retrieval
[00:09:54] as an iterative process instead of a
[00:09:56] one-shot pipeline. And that matters
[00:09:58] because what's relevant changes at every
[00:10:00] step of a multi-step task, and the agent
[00:10:02] is the only one who knows what it needs
[00:10:04] next. So, what does the agent actually
[00:10:06] select from? LangChain and Pinecone both
[00:10:08] distinguish three types of memory it can
[00:10:10] draw on. Episodic memory is basically
[00:10:12] few-shot examples. Here's how you
[00:10:14] handled something similar before.
[00:10:16] Semantic memory is a repository of facts
[00:10:18] the agent has learned or been told. And
[00:10:20] procedural memory is standing behavioral
[00:10:21] instructions, like the rule files we
[00:10:23] talked about. A well-designed agent
[00:10:25] draws from all three depending on the
[00:10:26] step. But, there's one selection problem
[00:10:28] that trips people up more than any
[00:10:30] other, tools. If your agent has access
[00:10:32] to a 40-something tools, that's
[00:10:34] potentially 10,000 tokens of tool
[00:10:36] definitions sitting in the context
[00:10:37] before any work has even started. And as
[00:10:40] we'll see in the failure mode section,
[00:10:41] too many tools doesn't just waste space,
[00:10:43] it actively confuses the model. The fix
[00:10:45] is to use rag over the tool definitions
[00:10:48] themselves. Instead of dumping every
[00:10:50] tool definition into the context every
[00:10:51] time, you use semantic search to surface
[00:10:54] just the relevant tools for the current
[00:10:56] step. A paper called rag MCP tested this
[00:10:58] and found tool selection accuracy jumped
[00:11:00] from 14% to 43% while cutting prompt
[00:11:03] tokens roughly in half.
[00:11:04] >> [music]
[00:11:04] >> Anthropic's general advice here is what
[00:11:06] they call a hybrid strategy. Load some
[00:11:08] essential information up front for
[00:11:10] speed, like the claw.md file, but let
[00:11:13] the agent do just-in-time retrieval for
[00:11:15] everything else. Front-load the basics
[00:11:17] and retrieve the rest on demand. But,
[00:11:18] even with good selection, context still
[00:11:20] accumulates. Every tool call the agent
[00:11:22] makes, document it retrieves, and
[00:11:24] decision it records all stays in that
[00:11:26] window. And that brings us to the third
[00:11:28] strategy, [music]
[00:11:29] compress. This one directly addresses
[00:11:31] the context rot problem that we talked
[00:11:33] about earlier. Imagine your agent has
[00:11:35] made 20 tool calls. Its context now
[00:11:37] contains, let's say, 80,000 tokens of
[00:11:40] accumulated tool outputs, conversation
[00:11:42] history, and reasoning traces. Most of
[00:11:44] those tool outputs are no longer
[00:11:46] relevant since the agent already acted
[00:11:48] on them, but they're still sitting there
[00:11:49] taking up space, degrading the model's
[00:11:51] attention, and driving up cost and
[00:11:53] latency. So, compression is about
[00:11:55] reducing token count while preserving
[00:11:57] the information that actually matters
[00:11:58] for whatever you're working on. And you
[00:12:00] can compress at three different points
[00:12:01] in the pipeline. First, before
[00:12:03] information enters the context at all.
[00:12:05] This is where chunking comes in, which
[00:12:06] is breaking large documents into smaller
[00:12:08] coherent pieces before retrieval and
[00:12:10] re-ranking them so that only the most
[00:12:11] useful chunks make it into the window at
[00:12:13] all. You can also summarize tool outputs
[00:12:15] on the fly before they enter the main
[00:12:16] context. [music] The second opportunity
[00:12:18] to compress context is while the agent
[00:12:20] is working. The most common technique
[00:12:22] here is summarization of conversation
[00:12:24] history. [music] A running summary gets
[00:12:26] continuously updated after each
[00:12:28] exchange. So, you always have a compact
[00:12:30] version of everything that's happened. A
[00:12:32] popular pattern is a hybrid approach
[00:12:33] where you keep, say, the last 10
[00:12:35] messages verbatim since the agent might
[00:12:37] still need the exact details, but you
[00:12:39] summarize everything older than that.
[00:12:41] Beyond summarization, there's plain
[00:12:43] trimming using hard-coded heuristics
[00:12:45] that remove older messages once the
[00:12:47] context hits a certain size. And Claude
[00:12:50] Code has auto-compaction built in. When
[00:12:52] the context hits 95% capacity, it
[00:12:55] automatically summarizes the full
[00:12:56] trajectory. That's a safety net, but
[00:12:58] ideally you're compressing proactively
[00:13:00] and not waiting for that trigger. And
[00:13:02] finally, you can use compression after
[00:13:04] the agent has acted on something. An
[00:13:06] easy win here is tool result clearing.
[00:13:08] Once a tool was called 15 steps ago and
[00:13:10] the agent already used the result, you
[00:13:12] can just drop the raw output. The agent
[00:13:14] doesn't need the full text of a web page
[00:13:16] it fetched ages ago, for example. You
[00:13:18] can replace it with a one-line summary
[00:13:20] or remove it entirely. Now, let's move
[00:13:22] on to the fourth and final strategy,
[00:13:23] which is arguably the most powerful one.
[00:13:25] Isolation is the strategy that makes
[00:13:27] multi-agent systems possible. So, here's
[00:13:29] the problem. If a single agent tries to
[00:13:32] do everything, like research, plan,
[00:13:34] code, test, and debug all in one long
[00:13:37] conversation, it will inevitably fill up
[00:13:39] its context. But, the deeper issue isn't
[00:13:40] just space, it's actually contamination.
[00:13:42] [music] The detailed file searches from
[00:13:44] the research phase are still sitting in
[00:13:46] the context when the [music] agent moves
[00:13:47] to implementation. That old research
[00:13:49] context is now just noise. It's
[00:13:52] distracting the model during a phase
[00:13:53] where it needs to be focused on writing
[00:13:55] clean code. [music] The solution is
[00:13:56] context isolation, which means giving
[00:13:58] different parts of the work their own
[00:14:00] separate context windows. The most
[00:14:02] obvious form of this is using
[00:14:03] sub-agents. A parent agent delegates a
[00:14:06] focused sub-task, like [music] search
[00:14:09] the code base for all files related to
[00:14:10] authentication, to a sub-agent. That
[00:14:13] sub-agent works on its own clean context
[00:14:15] window. When it reports back to the
[00:14:16] parent, it returns only a condensed
[00:14:18] summary, and all the messy search
[00:14:20] operations stay isolated in the
[00:14:21] sub-agent's context and never pollute
[00:14:23] the parent. Okay, so to sum up, the four
[00:14:25] key strategies are write, select,
[00:14:27] [music] compress, and isolate.
[00:14:28] Everything we cover from here forward is
[00:14:30] an application of one or more of them.
[00:14:32] Now that we understand the strategies
[00:14:34] for managing context well, let's look at
[00:14:36] what happens when we don't do a good
[00:14:37] job, because understanding failure modes
[00:14:39] is a really good way to proactively
[00:14:41] learn what we're trying to avoid. Drew
[00:14:42] Breunig published an influential
[00:14:44] two-part series in mid-2025 identifying
[00:14:46] four distinct ways that agents fail as
[00:14:48] their context grows. The first failure
[00:14:50] mode is context poisoning. Sounds very
[00:14:52] serious. This is when a hallucination or
[00:14:54] an error enters the agent's context and
[00:14:57] then gets referenced over and over in
[00:14:58] subsequent steps. Like if a tool
[00:15:00] returned bad data, or the agent itself
[00:15:02] made a flawed inference five steps ago,
[00:15:04] that bad information is now sitting in
[00:15:06] the context,
[00:15:07] >> [music]
[00:15:07] >> and the agent keeps building on top of
[00:15:08] it. This is a problem because agents
[00:15:10] iterate on their own output. So, each
[00:15:12] bad step compounds into the next one.
[00:15:14] The fix is context pruning, or actively
[00:15:16] removing outdated or conflicting
[00:15:18] information as new details arrive. You
[00:15:20] should also validate tool outputs before
[00:15:22] they enter the context, especially from
[00:15:24] external sources. And after the agent
[00:15:25] recovers from an error, compress the
[00:15:27] failed attempt history. Don't leave 10
[00:15:29] steps of dead-end debugging visible in
[00:15:31] the context when only the resolution
[00:15:33] matters. The second failure mode is
[00:15:35] context distraction. This is when the
[00:15:37] context gets so long that the model
[00:15:39] starts over-relying on its recent
[00:15:40] history and under-relying on what it
[00:15:42] learned during training. The agent
[00:15:44] basically stops thinking for itself and
[00:15:46] just repeats patterns from what it's
[00:15:47] recently seen. So, instead of
[00:15:49] synthesizing a novel plan, it rehashes
[00:15:51] past actions. [music]
[00:15:52] The fix is the same as the general
[00:15:53] advice we've been discussing. Summarize
[00:15:55] and prune aggressively, even when you
[00:15:57] have a large context window available.
[00:15:59] The third failure mode is context
[00:16:00] confusion. [music] This is when
[00:16:02] superfluous content gets in the context
[00:16:04] and ends up leading to low-quality
[00:16:06] responses. The classic example is tool
[00:16:08] confusion. The agent sees 46 tool
[00:16:11] definitions in its context and starts
[00:16:13] calling tools that have nothing to do
[00:16:14] with the task. There's a really good
[00:16:15] example of this from a benchmark study.
[00:16:17] A quantized Llama 3.18 billion model
[00:16:20] failed on Geo Engine benchmark when
[00:16:22] given all 46 available tools, even
[00:16:24] though the context was well within its
[00:16:25] window limit. But, it worked fine when
[00:16:27] only given 19 tools. The tools weren't
[00:16:29] too many for the context to hold, but
[00:16:31] they were too many for the model to
[00:16:32] reason about clearly. The fix is dynamic
[00:16:35] tool management. Keep the tool set
[00:16:37] relevant to the current phase. Use
[00:16:39] approaches like RAG MCP, which we talked
[00:16:41] about earlier, which does semantic
[00:16:42] retrieval over tool descriptions to
[00:16:44] surface only the relevant tools for each
[00:16:46] step. The fourth and final failure mode
[00:16:48] is context clash. This is when new
[00:16:50] information the agent has gathered
[00:16:52] during its run contradicts something
[00:16:54] already in the context. Maybe the system
[00:16:56] prompt says one thing, but a retrieved
[00:16:58] document says something different. The
[00:16:59] agent can't reconcile the contradiction,
[00:17:01] so it produces inconsistent behavior.
[00:17:03] Sometimes following one source,
[00:17:04] sometimes the other, and sometimes doing
[00:17:06] something that doesn't match either one.
[00:17:08] The fix here is to establish a clear
[00:17:10] authority [music] ordering in your
[00:17:11] context. For example, the system prompt
[00:17:14] takes priority over retrieved facts,
[00:17:15] which take priority over conversation
[00:17:17] history. When new information comes in,
[00:17:19] validate it against what's already in
[00:17:20] the context before injecting it. And use
[00:17:23] structured section. When new [music]
[00:17:24] information comes in, validate it
[00:17:26] against what's already in the context
[00:17:28] before injecting it. And use structured
[00:17:30] sections, XML tags, clear headers, so
[00:17:33] the model can parse which information
[00:17:35] comes from which source and which source
[00:17:37] to trust. [music] These four failure
[00:17:39] modes, poisoning, distraction,
[00:17:40] confusion, and clash, cover most of the
[00:17:43] ways agents break [music] down in
[00:17:44] practice. And the good news is, once you
[00:17:47] can name the failure, the solution maps
[00:17:48] to one of the four strategies we just
[00:17:50] covered. Poisoning is solved by
[00:17:52] compression and pruning. Distraction is
[00:17:54] solved by compression. Confusion is
[00:17:56] solved by selection. And clash is solved
[00:17:58] by writing and selection. It all
[00:18:00] connects back to write, select,
[00:18:01] compress, and isolate. So, now that we
[00:18:03] have the strategies and the failure
[00:18:04] modes, let's get into the practical
[00:18:06] stuff, starting with two things you'll
[00:18:08] work on first when building an agent,
[00:18:10] the system prompt and tool definitions.
[00:18:12] The way you approach these for an agent
[00:18:14] is really different from a chatbot. A
[00:18:15] system prompt for a chatbot basically
[00:18:17] sets the tone, like you are a helpful
[00:18:19] assistant, be concise and friendly, that
[00:18:21] kind of [music] thing. On the other
[00:18:22] hand, an agent system prompt defines its
[00:18:24] architecture. It specifies control flow,
[00:18:26] like how the agent should approach
[00:18:28] different types of tasks,
[00:18:29] >> [music]
[00:18:29] >> what tools to use in what situations,
[00:18:31] what to do when it encounters an error,
[00:18:33] and what safety guardrails to follow.
[00:18:35] It's closer to kind of writing a job
[00:18:36] description for an autonomous employee.
[00:18:38] Anthropic has a useful concept here that
[00:18:40] they call writing at the right altitude.
[00:18:43] There's kind of a Goldilocks zone for
[00:18:45] agent system prompts. Too prescriptive
[00:18:47] is bad.
[00:18:47] >> [music]
[00:18:48] >> If you write something like, "If the
[00:18:49] user mentions billing and also mentions
[00:18:51] a refund and the amount is over $100,
[00:18:54] call tool X." That's just way too
[00:18:56] fragile and it will break on every edge
[00:18:58] case you didn't anticipate. On the other
[00:19:00] hand, too vague is also bad. "Be helpful
[00:19:02] and use the appropriate tools." gives
[00:19:04] the agent nothing to work with. It
[00:19:06] doesn't know which tools are appropriate
[00:19:07] for what, and it can't make good
[00:19:09] autonomous decisions without concrete
[00:19:10] signals. So, [music] the sweet spot is
[00:19:12] specific enough to guide autonomous
[00:19:13] behavior, but flexible enough to let the
[00:19:15] model apply its own judgment in novel
[00:19:17] situations. You're giving the agent
[00:19:19] strong heuristics, not rigid rules. Here
[00:19:22] are a few more practical tips on writing
[00:19:24] system prompts. [music]
[00:19:25] Organize your system prompt with
[00:19:26] structure like XML tags or markdown
[00:19:28] headers that break it into sections that
[00:19:30] are distinct like [music] background
[00:19:32] information, instructions, and tool
[00:19:34] guidance. Start minimal and iterate on
[00:19:36] failures.
[00:19:37] >> [music]
[00:19:37] >> Don't try to anticipate every edge case
[00:19:39] up front. Run the agent against real
[00:19:40] tasks, observe where it breaks, and add
[00:19:42] instructions to address those specific
[00:19:44] failure modes. Remember that minimal
[00:19:46] doesn't necessarily mean short.
[00:19:48] >> [music]
[00:19:48] >> An agent system prompt for a complex
[00:19:50] workflow might be thousands of tokens,
[00:19:52] and that's fine as long as every token
[00:19:54] is relevant and necessary. And use
[00:19:56] few-shot examples. Instead of trying to
[00:19:58] articulate every rule in words, show the
[00:20:00] agent what good behavior looks like.
[00:20:02] Give the agent diverse canonical
[00:20:03] examples of correct tool selection, good
[00:20:05] reasoning, and proper multi-step
[00:20:07] execution. Beyond the system prompt,
[00:20:09] you'll also need to think about tool
[00:20:10] definitions. Every tool the agent could
[00:20:12] potentially call needs a schema that
[00:20:14] describes what it does, what parameters
[00:20:16] it takes, and when to use it. Each
[00:20:18] definition should be self-contained,
[00:20:20] robust to error, and have clear
[00:20:21] instruction. This means tool definitions
[00:20:23] can use a lot of context. In production,
[00:20:26] this is increasingly handled through
[00:20:27] MCP, the model context protocol, which
[00:20:29] is basically a standard way for agents
[00:20:31] to connect to external tools and data
[00:20:33] sources. You hook your agent up to an
[00:20:34] MCP server for GitHub, another for your
[00:20:36] database, another for your file system,
[00:20:39] and each
[00:20:40] its tools through a consistent
[00:20:42] interface. The catch is that MCP makes
[00:20:44] it really easy to plug in a lot of
[00:20:45] tools, and that's exactly the trap. When
[00:20:48] you've got four or five MCP servers
[00:20:50] connected, tool definitions can eat
[00:20:51] thousands of tokens before any work has
[00:20:53] even started. The default advice is to
[00:20:55] curate a minimal viable set of tools.
[00:20:58] But what if your agent legitimately
[00:20:59] needs a lot of tools? There are two main
[00:21:02] approaches to scaling. The first comes
[00:21:04] from Manas, a production agent platform.
[00:21:06] They explicitly warn against dynamically
[00:21:09] adding and removing tools
[00:21:10] mid-conversation. And the reason has to
[00:21:12] do with something that most people
[00:21:14] building agents don't even know about,
[00:21:15] the KV cache. Here's how it works. When
[00:21:18] you send tokens to an LLM, the model
[00:21:20] computes key value representations for
[00:21:23] each token. This is computationally
[00:21:25] expensive, so inference providers cache
[00:21:27] these representations. If the beginning
[00:21:30] of your context, the prefix, stays the
[00:21:32] same between API calls, the provider can
[00:21:35] reuse the cache computation and only
[00:21:37] process the new tokens at the end, which
[00:21:39] is much faster and cheaper. But if you
[00:21:41] rearrange or change the early part of
[00:21:43] your context between calls, you
[00:21:45] invalidate the cache and the provider
[00:21:47] has to recompute everything from
[00:21:49] scratch. For example, with Claude
[00:21:51] Sonnet, cached input tokens cost 30
[00:21:53] cents per million, while un-cached
[00:21:55] tokens cost $3 per million, a 10 times
[00:21:58] difference. For an agent making 30 or 40
[00:22:00] API calls per task, that adds up really
[00:22:02] fast. This is why Manifold recommends
[00:22:04] tool masking instead of tool removal.
[00:22:07] You keep all the tool definitions stable
[00:22:09] in the context. They sit near the top in
[00:22:11] that prefix that gets cached, but you
[00:22:13] mark certain tools as unavailable for
[00:22:15] the current phase. The definitions are
[00:22:16] still there for cache stability, but the
[00:22:18] agent knows not to use them. They also
[00:22:20] use consistent naming prefixes, which
[00:22:22] help the agent to reason about tool
[00:22:24] categories. The second approach when
[00:22:26] dealing with lots of tools is rag-based
[00:22:28] tool selection, which we touched on
[00:22:29] earlier. Instead of including every tool
[00:22:31] in every call, you use semantic
[00:22:33] retrieval to preselect only the tools
[00:22:35] relevant to the current step. The RAG
[00:22:37] MCP paper showed this improved accuracy
[00:22:39] by over three times while cutting token
[00:22:41] usage in half. These two approaches
[00:22:43] aren't mutually exclusive. Masking works
[00:22:45] well when your tool set is moderate, and
[00:22:47] rag-based selection works well when you
[00:22:49] have a really large number of tools. The
[00:22:52] broader principle behind all of this is
[00:22:53] simple. Stable content goes at the top
[00:22:56] of your context. This includes the
[00:22:57] system prompt, tool definitions, and
[00:22:59] anything that doesn't change between
[00:23:01] turns. Then dynamic content like
[00:23:03] conversation history, the current step,
[00:23:05] and the agent state go at the bottom.
[00:23:07] So, we've covered the four strategies
[00:23:08] for context engineering, common failure
[00:23:10] modes, and how to engineer system
[00:23:12] prompts and tools. Now, let's see what
[00:23:14] all of this looks like when you actually
[00:23:16] sit down to build something. This next
[00:23:17] part applies whether you're using a
[00:23:19] coding assistant or building your own
[00:23:20] agent from scratch. The principles are
[00:23:23] the same. The only difference is whether
[00:23:25] you're structuring the workflow yourself
[00:23:27] or programming the agent to do it. Dex
[00:23:29] Horthy, the CEO of Human Layer,
[00:23:31] presented a methodology at the AI
[00:23:33] Engineer Code Summit that's a really
[00:23:34] clean example of this. His team
[00:23:36] reportedly used it to ship around 35,000
[00:23:38] lines of code to a large Rust code base
[00:23:41] in a single 7-hour [music] session. The
[00:23:43] core idea is what Horthy calls frequent
[00:23:45] intentional compaction. Basically, you
[00:23:47] should proactively structure your
[00:23:48] agent's work into phases, where each
[00:23:51] phase produces a compacted artifact like
[00:23:53] a structured markdown summary, and each
[00:23:55] new phase starts with a fresh context
[00:23:57] window containing only that artifact.
[00:23:59] This way, you're deliberately staying
[00:24:00] below that 40 to 60% of the context
[00:24:02] window. Here's how it works in practice,
[00:24:04] and I'll mention which strategies show
[00:24:06] up at each step. Phase one is research.
[00:24:08] Before any code gets written, the agent
[00:24:10] explores [music] the code base. It reads
[00:24:12] files, traces data flows, and maps out
[00:24:15] the architecture relevant to the task.
[00:24:17] Sub-agents handle the raw file searches
[00:24:19] and code analysis. All those grep
[00:24:21] results and file contents stay in the
[00:24:23] sub-agent's context windows and never
[00:24:25] pollute the parents. That's the isolate
[00:24:27] strategy. The output of this phase is a
[00:24:29] research file, a compact markdown
[00:24:31] document with file paths, function
[00:24:34] signatures, existing patterns, and
[00:24:35] gotchas. That's the write strategy. The
[00:24:38] agent persists its findings externally,
[00:24:40] so they go on to the next step. And the
[00:24:42] [music] next step is a context reset.
[00:24:44] The raw research might have consumed 60
[00:24:46] to 80% of the context, but the research
[00:24:48] artifact compresses all of that down to
[00:24:50] maybe 15 to 20%. That's the compress
[00:24:52] strategy. Phase two is planning. A brand
[00:24:55] new context window opens containing only
[00:24:57] the research document and the problem
[00:24:59] definition. The agent uses this clean
[00:25:01] context to produce a detailed
[00:25:03] implementation plan. This is also the
[00:25:05] most important point for human review.
[00:25:07] If there's a logical error, you catch it
[00:25:09] here where fixing it is easy. If you're
[00:25:11] building your own agent, this is where
[00:25:13] you'd build in the human in the loop
[00:25:14] checkpoint if it's relevant. Phase three
[00:25:16] is implementation. At this point, we use
[00:25:18] another fresh context window, this time
[00:25:20] containing only the plan. The agent
[00:25:22] follows it step-by-step. For complex
[00:25:24] tasks that require multiple compaction
[00:25:26] cycles, a progress.md file tracks what's
[00:25:29] been completed and what remains. That's
[00:25:31] the right strategy again. This approach
[00:25:33] is really similar to what I do in my
[00:25:34] daily work at Twitch, and you'll see
[00:25:36] some version of it in most production
[00:25:38] systems. So now let's spend a few
[00:25:39] minutes looking at how some of the big
[00:25:41] boys approach context engineering.
[00:25:42] Claude Code is Anthropic's CLI-based
[00:25:45] coding agent, obviously, [music] and
[00:25:46] it's one of the best-documented examples
[00:25:48] of context engineering in practice. It
[00:25:50] uses a hybrid retrieval model where
[00:25:52] Claude.md files are loaded up front
[00:25:55] start of every session for foundational
[00:25:56] context, and then the agent uses tools
[00:25:58] like glob and grep for just-in-time
[00:26:00] navigation of the code base. It doesn't
[00:26:02] try to pre-index everything, but just
[00:26:04] explores on demand. It also has auto
[00:26:06] compaction that triggers at 95% context
[00:26:08] utilization, preserving architectural
[00:26:10] decisions in the five most recently
[00:26:12] accessed files. [music] It can spawn
[00:26:14] sub-agents for complex tasks, giving
[00:26:16] each one a clean context window.
[00:26:17] >> [music]
[00:26:18] >> And it has a memory tool for persisting
[00:26:19] information across sessions. Anthropic's
[00:26:21] overall philosophy here is do the
[00:26:23] simplest thing that works. They don't
[00:26:25] over-engineer the context pipeline.
[00:26:27] [music] They let the model be smart
[00:26:28] about what it needs and give it the
[00:26:29] tools to go find it. Manifold takes a
[00:26:31] more infrastructure-heavy approach than
[00:26:33] Anthropic. They've served hundreds of
[00:26:35] thousands of users with a
[00:26:36] general-purpose agent, so efficiency at
[00:26:38] scale is important. Their standout
[00:26:40] contribution is KB-cache aware context
[00:26:43] ordering that we talked about earlier.
[00:26:44] This is structuring every context so the
[00:26:46] prefix stays stable across turns to
[00:26:48] maximize cache reuse, and using tool
[00:26:50] masking rather than dynamic removal.
[00:26:52] They have an observation compression
[00:26:54] pipeline that processes every tool
[00:26:56] output before it enters the agent's
[00:26:57] [music] context. They maintain a
[00:26:59] persistent to-do list for state
[00:27:00] tracking, and they use the file system
[00:27:02] as overflow memory for evicted context.
[00:27:05] OpenAI's approach with ChatGPT agent,
[00:27:07] which evolved from the operator product,
[00:27:09] is architecturally different from both
[00:27:11] Claude Code and Manas. It's powered by a
[00:27:13] computer using agent model, and it takes
[00:27:15] a GUI-first approach. Instead of
[00:27:17] text-based tool calls, the agent
[00:27:19] interacts with a visual browser.
[00:27:21] Screenshots get added to the context as
[00:27:23] visual snapshots, and the model reasons
[00:27:25] over what it sees on the screen, plus
[00:27:26] its history of past screenshots and
[00:27:28] actions. The context engineering
[00:27:30] challenge here is different, of course.
[00:27:31] Visual tokens are expensive, so the
[00:27:33] agent needs to be selective about how
[00:27:35] many screenshots to keep. OpenAI uses
[00:27:37] reinforcement learning to discover
[00:27:39] optimal tool use strategies. Rather than
[00:27:41] explicitly programming when to use each
[00:27:43] tool, they train the agent across
[00:27:44] thousands of virtual machines and let it
[00:27:46] learn what works. Deep Research and
[00:27:48] Operator share state, enabling fluid
[00:27:50] transitions between browsing, text
[00:27:52] analysis, and code execution. The
[00:27:54] contrast with Claude Code is really
[00:27:55] interesting. Claude Code is code-centric
[00:27:57] with large context windows and
[00:27:59] text-based tool calls. ChatGPT agent is
[00:28:01] visual and general-purpose. Both need
[00:28:03] context engineering, but the specific
[00:28:05] challenges and solutions are, of course,
[00:28:07] different. Lastly, Google's ADK takes
[00:28:09] the [music] most principled
[00:28:10] architectural approach. They've codified
[00:28:12] three design principles for agent
[00:28:13] context. First, separate storage from
[00:28:15] presentation. The agent's durable state
[00:28:18] is not the same as what appears in each
[00:28:19] API call. Second, use explicit
[00:28:21] transformations, named ordered
[00:28:24] processors that transform context into
[00:28:26] testable, composable steps, rather than
[00:28:28] ad-hoc string concatenation. [music]
[00:28:30] And third, scope context by default.
[00:28:33] Every model calls these only the minimum
[00:28:35] required information, and nothing lands
[00:28:37] in context unless it's explicitly
[00:28:38] included. This is a more engineering
[00:28:40] discipline approach to context assembly,
[00:28:42] treating it as a pipeline with clear
[00:28:44] stages, rather than a prompt you just
[00:28:46] keep appending to. When you look across
[00:28:48] all these platforms, a common pipeline
[00:28:50] emerges. On [music] every single agent
[00:28:52] turn, the system goes through roughly
[00:28:54] the same steps. First, collect all the
[00:28:56] candidate information like user input,
[00:28:58] conversation history, tool results,
[00:29:00] retrieve documents, and agent state.
[00:29:02] Then select what's relevant for the
[00:29:03] current step and the remaining token
[00:29:05] budget. Then compress. [music] So,
[00:29:06] summarize, truncate, or restructure
[00:29:08] selected content to fit in the context.
[00:29:10] Arrange everything for maximum KB cache
[00:29:12] reuse, stable content [music] first, and
[00:29:14] dynamic content last. Then assemble the
[00:29:16] final context and make the API call.
[00:29:18] This stuff is changing quickly and
[00:29:20] there's still so much to learn. As
[00:29:22] usual, the best way to get good at this
[00:29:23] stuff is just to try things out. [music]
[00:29:25] Experiment and build and see what works.
[00:29:27] I've linked all my sources in the
[00:29:28] description, so if you want to go deeper
[00:29:30] on any of this, those are really good
[00:29:31] starting points. And if you're
[00:29:32] interested in the fundamentals of
[00:29:34] agents, I have a comprehensive course on
[00:29:36] that as well. Check that out up next.

---
*RAW — not yet passed through D.R.D deconstruction. Do not integrate into department files.*
