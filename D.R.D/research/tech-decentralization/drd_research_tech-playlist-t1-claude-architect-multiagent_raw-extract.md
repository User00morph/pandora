# RAW EXTRACT — Claude Architect: Multi-Agent Orchestration

## Source Metadata
- **Title:** Claude Architect: Multi-Agent Orchestration
- **URL:** https://www.youtube.com/watch?v=vRYBG_R8JAI
- **Tier:** 1
- **Extracted:** 2026-06-09
- **Domain:** tech-decentralization / agentic-systems
- **Playlist:** Pandora Tech Playlist — PLWKcfqsabTLUxfC7OFs7UZ8EIJ6hjY_M8
- **Word Count:** ~23499

## Transcript (timestamped)

[00:00:01] Let's take a look at hub and spoke
[00:00:02] architecture. So, hub and spoke
[00:00:03] architecture is a pattern where one
[00:00:05] coordinator agent sits at the center and
[00:00:07] all sub agents talk to the coordinator.
[00:00:10] I highlighted that weird word
[00:00:11] coordinator because you're going to be
[00:00:13] seeing a lot of coordinator agent. And
[00:00:16] when you think of like Claude
[00:00:19] Claude code, I have a feeling that this
[00:00:22] is at least one of the means at least
[00:00:24] when you're working with sub agents of
[00:00:26] our communication, right? So, this is
[00:00:28] going to be something really really
[00:00:29] useful to learn.
[00:00:30] It's going to be really fun and
[00:00:31] something that you can apply
[00:00:34] like immediately, okay? So, sub agents
[00:00:36] never have direct lines to each other.
[00:00:38] So, if you have like a research agent
[00:00:39] over here, it cannot directly talk
[00:00:43] to the review agent a river agent. It
[00:00:44] has to go through the coordinator.
[00:00:47] And so, that is pretty clear. And the
[00:00:49] coordinator is going to own the routing.
[00:00:50] So, it's going to decide how to route
[00:00:51] things. Context sharing, so what will be
[00:00:53] shared? So, the research agent is not
[00:00:56] going to be aware of what everyone's
[00:00:57] doing unless the coordinator passes that
[00:00:59] information along and it gets injected.
[00:01:01] So,
[00:01:02] it really won't know.
[00:01:03] And any kind of error handling, any kind
[00:01:05] of observability, any anything like
[00:01:07] that, okay?
[00:01:08] And obviously that would
[00:01:10] make it really good for observability
[00:01:12] because now everything's passing through
[00:01:13] there and we have a choke point where we
[00:01:15] can check and collect information,
[00:01:17] right?
[00:01:18] And so, here we have kind of the task
[00:01:20] life cycle
[00:01:22] of like, okay, we have something that
[00:01:24] needs to be done and how is it going to
[00:01:28] get executed out? So, the role of that
[00:01:29] coordinator is task decomposition. So,
[00:01:31] break
[00:01:33] break
[00:01:35] the task into subtasks, right? Then we
[00:01:37] have task delegation. So, who is going
[00:01:40] to be working on that problem? Result
[00:01:43] aggregation. So, bring it all back
[00:01:46] together
[00:01:47] to produce a final result and decide
[00:01:49] which sub agents to invoke based on
[00:01:51] query complexity. So, um you know, we
[00:01:53] have a a lot of things going on here,
[00:01:56] but let's just kind of walk through it.
[00:01:58] So, imagine you're a coordinator and
[00:02:00] when given a task, it'll break down
[00:02:02] subtask for each of the available tools
[00:02:06] and we're saying do not do the work
[00:02:07] yourself. So, we're basically here
[00:02:08] defining
[00:02:10] you know, that you are a coordinator and
[00:02:12] this is what you're going to be doing,
[00:02:13] okay?
[00:02:14] And then here it's like you're a
[00:02:15] coordinator and use your judgment.
[00:02:16] Simple factual questions, use a single
[00:02:18] agent. Multi-step task, delegate out to
[00:02:21] a sequential passing the results
[00:02:22] forward. Independent subtask, delegate
[00:02:24] in parallel. So, we're basically
[00:02:26] defining, okay, what does the routing
[00:02:28] look like? So, it's not just like static
[00:02:29] routing. Like it's, you know, use the
[00:02:31] routing you need to route based on the
[00:02:34] use case, right?
[00:02:35] Which I think is really really
[00:02:36] interesting. And then down below here
[00:02:38] it's like, okay, you've gotten all the
[00:02:40] outputs from multiple agents, combine
[00:02:41] them into a single coherent response,
[00:02:44] resolve any conflicts and make the data
[00:02:46] pretty. So,
[00:02:48] that's the most basic thing when we're
[00:02:50] talking about this coordinator agent.
[00:02:52] There's a lot of stuff we have to
[00:02:53] consider when implementing this, but we
[00:02:55] will go and set up a super skeleton one
[00:02:58] really quickly here and then we will
[00:03:01] iterate on it, okay?
[00:03:03] Okay, folks. So, what I want to do in
[00:03:04] this follow along is implement a very
[00:03:06] simple
[00:03:08] coordinator agent. So, we'll say
[00:03:09] coordinator
[00:03:12] agent
[00:03:14] simple
[00:03:16] or basic.
[00:03:17] And in here we will make a new main
[00:03:21] .py
[00:03:23] And I suppose that we could
[00:03:26] um
[00:03:28] pull up some code. I'm going to see if
[00:03:29] we can switch over to Haiku
[00:03:33] and save some credits here
[00:03:35] because it might be able to do it. We'll
[00:03:37] see.
[00:03:39] Haiku. There we go. So, now it's
[00:03:40] switched over to the Haiku 4.5 model.
[00:03:42] And so, I'm going to tell it uh
[00:03:45] um create
[00:03:47] uh
[00:03:48] a very basic coordinator agent
[00:03:52] um
[00:03:54] in
[00:03:56] coordinator basic main.py
[00:04:00] Please follow
[00:04:02] our general
[00:04:04] um
[00:04:06] coding
[00:04:08] example would be
[00:04:11] uh what was one we did? Decision making
[00:04:14] would probably be one
[00:04:15] model driven
[00:04:17] model driven.py. And so, I'm hoping that
[00:04:19] by giving it that reference, it will
[00:04:21] know how to reference that stuff and
[00:04:23] produce something that's going to be
[00:04:24] generally okay,
[00:04:26] but we'll see how Haiku does. I really
[00:04:28] should run Haiku a lot more. I just kind
[00:04:29] of stick at Sonnet. Um
[00:04:31] and that's my that's my fault there,
[00:04:33] right? And so, we will give it a bit of
[00:04:35] time here, let it accept here and then
[00:04:37] we will decide whether Haiku could even
[00:04:38] do it or not and does it have all the
[00:04:40] components we need? And there it is.
[00:04:41] That was pretty darn fast. Maybe it
[00:04:43] needs a little bit more work to do.
[00:04:45] But we have the start of it. Let's close
[00:04:46] out the tab here. Sometimes it helps to
[00:04:48] close out the tab and reopen it for
[00:04:49] whatever reason. It's already done. So,
[00:04:51] here it says I've created a basic
[00:04:53] coordinator. We have create task, get
[00:04:55] task status, complete task task list.
[00:04:59] And so, we have the basic stuff. Let's
[00:05:01] take a look here and see if it's any
[00:05:03] good. Um so, we have tool
[00:05:05] implementation. So, tool create task.
[00:05:09] Um task status. And so, it's talking
[00:05:11] about how it has to manage the tasks
[00:05:13] generically.
[00:05:14] Right?
[00:05:15] Um then down below here, yep, so we have
[00:05:17] that.
[00:05:19] Create a task with an optional list of
[00:05:20] task IDs.
[00:05:22] Um get the current status of the
[00:05:24] specific task, mark it as complete, list
[00:05:26] all tasks as completed.
[00:05:28] Um so, it seems like it's pretty simple.
[00:05:30] Your role is to manage and coordinate
[00:05:32] tasks.
[00:05:33] Well, a coordinator does that in
[00:05:34] general, but I guess the thing is like
[00:05:36] this is literally it sounds like it's
[00:05:38] managing tasks. Create tasks as needed
[00:05:40] for the workflow, check the task status
[00:05:42] and dependencies, complete tasks when
[00:05:43] appropriate. So, what I'm trying to
[00:05:45] figure out here is what is the use case?
[00:05:47] So, set up a
[00:05:49] Let's go down here for a second. So, we
[00:05:50] have
[00:05:52] user message. So, set up a workflow
[00:05:55] create a task design and then create a
[00:05:58] task implementation that depends on
[00:06:00] design and then complete design task
[00:06:02] first. This is so generic, it's really
[00:06:04] hard to make sense of it. We have our
[00:06:06] while loop here. It brought in the while
[00:06:08] true, so we don't have that max
[00:06:09] iteration.
[00:06:11] Um
[00:06:12] And maybe maybe might not be a a major
[00:06:14] issue, but we still might want that in
[00:06:15] there. I probably should have referenced
[00:06:16] the other code.
[00:06:18] And
[00:06:20] Mhm.
[00:06:24] So, I'm just carefully looking here
[00:06:26] at what we have.
[00:06:29] So, we have our tools over here.
[00:06:32] And so, I'm not really sure if that
[00:06:34] really fits our pattern exactly. I'm
[00:06:36] going to go take a look at our
[00:06:38] uh diagram here. What do we have? We
[00:06:39] have decom decompose
[00:06:42] uh the routing and the aggregation,
[00:06:45] right? So, um
[00:06:48] I don't think I see all those steps
[00:06:50] here. Okay, so what I'm going to do is
[00:06:51] I'm going to go back to our smarter
[00:06:53] model here, Sonnet.
[00:06:56] Okay.
[00:06:58] And I'm going to go and ask the
[00:07:00] coordinator
[00:07:03] or I'm going to ask
[00:07:04] it to improve our coordinator code. So,
[00:07:06] uh you know, for a coordinator agent
[00:07:10] we should have
[00:07:12] decomposition tasks.
[00:07:16] Um
[00:07:17] Just a moment here.
[00:07:25] Routing.
[00:07:27] It says assess complexity, but we have
[00:07:28] routing.
[00:07:30] Um
[00:07:33] We'll say assess complexity
[00:07:38] complexity
[00:07:39] and routing and aggregate
[00:07:42] results. The use case here is
[00:07:46] um
[00:07:47] too generic.
[00:07:50] Need
[00:07:52] a better
[00:07:54] use case. Okay. And so, we'll go ahead
[00:07:55] and we'll see if it can improve that
[00:07:57] code. And if not, I might have to write
[00:08:00] even more detailed prompt. I'm just kind
[00:08:02] of low
[00:08:03] on our usage unless
[00:08:06] the window has rolled over.
[00:08:08] Let me take a look here.
[00:08:11] Nope, I still got 50 minutes for my time
[00:08:13] to roll over over here, but we'll see.
[00:08:15] And so, I just wanted to kind of see it
[00:08:18] mimic these patterns here. And so, it's
[00:08:21] not to say that it's not exactly doing
[00:08:22] it, but it's definitely uh
[00:08:25] not that sophisticated, right?
[00:08:29] Because I would expect there to be a
[00:08:30] prompt for the routing component here
[00:08:32] and I'm not seeing it here, right?
[00:08:34] It does say set up a workflow. So,
[00:08:35] technically that is that that right
[00:08:38] there.
[00:08:39] So, maybe maybe it is kind of being
[00:08:40] implemented, but we'll give it a second
[00:08:41] here. Now, I'll rewrite a concrete use
[00:08:43] case. Technical due diligence, decompose
[00:08:45] the complex software review.
[00:08:48] Oh, I don't like that.
[00:08:51] No, I'm going to stop this for a second
[00:08:53] here. Stop stop stop stop. I I don't
[00:08:55] like the use case.
[00:09:00] Oh, it already stopped, basically.
[00:09:05] So, it says breaks the request into five
[00:09:07] fixed areas. Well, I already got the
[00:09:09] code, I guess. Let's just take a look
[00:09:10] here.
[00:09:12] Um
[00:09:18] So, here it says a user submits a
[00:09:19] software system for technical review.
[00:09:22] The coordinator has a decomposed the
[00:09:23] requests assesses the complexity per
[00:09:25] area, routes and and does that, runs an
[00:09:28] appropriate handler, aggregates all
[00:09:29] findings into a single report. So, that
[00:09:31] sounds good.
[00:09:33] Uh we have tool decompose request, tool
[00:09:36] assess complexity.
[00:09:37] Um
[00:09:44] I don't really like
[00:09:47] the use case because I want something
[00:09:48] that's going to be easy for us to
[00:09:49] validate and test and this will be too
[00:09:50] complicated. I don't like the use case.
[00:09:53] Can you propose to me
[00:09:56] uh 10 possible use cases.
[00:10:00] I want something that,
[00:10:03] uh,
[00:10:04] is not super complex
[00:10:06] that will be like super computational
[00:10:10] but would need complex routing and
[00:10:12] choices.
[00:10:15] Uh,
[00:10:16] don't implement, just
[00:10:19] suggest ideas. Okay. And so, I want to
[00:10:22] see if we can pick something a bit
[00:10:23] better. If it can't, then I might have
[00:10:25] to, uh, decide on myself here. Here's a
[00:10:26] So, job application screener.
[00:10:29] Um,
[00:10:31] event planning coordinator, bug triage,
[00:10:33] restaurant order customizer.
[00:10:40] I mean, I like the travel one that might
[00:10:42] have to go through the internet. I don't
[00:10:43] necessarily want to do that.
[00:10:46] Mm.
[00:10:55] Okay. So, like with number
[00:10:58] what would be the subtasks?
[00:11:02] The subagents used.
[00:11:05] Because this is what I'm trying to
[00:11:06] figure out. And this comes back to, you
[00:11:07] know, this idea where we have an idea
[00:11:10] and it's doing a bunch of stuff, right?
[00:11:12] So, like coder, writer, researcher,
[00:11:14] planner, data, right? So, I'm trying to
[00:11:15] see what we have.
[00:11:17] And so, we go over to here.
[00:11:19] And so, we have request to composer. So,
[00:11:22] takes the job posting
[00:11:24] resume extracts it out.
[00:11:28] Looks at each criteria and decides the
[00:11:30] routing.
[00:11:32] Okay. Executing execution phase.
[00:11:36] Um, the actual routing targets.
[00:11:40] Aggregation phase.
[00:11:43] And so, it has two different ones here.
[00:11:45] So, I guess my question is like, is the
[00:11:47] ownership
[00:11:52] I mean, like, should the coordinator
[00:11:56] be routing to a decomposer
[00:11:59] and
[00:12:01] uh,
[00:12:04] router routing because I thought
[00:12:08] the composer is supposed to
[00:12:11] own it
[00:12:14] in a hub and spoke
[00:12:17] architecture. And so, that's the only
[00:12:19] thing I'm I'm just making sure like
[00:12:20] maybe these are just tools and it's
[00:12:21] calling out to them and so, it still has
[00:12:23] ownership. So, you're right. In a proper
[00:12:25] hub and spoke architecture, the
[00:12:26] coordinator is the hub. It owns it. The
[00:12:27] decomposer isn't a sub subagent. That's
[00:12:29] why the coordinator owns its
[00:12:30] responsibility. So, we have that. Sure.
[00:12:32] That looks like something.
[00:12:34] So, the coordinator decomposes, assess
[00:12:35] complexity, decides routing, aggregates.
[00:12:38] The spokes just execute. This smells
[00:12:40] like something belongs to the
[00:12:41] coordinator versus subagent. Does it
[00:12:43] need a full picture?
[00:12:47] Does it need the full picture to do the
[00:12:48] its job? Decomposer is always routing,
[00:12:50] always needs the full picture.
[00:12:55] Uh, I don't
[00:12:57] I don't I don't know what you mean by
[00:12:59] full picture.
[00:13:03] But we are implementing
[00:13:07] hub and spoke model
[00:13:11] architecture. Okay. So, I don't know
[00:13:13] what he's trying to say there, but, um,
[00:13:16] maybe it means like I think I think that
[00:13:18] the context. You're right. Okay. So, it
[00:13:19] says you're right. Oh, yeah, of course
[00:13:20] I'm always right. Um, receives the
[00:13:22] request, call spokes, aggregates the
[00:13:24] results.
[00:13:25] Independent workers, each job does one,
[00:13:27] no knowledge of each other. That's
[00:13:28] right. Okay. So, for job app application
[00:13:30] screener, now we have keyword scanner,
[00:13:32] deep evaluation, red flag detector,
[00:13:34] score aggregator.
[00:13:36] Takes all the spoke spoke outputs.
[00:13:40] The coordinator owns calling each spoke
[00:13:42] with the right input deciding which
[00:13:44] spoke to call
[00:13:46] collecting and combining their outputs.
[00:13:47] Yes. Okay. And so, now we're getting
[00:13:50] something there.
[00:13:51] Just because it said it did it, does not
[00:13:53] mean it did. And this is me looking at
[00:13:55] it going,
[00:13:56] "Uh, that doesn't seem right." Right?
[00:13:58] Um, and so, we will let it go ahead and
[00:14:00] do that. I'm not getting any more
[00:14:01] warnings. So, oh, it says now using
[00:14:03] extra credits.
[00:14:05] So, I'm over my usage.
[00:14:06] >> [laughter]
[00:14:08] >> But I should be okay.
[00:14:11] This is You'd be surprised how long or
[00:14:13] how far five five dollars will take you
[00:14:15] here.
[00:14:16] Okay. So, it says it's completed the
[00:14:17] architecture here.
[00:14:19] Um, let's go take a look and check out
[00:14:22] the code.
[00:14:23] So, now we got a lot of stuff here.
[00:14:25] Okay. So, keyword scanner prompt. You
[00:14:28] are a resume keyword scanner. Check
[00:14:30] whether it required skills from the job
[00:14:31] posting, uh, appear explicitly in the
[00:14:33] resume.
[00:14:35] For each required skill, output one
[00:14:37] line. Be literal. Do not infer or
[00:14:39] extrapolate. Report only what is
[00:14:41] explicitly stated. Okay. And so, then we
[00:14:43] basically have all the ones here and
[00:14:45] they're fine. Of course, if we're doing
[00:14:46] this for real, we would be tweaking this
[00:14:48] all by hand, of course. And then here we
[00:14:51] have the actual, um,
[00:14:54] I guess they're saying the spokes. We
[00:14:56] could say subagents, if you would, or
[00:14:58] they have them called the spokes.
[00:15:00] And each of them are individually
[00:15:02] calling
[00:15:03] uh, this stuff. I'm not sure why they're
[00:15:05] doing it this way. It seems like this
[00:15:06] could be easily refactored. This seems a
[00:15:08] little bit, uh,
[00:15:10] messy. Maybe they're doing this so that
[00:15:11] you could improve it later on, but to me
[00:15:13] this,
[00:15:14] um, seems like this should all be just
[00:15:16] one function.
[00:15:17] And then we have the spoke aggregator
[00:15:19] where there actually is a little bit
[00:15:20] different. So,
[00:15:22] they do have that there, which is fine.
[00:15:24] Then we have our dispatch tool.
[00:15:27] Okay. So, basically like where should it
[00:15:28] go? We have
[00:15:31] And yeah, whether it should go there or
[00:15:32] not. Tool schema. So, what the
[00:15:33] coordinator hub sees.
[00:15:37] Mhm.
[00:15:39] So, we have run keyword scanner.
[00:15:42] Oh, like these are the actual tools
[00:15:44] deciding whether they should get
[00:15:45] triggered or not. That's fine.
[00:15:47] Then we have our coordinator prompt. So,
[00:15:48] you are a job application screening
[00:15:50] coordinator. That's fine. Your job is to
[00:15:52] orchestrate three independent screening
[00:15:53] agents.
[00:15:55] Mhm.
[00:15:57] Uh, your job is to orchestrate the three
[00:15:59] independent screening agents and then
[00:16:01] aggregate the results.
[00:16:03] You may run three screening agents in
[00:16:05] order. Do not skip any of them. And so,
[00:16:08] here it's defining that saying you have
[00:16:10] a explicit order. And so, obviously
[00:16:13] there could be more complex routing than
[00:16:14] this, but this is all there is.
[00:16:17] Then we'll go down to here.
[00:16:18] And so, here we have our job postings. I
[00:16:20] was going to wonder where this data was.
[00:16:22] Cuz I was going to be like, is there,
[00:16:24] are the resumes generated here? And they
[00:16:25] do. So, our we have our job posting,
[00:16:28] then we have our our resume. We only
[00:16:29] have we only have a single resume, which
[00:16:31] is fine.
[00:16:32] Alex Chen, that's interesting. Okay. So,
[00:16:34] we go down here and we're passing that
[00:16:37] data in. It's going through that loop.
[00:16:39] Again, we have this while true. So, I'm
[00:16:41] not sure if that's the best idea to have
[00:16:44] that while true like there, but I will
[00:16:46] run it and
[00:16:48] uh,
[00:16:50] take the risk.
[00:16:52] I think it's fine.
[00:16:55] Uh, you know what? I I do want a max
[00:16:57] iteration. So, I'm going to go here and
[00:16:58] just say like
[00:17:01] uh, the while loop is true. Do you think
[00:17:06] we should have a
[00:17:08] max iteration or any other suggestions
[00:17:12] so it doesn't go
[00:17:19] on forever.
[00:17:20] Okay. And so, that's
[00:17:23] what I want it to answer there. We have
[00:17:25] the max We might just do the max
[00:17:26] iteration cuz now I've basically told it
[00:17:28] to do that.
[00:17:30] So, here it says, um, a while true loop
[00:17:33] with no exit condition. I mean, there is
[00:17:35] an exit condition. It's the break right
[00:17:37] here.
[00:17:38] Um,
[00:17:40] And then we have a timeout for this use
[00:17:41] case.
[00:17:44] So, a max steps caps is is the right
[00:17:46] fit. That's what it's suggesting.
[00:17:51] Fair enough.
[00:17:55] Mhm.
[00:17:57] How's it uh, counting the max steps?
[00:18:02] So, the loop executes only when the
[00:18:04] condition becomes false, max steps, and
[00:18:06] not when and not when the break is hit.
[00:18:09] So, it cleanly catches runaway loops
[00:18:11] without needing extra flag. Okay, that's
[00:18:12] fine. The cap is 10, double the expected
[00:18:16] five steps, give the model room to
[00:18:17] retry. I just don't see where it's
[00:18:19] counting them. Oh, I guess it's right
[00:18:21] here.
[00:18:22] Oh, sure.
[00:18:24] I I guess so, but I mean, that's the
[00:18:26] same thing as a max iteration.
[00:18:29] Um, so,
[00:18:33] max steps is the same as
[00:18:36] max iteration.
[00:18:40] I guess it's fine. I mean, I'm sure it
[00:18:41] will still work. So,
[00:18:44] if it doesn't, we'll find out. And
[00:18:45] again, you know, you can just watch and
[00:18:47] see what my outcome is before you do
[00:18:49] this if you do not want to waste credits
[00:18:51] because I've made a poor decision. Um,
[00:18:55] you know, like I'm loading my thing up
[00:18:56] with like five dollars at a time. So,
[00:18:58] I'm I'm not that worried about, um,
[00:19:01] uh, small losses like that. So, we'll go
[00:19:03] ahead and go into here.
[00:19:05] And let's go ahead and execute this.
[00:19:12] And yeah, I'm not using my subscription.
[00:19:14] Now, we could probably port this over to
[00:19:15] agent SDK,
[00:19:17] um, and this would be greatly
[00:19:17] simplified. We might do that later to
[00:19:19] see what's happening here, but won't do
[00:19:20] it right away. So, here it says, um,
[00:19:23] coordinator routes to the spoke.
[00:19:26] Okay. So, it's found stuff. Something's
[00:19:28] missing. Coordinator routes to the run
[00:19:30] deep evaluator.
[00:19:32] Uh, strong alignment with the senior
[00:19:34] level role with seven years of total
[00:19:36] experience. Cool. Strong fit.
[00:19:38] Uh, coordinator routes to the red flag
[00:19:41] detector.
[00:19:42] Imagine someone, uh, just coded this and
[00:19:44] this is what's keeping people out of
[00:19:45] their jobs. That that would be a bummer.
[00:19:47] And then we have step two
[00:19:49] of 10. So, match keywords.
[00:19:52] Uh, strong, no flags, decision higher.
[00:19:55] Alex demonstrates strong alignment with
[00:19:57] senior level requirements. Coordinator
[00:20:00] for final recommendation for hire, so
[00:20:02] it's recommending it.
[00:20:04] Six out of the seven, strong, no red
[00:20:06] flags.
[00:20:07] All core required skills present.
[00:20:10] Seven years experience, whatever,
[00:20:11] whatever.
[00:20:12] And so we just implemented our own
[00:20:14] coordinator. Again, the only thing
[00:20:15] that's really simple, like I'm still not
[00:20:17] the confident about the wild loop, but
[00:20:19] the only thing that is um
[00:20:21] very simple is the routing. But the
[00:20:23] routing obviously is being handled here.
[00:20:25] Um and so, you know, like in that
[00:20:28] diagram, it just seems like it's a
[00:20:29] separate step. Like you cut them up and
[00:20:32] then you do that.
[00:20:34] Um and so I'm not sure if that should be
[00:20:36] separated out, but the point is we did
[00:20:37] implement coordinator agent. Um and
[00:20:39] that's something we could decide later
[00:20:41] on if we wanted to have an individual
[00:20:42] step for more intelligent routing. So,
[00:20:45] that's the only thing that I might um
[00:20:48] consider. Like I I would probably ask it
[00:20:50] right now like if it should be ran
[00:20:53] twice, but I'm I don't know. I don't
[00:20:54] want to
[00:20:56] cuz I don't think it's going to just
[00:20:56] tell me. I think it's going to actually
[00:20:57] try to do it. And so I don't want to
[00:20:58] muck with it. And so I'd say that's
[00:21:00] fine, but just consider that that's an
[00:21:02] uncertainty that I have right now.
[00:21:04] And so I'm going to go back a directory
[00:21:05] here. We'll just say get at all, get
[00:21:07] commit {hyphen} M. Uh
[00:21:10] basic coordinator.
[00:21:12] I thought that was kind of fun.
[00:21:15] I thought the results were pretty good.
[00:21:18] Okay, and I will see you in the next
[00:21:20] one, okay? Ciao, ciao.
[00:21:22] Okay, let's take a look at narrow task
[00:21:25] decomposition. So, when uh Claude decom-
[00:21:28] decomposes a task, it can only delegate
[00:21:30] what it thinks to ask for. Okay, so here
[00:21:33] we have an example where it says, "Give
[00:21:34] me a comprehensive analysis of the EV
[00:21:36] market. Break the user's task into
[00:21:39] subtasks and delegate them out." And so
[00:21:41] here we see the subtasks. We have
[00:21:43] research EV sales figures, research EV
[00:21:46] battery technology, research major EV
[00:21:48] manufacturers. So, the initial
[00:21:50] decomposition is too narrow, entire
[00:21:53] topics never get researched. It's
[00:21:56] because each subagent only sees its uh
[00:21:58] its its own isolated context. None of
[00:22:01] them can flag what's missing. So, what
[00:22:04] got missed? Charging infrastructure,
[00:22:06] government policies and subsidies,
[00:22:08] second-hand EV markets, consumer
[00:22:10] sentiment and adoption barriers, supply
[00:22:12] chains like lithium and cobalt, grid
[00:22:15] capacity implications. Okay? Um so, you
[00:22:19] need to be very specific on the task so
[00:22:22] it fully covers what you expect. So,
[00:22:23] here it says, "Give me a comprehensive
[00:22:25] analysis of the EV market." Again, and
[00:22:27] so as the coordinator, when decomposing
[00:22:30] the task, of course we're generating out
[00:22:32] the the subtasks, but ask yourself,
[00:22:35] you know, more information. Ask subtasks
[00:22:37] to cover those gaps. Only then begin
[00:22:39] delegating. And for research tasks,
[00:22:42] specifically consider this information.
[00:22:44] Now, what's interesting here is like we
[00:22:46] created
[00:22:48] um in our our job application thing, but
[00:22:51] this thing is talking about research.
[00:22:52] So, they might they might have just a
[00:22:53] single subagent that just does research.
[00:22:56] And so the idea is that all these tasks
[00:22:57] are going to the same subagent as maybe
[00:22:59] separate um
[00:23:01] instances that are spawned, and they're
[00:23:03] being tasked with doing different
[00:23:04] things. And so this is where you have a
[00:23:06] little bit more complex routing, right?
[00:23:08] Or different kinds of routing. Um
[00:23:11] and so one thing that we can do to catch
[00:23:14] weak decomposition is uh cuz like let's
[00:23:17] say um for whatever reason,
[00:23:20] in here, uh this coordinator uh that you
[00:23:24] wrote here to help it be very specific,
[00:23:26] uh it fails or you just don't do a good
[00:23:28] job. Then you could implement a tool.
[00:23:31] And so the tool um can try to catch it.
[00:23:35] Because now when the court or when the
[00:23:37] agent goes and does a task, it's going
[00:23:40] to say, "Oh, did you submit a a subtask
[00:23:42] breakdown for review for delegating?"
[00:23:43] Well, then trigger this tool and then
[00:23:46] make sure right here that you do this
[00:23:48] up. And this gives you a guarantee um
[00:23:51] you know, of this. Or maybe you want to
[00:23:53] be a little bit more flexible what the
[00:23:54] input is from the user. And uh so this
[00:23:58] thing being decoupled might do that. Um
[00:24:01] another way uh that you can fix this
[00:24:03] problem is at the aggregate level. So,
[00:24:06] after you're aggregating the results, it
[00:24:07] can check here and say, "Hey, um did you
[00:24:09] make sure before writing the answer that
[00:24:11] you uh met these things?" And so you now
[00:24:13] have basically two different safeguards
[00:24:15] for um improving over uh narrow task
[00:24:19] decomposition. So, I'm not sure if this
[00:24:21] will work in the one that we're building
[00:24:23] right now or we'll have to build a new
[00:24:25] little coordinator. Um but we'll go and
[00:24:28] try it out, okay?
[00:24:30] All right, so we are back. And um what
[00:24:32] we'll do here is we'll try to figure out
[00:24:34] this narrow task decomposition. I don't
[00:24:36] know if it's going to work for our case.
[00:24:38] Because um for research, it's a really
[00:24:41] good um use case, but will it be for
[00:24:43] this one? I don't know.
[00:24:45] Um so, I'm going to go ahead and just
[00:24:46] copy all this code here because we
[00:24:48] already have some of this. Good.
[00:24:50] And Claude's going to have an easier
[00:24:51] time working
[00:24:52] with tweaking that.
[00:24:55] I would have an easier time working off
[00:24:57] of this.
[00:24:58] So, um
[00:25:01] let's go down to where the main
[00:25:03] coordinator prompt is. So, here it says,
[00:25:06] "Uh you're a job application screening
[00:25:08] coordinator. Your job is to orchestrate
[00:25:10] three independent screening agents and
[00:25:12] the aggregate their results. Run all
[00:25:14] three screening agents,
[00:25:16] keywords, deep evaluators, detectors.
[00:25:19] So, um let's go ahead and just ask it."
[00:25:23] Okay, so we'll go here.
[00:25:24] We'll say, um for our
[00:25:28] narrow task decomposition main
[00:25:31] for
[00:25:32] uh our coordinator prompt,
[00:25:36] is the uh decomposition
[00:25:40] um
[00:25:44] is our
[00:25:47] task decomposition
[00:25:49] too narrow?
[00:25:51] And what do we need
[00:25:54] to ask for better
[00:25:56] decomposition?
[00:26:00] Okay, because this one's pretty darn
[00:26:01] simple, right? It's just like there's
[00:26:03] these three things, feed it into those
[00:26:04] three things. Cuz it's not conducting
[00:26:06] research, right? Um it's not going out
[00:26:09] and looking at large bodies of text and
[00:26:11] trying to figure it out.
[00:26:12] So, you know, maybe if there was like
[00:26:14] more than one source, then that would be
[00:26:16] useful. And so maybe that's what we
[00:26:18] might recommend here in just a moment. I
[00:26:19] might say, "Hey, like uh you know,
[00:26:21] assume that you're ingesting more than
[00:26:23] one source of information, um and that
[00:26:25] might be a better example." But let's
[00:26:27] see what it comes back with here, and
[00:26:28] then I'll tell you whether I agree with
[00:26:29] it or not. Just because it will produce
[00:26:32] something doesn't mean that it's useful.
[00:26:33] So, we will find out here, okay?
[00:26:36] Also, I was just thinking about this.
[00:26:37] What we should have done is just taken
[00:26:39] the coordinator information and provided
[00:26:41] it uh to here with the basic information
[00:26:43] because I feel like it's consuming a lot
[00:26:45] more um tokens than it should require. I
[00:26:47] mean, it's not saying there's that many
[00:26:48] here, but it is taking uh some time
[00:26:50] here, and I again I'll just wait, but I
[00:26:52] should have really just extracted out
[00:26:54] that individual information.
[00:26:56] So, let's take a look here. And oh,
[00:26:58] yeah, we can edit the main file. That's
[00:26:59] fine, yep. I thought it was done. I
[00:27:02] guess it's not done.
[00:27:04] Okay, so let's take a look at the
[00:27:05] problem here.
[00:27:08] Spokes are narrowly scoped but
[00:27:10] appropriately interpretive. That's
[00:27:11] actually reasonable. But if you're
[00:27:13] designing new coordinators,
[00:27:16] well, I'm not designing new
[00:27:17] coordinators. But we'll we'll take a
[00:27:18] look here. Spokes answers what is X.
[00:27:20] Python found.
[00:27:23] But without access to the resume.
[00:27:30] Um spokes answers what does X mean for
[00:27:32] the higher?
[00:27:35] Receives pre-interpreted signals and can
[00:27:38] make the uh integrated judgment.
[00:27:41] So, I guess we're trying to determine
[00:27:43] like is it fine? So, what to ask? So,
[00:27:45] so is it narrow? So, is skill X listed?
[00:27:48] Does experience demonstrate the skills X
[00:27:51] required? So, if it's narrow, saying
[00:27:53] like is it just listed or is it actually
[00:27:56] telling us? So, that would be better.
[00:27:57] That's true.
[00:27:59] Uh narrow, resume only. And so this is
[00:28:01] what I was talking about where we would
[00:28:02] have more than one type of um
[00:28:05] uh information feed. But here it's
[00:28:06] saying in feed in the resume and the job
[00:28:08] posting for the fit.
[00:28:11] Context, what granu- granularity? So,
[00:28:14] one spoke per keyword, one spoke per uh
[00:28:18] decision dimension, whatever. So, this
[00:28:21] file runs both the coordinator of the
[00:28:22] same candidate.
[00:28:25] So, you can see how the narrow
[00:28:26] decomposition loses
[00:28:29] the 50 million requests per day nuance.
[00:28:33] While the better one catches it.
[00:28:35] Okay, so we'll go back up to here. I'm
[00:28:37] just trying to make clear the this thing
[00:28:39] that we're looking at. So, narrow
[00:28:40] antipattern.
[00:28:41] What is X? Python found.
[00:28:44] Six years, three, no gaps. That's
[00:28:46] probably like how actually recruitment
[00:28:47] people work. They aggregate receives new
[00:28:50] facts, it still has to do all the
[00:28:52] reasoning, but now without access to the
[00:28:54] resume.
[00:28:55] So, it spokes answers what does X mean
[00:28:57] for the higher?
[00:28:59] Strong trajectory risk. Okay, so one
[00:29:01] thing I I was thinking of is like
[00:29:04] you need to cross-coordinate this
[00:29:05] information, right?
[00:29:07] So, um
[00:29:09] I would say, you know, one thing one
[00:29:11] thing I noticed is, you know, can we
[00:29:14] validate
[00:29:16] the number of years
[00:29:20] based on based on the resume
[00:29:21] information?
[00:29:23] Can we mock
[00:29:25] other data sources that uh that we would
[00:29:30] feed in where uh if we didn't do better
[00:29:38] task decomposition
[00:29:40] with very specific
[00:29:42] things to check,
[00:29:44] we would run into an issue?
[00:29:47] Because that's I think what's going to
[00:29:48] take it, but like that was one example
[00:29:49] of like, okay, well, you know, if you
[00:29:51] had to validate how many years someone
[00:29:53] had experience, you'd look at the
[00:29:54] resume, but you might also look at uh
[00:29:56] projects or references or other stuff.
[00:29:59] And so, let's just see if it can, you
[00:30:00] know, consider other data sources.
[00:30:04] Uh maybe we should just want to do EV
[00:30:05] one because research is a really a
[00:30:07] really good one, but I mean in the sense
[00:30:08] like we are researching if there are
[00:30:10] multiple things. Like maybe they have
[00:30:12] blog posts and stuff like that. But
[00:30:14] we'll we'll see what comes back here and
[00:30:15] I might make send uh suggestions for
[00:30:17] data sources, okay?
[00:30:21] All right, it is back. Let's see what
[00:30:22] it's done. So, we'll go up to here. Key
[00:30:24] addition. So, show activity since 2018
[00:30:27] from uh a Git profile. Let's see. All
[00:30:30] All assessed skills are above senior
[00:30:32] threshold. Verified 7.6 years
[00:30:34] experience.
[00:30:36] Um
[00:30:38] okay. I mean, did it run it again? I
[00:30:39] didn't tell it to run it, but um
[00:30:42] I guess what we should do is just take a
[00:30:43] look
[00:30:44] at what the new coordinator information
[00:30:46] is.
[00:30:49] Your job is to coordinate uh three
[00:30:51] independent screening agents and then
[00:30:53] aggregate the results.
[00:30:55] I mean, this isn't
[00:30:57] this is showing steps, which is fine.
[00:30:59] But we're not seeing
[00:31:02] it doesn't seem to understand what I'm
[00:31:03] trying to tell it. Okay. So,
[00:31:06] No, I don't think it understands. So,
[00:31:08] what I'll do, just give me a second
[00:31:10] here.
[00:31:11] I need to give it an example and I just
[00:31:13] need to extract out of that.
[00:31:16] Give it a better example here and we're
[00:31:18] just going to plot I have my screenshot.
[00:31:20] I just don't have the raw data. And so,
[00:31:21] I'm just going to
[00:31:22] uh chat GPT or something here off screen
[00:31:24] be like, uh get me get me the text.
[00:31:29] Okay.
[00:31:30] And just give me just a moment here.
[00:31:32] Just getting the text here off screen.
[00:31:33] See, so getting the text.
[00:31:36] And I'm going to feed it as an example
[00:31:39] of like
[00:31:41] more information.
[00:31:47] Okay, so like
[00:31:51] we'll go back here.
[00:31:55] Uh so, you know, you know, you know, I
[00:31:57] don't think you understood.
[00:32:02] Uh to improve
[00:32:04] narrow task decomposition,
[00:32:08] we should be giving it
[00:32:11] specific
[00:32:14] considerations.
[00:32:19] Okay.
[00:32:21] Oh, no, I didn't say it to do that yet.
[00:32:23] Okay, we'll paste that in
[00:32:25] as an example, right? So, I don't know
[00:32:27] if it knows that's an example, but I
[00:32:28] think it might know.
[00:32:35] So, hopefully it understands cuz we're
[00:32:37] talking about this this area here.
[00:32:40] Um and if this fails, then we could just
[00:32:42] again just make it it might even try to
[00:32:43] change to EV, but we will see what
[00:32:45] happens here.
[00:32:46] Um and wait a moment and see what it
[00:32:48] comes back with.
[00:32:49] Okay, so
[00:32:54] some of your examples general through
[00:32:56] that Now, did it change it to EV stuff
[00:32:58] or is it actually changing it to uh
[00:33:01] a better part here. So, let's take a
[00:33:02] look here.
[00:33:03] So, what did it change?
[00:33:09] Let's take a look here. So, here's what
[00:33:11] changed. The domain EV. No, I didn't
[00:33:14] want you to change the domain. I just
[00:33:17] wanted you to use that as an example of
[00:33:21] uh specific task decomposition.
[00:33:24] Okay, so there it's already kind of
[00:33:26] messed up and I had a feeling that it
[00:33:28] would do that because I literally did
[00:33:29] not put e.g. or stuff in there. And
[00:33:31] maybe it's just that what we're trying
[00:33:33] to do does not work for our use case.
[00:33:36] Right? Maybe but it like I I still think
[00:33:37] it is because you are doing research.
[00:33:39] You're collecting information and and
[00:33:40] gathering it, but we're just assuming
[00:33:42] that we already have these things and
[00:33:43] doing analysis on that information. But
[00:33:47] uh you know, when you're doing broad
[00:33:48] research and there's a lot of
[00:33:49] information, then it can do do more
[00:33:51] there. So, revert the domain name, but
[00:33:53] we'll do self-reflection structure into
[00:33:55] the hiring coordinator.
[00:33:56] Um
[00:33:58] And so, we'll take a look at what it has
[00:33:59] and maybe we still will do the EV
[00:34:02] example separately.
[00:34:03] Um
[00:34:06] I mean, it still has these in here. So,
[00:34:07] I'm not sure what it was saying. I
[00:34:09] should don't save cuz I'm not trying to
[00:34:10] change that right now.
[00:34:15] Yeah, so like you are a research
[00:34:16] coordinator.
[00:34:17] >> [laughter]
[00:34:18] >> And uh I don't know if this is the way
[00:34:20] that uh the topic makes money where uh
[00:34:22] you tell something and it doesn't do the
[00:34:23] right thing and
[00:34:25] uh it's making more stuff here. But
[00:34:26] we'll wait a little bit, okay?
[00:34:28] All right, so it's back. And so, we say,
[00:34:29] okay, um back to original domain right
[00:34:32] in the pattern. What changed? Narrow
[00:34:33] coordinator mirrors
[00:34:35] the agent basic tells them all exactly
[00:34:37] the three checks. Fix the pipeline, no
[00:34:38] self-reflection. But that's not what I
[00:34:40] want. Better coordination. Same domain,
[00:34:42] same spokes. General initial screening
[00:34:44] angles. What am I missing? Fill the
[00:34:45] gaps.
[00:34:47] And you know, I think I think it's
[00:34:49] struggling here. Let's go back down
[00:34:50] here. So, we'll go and take a look here
[00:34:52] again.
[00:34:54] Well, here we have the
[00:34:55] narrow coordinator. So, it says here,
[00:34:57] screen the uh the candidate by running
[00:34:59] the following checks.
[00:35:01] And then down below here we have better
[00:35:02] coordinator. So, generate initial list
[00:35:05] of screening angles. Ask yourself, what
[00:35:07] perspective stakeholders or dimensions
[00:35:09] are missing? Add screening angles to
[00:35:11] cover those gaps. Only then begin
[00:35:13] delegating to screening agent tool. For
[00:35:16] hiring decisions, specifically consider
[00:35:17] technical skills and soft skills, hard
[00:35:20] requirements, what candidate has done
[00:35:22] and etc. After all screening angles are
[00:35:24] covered, synthesize report here. So, now
[00:35:28] I would imagine that it's basically just
[00:35:30] hitting a single agent. Yes, it is. And
[00:35:33] so, before we had those separated out
[00:35:36] tasks, right?
[00:35:38] But just as I thought, it's like in
[00:35:40] order to do it,
[00:35:41] um
[00:35:43] the idea is that you say you're you're
[00:35:45] screening agent and then you are
[00:35:47] contextualizing each one of it. So, in a
[00:35:50] sense, each of these are basically
[00:35:52] turning that into a specialized um
[00:35:55] a specialized one as before we literally
[00:35:57] had three separated one out.
[00:35:59] Right? So, that I think that's what
[00:36:00] we're getting at. So, that is what we
[00:36:02] want. That's actually good. So, we'll go
[00:36:04] all the way down here.
[00:36:05] And what we'll do is we'll go It says
[00:36:08] both the screen agent is identical both.
[00:36:09] The only variable is the coordinator
[00:36:10] prompt. So, with a uh hiring specific
[00:36:13] checklist of what the coordinator
[00:36:14] routinely uh looks for. So, let's go
[00:36:15] ahead and run that. I believe that's
[00:36:18] going to give us a better result. Okay,
[00:36:19] so we'll go here.
[00:36:21] We'll say, python main.py.
[00:36:24] I'll run it.
[00:36:28] And
[00:36:30] so, here it's going through it. So,
[00:36:34] and we're seeing the numbered values of
[00:36:36] what it's checking for.
[00:36:40] Okay.
[00:36:42] Does the resume demonstrate all the
[00:36:44] required skills? Does the candidate
[00:36:45] experience depth? Are there there any
[00:36:47] red flags?
[00:36:51] Has somebody else experience the
[00:36:53] limited?
[00:36:54] Um
[00:36:57] uh in the 5-8 senior range.
[00:37:00] No employment gaps or job hopping
[00:37:02] detected. The career directory is
[00:37:03] logical etc.
[00:37:05] Um and so, we have that there.
[00:37:09] This is the narrow one, right? So, fixed
[00:37:11] checklist, no gap check. Okay, so let's
[00:37:13] go down to the more complex one.
[00:37:15] Um
[00:37:17] So, we'll go down to this one. So, now
[00:37:19] we have way more information. So,
[00:37:20] instead of those three individualized
[00:37:22] things,
[00:37:23] um and remember there there was three
[00:37:25] separate things before. Now, we have
[00:37:28] um these I just want to compare the old
[00:37:29] one quickly here cuz I just can't fully
[00:37:31] remember.
[00:37:32] We go here.
[00:37:34] Yeah, notice that we have three
[00:37:36] individualized prompts. And even with
[00:37:38] the narrow one, I guess it's still only
[00:37:41] passing it through those three. And so,
[00:37:44] um that's interesting. But anyway,
[00:37:46] So, here does the candidate demonstrate
[00:37:47] mastery of etc. Okay, so we go down
[00:37:49] here.
[00:37:51] And
[00:37:53] I guess we can't really see the
[00:37:54] individualized results. So, that would
[00:37:55] be something that you might want to do
[00:37:56] is like
[00:37:57] output all of them and then save them
[00:38:00] and then save the generated uh final one
[00:38:03] to to exactly see what it is.
[00:38:05] So, core stack matches excellent. Okay.
[00:38:08] Risk and gaps.
[00:38:10] Questions for interviews. Final Final
[00:38:12] recommendation. Now, we have a maybe.
[00:38:14] Alex is qualified candidate, but has
[00:38:15] some gaps for a true senior role. Hire
[00:38:18] if your team values this passive
[00:38:19] whatever. Bottom line, Alex is a strong
[00:38:21] back-end engineer. And then we have
[00:38:23] coverage.
[00:38:24] So, it's way better in terms of its
[00:38:27] information. But really to test this,
[00:38:30] you'd actually have to um
[00:38:32] you know, create sample data, right? And
[00:38:34] test it and then and then adjust and
[00:38:36] say, hey look, uh this is not how I
[00:38:37] would have judged it, right? Based on
[00:38:38] that information. But this is the
[00:38:41] example that we wanted, but really that
[00:38:42] works when you know, there's a generic
[00:38:45] research agent and then these
[00:38:47] individualized things are going in and
[00:38:48] kind of helping to specialize that
[00:38:50] research agent for its task. Um but
[00:38:52] yeah, that was cool.
[00:38:55] All right, let's talk about dynamic
[00:38:56] selection. So, the idea here is that
[00:38:58] when you have your coordinator and you
[00:38:59] have sub agents, um you might uh find
[00:39:03] that if you run the entire pipeline for
[00:39:05] every single possible spoke uh in a
[00:39:08] sequence, that you are consuming as much
[00:39:11] as you can. And so, with your
[00:39:13] coordinator, you probably want to tell
[00:39:16] it to think about what kind of passing
[00:39:18] it needs or what kind of routing it
[00:39:20] should have and give it ideas of kind of
[00:39:23] routing that it can perform under
[00:39:24] certain circumstances so that it's doing
[00:39:26] exactly what it needs to do. Even here
[00:39:28] it's saying like, you know, uh only
[00:39:30] invoke it if it makes sense. Um and a
[00:39:32] way we can catch that problem. So, if we
[00:39:34] have a a poorly designed um
[00:39:38] uh dynamic selection system, you can set
[00:39:41] up a tool just like how we talked about
[00:39:43] with the narrow task decomposition, you
[00:39:44] could set up a tool that says, "Hey, did
[00:39:47] you do a good job here?" You can do the
[00:39:48] same thing with a tool as well.
[00:39:50] Um
[00:39:52] and I mean, it's really going to depend
[00:39:53] depend on what you're doing, but that's
[00:39:55] something that you know, you you'll want
[00:39:57] to consider, okay?
[00:39:59] Hey folks, we are back and we are going
[00:40:01] to try to do some dynamic selection. So,
[00:40:04] um you know, for hours, uh our our job
[00:40:07] application,
[00:40:09] um basically, we are taking in
[00:40:12] um information from from one thing, but
[00:40:14] basically,
[00:40:16] uh it's just checking everything. And
[00:40:18] so,
[00:40:19] you know, the question is like, can we
[00:40:20] even think of any kind of select dynamic
[00:40:23] selection that would be needed to be
[00:40:24] performed for a job application? Because
[00:40:26] I feel like it would be more if you were
[00:40:28] to ask certain questions to the agent
[00:40:31] along with this coordinator, then that's
[00:40:34] where it would want to choose different
[00:40:36] types of pathing. And so, I'm not
[00:40:37] exactly sure. We'll let it help us
[00:40:40] think of an idea, but I do want to
[00:40:41] remind that we are just doing this to
[00:40:43] learn. If you are doing this for real,
[00:40:45] write these things by hand yourself. Use
[00:40:48] your brain. That's how you're going to
[00:40:50] get the best result. Garbage in means
[00:40:53] garbage out. So, just cuz this thing
[00:40:54] works, doesn't mean that this is
[00:40:56] well-designed. We're just going through
[00:40:58] this
[00:40:59] uh to learn these concepts, right? Okay?
[00:41:02] Um I'm not saying that this is the best.
[00:41:04] But anyway, we'll go ahead here and make
[00:41:06] a new folder. This one will be called
[00:41:08] dynamic selection.
[00:41:10] Okay, and I'm going to go ahead and make
[00:41:12] a new main.py file.
[00:41:15] And I'm going to go ahead
[00:41:18] and select this code.
[00:41:22] And we're going to copy this.
[00:41:25] And we'll paste this
[00:41:26] into here. And so, I need to give it a
[00:41:29] concrete example of what we're talking
[00:41:30] about for dynamic selection.
[00:41:32] I do not have my text here. I put it in
[00:41:35] there. I'm going to get uh ChatGPT to
[00:41:37] extract it out just how we did with the
[00:41:39] narrow narrow one. So, just ask it to
[00:41:43] you know, extract out the text for me
[00:41:46] here. I'm just doing this off-screen
[00:41:47] here cuz I need to give it a practical
[00:41:49] example
[00:41:50] and try to describe what we're doing
[00:41:52] here. We're going to CD back a couple
[00:41:55] and we'll open that up.
[00:41:57] And so, we'll go here and just say,
[00:42:00] you know, I want to implement dynamic
[00:42:05] dynamic selection
[00:42:07] for my
[00:42:10] uh
[00:42:11] uh
[00:42:12] coordinator.
[00:42:15] Um
[00:42:16] so that it's
[00:42:18] not running the entire pipeline,
[00:42:21] but trying to choose
[00:42:24] the best uh things to run based on use
[00:42:27] case.
[00:42:30] Here is an example
[00:42:33] of good
[00:42:34] dynamic selection
[00:42:36] where we have
[00:42:38] different pipelines.
[00:42:40] Okay.
[00:42:42] You can use to uh help you.
[00:42:45] Okay?
[00:42:47] And the other thing is like, edit the
[00:42:51] dynamic
[00:42:53] selection main.py file. Okay. So, it's
[00:42:55] going to go off and do that and uh we'll
[00:42:58] see what it comes back with. Hopefully,
[00:43:00] something that is useful. But, you know,
[00:43:01] if we don't kind of guide and say like,
[00:43:03] these are the use cases, you know,
[00:43:06] I'm I'd be surprised if it doesn't come
[00:43:07] back with anything good, but we will try
[00:43:09] here
[00:43:10] um just for learning purposes, okay?
[00:43:12] All right, it's come back with
[00:43:13] something. Let's take a look at what we
[00:43:14] have.
[00:43:15] Um so, dynamic coordinator. Oh, we still
[00:43:19] have that narrow coordinator in there.
[00:43:20] We should really remove that out of
[00:43:21] there because it probably is confusing.
[00:43:24] We now have like three coordinators. Um
[00:43:28] I don't want to have three.
[00:43:31] So, [snorts]
[00:43:34] we'll go here. I'm just going to tell
[00:43:35] like,
[00:43:36] look, I I only need a single
[00:43:39] coordinator prompt. So,
[00:43:43] uh we'll
[00:43:44] I'm being lazy here. If we don't need
[00:43:47] the other ones, we can just delete them
[00:43:48] out, right? We have this narrow one.
[00:43:50] So,
[00:43:51] we know this one is not something we
[00:43:54] want, so we'll take that out.
[00:43:58] Then audits the gaps if we're delegating
[00:44:00] specific domains.
[00:44:01] And then here we have the dynamic one.
[00:44:03] So, we'll take this one out.
[00:44:05] Okay. Look at that. We wasted no tokens.
[00:44:08] There's no reason we can't do that. We
[00:44:09] don't have to prompt everything. Then
[00:44:11] we'll go down here and take a look. So,
[00:44:12] this coordinator reads the roles, then
[00:44:14] decides which dimensions actually
[00:44:15] matter. So, routing the logic.
[00:44:18] So, strong technical match or whatever
[00:44:20] whatever. Let's take a look and see what
[00:44:21] we have.
[00:44:22] So, routing guidance. Adapt to what you
[00:44:26] observe. Don't apply mechanically. So,
[00:44:28] simple factual match. Skip keyword scan.
[00:44:33] Go to straight to this. Non-traditional
[00:44:35] background. Transfer skills. Oh, this is
[00:44:37] cool. I like this. Never invoke a
[00:44:39] screening agent unless it's answers a
[00:44:41] real question. So, I think that actually
[00:44:43] um worked out perfectly.
[00:44:45] That's a great example of of that. And
[00:44:48] so, we'll go ahead here and I'm just
[00:44:50] going to go and run it. So, we'll CD
[00:44:52] into dynamic
[00:44:53] selection.
[00:44:55] This has actually been quite fun. Um is
[00:44:57] it useful? I don't know. Depends on what
[00:44:59] you're building.
[00:45:01] And oh yeah, we don't have the narrow
[00:45:03] coordinator. So, we'll go here and just
[00:45:04] make sure narrow coordinator.
[00:45:06] Um
[00:45:08] I want to get rid of these other ones. I
[00:45:09] don't want to waste all that here.
[00:45:14] And so, uh I'm just going to go back a
[00:45:16] step and just say,
[00:45:18] uh this should be fine. Let's just do
[00:45:19] that.
[00:45:21] I didn't realize there's more to rip
[00:45:22] out.
[00:45:23] I think it'll still work though.
[00:45:25] This is all three coordinators. There's
[00:45:26] only one though, right? Because I ripped
[00:45:28] them out.
[00:45:30] So, here it says, "Describe the most
[00:45:32] complex
[00:45:34] screening angles delegated."
[00:45:42] Okay. And the only the only way to
[00:45:43] really know if this is different
[00:45:49] What happened here?
[00:45:52] Uh we have narrow QS. We still have some
[00:45:54] of that remaining remaining code there.
[00:45:55] So, it's just some of this stuff.
[00:45:58] And so, I'll go ahead and try that
[00:45:59] again.
[00:46:04] I'm not sure if that will work if it's
[00:46:05] just a single item, but I'm hoping that
[00:46:06] it does.
[00:46:09] Um but here, um you know, my best guess
[00:46:11] is that it's choosing exactly what it
[00:46:13] needs cuz if we go back up to here,
[00:46:15] that's what it looks like it's doing.
[00:46:23] Oh my goodness. So, I'm going to go back
[00:46:25] a directory here
[00:46:27] um cuz this is very frustrating.
[00:46:31] Uh remove the better
[00:46:34] I only have a
[00:46:37] single coordinator.
[00:46:39] But, I remove some
[00:46:41] of the other code
[00:46:44] uh because I only really
[00:46:46] need a single coordinator here.
[00:46:49] Can you fix
[00:46:50] fix the code?
[00:46:52] You know what's funny is that sometimes
[00:46:54] like I will type things and every single
[00:46:56] letter will be wrong and it still knows
[00:46:57] what I'm saying because it like it does
[00:46:59] the off-shift, which I think is really
[00:47:00] cool. As someone that's dyslexic, as
[00:47:02] long as it understands me, I I love
[00:47:04] that. Um
[00:47:09] Yeah, and so, I'm just asking it to
[00:47:10] clean it up. I just want to make sure
[00:47:11] that it's in a working state before we
[00:47:12] move on here.
[00:47:14] All right. So, it thinks it's cleaned it
[00:47:15] up. We'll go into here again.
[00:47:21] And we'll run this again.
[00:47:24] So, screening angles detected.
[00:47:28] What I'm trying to determine when it
[00:47:29] runs here is like, how is it selecting
[00:47:31] stuff? So, in your current role at the
[00:47:32] fintech, what is the scale of your
[00:47:33] system that you worked on?
[00:47:35] Your transmission from this. Have you
[00:47:36] designed or refactored it?
[00:47:38] So, what it looks like it's doing
[00:47:40] is it's actually uh generating out uh
[00:47:43] possible angles based on this
[00:47:45] information. And so, it's literally
[00:47:47] creating dynamic routing on the fly. So,
[00:47:49] it's not like, here is a list
[00:47:52] that we had before here, but literally
[00:47:54] like, here are things that you can check
[00:47:55] and then choose what you want to put in
[00:47:57] here. So, it's not always applying the
[00:47:58] same thing.
[00:48:01] And we'll go back up to here.
[00:48:03] It's still conditional maybe, but yeah,
[00:48:05] we're getting something that is it's
[00:48:06] again very interesting to see this play
[00:48:08] out.
[00:48:09] Um again, you know, we don't know if
[00:48:11] it's actually useful,
[00:48:13] but it's fun to see the system working.
[00:48:16] Um and there you go, okay?
[00:48:18] Let's take a look at partitioning
[00:48:20] research. So, if you give three research
[00:48:22] agents the same brief, you get three
[00:48:26] overlapping answers and wasted tokens.
[00:48:28] So, if you're trying to paralyze things,
[00:48:31] right and say, "Research CV market.
[00:48:32] Research CV market." And they're all
[00:48:34] doing the same thing, that's going to be
[00:48:35] nonsense, right? So, carve up the scope
[00:48:37] so each agent owns a distinct slice. And
[00:48:41] so, here we are seeing partition
[00:48:42] information where um we are creating
[00:48:45] structured data and we're providing
[00:48:47] detailed information like topic, cover,
[00:48:49] excluded, things like that and providing
[00:48:52] that information there. And as per
[00:48:54] usual, we can create a tool that would
[00:48:56] check and make sure that we're dividing
[00:48:58] the research scope into non-overlapping
[00:49:00] assignments before delegation. What's
[00:49:02] really interesting here is that it's
[00:49:03] making a structure.
[00:49:05] Um and I mean, you know, in the last
[00:49:07] thing that we did, technically it is
[00:49:08] already kind of assembling um its own
[00:49:11] way of doing stuff, but um I suppose
[00:49:13] what we could do is we could generate
[00:49:15] out into partitions
[00:49:17] um in this sense and make sure that it's
[00:49:19] even more detailed in terms of what it's
[00:49:21] covering as an intermediate step um to
[00:49:24] make sure that it's not doing the exact
[00:49:25] same thing. But, this one's more focused
[00:49:27] on very specific things that it's
[00:49:28] researching.
[00:49:29] Um but yeah, the question is like, does
[00:49:31] our current one,
[00:49:33] even if it's not the exact same one, is
[00:49:34] it having overlapping tasks? And that's
[00:49:36] what we don't know. And so maybe um
[00:49:39] putting a structured structure a
[00:49:40] structure with partitions might help.
[00:49:43] But we'll have to experiment, okay?
[00:49:46] Okay, so let's see if we can implement
[00:49:49] partitioning in here.
[00:49:51] So what I'm going to do is make a new
[00:49:52] folder here called research
[00:49:54] partitioning.
[00:49:56] Partitioning.
[00:49:58] And we'll go ahead and make ourselves
[00:49:59] another new main.py file. We're having
[00:50:02] lots of fun here. And so we'll grab this
[00:50:05] wasn't this one this is the last one we
[00:50:06] worked on, right?
[00:50:08] Going to grab this here.
[00:50:11] Copy it.
[00:50:12] And
[00:50:13] um
[00:50:15] go all the way down.
[00:50:17] And oh wait, no no no this one's empty.
[00:50:19] Here we go. Okay. So now we are back
[00:50:21] with our dynamic one. So here we have uh
[00:50:24] off screen here I just told it to
[00:50:26] extract it out.
[00:50:28] Right? And
[00:50:30] um I'm going to just say here like, you
[00:50:32] know, I want to make sure I want to make
[00:50:35] sure
[00:50:37] um
[00:50:38] my
[00:50:40] uh research
[00:50:41] what are they called?
[00:50:45] What did they call them here?
[00:50:48] My research agent
[00:50:50] agents aren't wasting credits
[00:50:54] uh tokens by having
[00:50:57] and time by having uh overlapping
[00:51:01] tasks.
[00:51:03] And so I would like to have another
[00:51:08] step
[00:51:09] where we have uh partitions.
[00:51:13] Um
[00:51:15] And I mean like the thing is like you
[00:51:17] could manually make this stuff, but I'd
[00:51:18] rather just generate it out so it makes
[00:51:20] it easier for us. So we have partitions
[00:51:22] uh uh
[00:51:23] have a
[00:51:24] step where we generate out
[00:51:28] partitions
[00:51:30] based on a JSON structure.
[00:51:33] And then we can determine
[00:51:36] if there is
[00:51:39] if they are
[00:51:40] truly not
[00:51:42] doing the same task.
[00:51:45] Make sure to print out
[00:51:47] the structure so the human can uh see it
[00:51:52] on the run of the coordinator agent.
[00:51:57] Update the
[00:52:00] research partitioning main.py and here
[00:52:04] is an example
[00:52:07] of partitioning
[00:52:12] uh
[00:52:13] from a different use case.
[00:52:16] Okay. And so I'm going to copy this
[00:52:18] over.
[00:52:20] Bring it on over here.
[00:52:22] Right? And I'm hoping that this will
[00:52:25] work.
[00:52:26] Right? But I mean like this could also
[00:52:28] could just be like a static way. Like if
[00:52:30] you were just statically building a
[00:52:32] research agent
[00:52:34] that this would be a means to which you
[00:52:35] could do it and you don't have to
[00:52:37] delegate so much out to the agent if you
[00:52:39] will. But then now we're kind of relying
[00:52:42] more on
[00:52:43] um
[00:52:44] code driven logic. But you can mix them
[00:52:46] by the way. We didn't We didn't mention
[00:52:48] that, but you can take a hybrid approach
[00:52:50] where some of it is the coordinator and
[00:52:52] some of it is code driven. There's
[00:52:53] nothing wrong with it. There's no rules
[00:52:54] here, folks.
[00:52:56] There's no 100% bad. It's what you want
[00:52:58] to do, right? Um and so we will see if
[00:53:01] it can come up with something here and
[00:53:02] then we will review that code, okay?
[00:53:06] Okay, let's take a look and see what it
[00:53:09] thinks it's doing here. So
[00:53:12] uh narrow We still got this language
[00:53:14] like narrow versus better. I probably
[00:53:16] should get that out of there.
[00:53:20] Mhm mhm mhm. I really should be taking
[00:53:23] this out so that uh it's not getting as
[00:53:25] complicated
[00:53:27] here. So screening agent prompt You are
[00:53:30] a specialist hiring analyst. You will be
[00:53:31] given specific screening uh questions
[00:53:34] about a candidate. Answer the questions
[00:53:37] two to three focus sentences. Be
[00:53:39] concrete and specific. So really changed
[00:53:41] it in this case.
[00:53:42] Um
[00:53:44] Oh no no, this is fine. This is still
[00:53:46] the same.
[00:53:47] Runs a specialized agent, calls once per
[00:53:49] screening, etc. etc.
[00:53:51] Um
[00:53:53] I don't want Oh, I do not want multiple
[00:53:57] agents. Look, I don't want more more
[00:54:00] than one coordinator.
[00:54:03] Uh
[00:54:03] we don't need
[00:54:06] the narrow
[00:54:08] coordinator, okay? And so it's just
[00:54:10] because we copied it and I had some of
[00:54:12] the code still lying around and that's
[00:54:13] what's Oh, no no no no no no no no no no
[00:54:16] no.
[00:54:17] I just realized I was editing the wrong
[00:54:19] file.
[00:54:20] >> [laughter]
[00:54:21] >> Okay. So I went back there and I'm going
[00:54:23] to make sure I didn't muck that one up.
[00:54:26] Uh yeah, I don't want to muck with this
[00:54:29] one.
[00:54:33] Oh now I don't know.
[00:54:36] Did I break it good?
[00:54:38] Um
[00:54:42] Mhm.
[00:54:47] I think I can just go ahead here and
[00:54:49] discard the changes. I think it'll be
[00:54:50] fine.
[00:54:51] Okay. And so we'll go over to here and
[00:54:53] this is the one we actually wanted.
[00:54:55] And so it still has that logic in here
[00:54:57] which is kind of a problem, but I will
[00:54:59] see if it actually is an issue.
[00:55:02] Cuz we only have one, right? And I'm
[00:55:04] just going to remove it. I just don't
[00:55:05] want it to get confused.
[00:55:11] And I don't want to explain any of that
[00:55:13] here. So I'm just going to take that
[00:55:14] out.
[00:55:16] So let's take a look here.
[00:55:17] Says for both coordinators. So spoke
[00:55:19] system prompts. I'm just going to take
[00:55:21] that out.
[00:55:22] It keeps talking about like
[00:55:26] Okay.
[00:55:29] And now let's take a look here. So you
[00:55:31] are a partitioning uh a screen
[00:55:33] partitioning planner given a job posting
[00:55:35] resume. Output a JSON array of non
[00:55:38] overlapping screen partitions. Each
[00:55:40] partition object must have an agent, a
[00:55:43] scope.
[00:55:44] Um rules design partitions so that
[00:55:46] together they cover all relevant hiring
[00:55:49] questions. No two partitions may share
[00:55:52] the same cover uh cover aspect. Only
[00:55:55] include partitions that are genuinely
[00:55:56] needed for this candidate. I feel like
[00:55:59] uh we lost uh information here.
[00:56:04] We have
[00:56:05] Oh this is the planner part. Okay, so
[00:56:07] this is actually a separate part. Okay,
[00:56:08] so that just generates the partition,
[00:56:10] all right? And then down below here
[00:56:12] we have
[00:56:14] um
[00:56:15] the actual dynamic coordinator. So you
[00:56:17] you're here invoke exactly one screen
[00:56:19] partition call per partition, no more or
[00:56:21] less. Formulate the questions for each
[00:56:23] cell. Do not invent additional screening
[00:56:25] angles beyond the partitions provided.
[00:56:28] They were designed to cover all relevant
[00:56:30] dimensions without overlap. And so I
[00:56:31] mean like that's another way where it's
[00:56:33] just
[00:56:34] specifying it in a different
[00:56:37] way, but I guess it's generating out the
[00:56:38] partitions.
[00:56:40] So in the other one we literally listed
[00:56:42] out possible things and here it's
[00:56:44] generating them out. Oh here it is.
[00:56:47] Um
[00:56:48] Mhm.
[00:56:50] Is this good?
[00:56:53] Because before we had a list, right? So
[00:56:54] if we go back over to our
[00:56:57] um we'll just put this for a second.
[00:56:59] And we go back to our dynamic selection
[00:57:01] here.
[00:57:06] Right? And so here
[00:57:10] we had this, but we lost our routing
[00:57:11] guidance.
[00:57:14] So this is what I'm going to ask.
[00:57:18] I'm going to resume the last
[00:57:19] conversation we had.
[00:57:22] Going to make this a bit larger here.
[00:57:34] No. So does it We don't have it anymore,
[00:57:36] unfortunately. Or maybe I ran into a
[00:57:37] subfolder and that's my problem. So I'm
[00:57:39] going to go here and ask it like
[00:57:43] We have uh we have a dynamic
[00:57:47] What is it that we have? We have a
[00:57:51] uh
[00:57:52] research partition
[00:57:55] so that we don't have uh overlapping
[00:57:58] researchers doing the same thing.
[00:58:02] Did we lose
[00:58:04] uh
[00:58:05] selective routing
[00:58:08] based on task? Uh
[00:58:10] and do we need to
[00:58:13] bring that back in
[00:58:15] while preserving
[00:58:20] our partitioning?
[00:58:23] Okay. And so I'm going to go point to
[00:58:27] dynamic selection
[00:58:31] has the original
[00:58:33] prompt that had routing.
[00:58:38] And then here we have research
[00:58:39] partitioning
[00:58:43] is our um
[00:58:45] new prompt with partitioning.
[00:58:48] But the routing was removed.
[00:58:51] And so
[00:58:52] how would it know
[00:58:54] to do
[00:58:57] routing?
[00:58:59] Like do like how would it know
[00:59:02] to
[00:59:03] choose the appropriate
[00:59:06] dynamic selection?
[00:59:09] Okay. And so that's where I think
[00:59:12] there's a bit of an issue.
[00:59:14] Okay? Because sure, like we now it will
[00:59:18] generate out that structure and things,
[00:59:20] but how does it know to drive what to
[00:59:22] generate?
[00:59:24] Cuz it doesn't say that, right?
[00:59:26] And so dynamic both selects the angles,
[00:59:29] matters, and delegates. It has routing
[00:59:31] that skips the scan and strong matches.
[00:59:34] Now owns the selection step, but it has
[00:59:36] no routing rules. It just generates
[00:59:37] non-overlapping partitions without
[00:59:38] guidance which
[00:59:40] on which one will skip.
[00:59:44] And so here
[00:59:49] Okay.
[00:59:55] I'm just going to hit tab here.
[00:59:57] Okay, you are moving it
[01:00:00] back in, but are you thinking about
[01:00:04] how it will work
[01:00:06] or you're just dumping it back in?
[01:00:10] Okay?
[01:00:13] Because I could have done that.
[01:00:16] That doesn't mean that's a smart
[01:00:17] approach.
[01:00:19] And maybe that's all we need to do.
[01:00:21] But let's take a look and see what it
[01:00:23] comes up with.
[01:00:25] I'm telling you these things aren't
[01:00:26] smart, folks. You've got to
[01:00:29] think for it. So here we go. Fair point.
[01:00:31] Let me think about it. So we have
[01:00:32] partitioning that sees the resume and
[01:00:34] then the dynamic coordinator which sees
[01:00:36] the partitions. Where does the routing
[01:00:37] actually live now? So dynamic selection
[01:00:39] the coordinator was doing two of one
[01:00:40] things, deciding what to check and
[01:00:42] calling agents. Uh and the research
[01:00:44] partitioning now splits routing
[01:00:45] partition planner
[01:00:47] planner's job and then the coordinator's
[01:00:49] job. So the routing rules do belong
[01:00:52] to the partitioning planner, but they
[01:00:53] need to be reframed. In the original one
[01:00:55] it says never invoke the rules unless
[01:00:57] here we should say only create partition
[01:00:59] if the rules govern partition creation.
[01:01:02] The coordinator in the new architecture
[01:01:03] should stay as is. It's correct to be
[01:01:05] dumb selection because the decision was
[01:01:07] already made upstream.
[01:01:09] Uh giving it routing logic again would
[01:01:11] create a conflict of two places fighting
[01:01:13] over what gets evaluated. Um the
[01:01:15] partition planner currently says only
[01:01:18] include the partition genuinely needed.
[01:01:20] That's vague. Adding a specific
[01:01:22] heuristic routing. I mean like I would
[01:01:25] have thought
[01:01:26] and you might agree with me is that
[01:01:29] in the dynamic coordinator we had that
[01:01:31] list.
[01:01:32] Uh but the thing is is like it was
[01:01:34] saying like okay, if you do this then
[01:01:36] then do this or do that, but maybe the
[01:01:37] the problem was is that when we looked
[01:01:39] at the EV research, it literally had
[01:01:42] pipelines where in this dynamic router
[01:01:43] it just had things that you could choose
[01:01:45] from that you might want to consider.
[01:01:48] Okay, but it wouldn't run them all.
[01:01:50] So here it says we receive a set of
[01:01:52] pre-planning partitions as JSON.
[01:01:55] Invoke exactly one screening agent.
[01:01:59] Uh-huh.
[01:02:02] Okay, well let's just see what we get.
[01:02:05] Okay.
[01:02:08] I'm not sure if I like it, but
[01:02:11] we're trying here, right?
[01:02:13] And we'll go main.py and we'll run it.
[01:02:18] And see what happens.
[01:02:22] So we have we have
[01:02:24] core stack proficiency.
[01:02:33] Assess REST API capabilities.
[01:02:37] Okay, so we have here
[01:02:39] um core stack proficiency. Evaluate
[01:02:40] mastery of required technologies
[01:02:42] directly matching the job stack.
[01:02:47] Uh-huh. Access REST API design
[01:02:49] capabilities.
[01:02:52] Evaluate exposure to scaling patterns
[01:02:54] and nice-to-have technologies. Confirm
[01:02:56] senior-level experience.
[01:03:02] And then here we have screening angles
[01:03:04] delegated. Does the candidate
[01:03:05] demonstrate mastery of required stuff?
[01:03:08] Uh okay.
[01:03:13] And here we're getting partials. So we
[01:03:15] have a maybe recommendation. Alex is
[01:03:17] qualified to mid to senior.
[01:03:21] And we have different coverage. So I
[01:03:23] still don't know this is better. I mean
[01:03:24] like we should be dumping all these logs
[01:03:27] out and then comparing them and then and
[01:03:28] doing stuff. So obviously we were just
[01:03:30] trying to meet the requirements of
[01:03:33] learning this stuff and kind of having a
[01:03:35] sense of it, but is it good? Is it is
[01:03:37] another question that will take more
[01:03:38] time and I'm going to keep repeating
[01:03:40] that because I just want you to know
[01:03:41] just cuz we're doing it doesn't mean
[01:03:42] it's great.
[01:03:44] And you should be thinking about like
[01:03:45] okay, if I had these three four
[01:03:47] different ways um you know, determine
[01:03:49] usage, determine outcomes, have your
[01:03:51] examples. Don't have them for you here.
[01:03:53] That'd be a lot of work for me to set up
[01:03:54] for you. Um but uh yeah, it's
[01:03:57] interesting trying to try out these
[01:03:59] techniques and apply them, okay?
[01:04:01] Let's take a look at a refinement loop.
[01:04:03] So the idea right now is that um
[01:04:05] everything's been one shot. The idea is
[01:04:07] it goes through it, it produces an
[01:04:09] evaluation and then then it's over. But
[01:04:11] what if we could feed it back in the
[01:04:13] loop and refine it until we are happy
[01:04:14] with it and that's the idea behind a
[01:04:16] refinement loop to make our research
[01:04:18] system really really good.
[01:04:20] Um so if you look at this prompt here
[01:04:22] for our coordinator the idea here is
[01:04:24] that we are telling it that we can have
[01:04:26] up to maximum four refinement iterations
[01:04:29] and that we are going to delegate the
[01:04:31] information back into here. And so
[01:04:33] you'll notice here we have like an
[01:04:34] evaluation coverage and when to submit
[01:04:37] final uh and uh
[01:04:40] uh creating the synthesis and things
[01:04:42] like that. And so we will go ahead and
[01:04:44] try to apply refinement loop to our um
[01:04:49] our agent, okay?
[01:04:51] Hey folks, this is Andrew. In this video
[01:04:53] we're going to implement our own
[01:04:54] refinement loop. Uh so what we'll do as
[01:04:56] per usual, I'm going to go ahead and
[01:04:58] make a new folder. This will be my
[01:04:59] refinement
[01:05:01] loop.
[01:05:03] Okay. And then what we're going to do is
[01:05:06] we're going to go ahead. Let's just grab
[01:05:08] our code here, main.py. We're going to
[01:05:10] go grab our last one which was research
[01:05:12] partitioning.
[01:05:14] Cuz we're building off of it every
[01:05:16] single time trying to make this thing a
[01:05:17] little bit better. And we are going to
[01:05:21] implement the refinement loop. I need to
[01:05:23] extract the text out because again I I
[01:05:26] don't have it on on hand, but let me go
[01:05:28] grab it from that slide, okay?
[01:05:31] There we go. I grabbed it. And if you
[01:05:32] want to grab it, too, all you got to do
[01:05:33] is take a screenshot, feed it to Claude
[01:05:35] or ChatGPT and extract it out, folks. Um
[01:05:38] because you can. You can. Make sure you
[01:05:40] do that, okay? It's not hard. Just
[01:05:44] build up those skills, okay?
[01:05:45] So I'm going to go ahead here and just
[01:05:47] CD out here. We're going to go into our
[01:05:49] Claude. And um you know, I need to
[01:05:54] implement a refinement loop
[01:05:57] um
[01:05:58] uh in my agent for
[01:06:03] research
[01:06:04] partitioning main. Here is uh a example
[01:06:11] from another
[01:06:14] use case
[01:06:15] you can use as inspiration.
[01:06:20] As guidance.
[01:06:22] Okay. And so I'm going to paste that in
[01:06:24] there. And so the idea though is that
[01:06:26] with that information
[01:06:28] I'm hoping that it can develop that
[01:06:30] refinement loop in here. So we will see
[01:06:32] what it produces, okay?
[01:06:34] All right. So in here we have um
[01:06:37] changes. Let's take a look and well it's
[01:06:38] still trying to edit stuff. So yes.
[01:06:41] Um
[01:06:42] and let's see
[01:06:44] uh what we have. Okay, so it is bringing
[01:06:48] in
[01:06:49] um evaluate coverage. Okay, so we have
[01:06:53] that.
[01:06:54] Uh submit final. So it's setting
[01:06:56] different states based on whether
[01:06:58] you know, higher maybe or pass. Only
[01:07:00] call this when the evaluation confirms
[01:07:02] uh sufficient coverage.
[01:07:04] And final recommendation. So we have
[01:07:06] that in our loop.
[01:07:07] Here it is adding the evaluation agent,
[01:07:10] okay?
[01:07:12] And we have some tweaks here. So we have
[01:07:13] initial screening. Invoke exactly one
[01:07:15] screening agent call per partition.
[01:07:20] Formulate each question. That's fine.
[01:07:21] Phase two, evaluate coverage. After all
[01:07:23] initial partitions agents have reported
[01:07:25] call evaluation coverage with plain
[01:07:27] text.
[01:07:28] And here we have refinement max three
[01:07:29] iterations. If the evaluation coverage
[01:07:32] returns sufficient false
[01:07:34] invoke screening agents to fill only
[01:07:36] identified gaps.
[01:07:37] Uh call submit final etc. etc. Do not
[01:07:40] call the submit final before evaluation
[01:07:42] uh if it's only once, okay? So here is
[01:07:45] obviously done a lot. I'm kind of
[01:07:47] curious to think like maybe it's just
[01:07:48] like you're brute forcing to make it
[01:07:50] either that you really want this person
[01:07:51] or you really don't want this person.
[01:07:53] It'd be interesting to have a larger
[01:07:54] data set like let's say 100 applicants
[01:07:56] and you ran it through and to see if it
[01:07:58] just skewed it to one location or or one
[01:08:00] side or not. Um but it'd be very
[01:08:03] interesting to find out, but we'll go
[01:08:05] back up to
[01:08:07] here and so we can see the changes.
[01:08:11] And let's go and run this thing.
[01:08:14] Notice as we are progressing it's
[01:08:15] becoming easier and easier for us to
[01:08:18] update our agent. And so far we've been
[01:08:20] just using the Anthropic um SDK not
[01:08:24] using the agent SDK. The agent SDK is
[01:08:26] awesome, but uh
[01:08:27] we will just continue on here. It'd be
[01:08:29] interesting to convert it over and see
[01:08:30] what the code looks like and we'll
[01:08:32] probably do that. Um but let's go ahead
[01:08:34] and do python main.py and we'll go ahead
[01:08:36] and run that. And the idea it's going to
[01:08:39] run it says dynamic coordinator.
[01:08:40] Obviously it's the refinement one. We
[01:08:41] don't change those names. And so here
[01:08:44] reads candidates first, routes to the
[01:08:46] relevant checks only. So evaluate depth.
[01:08:50] Access to database caching. Verify API.
[01:08:53] Confirm senior-level experience.
[01:08:55] And
[01:08:57] is the candidate senior level? Okay,
[01:08:58] great. So now we're going into iteration
[01:09:00] one.
[01:09:02] Okay.
[01:09:04] So we have coverage score, code quality
[01:09:06] practices, no evidence etc. etc. And so
[01:09:09] it is going again here.
[01:09:13] Asking questions.
[01:09:17] They are I think they are different
[01:09:18] questions.
[01:09:20] It's hard to be because we have the this
[01:09:21] up here, right? And then down below
[01:09:24] Oh look, the the coverage score is going
[01:09:26] down now. Interesting.
[01:09:31] And so we are done and over with.
[01:09:34] We'll go and uh look up here. So did two
[01:09:37] iterations.
[01:09:39] And their score went down.
[01:09:43] So yeah, that's iteration loop. Is that
[01:09:45] good? I don't know. It takes a lot of
[01:09:47] work to evaluate this stuff. We would
[01:09:49] spend hours hours upon hours tweaking
[01:09:52] this
[01:09:54] to figure out is this valuable
[01:09:56] information? Is our data set good? Etc.
[01:09:58] etc.
[01:09:59] There's no magic here, folks. We can
[01:10:02] uh code these out very quickly, but to
[01:10:04] make sure they actually work good is a
[01:10:05] different story. I'm going to keep
[01:10:06] repeating that because it's true. Uh but
[01:10:09] that is what the refinement look uh
[01:10:11] refinement loop looks like, okay?
[01:10:14] Okay, folks. Let's take take a look at
[01:10:16] observability. So the idea of having
[01:10:19] this centralized coordinator is the fact
[01:10:21] that everything's going to pass through
[01:10:22] it, okay? So no matter who has to talk
[01:10:25] to who, it's going to pass that
[01:10:27] coordinator. And because of that, um the
[01:10:29] coordinator is at a choke point where it
[01:10:31] can observe um anything and catch any
[01:10:33] kind of errors because it is
[01:10:35] coordinating stuff. But when you uh do
[01:10:37] not have that, then everyone is just
[01:10:38] communicating with each other and you
[01:10:40] can't observe what was said. You can't
[01:10:42] catch errors consistently. You can't
[01:10:43] control what information crosses
[01:10:45] boundaries. But the coordinator can do
[01:10:47] all those things. And so we are using
[01:10:49] the coordinator pattern.
[01:10:51] Um do we have observability? That's a
[01:10:53] good question. So I would say let's go
[01:10:54] back to our thing and see uh if it is
[01:10:57] working. I would probably ask like,
[01:10:59] "Hey, can it actually wrote to other
[01:11:00] ones and is it capturing information?"
[01:11:02] Um
[01:11:03] I know it already probably is working
[01:11:05] this way, but let's confirm and go back
[01:11:07] to our code, okay?
[01:11:09] Hey folks, we are back and I'm going to
[01:11:11] make a new folder and this will be uh
[01:11:13] coordinator observability.
[01:11:15] Because the idea here
[01:11:18] is that our coordinator should act as an
[01:11:20] observable layer. And so I want to make
[01:11:22] sure that it actually is doing that. So
[01:11:24] let's go
[01:11:26] back here.
[01:11:27] And we'll uh
[01:11:28] uh go into um Well, we'll type cloud
[01:11:31] here, right? And we already have the
[01:11:33] refinement loop over here. So I'm going
[01:11:35] to go ahead and grab all this code.
[01:11:39] Okay, I'm going to grab all this code
[01:11:41] and we'll make a new file called
[01:11:42] main.py. You're starting to get the
[01:11:44] pattern here what we're doing, right?
[01:11:46] Very repetitive, but it really is good
[01:11:48] in iteration. So um what I want to
[01:11:51] figure out is do we actually have those
[01:11:53] values? Is the coordinator acting like a
[01:11:56] coordinator? So um
[01:12:00] I'm just thinking about this for a
[01:12:01] second. So what we want to do,
[01:12:03] so we're going to say uh I have an agent
[01:12:07] uh a coordinator agent
[01:12:10] uh here. So we'll say uh coordinator
[01:12:15] observability.
[01:12:19] Here, I'm going to put this in a plan
[01:12:21] mode. Here are the questions I have. Is
[01:12:24] my coordinator
[01:12:26] operating from observability level?
[01:12:31] Observability and
[01:12:33] um
[01:12:35] uh
[01:12:36] I'm trying to think of what like and
[01:12:38] controlling controlling flow of
[01:12:40] information.
[01:12:42] Uh you know,
[01:12:43] is it uh
[01:12:46] managing, you know, like is it I'm
[01:12:48] trying to think like here. I have a
[01:12:49] coordinator agent, right?
[01:12:52] Here are the questions I have. Is my
[01:12:53] coordinator operating operating from uh
[01:12:55] uh operating
[01:12:57] with an observability layer?
[01:13:01] So we can capture
[01:13:05] uh any errors.
[01:13:07] All messages that that that are being uh
[01:13:09] sent to our spokes.
[01:13:13] Sub agents.
[01:13:16] Is it controlling
[01:13:19] context in what is passed
[01:13:22] uh to my um
[01:13:25] uh spokes
[01:13:27] and only those sub agents
[01:13:34] can talk to the coordinator.
[01:13:41] Right?
[01:13:44] Is there something I am missing
[01:13:48] to make my coordinator
[01:13:53] a good coordinate coordinator, right?
[01:13:55] That's what we want to know. And we'll
[01:13:56] go ahead and hit plan there. You're
[01:13:57] thinking, "Well, you know,
[01:13:59] you're just writing whatever out." But
[01:14:00] that's that's a fine problem. You can't
[01:14:02] make perfect prompts here, folks.
[01:14:04] I mean, you can make better prompts
[01:14:05] yourself and spend time engineering
[01:14:08] them, but this is good enough to start
[01:14:09] getting some information. So let's see
[01:14:11] what it comes back with. And I'd be
[01:14:12] curious to uh layer something here uh
[01:14:15] there. So I'm just curious what we can
[01:14:17] do
[01:14:18] um to make our observability better.
[01:14:21] Um but we will wait for that generation,
[01:14:23] okay?
[01:14:25] Okay, so let's take a look and see what
[01:14:28] it thinks.
[01:14:29] Um So we'll go all the way to the top
[01:14:31] here. So
[01:14:32] the user's coordinator uses a
[01:14:34] partition-based hub-spoke pattern for
[01:14:36] job screening. They want to know, does
[01:14:37] it have proper observability? Does it
[01:14:39] capture all messages to spoke? Does it
[01:14:40] control context passed to spokes? Is Is
[01:14:43] the spoke-coordinator communication
[01:14:44] isolated? What is missing to be a good
[01:14:46] coordinator? So it says observability is
[01:14:47] weak. I absolutely agree. We haven't
[01:14:49] done anything for it. Um
[01:14:52] Could we do something better than just
[01:14:54] Oh, yes, it's only print statements. I
[01:14:55] agree with that. Um
[01:14:57] uh error handling anywhere it says JSON
[01:14:59] loads. Yeah, that makes sense. API level
[01:15:01] tracing. No token counts. No latency. No
[01:15:03] request IDs. Yeah, token counts would be
[01:15:05] really useful.
[01:15:06] Uh no persistent audit trail of all
[01:15:09] output and ephemeral stdout. We have
[01:15:11] message capture partial. So delegate
[01:15:13] list. We are printing some stuff, right?
[01:15:15] Cuz I told it to do that, but um
[01:15:18] Tracks questions sent to spokes. Spokes
[01:15:20] responses are never stored. They go
[01:15:22] straight into the tool results and are
[01:15:24] lost out of the coordinator. No record
[01:15:26] of partition each question uh uh
[01:15:28] addressed X. No log of coordinator's own
[01:15:31] reasoning text between tool calls. Mhm.
[01:15:35] Every spoke receives the full job
[01:15:37] posting.
[01:15:39] And so it's saying context control
[01:15:40] loose. Resume regardless of its
[01:15:42] partition.
[01:15:43] I mean, it would need it anyway, right?
[01:15:45] Like all of them need it. So we're not
[01:15:46] really giving them separate data.
[01:15:48] Uh regardless of its partition scope.
[01:15:52] So cover exclude is only advisory passed
[01:15:56] by JSON to the coordinator prompt, but
[01:15:58] not enforced at the spoke level.
[01:16:00] Uh the coordinator uh could ask any
[01:16:02] question. No mechanism validates the
[01:16:05] question stays within the uh assigned
[01:16:07] partition.
[01:16:09] Fair enough. Spoke isolation one
[01:16:11] direction one directional enforce. So
[01:16:13] spokes are stateless functions called by
[01:16:14] the coordinator. No cross no cross spoke
[01:16:18] communication. So that's good. But
[01:16:20] spokes have no awareness of their
[01:16:21] assigned partitions. They can't reject
[01:16:23] out of scope questions. Oh, that's
[01:16:24] actually a good good point. No
[01:16:27] uh only these spokes can talk to
[01:16:29] coordinator mechanism is just a single
[01:16:31] plane one. So where are gaps? Can't
[01:16:34] debug or audit the run. Silent crashes
[01:16:36] on failures. Can't replay or inspect
[01:16:38] what's wrong. Coordinator doesn't know
[01:16:40] if all dimensions are covered mid run.
[01:16:42] Recommendation may be issued before all
[01:16:44] uh angles are addressed. Spokes are all
[01:16:47] data even if relevant. All partitions
[01:16:49] even if some obviously irrelevant. A
[01:16:51] single pass cannot fill gaps during it.
[01:16:53] And also our data like if I'm really if
[01:16:55] we maybe want to make this better, we
[01:16:57] would be sending like different payloads
[01:16:58] of different information to specific
[01:17:00] research agents. But right now
[01:17:02] everyone's getting the same job posting.
[01:17:03] Um So here they have recommend fixes so
[01:17:06] structured logging with timestamp
[01:17:08] levels.
[01:17:09] That seems good. Uh that's fine, sure.
[01:17:12] And it's going to log that out. Error
[01:17:14] handling. So wrap the JSON load.
[01:17:16] Generate the partition.
[01:17:18] Uh persist spoke inputs outputs so
[01:17:20] extend beyond the tracking.
[01:17:22] Add coverage evaluation tool at at
[01:17:24] explicit gates.
[01:17:26] Force the coordinator to call submit
[01:17:27] final.
[01:17:29] And so these are fine.
[01:17:31] Um
[01:17:33] The
[01:17:36] only challenge here is I don't I feel
[01:17:38] like there's a lot of tasks here. So I'm
[01:17:39] just going to go here and say,
[01:17:40] "There is a lot of am concerned
[01:17:44] uh you will
[01:17:46] uh not be able to remember all the
[01:17:49] tasks.
[01:17:51] Can you create
[01:17:53] this uh plan in a readme with a task
[01:17:57] checklist?
[01:17:59] And can you
[01:18:01] check off
[01:18:02] the tasks
[01:18:04] as you complete them?"
[01:18:07] Okay. And so the goal there is to help
[01:18:10] it out a bit. Um that's not exactly
[01:18:12] spec-driven development, but the only
[01:18:13] thing is like if we really wanted this
[01:18:15] to drive and be really good, we would
[01:18:17] want something that would clear context
[01:18:19] each time. But we're not set up that
[01:18:21] way. I'm not here to roll a a small
[01:18:23] spec-driven development little thing for
[01:18:26] us here. So that's totally fine.
[01:18:28] And um
[01:18:31] readme with tasks and checklist.
[01:18:34] As long as it knows what it's doing
[01:18:35] that, that's fine. But where's it going
[01:18:36] to put that file?
[01:18:38] Yeah, I'm just going to trust that it
[01:18:39] can do it.
[01:18:40] Let's go ahead and let her rip.
[01:18:44] Okay? Um and so the idea again here is
[01:18:47] to improve observability and we will
[01:18:49] uh see how that goes. Another thing is
[01:18:51] like I would imagine that if you were to
[01:18:53] put this into production, you want to
[01:18:54] productionize it, you might want to
[01:18:56] contain these sub agents into
[01:18:57] containers. And then you might want to
[01:18:59] use Otel
[01:19:01] as another observability layer.
[01:19:03] That's how I'm kind of thinking about
[01:19:04] it.
[01:19:05] But we're keeping it all monolith for
[01:19:07] now and we're not going to overly
[01:19:09] complicate it at this stage. Um and I'm
[01:19:11] going to let it go and burn away all my
[01:19:13] credits. Look at that. 6.2 thousand
[01:19:15] credits. Wow. Let's go over here. It's
[01:19:18] like the worst time to do this. People
[01:19:19] are like there's a on Twitter they're
[01:19:21] like, "Oh, it's down." And the usages
[01:19:24] are gone and stuff like that. It's me.
[01:19:26] It's me. I'm the I'm the problem.
[01:19:29] So go over here and right off the bat
[01:19:31] like we are
[01:19:33] Oh, resets in 9 minutes though, that's
[01:19:34] really good. But we're only 33% Well,
[01:19:35] let's burn, burn, burn, baby. Though my
[01:19:38] week is is is getting up to use very
[01:19:41] quickly there. Um but anyway,
[01:19:46] Oh, yeah, it's it's going up. So, yeah,
[01:19:49] we're going to consume tokens like it's
[01:19:51] nobody's business.
[01:19:52] Um but I think it'll be worth it for
[01:19:54] this stage of the thing as we are
[01:19:57] continually refining it, okay?
[01:19:59] Uh that was fast. I feel like it should
[01:20:01] have taken longer than that. All six
[01:20:02] fixed fixes are implemented. I mean, I
[01:20:04] would rather have been more granular and
[01:20:06] clearing contacts between it so that we
[01:20:08] would have um
[01:20:10] you know,
[01:20:10] better stuff. Well, that's fine. So, is
[01:20:11] my coordinator operating with
[01:20:12] observability? No, it had only print
[01:20:14] statements, etc., etc. What was I
[01:20:16] missing? Error handling, mid-run gap
[01:20:18] detection, no exit gate. And I'm not
[01:20:20] even saying like this is the best, but
[01:20:23] um you know, it's pretty good for
[01:20:26] us throwing things here together. Let's
[01:20:27] see if we can see what I mean, it
[01:20:29] probably will just tell us what code
[01:20:30] changes were made.
[01:20:32] I suppose that's the easiest way to
[01:20:33] check.
[01:20:35] And um
[01:20:37] I'm just going to go all the way up
[01:20:38] here. Let's take a look here. So, we've
[01:20:39] added logging, okay?
[01:20:43] And we are implementing the logger.
[01:20:46] Here, it says scope to each partition.
[01:20:50] Partition agent name uh is the names the
[01:20:53] question belongs to from the partition
[01:20:54] JSON. Okay, so it's being very
[01:20:56] particular to make sure that it's
[01:20:57] scoped. That's good. Evaluate coverage.
[01:20:59] So, mid-run gap detection tool. Evaluate
[01:21:02] whether the screening finds are
[01:21:03] efficient to make a confident
[01:21:04] recommendation.
[01:21:06] Um confident that all partitions agents
[01:21:09] have reported. Return a coverage score,
[01:21:11] etc., etc.
[01:21:13] Okay, submit final explicit exit gate.
[01:21:16] Submit the final hiring recommendation
[01:21:18] only this
[01:21:20] Call this only after evaluate coverage.
[01:21:22] Fair enough.
[01:21:24] So, go down below here.
[01:21:26] Mhm. Fix error handling.
[01:21:30] So, here we have
[01:21:34] uh
[01:21:35] Here's down the error handling down here
[01:21:37] below. Fair enough. That's very basic.
[01:21:39] That's not really that important.
[01:21:42] And then we have the screening agent.
[01:21:46] So, we are seeing
[01:21:50] Oh, to scope it in the boundary, right?
[01:21:52] So, making sure that it's scoped.
[01:21:54] Fair enough.
[01:21:57] Here we have rule changes.
[01:22:00] And so, it's about passing that
[01:22:02] information and it's talking about that
[01:22:03] evaluation coverage in the final
[01:22:04] recommendation.
[01:22:08] Okay. And then we got logs, logs.
[01:22:17] And more logic. Now, this thing is
[01:22:19] pretty wild. I would probably want to
[01:22:23] take it farther and refactor it, but I
[01:22:25] don't really want to uh
[01:22:27] Like this is just this is a mess. Like
[01:22:29] this is not how you should have your
[01:22:31] code base. But I don't want to go
[01:22:34] overboard at this stage. I just want to
[01:22:36] make sure that this works.
[01:22:37] Okay, so what we're going to do cuz I'm
[01:22:39] expecting logging to appear, right?
[01:22:41] Um
[01:22:45] And so, I would probably say like we
[01:22:46] could just run it.
[01:22:48] But the other challenge would be like we
[01:22:50] need actual ways to test that the stuff
[01:22:52] works. So, probably what would have been
[01:22:54] better
[01:22:55] but it would have taken a lot like this
[01:22:56] would have took an hour or two and you
[01:22:57] folks don't want to wait around that
[01:22:59] long to test that. But what I would have
[01:23:00] done if we had the time and you wanted
[01:23:03] to go through it, what I would do is I
[01:23:05] would stage
[01:23:07] examples and and and I would want to see
[01:23:09] if like we could pollute um
[01:23:12] pollute the context between agents and
[01:23:16] make sure that it is only receiving
[01:23:19] proper questions and it rejects it and
[01:23:20] those would be things that we test for.
[01:23:22] So, we really are skipping a lot of that
[01:23:25] stuff and that's stuff that you would
[01:23:26] still have to do. But just because I'm
[01:23:28] not doing it here doesn't mean that I
[01:23:29] wouldn't do it. Um it's just I'm not
[01:23:31] doing it because you folks don't like
[01:23:33] when I make like two, three-hour videos.
[01:23:35] Um even though that's the actual effort
[01:23:37] for the work and I can't really just
[01:23:40] you know, fake that along, right? So,
[01:23:42] we'll go ahead and we'll run that. I
[01:23:43] think it's spelled observability wrong,
[01:23:44] which is fine. And so, what I'm
[01:23:46] interested in is do we get any logging?
[01:23:48] Where is our logging? I don't see it.
[01:23:51] Okay.
[01:23:53] I mean, it's just going to ST out. So,
[01:23:55] it's not logging to anywhere in
[01:23:57] particular.
[01:24:04] Which is fine. Uh so, I you know, I'd
[01:24:06] probably just have it log to like into
[01:24:08] in a log directory and that's
[01:24:10] the only thing that might be missing
[01:24:11] here.
[01:24:19] Okay.
[01:24:23] And I'm just going to wait for it to run
[01:24:24] Oh, there we go. There it's done.
[01:24:26] And so, we have our final information.
[01:24:27] Did it call that final evaluation step?
[01:24:32] Yeah, final recommendation. There it is.
[01:24:35] So, there you go. That's all it took to
[01:24:36] improve it.
[01:24:38] Definitely better than what we had
[01:24:39] before.
[01:24:41] Um but yeah, I would probably want to
[01:24:42] refactor this so that's
[01:24:45] like you shouldn't have one big dumb
[01:24:46] file like this. Um and so, we might do
[01:24:49] that in a separate video. Especially if
[01:24:50] we want to convert it over to the agent
[01:24:53] SDK to compare. That might be something
[01:24:54] we might want to do, okay? Um but yeah,
[01:24:57] now we've added observability.
[01:24:59] Hey folks, it's Andrew and in this
[01:25:01] video, what I want to do is I want to
[01:25:02] refactor our coordinator that we've been
[01:25:04] working on up to this point as I'm going
[01:25:07] to want to port it over maybe to agent
[01:25:08] SDK to just take a look and see what
[01:25:10] that looks like. And so, we're just
[01:25:12] going to say
[01:25:13] um uh coordinator
[01:25:15] refactor here.
[01:25:17] And I'm going to go ahead and grab the
[01:25:19] code here.
[01:25:21] And we are going to ask it
[01:25:23] to refactor.
[01:25:25] Um and let's just see if we can make
[01:25:27] this a little bit more maintainable,
[01:25:29] okay? If you are not a programmer, you
[01:25:31] might not know that this is not good
[01:25:33] code.
[01:25:34] Okay? And it like it works for this
[01:25:37] point that we've been able to hold this
[01:25:39] all into memory, but if we came back
[01:25:40] later, we wouldn't be able to really
[01:25:42] make sense of it. And just because the
[01:25:44] agent can make sense of it and summarize
[01:25:46] it to it, that's not good enough. We
[01:25:48] need to make it so that it is more
[01:25:50] human-readable
[01:25:51] um and that is what we are going to do.
[01:25:53] So, I'm just going to CD out of here and
[01:25:56] we're going to go into Claude. And
[01:26:00] uh we are going to get some refactoring
[01:26:02] going on. So, what I'm going to do is
[01:26:03] I'm going to make a new file called
[01:26:04] refactor.
[01:26:06] Um
[01:26:07] refactor
[01:26:10] MD. And I'm going to go say refactor
[01:26:13] um tasks.
[01:26:14] So, this is this document um is the
[01:26:19] tasks I want completed to refactor
[01:26:24] uh this uh
[01:26:27] our
[01:26:28] coordinator agent.
[01:26:30] Uh currently,
[01:26:31] all code sits in the main.py and we need
[01:26:35] to uh
[01:26:37] break it into
[01:26:39] multiple files.
[01:26:41] Okay?
[01:26:43] So, uh let's go ahead and start making
[01:26:46] some tasks. I'm just going to make my
[01:26:48] observations of
[01:26:49] what I don't like. So, the first thing
[01:26:52] is um
[01:26:54] the prompt. So,
[01:26:56] all prompts should be uh stored
[01:27:00] as um
[01:27:04] All prompts should be stored All prompts
[01:27:06] should be stored as markdown files
[01:27:11] in a prompts
[01:27:14] directory.
[01:27:15] Okay? So, that's step number one. The
[01:27:17] other thing is like tools. See how tools
[01:27:19] is very uh wieldy? So, uh tools should
[01:27:23] be
[01:27:24] uh individually
[01:27:27] defined as their own files in the tools
[01:27:32] directory.
[01:27:35] We should have .py files for each actual
[01:27:39] tool code.
[01:27:41] And the
[01:27:43] um
[01:27:44] tools.
[01:27:45] The tools
[01:27:47] I mean, like can we this is JSON, right?
[01:27:50] Um
[01:27:52] can we? I don't think there's anything
[01:27:53] special about this and the
[01:27:55] um tools.json
[01:27:58] for the long tool.
[01:28:02] Right? I I think it will understand what
[01:28:04] that is for the uh
[01:28:08] gets passed
[01:28:10] to create. So, that is definitely
[01:28:12] something I would like fixed.
[01:28:14] What else? What else?
[01:28:16] Um
[01:28:18] Do your partitions.
[01:28:22] We do have the partition system.
[01:28:27] So, say partition uh generation
[01:28:30] should be
[01:28:32] in lib
[01:28:34] as its own file. That's something else I
[01:28:36] would do.
[01:28:38] Um that's a function that is that. Run
[01:28:42] coordinator.
[01:28:44] Um
[01:28:48] The logging is inconsistent. I don't
[01:28:50] like how the logging is. So,
[01:28:52] um
[01:28:53] we should have a logger that um
[01:28:57] refactors
[01:28:59] all the logs to be consistent in a file
[01:29:04] in a file called logger
[01:29:07] in our logger.py
[01:29:09] in our uh
[01:29:11] lib directory.
[01:29:13] That'd be another thing I would want.
[01:29:16] Um
[01:29:20] Yeah, so I think that's a start.
[01:29:22] And so I'm going to go ahead and just
[01:29:23] say uh
[01:29:27] coordinator
[01:29:33] I want you to refactor
[01:29:37] my code base on
[01:29:39] that markdown file's
[01:29:41] tasks for the
[01:29:44] main.py in the
[01:29:47] coordinator refactor, okay? And so we
[01:29:50] will let it go do that
[01:29:52] and we'll see if we can really reduce
[01:29:54] and organize that code base cuz it
[01:29:56] really should be really easy for us to
[01:29:57] read. Right? Like I know we can make
[01:29:59] sense of it because we've been carrying
[01:30:01] forward it, but we really need to be at
[01:30:02] 100% like yes, absolutely, I know what
[01:30:05] I'm looking at, okay?
[01:30:07] Um
[01:30:08] So I'm just going to accept everything
[01:30:10] that goes along here and then we will
[01:30:11] take a look and see what we have. So
[01:30:13] it's already off to the races. We have
[01:30:14] our prompt, our partition planner, our
[01:30:16] screening uh agent.md. For me like I
[01:30:19] would probably want these to be
[01:30:20] templates that you can inject stuff
[01:30:22] into, but there's no reason for that
[01:30:23] right now. We don't really need dynamic
[01:30:25] injection, but it's definitely something
[01:30:26] that would be uh interesting to do. We
[01:30:29] have our tools directory. I think we
[01:30:31] only have the one agent here and then we
[01:30:33] have our tools JSON, so that is uh
[01:30:36] working out pretty well so far. It's
[01:30:38] going pretty quick, too. Man, these
[01:30:40] things are getting really, really
[01:30:41] better. Here we have our logger and then
[01:30:44] we are going to have our partitions.py.
[01:30:46] I really don't like that we have
[01:30:47] constants. I do not like using constants
[01:30:49] whatsoever. I think they're just it's
[01:30:51] just bad, bad code. Um but we'll
[01:30:53] continue on here and
[01:30:55] uh check it out in a moment. I'm going
[01:30:57] to just check how my usage is going.
[01:30:59] And uh you doesn't matter, it just
[01:31:01] reset. I'm back at 2%. Look at that.
[01:31:04] Lucky me, eh?
[01:31:05] Okay.
[01:31:06] So we are just chilling out here waiting
[01:31:08] for this to generate.
[01:31:10] I'm going to pause here and we will
[01:31:13] come back in a moment.
[01:31:15] I think it might be done. I didn't even
[01:31:16] really wait that long. And so we'll go
[01:31:18] up here and take a look.
[01:31:21] And so we have our main.py, we have our
[01:31:22] prompts, we have our tools, we have our
[01:31:24] libs. Let's go take a look here and see
[01:31:27] if this is reduced enough.
[01:31:29] Okay, and
[01:31:31] I probably should have told it to check
[01:31:33] box off these.
[01:31:35] Uh which is fine.
[01:31:37] So I'll just go here and just check them
[01:31:39] off myself.
[01:31:40] I just didn't feel like telling it to do
[01:31:42] that. I don't know.
[01:31:44] I assumed it would be fine.
[01:31:47] I could also ask it like hey, is there
[01:31:48] anything else that we could do to
[01:31:50] refactor to make it more human readable?
[01:31:52] But I don't feel like it would know cuz
[01:31:54] it's not a human.
[01:31:58] And then it's trained on garbage repos.
[01:31:59] Okay, so let's go into our main,
[01:32:03] wherever that is. Hold on here, our
[01:32:04] main.
[01:32:06] And I I usually just have a sense of
[01:32:08] like is this readable, right? Um
[01:32:12] and
[01:32:15] it's still yuck. It's really, really
[01:32:17] long.
[01:32:22] So there's still some stuff in here that
[01:32:23] needs to be refactored. We'll go over to
[01:32:25] here.
[01:32:26] Um
[01:32:29] So say coverage report.
[01:32:35] Coverage report should be its own
[01:32:40] file in lib
[01:32:43] called coverage report.
[01:32:47] Okay.
[01:32:49] Um
[01:32:53] The other thing is like the data, so
[01:32:58] right now we have hard-coded data.
[01:33:07] Make a
[01:33:08] data folder and store data artifacts
[01:33:12] and load them into the app.
[01:33:17] Okay. That's another thing. Um
[01:33:27] Mhm.
[01:33:31] I really dislike the logging.
[01:33:40] Yeah, and we have the trace append.
[01:33:44] It's still very, very verbose.
[01:33:50] And there are still things that's like
[01:33:52] I'm noticing here like
[01:33:53] um
[01:33:57] There are
[01:33:59] There are templates for
[01:34:02] content for messages
[01:34:05] that should really
[01:34:07] be uh templated uh files
[01:34:11] that take variables.
[01:34:15] And load it in.
[01:34:18] Maybe um
[01:34:25] Okay, like is that a prompt? I mean like
[01:34:27] we have this, it's technically a prompt.
[01:34:28] So technically technically they are
[01:34:30] prompts.
[01:34:34] Our prompts for content.
[01:34:37] And so uh prompts
[01:34:40] So move them.
[01:34:44] Them to prompts folders.
[01:34:47] Okay.
[01:34:49] So there's that. There's a lot of those.
[01:34:50] Okay, and so we'll go back here, we'll
[01:34:51] save the file.
[01:34:54] Um all the way down to here.
[01:34:57] There are new tasks in the refactor.
[01:35:07] md, okay? And so we're going to have it
[01:35:09] go off and do those tasks.
[01:35:20] And so we'll give it a moment there. I'm
[01:35:21] going to pause and I mean I really
[01:35:23] should tell it to check them off. I
[01:35:24] didn't tell it to do that. Uh but we'll
[01:35:26] come back and take a look and then we'll
[01:35:27] ask it to do a general refactor. I'm
[01:35:29] still like I really don't like this.
[01:35:31] Like we see how we have like double
[01:35:32] lines and stuff like that. I don't need
[01:35:34] that kind of level logging. Um but I
[01:35:36] would have to explain to it um why
[01:35:37] that's an issue.
[01:35:39] Yeah, it's still just making them md
[01:35:41] files. It's not marking them whether
[01:35:42] they're templates or not, but we'll just
[01:35:44] treat them as templates.
[01:35:46] And here we're getting a lot more in
[01:35:47] here, so that's better.
[01:35:50] But I I just know what good code looks
[01:35:52] like and I I know that's not good code.
[01:35:54] Um but there's only so much you can do
[01:35:55] with Python.
[01:35:56] Certain languages have um
[01:35:58] the ability to have better readability
[01:36:00] like Ruby's really, really good at that.
[01:36:01] I'd love to port this over to Ruby. I
[01:36:03] just didn't check if the agent SDK is
[01:36:05] available. I don't think it is available
[01:36:06] in Ruby. I just think that the Anthropic
[01:36:09] one is and so if the agent SDK was in
[01:36:11] Ruby, I would absolutely be using it
[01:36:12] over uh the Python one as I really do
[01:36:14] not like Python code and um it do it
[01:36:17] just you just can't get it to be
[01:36:19] extremely human readable. Um
[01:36:21] unfortunately we are all kind of using
[01:36:22] it because of the way the industry is.
[01:36:25] Um as they've adopted it, not because
[01:36:27] it's good, just because of mass adoption
[01:36:29] in the uh
[01:36:30] data data science and stuff like that.
[01:36:32] So it just became de facto. Oh look,
[01:36:34] it's already done. And so we have uh
[01:36:36] that there and so we will again look at
[01:36:39] the main file. I'm just going to close
[01:36:40] it and reopen it. Sometimes it doesn't
[01:36:42] always show me right away.
[01:36:44] It didn't check box these off. I really
[01:36:45] should tell it to check box them off
[01:36:47] when it does that. So we'll go ahead and
[01:36:48] save that. We'll go back over to our
[01:36:50] main.py and we'll scroll up. And I get
[01:36:54] I'm looking that looking at this for uh
[01:36:56] for refactorability.
[01:36:57] And
[01:37:00] I would say like they haven't done a
[01:37:01] good job with logging, so I'd say
[01:37:06] you haven't done a good job refactoring
[01:37:10] the logging, right? So for example
[01:37:14] we have log log info partition like
[01:37:17] partition
[01:37:19] uh you should be making
[01:37:23] helper functions.
[01:37:24] Uh so these logs
[01:37:30] e.g. like log partition.
[01:37:36] Um or you know, like log right? Log warn
[01:37:40] and they will add
[01:37:46] uh the you know
[01:37:50] tags. The uh other thing is
[01:37:55] um you have superfluous
[01:37:58] logging that is great for
[01:38:02] human readability.
[01:38:05] But we want to
[01:38:06] focus on logging
[01:38:08] good for
[01:38:10] for uh logs. And
[01:38:13] uh we should be outputting
[01:38:16] logs to a log folder relative to the uh
[01:38:20] folder
[01:38:22] of this agent.
[01:38:24] Okay, and so that you know, that's one
[01:38:25] thing that's really bothering me.
[01:38:29] I really hate constants, so that'll be
[01:38:31] another thing that we fix here in just a
[01:38:33] moment.
[01:38:34] But again, we're just trying to get this
[01:38:36] to be in shape. Um
[01:38:41] Did it also move this out of here? Like
[01:38:42] what's this big thing? Like why is the
[01:38:44] tool used so large here?
[01:38:48] Okay.
[01:38:49] Um
[01:38:50] And while that is thinking, let's go
[01:38:52] review our other parts of code.
[01:38:58] Okay, I mean this is fine.
[01:39:02] I think I wouldn't mind if we had like
[01:39:03] this is a big JSON object, but I
[01:39:05] wouldn't mind if we had a shorter syntax
[01:39:07] for this. I don't want to do that right
[01:39:09] now because it's totally possible that
[01:39:11] um
[01:39:12] uh we will be able to do that in agent
[01:39:15] SDK where it probably already has like a
[01:39:17] shorthand to make that code smaller. And
[01:39:20] so I don't want to uh
[01:39:22] uh muck with that.
[01:39:25] And we'll look at the partition here.
[01:39:27] Really hate those those constants.
[01:39:30] And also I I really dislike how it's
[01:39:31] loading in the prompt template. So there
[01:39:33] should be a way to uh
[01:39:35] manage that.
[01:39:37] Look look at all this logger logic. Oh,
[01:39:39] no, that's the logger file.
[01:39:41] Yeah, here now we're starting to get
[01:39:42] those things that I that I was asking
[01:39:43] for. That's good.
[01:39:45] Um
[01:39:50] Okay.
[01:39:54] The other thing that that's And I mean
[01:39:55] we don't need to do this, but like
[01:39:56] technically, you know, we have all these
[01:39:58] subagents that are calling create. We
[01:39:59] could technically delegate them out to
[01:40:01] different models if we needed to.
[01:40:03] Um or we could even say like, "Hey, can
[01:40:05] you try to choose the best model as it's
[01:40:06] working through there?" But yeah, I
[01:40:07] guess the next thing on my task is to
[01:40:09] fix that um
[01:40:11] Like I'm not updating the refactor. We
[01:40:12] could keep updating that as a means to
[01:40:14] keep uh keep track of stuff, but I just
[01:40:16] don't care.
[01:40:17] Um
[01:40:18] And so
[01:40:20] Yeah, I want to fix those constants.
[01:40:23] And I want to get something that loads
[01:40:24] in the templates.
[01:40:27] I'm just going to take a look here at
[01:40:28] our usage.
[01:40:31] 9% doing okay over here.
[01:40:35] Okay. And so now that is uh fixed up.
[01:40:38] We'll take a look here. Again, I'm
[01:40:40] looking at my main seeing if it's
[01:40:41] shorter.
[01:40:43] Yeah, it's looking Yeah, this is way
[01:40:45] less messier.
[01:40:47] Um
[01:40:48] I don't like using constants.
[01:40:54] EG like
[01:40:57] this is a var. Please don't use these
[01:41:02] in the folder for the coordinator
[01:41:05] refactor. Fix the code.
[01:41:08] Okay, so that's something I really
[01:41:09] dislike.
[01:41:12] And so we will get that improvement
[01:41:14] there.
[01:41:16] This This to me is like there's a big
[01:41:18] issue with the loop. So I feel that we
[01:41:20] need to give it a better instructions on
[01:41:21] like how to better refactor the loop. I
[01:41:24] mean it's using just a big
[01:41:25] if self
[01:41:27] block. There might be some kind of uh
[01:41:29] state flow machine or something that
[01:41:31] could improve that loop. Um as I'm not
[01:41:34] happy about it. Before we do that, I
[01:41:35] want you to fix the template reading and
[01:41:37] loading of files.
[01:41:39] Um
[01:41:42] And so there it's just making basic
[01:41:44] changes for names.
[01:41:46] Right there. So those are getting
[01:41:47] changed. Good.
[01:41:50] And it'll be done here in probably just
[01:41:52] a moment. Yeah, it's just updating the
[01:41:53] main.py and then we will
[01:41:56] have those fixed. Come on. Come on.
[01:41:58] Hurry up. Hurry up.
[01:42:07] And also like loading these templates
[01:42:09] and populating them probably needs to be
[01:42:12] um
[01:42:13] its own thing. Yeah, great. Thanks.
[01:42:15] Okay. Another thing is uh loading
[01:42:18] loading files and templates where you uh
[01:42:21] inject
[01:42:22] variables.
[01:42:25] Um you can
[01:42:27] make a new uh uh uh template template um
[01:42:34] template file in the
[01:42:37] uh lib directory.
[01:42:39] And this
[01:42:41] should
[01:42:43] uh refactor
[01:42:45] having
[01:42:47] you know, large
[01:42:51] load
[01:42:52] code EG like this. Okay. And so that's
[01:42:55] another thing that's kind of bothering
[01:42:56] me. So we will get that cleaned up as
[01:42:58] well.
[01:43:01] Um
[01:43:04] There's other things like this. Like see
[01:43:05] how this is like something's happening
[01:43:06] here. So that should be refactored out
[01:43:08] into a function.
[01:43:10] Uh like everything here. Like just the
[01:43:12] units of code is is just not
[01:43:13] explainable.
[01:43:17] So the run coordinator definitely needs
[01:43:18] to be broken up into tons of functions.
[01:43:20] Every single of these if else blocks
[01:43:21] should be functions.
[01:43:24] Um
[01:43:26] And I would probably prefer stateless
[01:43:27] classes. I really prefer stateless
[01:43:29] classes as that makes it really easy to
[01:43:30] track inputs and outputs of stuff. Um
[01:43:35] And Python's pretty good for that
[01:43:36] because of the way it defines uh these
[01:43:38] label tags. I can't remember what
[01:43:39] they're called. The prop named
[01:43:40] properties.
[01:43:41] And so that will be good.
[01:43:43] I'm making a lot of changes here. So
[01:43:44] there's a high chance this might not
[01:43:46] work, but that's fine.
[01:43:47] Uh we can always work through that.
[01:43:49] Uh it's fine. You're fine, Claude.
[01:43:51] You're fine.
[01:43:52] >> [laughter]
[01:43:53] >> Okay. And so now that that's loaded. I'm
[01:43:55] not sure if uh that actually changed.
[01:43:56] We'll go back over to here.
[01:43:58] And so with that, now when it needs it,
[01:44:01] I feel Yeah, like load prompt exactly
[01:44:03] like this.
[01:44:04] Um
[01:44:06] So yeah, the big problem still is the
[01:44:07] run coordinator.
[01:44:10] So the run coordinator
[01:44:14] file is giant.
[01:44:17] Uh we should refactor
[01:44:21] um
[01:44:24] into a stateless
[01:44:27] uh uh a stateless function.
[01:44:30] And
[01:44:32] all the parts of code
[01:44:35] uh should be chunked
[01:44:39] into functions.
[01:44:41] So the functions basically
[01:44:44] act as documentation.
[01:44:46] You know, for example, the contents of
[01:44:49] if if uh if blocks are really
[01:44:54] uh should be uh function calls, right?
[01:44:57] We'll go ahead and we'll see if it
[01:44:58] understands what I'm trying to say. But
[01:44:59] like when you write good code,
[01:45:01] you know, like this would be a function.
[01:45:04] This would be a function. This would be
[01:45:06] a function. Um
[01:45:09] whatever this is.
[01:45:11] Right? These if blocks. And we'll see if
[01:45:14] it understands what I'm talking about.
[01:45:16] Um
[01:45:18] But I feel like that's a really
[01:45:19] important component. In fact, this run
[01:45:21] coordinator could also be in the lib
[01:45:24] directory. Um and we might suggest it to
[01:45:27] move that in a moment. But right now I
[01:45:28] want to see if it could even handle what
[01:45:30] I'm asking it to do. It might not
[01:45:32] understand. Uh cuz if I don't have like
[01:45:34] an example, it's just not going to know
[01:45:36] what I'm trying to ask for. Again,
[01:45:38] checking my coverage here. Uh we're at
[01:45:40] 11% usage. Some folks were suggesting
[01:45:42] that like when it's high peak usage, it
[01:45:45] depends on like if you overlap with
[01:45:46] Europe European time. I'm not uh
[01:45:49] obviously in Europe. And so um they said
[01:45:51] like just try a bit later when
[01:45:52] everyone's sleeping. And it's way later.
[01:45:55] So uh you know, it would be maybe um
[01:45:58] off-peak usage time. But anyway, we'll
[01:45:59] just wait here and see what happens.
[01:46:01] Okay?
[01:46:03] It's back with functions. And again, we
[01:46:04] could call plan to ask it to do this
[01:46:06] before, but I I don't really care that
[01:46:07] much. So we have plan partitions,
[01:46:09] validate index partitions, run. I've
[01:46:11] seen something like with partition
[01:46:12] information. I'm almost wondering if
[01:46:13] that should be really part of the
[01:46:15] partitions.py.
[01:46:17] Right? Um
[01:46:19] log coordinator reasoning, handle this
[01:46:22] information. And so those partition
[01:46:25] ones, there's three with partition ones.
[01:46:28] Right? And so we'll go over to here.
[01:46:32] Um
[01:46:34] I mean like sure, you could do it that
[01:46:36] way. That's not what I asked for. I need
[01:46:39] to verify this. So
[01:46:41] I got to go over here. Like what does a
[01:46:43] stateless
[01:46:45] class look like in Python? Can it be a
[01:46:50] class with static methods?
[01:46:54] Okay, cuz that's what I was asking for.
[01:47:00] Yeah, okay. So look.
[01:47:03] I don't It did not do what I wanted. I
[01:47:04] mean close. So
[01:47:06] Okay. We'll go all the way down here.
[01:47:13] You know, I wanted a stateless class.
[01:47:18] That is a class
[01:47:21] with static functions.
[01:47:23] Okay?
[01:47:26] Right? So you didn't uh
[01:47:29] And I noticed
[01:47:33] some of the functions were handling
[01:47:35] partition logic.
[01:47:38] Is that something that should really
[01:47:41] be part of the partitions
[01:47:44] uh py?
[01:47:46] Right? So that's something I'm noticing
[01:47:50] as we are shaping that code.
[01:47:54] Okay?
[01:48:05] And so we're going to give that a moment
[01:48:07] to shuffle those things around.
[01:48:12] Now, is it thinking about that or is it
[01:48:14] just shoving things over there? Index by
[01:48:15] agent for partitions. Sure.
[01:48:18] Build initial messages. Again, is that
[01:48:21] for partition? Is it actually asking
[01:48:23] that question? Does it belong over there
[01:48:24] or is it just that it's handling
[01:48:25] partition data?
[01:48:27] Because it moved it and it didn't
[01:48:29] actually question whether it goes there
[01:48:30] or not.
[01:48:33] Um
[01:48:37] But anyway, we'll go over to here and
[01:48:38] we'll take a look of what's changed.
[01:48:41] What's it still working?
[01:48:44] It's now this is looking a lot better.
[01:48:48] Um
[01:48:50] Cuz now we can see what is going in,
[01:48:51] what's going out, right?
[01:48:57] Okay.
[01:49:06] And so we have all these steps.
[01:49:10] So we have call.
[01:49:11] So create a message.
[01:49:13] Log reasoning.
[01:49:18] Again, like it does this logging stuff
[01:49:19] belong with the logger?
[01:49:21] Handle screening agent.
[01:49:25] Handle evaluation coverage. Handle
[01:49:28] files. Handle submit final.
[01:49:32] Process tool calls.
[01:49:34] Run. Did they put these at the bottom?
[01:49:36] They did. Sometimes people put these at
[01:49:38] the top or sometimes they put at the
[01:49:39] bottom, but like the one that obviously
[01:49:40] is the big one is this one here. And so
[01:49:42] the idea is that we should be able to
[01:49:44] easily see what it's doing. So we have
[01:49:46] generate partitions, partitions.
[01:49:48] Validate overlap. Index agents, right?
[01:49:50] And so this should be self-documenting
[01:49:53] as you read it. We go down here. We call
[01:49:55] the coordinator. We do the log
[01:49:57] reasoning.
[01:49:58] Why are these functions? Are these just
[01:50:01] loose functions?
[01:50:02] They are. Well, no, they're part of the
[01:50:04] partition. And so I would go over to
[01:50:05] here and I would say, you know, give the
[01:50:08] um
[01:50:10] give the partitions.py
[01:50:14] the partitions.py
[01:50:16] like
[01:50:20] all of our lib directory Now I'll say
[01:50:23] our partitions.py
[01:50:26] should be a stateless class.
[01:50:31] I So a class with static functions.
[01:50:37] Please update. And that's just the way I
[01:50:39] prefer it, okay? I like to group them
[01:50:42] into domain. I don't like having loose
[01:50:44] functions where we don't know where
[01:50:45] they're coming from and who who respects
[01:50:47] them or owns them.
[01:50:48] Um people in the data space are very
[01:50:50] much used to just randomly importing a
[01:50:52] bunch of stuff, so they have a less
[01:50:54] sensitivity to to that kind of thing,
[01:50:56] but to me as a very professional
[01:50:58] developer I I want to see where that
[01:51:00] stuff is coming from. We still have some
[01:51:02] of our if else stuff here. And notice in
[01:51:04] here like these again, these should be
[01:51:07] functions.
[01:51:09] Right? All they're all they're doing is
[01:51:10] calling these things, but still I want
[01:51:12] these as functions.
[01:51:14] If there's an if else statement in here,
[01:51:15] especially in our main loop, that's what
[01:51:16] it should be. We have a range of 1 to
[01:51:18] 31, so that's kind of defining how many
[01:51:20] steps it can take. Um I would rather
[01:51:23] that uplifted as a variable.
[01:51:26] But we're not going to go too crazy on
[01:51:27] this. I just want to get it in enough
[01:51:29] shape here. And mostly just to show you
[01:51:31] like what good code looks like. Um and
[01:51:34] what you should be doing before you move
[01:51:36] on stuff. You might say, "Well, Andrew,
[01:51:37] why like this is more work to read?"
[01:51:39] Yeah, but if if you want to write test
[01:51:40] code for this then you have an input and
[01:51:42] an output and you know exactly what to
[01:51:44] mock going in there and out of there.
[01:51:46] The only thing that I would also change
[01:51:48] is like if these are complex um
[01:51:50] objects I'd want them to be dumber and
[01:51:53] only pass in really dumb data so that we
[01:51:55] could mock it a lot easier. And this is
[01:51:56] pain points if you've spent a lot of
[01:51:58] time writing uh code. And you might say,
[01:52:00] "Well, you know, the AI can write the
[01:52:02] test code for us." But that doesn't make
[01:52:04] it good test reliable test and and
[01:52:06] you'll only know that by uh writing that
[01:52:08] stuff. But we'll go over here. We'll
[01:52:09] take a look at our partitions.
[01:52:11] And so that is fine. There's still lots
[01:52:13] of little improvements to be made like
[01:52:15] I'm looking at like why is that like
[01:52:16] that? I don't like hard-coded stuff like
[01:52:18] that. Um there's just a bunch of little
[01:52:20] things. But I'll just say we'll move the
[01:52:21] coordinator over. So uh the coordinator
[01:52:25] uh can be in its
[01:52:27] uh coordinator class
[01:52:30] should be uh in
[01:52:32] a its own file
[01:52:35] in the lib directory.
[01:52:38] Okay?
[01:52:39] And we'll move that over there. That'll
[01:52:40] be the last thing we do here.
[01:52:42] Um
[01:52:43] and then what we will do is we'll just
[01:52:45] run it, make sure it still works.
[01:52:47] And then we'll call this, you know
[01:52:50] done-ish, right? But again, you know, if
[01:52:53] this was something that I would want to
[01:52:54] put in production, I would take the time
[01:52:56] and fine-tune it. I would take the time
[01:52:58] and fine-tune it and and because that's
[01:53:00] about getting um
[01:53:03] uh the word I'm looking for is um
[01:53:07] uh technical ownership, right? That you
[01:53:09] have ownership of the code and and you
[01:53:10] know exactly what it's doing. When you
[01:53:12] shape it like that, then you have a
[01:53:13] better sense of it. So now the
[01:53:15] coordinator is over there. I want to
[01:53:17] just run it to make sure it works. So
[01:53:18] I'm going to CD into the coordinator
[01:53:20] refactor and we're going to go ahead and
[01:53:22] run python. or python.main.py.
[01:53:25] Okay? So we're going to run that and we
[01:53:27] will take a look and hopefully it still
[01:53:29] works.
[01:53:34] There we go.
[01:53:35] I wonder if it's going to make the log
[01:53:36] file.
[01:53:38] We do get our logs. Excellent.
[01:53:40] Coordinator.log. Okay, and see that's
[01:53:42] what I meant when I said I wanted it to
[01:53:43] be nice and
[01:53:44] uh and whatever. I might even suggest
[01:53:46] like I'd probably prefer it to log out
[01:53:48] JSON structure because then we could
[01:53:50] parse that information.
[01:53:52] Um
[01:53:54] yeah, I think I would that's what I
[01:53:55] would prefer especially like if you're
[01:53:56] data-driven and you have JSON L data as
[01:53:58] logs, it's super super useful.
[01:54:00] Um so instead of having like coordinator
[01:54:01] and delegate um I would probably just
[01:54:03] have JSON objects and then I could parse
[01:54:05] it and ingest it into something else.
[01:54:07] But again, these are little tricks that
[01:54:08] you learn building applications of all
[01:54:11] kinds. Um but the point is that it is
[01:54:14] running. We just want to see it to
[01:54:15] completion and then we will call this
[01:54:18] done and then we will move on because
[01:54:20] the next section of stuff we are looking
[01:54:22] at is um stuff that I feel like agent
[01:54:25] SDK is going to be uh very useful for.
[01:54:29] Um they'll all have to decide on that.
[01:54:30] And so it did run. Worked great. The
[01:54:32] only thing that I'd probably ask it to
[01:54:34] do, which it's not doing right now is
[01:54:35] that I would have it dump the coverage
[01:54:37] report into its own file. So that'll be
[01:54:39] the last thing that we do here.
[01:54:42] Okay, and so I'm going to go here.
[01:54:45] Cuz that would actually make it useful,
[01:54:46] right? So I'm going to go and just say
[01:54:48] um you know, for my
[01:54:51] coordinator refactor
[01:54:54] uh it currently generates
[01:54:57] it generates
[01:54:59] a coverage report
[01:55:02] in the logs but it really should be
[01:55:05] outputting
[01:55:07] outputting um uh the a a report
[01:55:11] timestamped
[01:55:13] uh in a reports directory
[01:55:16] um and formatted nicely
[01:55:20] for uh human to read.
[01:55:23] Right?
[01:55:25] And so that's the last thing I would
[01:55:27] absolutely say we need to do. I just
[01:55:29] realized that that's a little bit um
[01:55:30] gross on how it currently is.
[01:55:33] Uh and we never looked at our data, but
[01:55:34] yeah, we have our job posting and stuff.
[01:55:36] And this is we could enrich these later,
[01:55:38] but they're fine.
[01:55:39] There's really no new data here.
[01:55:43] Uh we could have made a research that
[01:55:44] would grab job postings and make it for
[01:55:46] us. Not that anyone really should care
[01:55:48] about job postings anymore because
[01:55:49] agents are just
[01:55:51] going at it, but we'll wait for this to
[01:55:52] finish. Okay? And then we might run this
[01:55:54] one more time.
[01:55:55] Okay, there we go. And so um it says
[01:55:57] it's there. The other thing is that I
[01:55:58] don't think we're logging uh usage.
[01:56:02] So that would be nice to be able to log
[01:56:05] that information out. But again, these
[01:56:06] might be things we get for free when we
[01:56:08] use the agent SDK.
[01:56:09] So I'm not exactly sure. Um and so now
[01:56:11] that is done, I'm going to go ahead and
[01:56:13] run this one more time. Clear.
[01:56:16] I have no idea how many um credits I'm
[01:56:18] burning. Like again, I haven't hit my I
[01:56:20] have like $5 or whatever. I haven't hit
[01:56:22] it yet and Bako's not going to get mad
[01:56:23] if I load up another $5. So so far it is
[01:56:26] not a pain problem. People don't know,
[01:56:28] Bako is the other Andrew, Andrew B. I'm
[01:56:30] Andrew B. And so we call him Bako so
[01:56:32] it's not confusing. He's definitely a
[01:56:34] real person. He's not um an agent. Or is
[01:56:37] he? We don't know. No one ever sees him.
[01:56:39] Uh so we're going to run this again. I'm
[01:56:41] going to pause here and then I just want
[01:56:42] to confirm the reports are there. But
[01:56:44] again, you can just see my thoughts of
[01:56:46] like what would be good to do. Okay?
[01:56:49] We still have the coverage report being
[01:56:50] logged here, which I don't like, but
[01:56:52] that's fine. As long as we got a I
[01:56:54] didn't we didn't tell tell it to not do
[01:56:56] that there. But we'll go here and then
[01:56:57] here is our report. We can go ahead and
[01:56:59] view it over like this.
[01:57:01] And so there is our final coverage
[01:57:03] assessment.
[01:57:05] Um I really don't like how long it's
[01:57:08] written this stuff. Like if you were
[01:57:09] human, would you want to read this much
[01:57:11] information? Probably not. Or you'd want
[01:57:14] it summarized in a different way, but we
[01:57:15] never gave it a coverage report
[01:57:16] template, so that's fine. We will
[01:57:19] consider this done. We'll say get add
[01:57:21] all, get commit refactor.
[01:57:25] But that wasn't bad for a quick
[01:57:26] refactor. Still lots of work to be done
[01:57:28] there, right? Um I'll see you in the
[01:57:30] next one. Ciao ciao.
[01:57:32] Hey folks, it's Andrew. We're back and
[01:57:34] it's time for us to port our coordinator
[01:57:36] application over to agent SDK. And the
[01:57:38] reason why is that we're going to be
[01:57:40] getting into um
[01:57:42] uh specific agent SDK um
[01:57:46] arguments and if we want to know how
[01:57:49] they work, we need to have an example
[01:57:51] over there. And I think we should just
[01:57:53] continue this project forward and I
[01:57:54] think it's not a bad idea. So what we
[01:57:57] are going to do um
[01:57:59] is we're going to call this uh port to
[01:58:03] to agent
[01:58:05] SDK.
[01:58:07] Okay? And so what I'm going to do here
[01:58:09] is I'm going to grab the contents of all
[01:58:11] this. Not the logs. We don't need the
[01:58:13] logs or the reports. But we will grab
[01:58:15] this, this, this, this, this, and this.
[01:58:18] Right click copy. We'll go down over to
[01:58:21] our port to agent SDK. We will paste
[01:58:25] this stuff in.
[01:58:26] And we're are going to
[01:58:29] let her rip and see if it will
[01:58:32] allow us to port it over in one go here.
[01:58:34] So
[01:58:36] I need to port the my code base
[01:58:41] uh of Anthropic SDK based on uh for my
[01:58:46] agent that uses directly
[01:58:49] the Anthropic
[01:58:51] SDK to use
[01:58:54] Claude agent SDK
[01:58:56] for this folder.
[01:58:59] Port SDK.
[01:59:01] And so we're going to ask it to go ahead
[01:59:03] and do that. That's a big thing. Again,
[01:59:05] we probably should have put it in a plan
[01:59:06] mode and ask it what it can do.
[01:59:08] But I'm just going to go off of the
[01:59:10] races and do that. And if it works, we
[01:59:12] will explore it and
[01:59:14] we'll have time to look at the code base
[01:59:16] quite a bit as we walk through other
[01:59:18] features, okay?
[01:59:20] All right, let's take a look here and
[01:59:21] see what we have.
[01:59:22] So we have the run updated. I'm not sure
[01:59:26] why it did that. It's not really that
[01:59:28] big of a deal.
[01:59:31] We removed the async Anthropic and
[01:59:33] coordinator. These are now internal to
[01:59:35] the coordinator. Sure.
[01:59:38] It has a complete rewrite. I was
[01:59:39] expecting that.
[01:59:41] That I assume that would be the largest
[01:59:43] rewrite for us.
[01:59:45] And I guess all those are unchanged.
[01:59:46] That's really interesting. And then we
[01:59:48] need to do a
[01:59:50] a update here. I mean, you know,
[01:59:53] you know, can you make the
[01:59:54] requirements.txt for me?
[01:59:57] Cuz that's what it should have done. But
[01:59:58] I we never copied it from a prior one.
[02:00:00] That's probably why.
[02:00:02] Yeah, we didn't. So let's go take a look
[02:00:04] at the the major changes. So we'll look
[02:00:06] at the main.py. And
[02:00:10] here we can see async Anthropic. Oh, so
[02:00:12] there's where it's different. Default
[02:00:15] async client. That's why there was a
[02:00:17] change there. This is the new one,
[02:00:18] right?
[02:00:19] There we go. Okay.
[02:00:21] And so this more or less looks the same.
[02:00:26] But we'll go into our coordinator
[02:00:27] directory here.
[02:00:30] And let's see if we can
[02:00:35] make the difference here.
[02:00:43] Okay. So I'm going to do is scroll up
[02:00:45] here. What I might do,
[02:00:47] just so that we can really clearly see
[02:00:49] the difference,
[02:00:50] we might refactor a smaller one because
[02:00:52] it's very hard to see the changes. They
[02:00:53] don't even show us the code changes
[02:00:54] here, right? Um
[02:00:57] So what I'm going to do,
[02:00:58] I'm going to make another repo.
[02:01:01] We have
[02:01:02] uh
[02:01:03] Make another folder here. Let's see.
[02:01:04] Port
[02:01:07] to
[02:01:09] Anthropic uh port to agent SDK small.
[02:01:18] And the reason I want to do that again
[02:01:20] is to really clearly see the difference.
[02:01:23] And so I'm trying to think of one that
[02:01:24] we were doing before, like narrow task
[02:01:25] decomposition.
[02:01:27] Yeah, where we have this one. This one's
[02:01:29] a lot simpler, right?
[02:01:31] And we actually might want to go one
[02:01:32] step before that where we are using tool
[02:01:34] use.
[02:01:35] Um
[02:01:38] Could be decision-making, model-driven,
[02:01:40] right? So this one here
[02:01:44] is a very simple one with multiple
[02:01:45] tools. So what we're we'll do is we'll
[02:01:47] copy this
[02:01:48] over here. And then I go into this
[02:01:50] directory just so we can clearly see
[02:01:53] the difference. And then also maybe just
[02:01:55] have another one that we can work on.
[02:01:57] Though I don't really like this use case
[02:01:58] per se. Okay. And so
[02:02:01] I'm going to go and say, "Okay, great.
[02:02:02] Can we Can we convert the code for port
[02:02:07] to agent
[02:02:09] uh SDK small?"
[02:02:15] over to agent SDK. Again, we haven't
[02:02:18] tested if these actually work. Hopefully
[02:02:20] it knows Claude agent SDK, not just some
[02:02:22] generic one. Um but anyway, I think it
[02:02:25] knows. I hope it knows. We'll wait here
[02:02:27] a moment, okay? All right, so we have
[02:02:29] the refactor already done for this one.
[02:02:31] Didn't take too long. Let's see what
[02:02:32] it's changed. So the imports are
[02:02:34] different.
[02:02:37] Yeah, it is using Anthropic, the correct
[02:02:39] one.
[02:02:40] No, no, no, no, no. It Yeah, it is.
[02:02:41] Okay, here it is. So here it is and
[02:02:46] here instead of handling tools here, we
[02:02:48] have a decorator.
[02:02:50] And then the functions are probably
[02:02:52] defined a particular way. See this whole
[02:02:53] big thing is probably gone. Yep. And so
[02:02:55] we have decorators on top of our
[02:02:57] functions making this code a lot
[02:02:59] smaller.
[02:03:01] Okay.
[02:03:02] Um the call is a bit different. So
[02:03:06] that's one thing.
[02:03:09] And
[02:03:10] we are creating the SDK MCP server to
[02:03:14] pass the tools over. So that is another
[02:03:16] thing that's changing.
[02:03:19] Okay.
[02:03:21] Um
[02:03:23] I mean, we have new modes and we're
[02:03:25] setting our MCP server
[02:03:27] with our tooling in it.
[02:03:30] Um okay. So basically we basically have
[02:03:33] an internal internal MCP. That's really
[02:03:35] interesting they make that with super
[02:03:36] super easy.
[02:03:38] And this call is a little bit different.
[02:03:39] So basically the big thing that we're
[02:03:41] seeing is that tool use.
[02:03:43] Um so let's go back to our larger
[02:03:45] refactor. And I want to take a look at
[02:03:48] our
[02:03:49] tools.
[02:03:50] And so that tool.json, do we even need
[02:03:53] that anymore? Does that even make any
[02:03:54] sense? So what we'll do is go back over
[02:03:56] here.
[02:03:57] Cuz now we know what was refactored,
[02:03:59] right? And we'll say,
[02:04:01] "Do we even need
[02:04:05] the tools.json
[02:04:07] anymore? And shouldn't we
[02:04:10] be using the decorator?"
[02:04:24] for port to
[02:04:27] agent SDK
[02:04:29] base for Claude
[02:04:32] agent SDK.
[02:04:34] And I imagine that you can probably pass
[02:04:36] in that JSON tools cuz it's it's doing
[02:04:39] it. No, we don't we don't know if it
[02:04:40] actually works or not. Um
[02:04:44] Like we go here, tools.json.
[02:04:47] Like I don't see it loaded in here.
[02:04:48] Maybe it's getting loaded in the main.
[02:04:50] It is refactoring probably right now, so
[02:04:51] we wouldn't even know.
[02:04:55] But we'll see what it says here.
[02:04:57] Cuz we do have tool right here, right?
[02:04:59] So it is. It's right here.
[02:05:01] So maybe it just has to delete it out.
[02:05:04] But if the tool is here, then why isn't
[02:05:06] that defined? Or does it have to sit in
[02:05:08] the same place?
[02:05:11] Right? So we have this one here. Is this
[02:05:13] just a repeat?
[02:05:16] Okay.
[02:05:30] And like look at all this inline stuff,
[02:05:31] eh?
[02:05:39] Object maybe pass rationals key strings.
[02:05:41] That's the structure that we actually
[02:05:43] wanted from before.
[02:05:44] Um
[02:05:46] And so here all three tool decorators
[02:05:49] are now using the simple peram.
[02:05:52] Okay, but like does the coordinator
[02:05:53] still have them in here?
[02:05:57] Do we have to have
[02:06:01] the tools in
[02:06:03] the coordinator
[02:06:07] .py or can they actually they live
[02:06:11] in the
[02:06:13] um
[02:06:14] tools directory
[02:06:18] as separate functions?
[02:06:21] Or it doesn't work because
[02:06:28] tight coupling
[02:06:30] of the decorator.
[02:06:34] Which is this part here. It might be the
[02:06:35] reason why they can't do that. And I
[02:06:38] mean, hopefully it knows what last
[02:06:40] directory we're in.
[02:06:42] Is it more than one? But
[02:06:44] we'll ask that question. And you know,
[02:06:46] this is what I'm trying to figure out.
[02:06:50] Let's see what it says here. So the key
[02:06:52] insight tools of decorator runs at call
[02:06:54] time, not import time. So you can apply
[02:06:55] it inside the factory function that
[02:06:57] captures state via normal closures.
[02:07:04] Okay. Well,
[02:07:06] speak English to me here.
[02:07:08] Can we move it or not?
[02:07:12] Coordinator class.
[02:07:14] Tools. Screening agent.
[02:07:18] Look look, I'm trying to keep my stuff
[02:07:20] lean here, folks.
[02:07:23] Did it move it out?
[02:07:25] Did it even tell me that it moved it
[02:07:27] out?
[02:07:29] Okay.
[02:07:31] So here coordinator state, make
[02:07:33] coordinator. So it did move it out from
[02:07:35] tools.
[02:07:37] I don't like how they're make
[02:07:39] coordinator tools.
[02:07:44] Okay. And then we have coordinator
[02:07:45] state.
[02:07:49] All right. Okay, I see. So they they
[02:07:50] have a state file separately for the I
[02:07:52] mean, state wouldn't belong in tools,
[02:07:55] now would it?
[02:07:56] So that doesn't make any sense.
[02:07:58] Unless it's coming from that file. Maybe
[02:08:00] it it's part of it. That's why. Okay.
[02:08:02] And so we go over to here.
[02:08:04] And we have make coordinator tools. Oh,
[02:08:06] and they do have it in here. Okay, so
[02:08:07] they were able to move it out.
[02:08:10] And so here we have
[02:08:12] our multiple tools. Okay. And so to me,
[02:08:15] that's what I would like it to be.
[02:08:17] So I'm going to go ahead and we're going
[02:08:18] to stop this. And we're going to CD into
[02:08:20] the port to agent SDK. And I just want
[02:08:23] to make sure that this still works.
[02:08:25] So we'll go ahead and say main.python.
[02:08:28] dot
[02:08:30] We have main
[02:08:31] or main. Python. I got it backwards.
[02:08:34] Python main.
[02:08:37] Whatever. Whoops.
[02:08:40] Okay.
[02:08:43] And I just want to make sure that it
[02:08:45] still runs. Because we've changed a lot
[02:08:47] of code or at least
[02:08:50] one large file to another framework.
[02:08:54] And um
[02:08:58] It's logging.
[02:09:00] We'll pause here and see the end result,
[02:09:01] but I'm pretty certain that it's going
[02:09:02] to work.
[02:09:04] Okay, so it ran without issue and we are
[02:09:07] in good shape. Um
[02:09:10] Yeah, so we are set up and the question
[02:09:12] will be like, you know, do we use this
[02:09:14] to test out all the agency decay stuff
[02:09:16] or do we come back to this project? We
[02:09:17] will see, but at least we made it to
[02:09:19] this point and I think the key takeaway
[02:09:22] here is the fact that uh the tool use
[02:09:25] call got easier and it's setting up an
[02:09:27] MCP server. Okay, so literally it's an
[02:09:30] internal NPC server.
[02:09:32] Um and so clearly
[02:09:34] uh Entropic is obviously making that a
[02:09:36] priority tool. But anyway,
[02:09:38] there we go and we will move on from
[02:09:39] that, okay? Ciao ciao.

---
*RAW — not yet passed through D.R.D deconstruction. Do not integrate into department files.*
