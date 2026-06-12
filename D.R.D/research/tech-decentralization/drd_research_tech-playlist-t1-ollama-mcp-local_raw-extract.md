# RAW EXTRACT — Running LLMs Locally Just Got Way Better - Ollama + MCP

## Source Metadata
- **Title:** Running LLMs Locally Just Got Way Better - Ollama + MCP
- **URL:** https://www.youtube.com/watch?v=GAyNvq6Ayps
- **Tier:** 1
- **Extracted:** 2026-06-09
- **Domain:** tech-decentralization / agentic-systems
- **Playlist:** Pandora Tech Playlist — PLWKcfqsabTLUxfC7OFs7UZ8EIJ6hjY_M8
- **Word Count:** ~5995

## Transcript (timestamped)

[00:00:00] If you want to run a local model that is
[00:00:02] free, private, and capable of connecting
[00:00:04] to all of your external tools like
[00:00:06] Google, Notion, Facebook Ads, you name
[00:00:09] it, anything that you want, then keep
[00:00:11] watching this video. What I'm going to
[00:00:13] show you how to do here is how to run a
[00:00:14] capable local model on your own machine,
[00:00:17] but more importantly, how to connect it
[00:00:18] to external services so that you can get
[00:00:20] the same tool use and advantages that
[00:00:22] you would by using something like Claude
[00:00:24] or OpenAI, but completely for free,
[00:00:27] completely private, and secure on your
[00:00:29] own machine, so you control everything.
[00:00:32] With that said, let's get into the
[00:00:33] video. Okay, so the way that we're going
[00:00:35] to do this here is we're going to use
[00:00:36] Ollama. I'll talk about how to install
[00:00:38] it and set it up. We're going to use a
[00:00:40] capable model. We'll discuss the
[00:00:42] criteria for using that in a second. And
[00:00:44] we're going to use something called the
[00:00:45] Zapier MCP server. This allows you to
[00:00:47] connect to over 8,000 different
[00:00:49] integrations. It is free to use. You can
[00:00:51] just create an account, and you can set
[00:00:53] it up. And this means that all of your
[00:00:54] integrations can be handled in one
[00:00:56] place, and you just connect a single MCP
[00:00:58] server to Ollama, which again, I'll
[00:01:00] explain to you how to do, and then
[00:01:02] you're good to go, and you can run a
[00:01:03] local model and effectively do anything
[00:01:05] you would with the better ones. Now,
[00:01:07] there are a few things that you should
[00:01:08] understand before doing this, so let me
[00:01:10] quickly go through them. Now, first, I'd
[00:01:12] like you to understand the difference
[00:01:13] between an LLM, a large language model,
[00:01:16] which is kind of what we've been talking
[00:01:17] about, and an AI agent. Now, an AI agent
[00:01:20] is something that's capable of actually
[00:01:22] taking action, and the way that it does
[00:01:24] that is by calling various different
[00:01:26] tools. An LLM, or a large language
[00:01:28] model, is just kind of a standard
[00:01:30] chatbot. What it's capable of doing is
[00:01:32] predicting text, in some cases calling
[00:01:35] tools or generating videos, images, etc.
[00:01:37] But what allows it to do that is you
[00:01:39] connecting it to something external. So,
[00:01:41] if you just have, you know, ChatGPT, or
[00:01:44] you have, I don't know, Claude or
[00:01:45] Anthropic, or some base model, whatever,
[00:01:48] if you don't connect it to anything, it
[00:01:50] can't really do anything. It could just
[00:01:51] give you some text back. Now, the exact
[00:01:53] same thing applies here when we're
[00:01:54] running these models on our own machine.
[00:01:56] It's very easy to run a local model on
[00:01:58] your own computer. You can type with it,
[00:02:00] it can give you a response back. That's
[00:02:02] cool, but we want to add that tool layer
[00:02:04] so we can actually take some actions and
[00:02:06] be useful to us. So, that's the key
[00:02:08] difference. The LLM is kind of like the
[00:02:10] brain, it can chat with you, it can do
[00:02:12] things, but what allows it to do
[00:02:13] something is connecting it to these
[00:02:15] tools. So, when we make that connection,
[00:02:17] now the LLM goes from a chatbot to
[00:02:19] something that can actually go out in
[00:02:21] the real world and take actions on your
[00:02:23] data, which makes it extremely valuable.
[00:02:25] Okay. So, in terms of setting this up,
[00:02:27] first thing we need to do is download
[00:02:29] and install Ollama. I'll leave a link to
[00:02:31] it in the description, but you can
[00:02:32] probably find it faster. It's
[00:02:33] ollama.com. What you're going to do here
[00:02:35] is just press the download button,
[00:02:37] download it for your operating system.
[00:02:38] If you already have it, I'd recommend
[00:02:40] just updating it. You can do that by
[00:02:41] running this command right here in your
[00:02:43] terminal. Okay? Now, once you've got
[00:02:46] Ollama installed, go ahead and open up a
[00:02:48] terminal or a command prompt. If you're
[00:02:50] on Mac like me, you can just search for
[00:02:51] terminal in the spotlight search. If
[00:02:53] you're on Windows, go to the Windows
[00:02:55] search and search for PowerShell or for
[00:02:57] CMD or even now I think they've called
[00:02:59] it terminal as well. Doesn't really
[00:03:01] matter, just open it up. From here,
[00:03:03] you're going to simply type Ollama like
[00:03:05] so.
[00:03:06] Let's zoom in and just make sure that
[00:03:08] this is working.
[00:03:09] Okay. Now, if it's your first time
[00:03:11] running this, you may need to just make
[00:03:13] sure that Ollama is started on your
[00:03:14] machine. To do that, you can also just
[00:03:16] search for the Ollama application and
[00:03:18] just double-click to run it and then it
[00:03:19] should run in the background. Okay, so
[00:03:21] once you've run Ollama here, you might
[00:03:23] see a screen that looks something like
[00:03:24] this where it says like, "Oh, launch
[00:03:26] these different things." It's like a
[00:03:27] brand new update they just released. For
[00:03:29] now, to get out of it, you can just hit
[00:03:30] escape because we're going to kind of
[00:03:31] pause on this for a second cuz what we
[00:03:33] need to do is find the model that we
[00:03:35] want to run. Okay, so from here, if you
[00:03:36] want to see a list of models that you
[00:03:38] can possibly run, just go to this models
[00:03:40] tab and you can see there are a ton of
[00:03:42] different ones and you can start
[00:03:44] searching through them. This is where we
[00:03:45] need to talk about kind of realistic
[00:03:47] expectations. The type of model that you
[00:03:49] can run on your computer really depends
[00:03:52] on the performance of your machine. And
[00:03:54] the main thing that we're focused on is
[00:03:56] the graphics processing unit or CPU that
[00:03:58] you have depending on your operating
[00:04:00] system, Mac versus Windows, and the
[00:04:02] amount of RAM that you have. Now, what
[00:04:04] I'm about to tell you is pretty much
[00:04:06] exclusively for newer devices, so I'm
[00:04:08] talking about in the last like 4 or 5
[00:04:09] years. If you're running a much older
[00:04:11] machine, you still can run these local
[00:04:14] models, but you're going to be really
[00:04:15] limited in what's possible just based on
[00:04:17] the current architecture of like the old
[00:04:19] devices versus the new devices. So, if
[00:04:22] you're running a newer Mac on any
[00:04:23] M-series chip, then you should have
[00:04:25] unified memory. That means that the RAM
[00:04:28] available to your computer is also
[00:04:30] available to your graphics card, uh or
[00:04:32] graphics processing unit, whatever you
[00:04:33] want to call it, or whatever, you know,
[00:04:35] Apple is calling it now. So, if you have
[00:04:37] 32 gigs of RAM on your machine, then you
[00:04:39] can run models that utilize maybe like
[00:04:41] 70 or 80% of that RAM. Now, if you're on
[00:04:43] a Windows machine or a Linux machine,
[00:04:45] it's unlikely that you have unified
[00:04:47] memory. Actually, I don't even know if
[00:04:49] that's possible on Windows. I don't know
[00:04:50] the current architecture. But, what I do
[00:04:52] know is that usually you're going to
[00:04:54] have these models running on your
[00:04:55] graphics card. So, if you have a 4090,
[00:04:58] for example, then you should have 24 GB
[00:05:00] of VRAM. Now, this is the memory that's
[00:05:02] exclusively available to your graphics
[00:05:04] card and can be used for running these
[00:05:06] models, and the models can use pretty
[00:05:07] much all of that. So, if you're on Mac,
[00:05:09] what you want to look at cuz you need to
[00:05:11] know your amount of RAM is, "Okay, how
[00:05:12] much RAM or unified memory do I have?"
[00:05:14] If you don't have unified memory, you're
[00:05:16] looking at the memory for your graphics
[00:05:18] card. And if you're on Windows, you're
[00:05:19] almost exclusively looking at the memory
[00:05:21] for your graphics card. If you don't
[00:05:22] have a graphics card, you can still run
[00:05:24] these models, but they're going to be
[00:05:25] extremely slow. So, you can always run
[00:05:27] these models assuming you have enough
[00:05:28] hard drive space. It's just a matter of
[00:05:30] like, are they actually usable and do
[00:05:32] they give you any kind of output that
[00:05:34] doesn't take like 5 hours to run?
[00:05:36] Because you can run them, but they're
[00:05:37] just going to be really, really slow if
[00:05:39] you don't have enough RAM. And the
[00:05:40] reason for this is that typically you
[00:05:42] load the entire model and all of its
[00:05:44] weights into the computer's memory. So,
[00:05:46] this is what we're focused on. Again, if
[00:05:48] you're on Mac, it's a little bit easier
[00:05:49] for you because you just look at the RAM
[00:05:50] amount. If you're on Windows, you need
[00:05:52] to know your graphics card, the amount
[00:05:53] of VRAM, and again, newer devices are
[00:05:55] just going to perform better. So, with
[00:05:57] all of that said, when we choose a model
[00:05:59] here, what we need to be looking for is
[00:06:01] one that's capable of tool calling. If I
[00:06:04] just search for like the Llama model
[00:06:06] here, and I'm using like an outdated
[00:06:07] model, something like Llama 3, you'll
[00:06:09] see that Llama 3 doesn't indicate that
[00:06:12] it has the ability to call tools. So, if
[00:06:14] I download this and use it, okay, cool,
[00:06:17] but I can't actually call any tools with
[00:06:19] it, so it's just not really usable,
[00:06:21] right, for doing the integrations. Now,
[00:06:23] you can use it as a chatbot, but but
[00:06:24] that's about it. So, when you're going
[00:06:26] to pick your model, you want to pick a
[00:06:27] model that has this tools ability. So,
[00:06:30] the one that I'm going to use in this
[00:06:31] video is Gwen 3.5, very good new model,
[00:06:34] updated 2 weeks ago, and you'll notice
[00:06:36] that when you start looking at these
[00:06:37] models, they have a ton of different
[00:06:40] options.
[00:06:41] So, if we scroll down, you'll see we
[00:06:42] have one that is 8 billion parameters, 2
[00:06:45] billion parameters, 4 billion, uh 9
[00:06:47] billion, 27 billion. Sorry, this is 0.8
[00:06:49] billion. And the number of parameters
[00:06:52] directly ties to the space that the
[00:06:54] model is going to take up on your
[00:06:55] computer in terms of storage space, but
[00:06:58] also in your RAM. So, the more
[00:07:00] parameters, the better performing the
[00:07:02] model is going to be. However, the more
[00:07:04] difficult it's going to be to run. So,
[00:07:06] when you're selecting the version of the
[00:07:08] model, and let's say you're using Gwen
[00:07:10] here, you need to be conscious of how
[00:07:12] much RAM you have available for the
[00:07:14] model to use. Now, in my case, because I
[00:07:16] have 32 GB of RAM on my machine, let's
[00:07:18] just quickly show you about this Mac,
[00:07:20] and this is unified memory on an M2 Max
[00:07:23] like MacBook here, I can use most likely
[00:07:25] the 35 billion or the 27 billion
[00:07:27] parameter model. The 122 billion one, I
[00:07:30] can still use it, but it's going to be
[00:07:32] incredibly slow and just not practical
[00:07:34] to run because it uses 81 GB, which
[00:07:37] means in order for it to be efficient, I
[00:07:39] would have to load all 81 GB into RAM,
[00:07:42] and my RAM is also still being used by
[00:07:43] some other processes on my machine.
[00:07:46] Okay? So, that's what you're paying
[00:07:47] attention to. I'm just explaining that
[00:07:49] because the model selection is the most
[00:07:50] important part. For most of you, running
[00:07:53] like a 9 billion parameter model will
[00:07:55] work. Again, it's not going to perform
[00:07:57] as good as Opus 4.6, but it will still
[00:07:59] give you decent performance and do some
[00:08:01] basic things that you need. So, the more
[00:08:03] hardware you have, the richer you are,
[00:08:05] right? The better models you can run,
[00:08:07] but that's kind of how it works. And
[00:08:08] again, if you wanted to connect to
[00:08:09] something else like a tool, you need
[00:08:10] this tool calling ability. If you go
[00:08:13] look at the models list, a lot of them
[00:08:15] now do have the ability to call tools or
[00:08:17] to do thinking or all of these different
[00:08:19] things. So, check those out, okay? And
[00:08:21] Gwen-3-Coder-Next is also a good model
[00:08:23] that's a little bit lighter that you can
[00:08:24] run as well on your own computer. Okay.
[00:08:27] So, now that we know the model that we
[00:08:29] want to use, what we can do is we can
[00:08:30] type "Ollama pull" and we can just go
[00:08:32] find the name of the model. So, mine I'm
[00:08:35] just going to go with maybe 35 billion,
[00:08:37] and I'm going to paste this here. So,
[00:08:38] Gwen-3.5-Coder-35B.
[00:08:41] Pull is now going to pull the manifest
[00:08:43] down and download the entire model and
[00:08:45] all of its weights. This is going to
[00:08:46] take a long time. Uh well, my case my
[00:08:48] internet is actually incredibly fast
[00:08:50] here,
[00:08:51] which I'm surprised by. You can see it's
[00:08:52] downloading 23 GB. So, I'm going to wait
[00:08:55] for this to finish. Once it's done, I'll
[00:08:57] be right back, and then we're going to
[00:08:58] start running the model, and then I'll
[00:08:59] show you how to connect the tools. All
[00:09:01] right, so this just finished, and now
[00:09:02] the first thing I want to do is just
[00:09:03] quickly test the model. So, to do that,
[00:09:06] I'm going to type "Ollama run" and then
[00:09:08] Gwen and this is going to be
[00:09:10] 3.5-Coder-35B.
[00:09:12] 35 billion, and then this is just going
[00:09:14] to run it directly in Ollama. I'm going
[00:09:16] to show you a better way to run it in 1
[00:09:17] second, but at least this will allow us
[00:09:19] to test it. Should take a second to
[00:09:20] load. Again, it does need to load up RAM
[00:09:23] here with all of the weights, and then
[00:09:24] as soon as it does that, we can start
[00:09:25] chatting with it and get like text-based
[00:09:28] responses. Okay, so I just gave it a
[00:09:29] random prompt like, "Hey, tell me what
[00:09:30] you're good at doing," and let's see
[00:09:31] kind of the response time that we're
[00:09:33] getting here from the model. Again, the
[00:09:35] larger the model, typically the slower
[00:09:37] it's going to be on your machine unless
[00:09:38] you have like a really fast good
[00:09:40] machine. And in my case, you can see
[00:09:42] this is taking a while, so I probably
[00:09:44] get downloaded a model that was a little
[00:09:46] bit too large for the specs that I had.
[00:09:49] Again, this one I believe is using 24 GB
[00:09:51] of RAM. If I go down to the 27 billion
[00:09:53] parameter one, I'm more at like 17,
[00:09:56] which is a little bit more manageable.
[00:09:57] So, if this takes too long, I'll switch
[00:09:59] over to the other one. Anyways, just
[00:10:01] want to show you the reality here. I
[00:10:02] don't really know exactly what's going
[00:10:03] to happen. You have to kind of test it
[00:10:05] out and see which models actually work
[00:10:07] on your machine. Okay, so trying to run
[00:10:09] the other one wasn't really working. I
[00:10:10] wasn't getting any response after like a
[00:10:12] minute, so I've just switched to use the
[00:10:14] 27 billion parameter model, which now is
[00:10:16] fine. It also doesn't help that I'm
[00:10:17] recording a video right now, and you can
[00:10:19] see that it's giving me its live
[00:10:20] thinking process. Well, we have quite a
[00:10:22] few tokens per second as the output. Now
[00:10:24] again, this is going to take a second to
[00:10:26] run, right? It's going to be slower than
[00:10:27] you running it in Claude, but the point
[00:10:29] is you're running it on your own
[00:10:30] machine, and you know, that's a huge
[00:10:32] advantage. So, you play around with the
[00:10:33] different models to determine what it is
[00:10:36] that you actually need. So, it's doing
[00:10:37] this whole thinking process. Hopefully,
[00:10:38] it's going to give me, you know, like a
[00:10:40] valid answer here in the second, but
[00:10:42] generally speaking, it's working, and
[00:10:44] now we can move on to the next step
[00:10:45] where we start doing the integrations.
[00:10:47] Oh, and there you go. Okay, it's giving
[00:10:48] me the answer as we speak. And I mean,
[00:10:50] that didn't take too long. That's pretty
[00:10:52] decent, and it looks like it's giving me
[00:10:53] a pretty comprehensive answer. So, it's
[00:10:55] not just like a super basic model. All
[00:10:57] right, so continuing here, let's now go
[00:10:59] to the tool integration component. Now,
[00:11:01] in order for us to actually run MCP
[00:11:03] servers inside of Ollama, we need to use
[00:11:06] something called the MCP client for
[00:11:08] Ollama. Now, there's a few other tools
[00:11:10] and abilities to do this, but Ollama
[00:11:12] does not natively support MCP. So,
[00:11:14] effectively, what we need to do is use
[00:11:16] something called a bridge, which is
[00:11:17] going to connect to the MCP server,
[00:11:19] discover the tools, and then share those
[00:11:21] with Ollama in real time, and just act
[00:11:23] as a proxy for doing the tool calling
[00:11:25] and getting the results. Now, the best
[00:11:27] one that I found is MCP client for
[00:11:28] Ollama. I'll leave a link to it in the
[00:11:29] description. Of course, it's open source
[00:11:31] and available, and I'll just show you
[00:11:33] the commands you need. You don't need to
[00:11:34] read this whole thing. Now, in order for
[00:11:36] us to use that, like I mentioned, we do
[00:11:37] need to use the Zapier MCP server.
[00:11:39] Again, massive shout out to them for
[00:11:41] sponsoring this video. This is free to
[00:11:43] use. The way that it works in terms of
[00:11:44] pricing is that yes, if you do use it a
[00:11:46] massive amount, you will need to pay for
[00:11:48] it, but it lends the same actions from
[00:11:50] your Zapier plan. So, if you're familiar
[00:11:52] with Zapier, it's very popular for
[00:11:53] automations. I use it in all of my
[00:11:55] businesses, and it does something called
[00:11:57] zaps. So, it like zaps an automation or
[00:11:59] zaps something to a platform. And each
[00:12:01] one of those zaps is like one credit,
[00:12:03] right? Or yeah, one zap. So, when you
[00:12:05] use the MCP server, every time you use
[00:12:07] it, it just acts as like one zap towards
[00:12:10] your plan, which is totally fine, and
[00:12:12] you can get, you know, like thousands of
[00:12:13] them for free effectively without you
[00:12:15] having to pay anything. So, the way that
[00:12:17] this will work is just go to this link.
[00:12:19] I'll leave it in the description. And
[00:12:20] what you can do is just press get
[00:12:21] started. When you do that, it should
[00:12:23] bring you to a page that looks something
[00:12:25] like this, where it shows Zapier MCP,
[00:12:27] and you can see like the number of
[00:12:28] tasks, right, that are being used I've
[00:12:30] currently used so far. Now, from here,
[00:12:32] what we're going to do is go to new MCP
[00:12:34] server. From the MCP server, we're just
[00:12:36] going to select other, but you also
[00:12:38] could connect this to any of the other
[00:12:40] AI agents that you're using. So, it
[00:12:41] doesn't just need to be, what do you
[00:12:43] call it, um,
[00:12:44] what am I using here? Olama? Okay, so
[00:12:46] I'm going to go other because this is
[00:12:48] Olama, and they don't just show that on
[00:12:49] here. From here, I'm now going to
[00:12:51] connect some different tools that I
[00:12:52] have. So, for tools, let's go ahead and
[00:12:54] connect something like Notion cuz that's
[00:12:55] like pretty visual and easy to see. And
[00:12:58] I'm just going to select all of the
[00:12:59] tools and just make them all available,
[00:13:01] but you can obviously safeguard which
[00:13:02] ones you want. So, I'm going to go ahead
[00:13:04] and now connect my Notion account. It's
[00:13:06] literally as easy as just using the
[00:13:07] OAuth, and then all of the security is
[00:13:09] handled for you. So, what I'm going to
[00:13:10] do is just connect it to my personal
[00:13:12] account so that I don't really care if
[00:13:14] it does something wrong. So, let's just
[00:13:16] connect it to new page and the second
[00:13:17] channel page, and maybe this December
[00:13:20] 2025 travel. You can see I have just all
[00:13:22] my travel stuff in here. So, let's just
[00:13:24] select all of it, and at minimum, it can
[00:13:26] maybe summarize some of the stuff that
[00:13:27] we have inside of here. Okay, so Notion
[00:13:29] is now connected. Editors, please just
[00:13:31] make sure you're blurring my email
[00:13:32] there. Let's add all of the tools here
[00:13:34] now to this MCP configuration. And just
[00:13:37] because we're at it, we can just add
[00:13:38] another one. So, let's add something
[00:13:40] like, I don't know, there's literally
[00:13:42] 8,000 of them. So, you kind of just have
[00:13:44] to figure out what you want and then you
[00:13:45] can start searching them to find
[00:13:47] anything. Like, I don't know, do they
[00:13:48] have meta?
[00:13:49] Let's see here. Yeah, they have like 100
[00:13:51] meta things. Okay. Let's try maybe
[00:13:54] Google Calendar. And let's just same
[00:13:57] thing, select all, connect, and let me
[00:13:59] just connect it to one of my accounts.
[00:14:01] All right, so I've got that connected.
[00:14:02] Obviously, I can go crazy and add as
[00:14:03] many of these as I want, but for now
[00:14:05] we'll just stick with these two. And now
[00:14:07] if we want to actually connect this to
[00:14:08] Ollama, we're going to go to this
[00:14:10] connect tab here and we're going to
[00:14:11] generate a new token. Now, when we
[00:14:13] generate the token, we've got to make
[00:14:14] sure we save this and obviously you
[00:14:16] don't want to share it with anyone else.
[00:14:17] So, you can see there's a full URL with
[00:14:19] the token. This is the one that I want,
[00:14:20] so I'm going to copy that, but you can
[00:14:22] also just connect, um, what is it? Like,
[00:14:24] through a standard MCP configuration
[00:14:26] using the authorization header. A few
[00:14:28] different ways depending on the tool
[00:14:29] you're using, you'll use a different
[00:14:30] one, but we want the URL with the token
[00:14:33] and we're just going to save that. So,
[00:14:34] put that somewhere safe uh, cuz we're
[00:14:35] going to use that in 1 second. All
[00:14:37] right, so as I mentioned, the next step
[00:14:38] here is we're just going to install this
[00:14:40] Ollama uh, MCP client connector thing so
[00:14:43] that we can actually connect to the MCP
[00:14:44] server. So, in order to do that, you can
[00:14:46] do this directly with pip. So, pip
[00:14:48] install upgrade OLLMCP.
[00:14:51] Then you can run OLLMCP. You can also do
[00:14:53] UVX OLLMCP or you can run this
[00:14:56] installation step right here. So, for
[00:14:58] those of you running it through pip,
[00:14:59] it's probably going to be the easiest.
[00:15:01] And the way you do that, it's just make
[00:15:02] sure you have Python installed on your
[00:15:04] machine first. Okay, now from here
[00:15:05] there's a ton of configuration options
[00:15:07] once you've got this installed. I
[00:15:09] already installed it, but effectively
[00:15:10] all you would do, right, is just run
[00:15:11] this pip command or run this UVX
[00:15:13] command. I'll leave the link to this in
[00:15:14] the description in your terminal. So,
[00:15:16] you just go here, right, if you have UV
[00:15:17] installed and you go UVX and then OLLMCP
[00:15:22] and it should just run, right, and
[00:15:24] install the dependencies and you should
[00:15:25] be good to go. Now, once that is
[00:15:28] installed, okay, so it's spun up and you
[00:15:29] can see by default it's using Gwen 2.5.
[00:15:31] I'll show you how we change the model in
[00:15:33] a second. Let's just quit so we can get
[00:15:35] out of that in the meantime. Uh there's
[00:15:37] a bunch of options you can use to run
[00:15:39] this. So you can do uh what is it?
[00:15:41] {dash} MCP server where you're
[00:15:42] specifically specifying an MCP server,
[00:15:44] which is what we're going to do. You can
[00:15:46] do auto discovery where it's going to
[00:15:47] look in your Claude's configuration
[00:15:49] actually. And then you can specify the
[00:15:51] model, the host, the version, all of
[00:15:53] that fun stuff. So what we want to do is
[00:15:55] we just want to specify the model and
[00:15:56] the MCP server. So I'm just going to
[00:15:58] show you the command to do this and that
[00:16:00] we can run it. Okay, so effectively
[00:16:01] we're going to run O L L M C P {dash}
[00:16:04] {dash} MCP server URL. We're going to
[00:16:06] take our server URL. I just stored it in
[00:16:09] my browser, which I know is horrible,
[00:16:10] but for the video that's fine. And I'm
[00:16:12] going to paste this in. So put the URL
[00:16:15] including the token. So we've just done
[00:16:16] that. And actually I believe we need to
[00:16:18] put this inside of quotation marks, a
[00:16:21] set of double quotes just so it
[00:16:22] identifies this as one argument. So
[00:16:24] let's do that and go back here. And then
[00:16:27] we're just going to specify the model
[00:16:29] that we want to run and it's going to
[00:16:30] run an Ollama-like environment for us.
[00:16:32] We're going to go {dash} {dash} model
[00:16:33] and then Gwen 3.5 {colon} and then 27B
[00:16:37] or whatever parameter version you're
[00:16:39] using and go ahead and hit enter. So
[00:16:41] again, Ollama MCP {dash} {dash} MCP
[00:16:44] server URL, put the server URL you want
[00:16:46] to connect to, {dash} {dash} model and
[00:16:48] we're good to go. You can connect to
[00:16:49] multiple servers if you want for MCP. Uh
[00:16:51] however, if you have Zapier you just
[00:16:53] need one because it connects to all of
[00:16:54] them by default. Okay. So now we're
[00:16:56] going to do that. It's going to try to
[00:16:57] connect to this URL. You can see it's
[00:16:59] connected and now has access to these
[00:17:01] various tools. It's also in thinking
[00:17:03] mode and you can see that you can change
[00:17:05] a bunch of stuff here. So if you want to
[00:17:06] change the thinking mode configuration,
[00:17:08] you can type a TM. If you want to show
[00:17:10] the thinking, ST. If you want to show
[00:17:11] the metrics, SM. If you want to view the
[00:17:13] various tools, type tools, right? So
[00:17:16] let's type T and we should be able to
[00:17:18] see all of the different tools here, and
[00:17:19] you can see it's exposing all of the
[00:17:21] tools that we connected with the Zapier
[00:17:23] MCP server. So, I'm just going to press
[00:17:25] Q to get out of that, okay? And it's
[00:17:27] going to bring us back here, show us
[00:17:29] that we're in thinking mode, and let's
[00:17:30] try something basic. Can you tell me
[00:17:33] where I was traveling in the last year
[00:17:34] based on my Notion documents? Okay? And
[00:17:38] then we're going to go ahead and press
[00:17:39] enter, and you can see that it begins to
[00:17:41] work, and now it should hopefully
[00:17:42] connect to our MCP integrations, start
[00:17:45] calling and using those tools, and
[00:17:46] giving us the result. Okay, so you can
[00:17:48] see it's actually prompting me if I want
[00:17:49] to enable the tool call. You can see
[00:17:51] that it's going to go travel and start
[00:17:53] searching in Notion to find this page by
[00:17:55] the title. So, let's go ahead and type
[00:17:57] Y. Now, again, I'm not going to lie to
[00:17:59] you. This is slow. It's not speedy
[00:18:02] execution. You're going to sit here for
[00:18:03] a little bit, but this is the kind of
[00:18:05] trade-off when you're running on your
[00:18:07] own machine. If I had a really high-end
[00:18:09] machine, which by the way, I'm
[00:18:10] considering buying soon because I can
[00:18:11] just run a ton of local models, this
[00:18:13] would be a lot faster. I can use a
[00:18:14] better parameter but also I could just
[00:18:16] go down to like the 9 billion parameter
[00:18:17] model, and then this is going to be
[00:18:19] lightning fast. I might get a little bit
[00:18:21] less accurate replies, but that's the
[00:18:22] trade-off. So, play with them. Let me
[00:18:24] know in the comments down below, but
[00:18:26] let's wait for this to finish and make
[00:18:27] sure it can actually kind of do what I'm
[00:18:28] saying. Okay, so it did take a second
[00:18:30] here. There was a lot of tool calls that
[00:18:31] it ran through, but it was able to get
[00:18:33] all the content, and we can see now that
[00:18:35] it has all of the details here and it's
[00:18:37] starting to show where I was traveling,
[00:18:38] what flights I was taking, all of this
[00:18:40] kind of stuff that I was doing back in
[00:18:42] December 2025. So, is it able to go
[00:18:45] through Notion? It was able to do that.
[00:18:46] Let's quickly test one with the
[00:18:47] calendar, and then I want to show you
[00:18:49] how we can do this from code. Can you
[00:18:51] create a new booking today at 4:00 to
[00:18:54] 5:00 p.m. that is just a time block
[00:18:56] saying eat lunch in my calendar? Let's
[00:18:58] just test something simple and just see
[00:18:59] if it can like take the action rather
[00:19:02] than just reading some content. Let's
[00:19:04] test it. Okay, so it's telling me here
[00:19:05] that it did create the event. Uh let me
[00:19:08] go check my calendar and see if that's
[00:19:09] true. Okay, so I did find it. It is at
[00:19:11] 4:00 to 5:00 a.m. not 4:00 to 5:00 p.m.
[00:19:14] So let's just tell it to fix that. Hey,
[00:19:16] the event's at 4:00 to 5:00 a.m. Move it
[00:19:18] to 4:00 to 5:00 p.m. Okay, probably just
[00:19:21] based on how it called the tool again.
[00:19:23] We're not using the best model possible,
[00:19:24] but if we scroll through here, we can
[00:19:26] see all of the stuff. And I'm also
[00:19:28] guessing that maybe this is a time zone
[00:19:29] issue because it's probably doing this
[00:19:31] in Eastern time which my calendar is set
[00:19:33] to and I'm currently 12 hours ahead of
[00:19:35] that. Okay, so that's it probably
[00:19:36] actually did do it at the correct time.
[00:19:37] It's just in the wrong time zone
[00:19:39] awareness area. So anyway, we'll skip
[00:19:41] this for now. I want to go over to the
[00:19:42] code. I want to show you how we can do
[00:19:43] this inside of code as well, not just
[00:19:46] from this kind of terminal environment
[00:19:48] in case you want to run a local model
[00:19:49] through something like LangChain. All
[00:19:51] right, so I just opened up cursor. I've
[00:19:52] got some code here. I just had Claude
[00:19:54] code generate this. So it's probably you
[00:19:55] know a more optimal way to run it. But
[00:19:57] effectively, I just want to show you
[00:19:58] that from code, you can just directly
[00:20:00] connect to a Llama because a Llama
[00:20:02] exposes a REST API server. And then from
[00:20:05] there, if you want to use an
[00:20:06] orchestration framework like LangChain,
[00:20:08] you can really easily connect to an MCP
[00:20:09] server. So you can see like I've defined
[00:20:11] my Zapier MCP URL. I define it as a
[00:20:14] client. I then just create a react agent
[00:20:16] using LangChain here. I think there's a
[00:20:18] newer version, but this one works just
[00:20:19] fine. I get all the tools, pass it
[00:20:21] there, and then I can just start
[00:20:22] chatting with my agent directly inside
[00:20:24] of code. So if you're building a
[00:20:25] product, you want to run a local model,
[00:20:27] you have high enough hardware, you can
[00:20:29] do it really easily. I just have a few
[00:20:31] packages, right? LangChain MCP adapters,
[00:20:33] LangChain a Llama, LangGraph in Python.
[00:20:35] You can do it in any language you want.
[00:20:37] And you don't even have to use these
[00:20:38] packages. They're just an abstraction on
[00:20:40] top of the HTTP server or REST API that
[00:20:42] is exposed. So you can just directly
[00:20:44] call a Llama, call your model, and then
[00:20:46] connect it up to the MCP server like I'm
[00:20:48] doing right here. So I'm just running it
[00:20:50] and I'm just going to go like
[00:20:52] you know, actually what calendar events
[00:20:55] do I have in the next, I don't know, 5
[00:20:58] days?
[00:20:59] Okay, and let's see what it gives us.
[00:21:01] Okay, so same thing. It's a little bit
[00:21:02] slow, but I got the response back here.
[00:21:05] You can see there's a bunch of data. I'm
[00:21:06] going to have to blur some of it because
[00:21:07] there's some custom stuff. So, um
[00:21:09] editors, please just like blur any of
[00:21:11] the important information. But
[00:21:12] effectively, it summarized all of the
[00:21:13] meetings that I have coming up here, and
[00:21:15] these are accurate based on what I know
[00:21:16] about the calendar. There we go, guys.
[00:21:18] With that said, that's going to wrap
[00:21:20] this up. This is super powerful,
[00:21:22] relatively easy to do. Yes, there's a
[00:21:24] few commands and set up, but once you
[00:21:25] get it, it's pretty much just plug and
[00:21:27] play. And I mean, this is a huge unlock
[00:21:29] if you want to run something locally, or
[00:21:31] you want to build anything that relies
[00:21:33] on local models. Again, play with them,
[00:21:35] try out different models, see what kind
[00:21:36] of speed accuracy combo you can find.
[00:21:39] Let me know what you think of the video,
[00:21:41] and I look forward to seeing you in the
[00:21:42] next one.

---
*RAW — not yet passed through D.R.D deconstruction. Do not integrate into department files.*
