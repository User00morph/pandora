# RAW EXTRACT — I Traded Options Using AI No Coding Required

- **Video ID:** AoHUcyVh7NY
- **Duration:** 1:27:33
- **Words:** ~15,073

---

[00:00:00] fixed right up. Okay, so we should be
[00:00:02] okay. What's up everyone? I am extremely
[00:00:07] stoked for this session. What we're
[00:00:11] doing today
[00:00:13] is going through and level setting on
[00:00:18] Sunday. The actual project no code
[00:00:21] launch video will be released. And as
[00:00:25] Shreyj just noted in the chat, shout out
[00:00:28] to Shreyj for taking a peek at this
[00:00:33] document, there's going to be a file
[00:00:36] that corresponds with that video that
[00:00:38] will be accessible to everyone. It's a
[00:00:41] quick start guide. It's like 20 some odd
[00:00:44] pages. And my vision for that document
[00:00:48] is it's a framework that literally
[00:00:51] anybody can download and follow to build
[00:00:56] effectively what I have in project no
[00:01:00] code. Now it's not gated by email. It's
[00:01:03] not a lead magnet. I get no data from
[00:01:06] anybody for going to it. It's something
[00:01:08] that I am extremely passionate about
[00:01:13] getting out to as many people as I can
[00:01:16] because I think for a lot of people this
[00:01:18] will massively change your trading. So
[00:01:23] ahead of that session on Sunday, that
[00:01:26] video will release in the afternoon. I
[00:01:29] wanted to take a second on an actual
[00:01:31] live stream with you guys. I'm going to
[00:01:32] work through some notes with you ahead
[00:01:35] of time on some like really basic stuff
[00:01:38] that didn't necessarily seem appropriate
[00:01:42] for that video. And then I'm going to
[00:01:46] actually give you guys a little bit of a
[00:01:48] tour of the the project workspace and
[00:01:52] stuff. So you'll have an idea of like
[00:01:53] what it actually looks like, some
[00:01:55] concepts on what it can do, how to
[00:01:57] interact with it, and there really
[00:02:01] should be a lot of time towards the end
[00:02:04] for open Q&A. I'm specifically
[00:02:06] scheduling this one. A lot of my streams
[00:02:09] are about a half hour now, 45 minutes.
[00:02:11] I'm I've cleared off the rest of the day
[00:02:14] effectively so that we can get everybody
[00:02:20] comfortable so that you are up and
[00:02:23] running.
[00:02:24] One admin note and this is actually for
[00:02:27] project no code itself. I'm actually
[00:02:30] super super duper stoked on is I just
[00:02:36] finished my last big data ingest for my
[00:02:40] database, which for those that don't
[00:02:43] know, in order to like really do this,
[00:02:46] I've actually put my personal database,
[00:02:50] the one that I've done most of my
[00:02:51] research over my trading career, I've
[00:02:54] actually put that on ice and I'm
[00:02:57] completely using project no code at
[00:03:00] least ideally for the foreseeable future
[00:03:02] if not forever right my intention is to
[00:03:05] kind of put my money where my mouth is
[00:03:06] in the context of like doing the
[00:03:08] research that I would do and it being
[00:03:11] done in a place that again I've made
[00:03:13] publicly accessible to everybody so it's
[00:03:15] not like some sort of you know niche
[00:03:18] thing that I have that nobody else has
[00:03:19] my old database very much was like that
[00:03:22] this one still will have that in terms
[00:03:24] of IP but in terms of structure and
[00:03:27] stuff We're all we're all working off
[00:03:29] the same sheet of music, which I'm
[00:03:31] really excited about. And the only thing
[00:03:35] I have to come clean about early on is
[00:03:38] for everything that I've built so far,
[00:03:41] and there has been from all public
[00:03:43] facing sources, I was using none of my
[00:03:45] own stuff from my old DB. The only
[00:03:48] change that I did make to that is for
[00:03:51] intraday level options data. And the
[00:03:55] reason is it was going to cost me like
[00:03:59] 20 grand to get a bulk download of what
[00:04:02] I wanted. I already have it. And that I
[00:04:07] I just wasn't going to do that. Now,
[00:04:09] that doesn't mean for you to get that
[00:04:11] same data, it's 20 grand. It's not. You
[00:04:13] can use the standard API and get it, but
[00:04:17] it's a little bit slow. So, it was going
[00:04:19] to take like 2 3 weeks for me to
[00:04:21] actually get it all. So what I did was I
[00:04:24] did a file transfer just like I would do
[00:04:26] effectively for an API, but I just did
[00:04:28] it from my own machine. So I have to put
[00:04:31] that out there. It's not data that
[00:04:33] nobody it's not like proprietary data
[00:04:35] that you couldn't access. You could
[00:04:37] absolutely access it. You can pay a lot
[00:04:40] of money and get a bulk download if you
[00:04:41] want or you could just be patient, which
[00:04:43] is what I think most people should do.
[00:04:45] Prioritize appropriately and just use an
[00:04:47] API, you know, few couple hundred bucks
[00:04:49] a month and run it that way. It's just
[00:04:52] going to take you a little bit longer.
[00:04:54] It's a pittance compared to what this
[00:04:56] whole thing was. Again, in the video
[00:04:58] that you're going to see on Sunday, I
[00:05:00] have literally spent deep into well over
[00:05:03] like six figures on getting data because
[00:05:06] it used to be way more [ __ ] expensive
[00:05:09] and way harder to get, which is also
[00:05:11] why, as you could tell, I'm I'm really
[00:05:13] emphatic about this whole thing. It's
[00:05:14] [ __ ] awesome. So, let's get this
[00:05:19] started. The purpose for the primer
[00:05:22] today is I want everybody to have at
[00:05:26] least a generalized base understanding
[00:05:29] of the main tools we're going to be
[00:05:31] using which is AI. And AI in this
[00:05:34] context looks a lot different than a lot
[00:05:36] of people understand. So, in order for
[00:05:39] us to have a good launch on Sunday and
[00:05:43] then for the Pro Plus members for us to
[00:05:45] kick off our workshop on Monday, we're
[00:05:48] going to do a Zoom session that's
[00:05:49] wrapped around some of this stuff to
[00:05:51] kick us off that we need these basics
[00:05:55] covered. So, let's let's talk about it.
[00:05:59] This you will see again on Sunday. This
[00:06:02] is just in case somebody doesn't catch
[00:06:03] that video or is completely unfamiliar
[00:06:05] with this thing that I've been doing
[00:06:06] called project no code. And I have a
[00:06:11] daily log for this that I'll give you a
[00:06:15] link to as well. This is on X. But the
[00:06:18] the cliff notes for this, I literally
[00:06:20] completely randomly started this last
[00:06:22] Monday. It was the 18th of May. I was
[00:06:25] doing research for something else and I
[00:06:28] literally was just like, ah, you know, I
[00:06:30] wonder what AI could do. I have
[00:06:31] subscriptions to all of the top AI
[00:06:33] models because they're super cool,
[00:06:35] interesting, and I like learning and I
[00:06:37] like new technology. So, I just started
[00:06:40] probing that a little bit. Long story
[00:06:42] short, it was really [ __ ] good. And I
[00:06:45] was just like, "Oh, damn." Like, I
[00:06:47] actually think this is at a point now
[00:06:49] that a regular person could do this. So
[00:06:53] what I wanted to do is approach this
[00:06:55] project from the pure lens of a trader
[00:06:59] who has experience in markets but not
[00:07:02] necessarily an engineer developer
[00:07:04] doesn't have like the coding background
[00:07:06] so to speak and I started off there that
[00:07:09] that's exactly what I've been working on
[00:07:11] the last two weeks now and what you'll
[00:07:15] be able to get following the quick start
[00:07:18] guide and the playbook here for project
[00:07:20] no code is you're going to spend some
[00:07:23] money upfront. Again, depending on what
[00:07:25] level of data you want, what fidelity of
[00:07:28] data you want, that all changes price.
[00:07:30] I'll give you some ideas on that in a
[00:07:32] little bit. But the crux is once it's
[00:07:37] built, you don't have to have some sort
[00:07:39] of recurring cost. The data is yours. So
[00:07:43] that's the cool part. The way to think
[00:07:44] about all the APIs and stuff, they're
[00:07:46] monthly subscriptions, but once you get
[00:07:49] what you need, you can always turn them
[00:07:51] off, pivot to free sources depending on
[00:07:53] what you have access to, and then you
[00:07:56] don't have to have any sort of ongoing
[00:07:58] cost other than storage, compute,
[00:08:00] maintenance, and the AI model that you
[00:08:02] pick. The underpinning for this is that
[00:08:06] we're using AI. So, you you you're going
[00:08:08] to have to pay for an AI model. I don't
[00:08:11] think this would be possible in any sort
[00:08:13] of reasonable time frame with free AI. I
[00:08:16] would say, you know, try it. There's no
[00:08:18] reason not to at least give it a shot if
[00:08:19] you're trying to do it on the super
[00:08:20] cheap. But the other thing I will remind
[00:08:23] you is that if you want to trade at a
[00:08:26] professional level like I do, there's
[00:08:29] there's a cost, right? It's just like
[00:08:32] any other business, any other business
[00:08:34] has some level of expense to be a
[00:08:37] business and do what they do. This is
[00:08:39] just part of it, but you'll have total
[00:08:43] optionality on what the whole thing
[00:08:45] looks like.
[00:08:47] The coolest thing about this so far is
[00:08:50] this continues to be the underpinning. I
[00:08:54] have written literally zero lines of
[00:08:58] code. Now, for those that don't know, I
[00:09:01] also don't have a coding background, but
[00:09:03] I self-taught myself in my 20s because I
[00:09:07] realized how important it was in order
[00:09:09] to be able to do that in our career
[00:09:12] field or in our general field. You can't
[00:09:16] successfully iterate fast enough on this
[00:09:19] kind of cycle without some type of
[00:09:24] technological backing.
[00:09:27] This should look roughly familiar to a
[00:09:29] lot of you guys. It's a little busy and
[00:09:31] I'll explain it in a second, but what
[00:09:33] this is in a nutshell is the outlier
[00:09:36] strategy process. This is the same thing
[00:09:38] that you guys have seen, I don't think
[00:09:41] that this is a stretch at this point,
[00:09:42] hundreds of times. This is nothing new.
[00:09:46] The entire purpose of the outlier
[00:09:50] strategy process in this context is to
[00:09:54] give you a framework for ideas. Oh [ __ ]
[00:10:00] Tablet just damn it. Tablet just died.
[00:10:04] Unbelievable.
[00:10:06] You get you get a new PC, super
[00:10:08] expensive, and your [ __ ] tablet dies.
[00:10:10] Well, anyways,
[00:10:12] the the whole point is to be able to
[00:10:15] operate on the outlier strategy process.
[00:10:18] But the thing that's very genuine is
[00:10:23] when I execute the outlier strategy
[00:10:26] process, this I'm using machines for in
[00:10:31] order to iterate fast enough. this. I'm
[00:10:34] using machines for this build strategy
[00:10:38] section or I'm sorry the the testing
[00:10:41] section. I'm also using machines for the
[00:10:44] point that I'm making is a lot of what I
[00:10:47] do in my personal
[00:10:51] implementation of trading is data
[00:10:54] analysis and some type of development
[00:10:58] work with Python, Jupiter, stuff like
[00:11:02] that or but the the coolest thing about
[00:11:06] this is now you all have access to it
[00:11:08] too. that that barrier is completely
[00:11:10] broken because you can use AI. The way
[00:11:13] that this will fit into your process is
[00:11:16] for something like a profit mechanism.
[00:11:18] Once you have enough data, you can just
[00:11:21] start casually looking through your data
[00:11:24] using AI to try and identify interesting
[00:11:28] market effects, interesting profit
[00:11:31] mechanisms that might be available to
[00:11:33] you. So rather than doing something like
[00:11:36] guessing if an opening range breakout
[00:11:39] works, you could run a test on it and
[00:11:43] later at the end of the session if we
[00:11:44] want to do a P app on something like
[00:11:46] that, we literally can. I can pull up
[00:11:48] the platform, you can do it live
[00:11:49] together. That's the cool part about
[00:11:50] this.
[00:11:52] So that that allows you to more
[00:11:55] efficiently go through this because the
[00:11:57] reality when you're trying to create a
[00:12:00] trading strategy this this first step
[00:12:02] and second step takes a lot of time. A
[00:12:05] lot of traders go into this kind of with
[00:12:07] the wrong expectation. The way you
[00:12:09] should think of it is like your primary
[00:12:11] function as a trader really is
[00:12:13] researcher. If you want to be a good
[00:12:15] trader, if you want to be a shitty
[00:12:16] trader that is lazy and will lose money,
[00:12:19] then yeah, sure. Don't do this. try to
[00:12:21] do like some sort of [ __ ] patterns
[00:12:23] on a chart and hope it works. But if you
[00:12:26] want this to actually work, have
[00:12:27] confidence in it, and be good at it long
[00:12:29] term, you have to research. And the
[00:12:33] issue with research is it takes a while.
[00:12:36] For example, opening range breakout.
[00:12:38] First, you have to learn what it is.
[00:12:40] Second, you have to kind of codify the
[00:12:42] general rule set around it. Then you
[00:12:44] have to figure out where you might want
[00:12:46] to look at it in. Meaning, what's the
[00:12:49] universe? Then if you don't have some
[00:12:51] sort of technological backing, you're
[00:12:53] going to have to open up literally
[00:12:55] thousands of charts and take hand notes
[00:12:58] or use Excel if you want to be slightly
[00:13:00] advanced and churn through tons of them.
[00:13:05] And that is unbelievably time consuming.
[00:13:08] That speed is a problem because what you
[00:13:12] have to accept upfront as a trader is
[00:13:15] literally 95% plus of what you look at
[00:13:19] is not going to work. You are you are
[00:13:23] literally digging for gold. That is what
[00:13:26] this stuff is. That's what edge is
[00:13:29] digging for gold. The cool part is
[00:13:32] especially for you guys here, I I
[00:13:37] without a doubt shortcut that process
[00:13:39] massively. And it's not just for the
[00:13:41] paid part of the community. It's
[00:13:42] literally for everybody. You can go
[00:13:44] through my YouTube channel. You can look
[00:13:45] up stuff like Edge. You can look up
[00:13:47] stuff like Profit Mechanisms. That's
[00:13:49] immediately going to advance you way
[00:13:51] past the majority of people right out of
[00:13:54] the gate. That's just the reality
[00:13:55] because it's going to teach you to
[00:13:57] actually develop a research process and
[00:14:00] understand like what to actually look
[00:14:02] for. That itself takes time. But once
[00:14:05] you have those pieces down, you know
[00:14:07] what to look for. Then you got to
[00:14:08] [ __ ] look. So this is a general
[00:14:12] process. It takes time. Going back to
[00:14:15] opening range breakout, you are familiar
[00:14:18] with my work. You've watched some of my
[00:14:19] videos and you've done your own
[00:14:21] research. By the way, this is not all
[00:14:23] about like [ __ ] Eric and what Eric
[00:14:24] has put out. A lot of you will do this
[00:14:26] on your own. And you go to SSRN and you
[00:14:31] find opening range breakouts. You
[00:14:33] research a bunch of papers on opening
[00:14:34] range breakouts. You have an idea of
[00:14:35] what it is. Then you go start looking
[00:14:37] for it. You say, "All right, I'm going
[00:14:39] to focus on a 15minute or 30 minute a
[00:14:43] and I'm going to track how that behaves
[00:14:46] and I think I can trade it."
[00:14:49] Then you say, well, okay, the 30 minute
[00:14:52] did this over 2,000 names over the last
[00:14:55] 10 years. However long it took you to do
[00:14:57] that. Let's say you did that. By the
[00:14:58] way, with project no code, literally it
[00:15:01] take you 5 minutes to get that. If that,
[00:15:04] then you say, well, [ __ ] I want to try
[00:15:06] 15 minutes. Maybe that's better. I want
[00:15:09] to try five minutes. Maybe that's
[00:15:10] better. [ __ ] it. I want to do a minute
[00:15:13] level grid search from the [ __ ] open
[00:15:16] and I want to see what's optimal. All of
[00:15:19] that now is open to you and the reality
[00:15:22] is that's where your edge ultimately
[00:15:25] will be developed how you can do that
[00:15:27] across different profit mechanisms.
[00:15:30] Now there is a required video that I
[00:15:36] rarely have like quote unquote hard
[00:15:38] requirements. This one is a no [ __ ] hard
[00:15:43] requirement for everybody is watch the
[00:15:45] video that I'm pasting in now. That
[00:15:48] video is called the basics of back back
[00:15:51] testing. That is a hard requirement. I'm
[00:15:54] actually going to link to it in the show
[00:15:56] notes below as well in case anybody
[00:16:00] isn't able to see the chat. I know that
[00:16:02] happens sometimes. The reason why that's
[00:16:05] a requirement is because one of the
[00:16:08] biggest issues
[00:16:10] of testing stuff like this is you can
[00:16:14] trick yourself. You can trick yourself
[00:16:16] really really easily and it's super
[00:16:19] duper dangerous. That's why it's a
[00:16:21] requirement. The reason why it's super
[00:16:23] duper dangerous is because you can go
[00:16:25] back through history. You can look at
[00:16:29] all different kinds of configurations of
[00:16:31] stuff and you can overfit your way into
[00:16:34] something that looks really really good.
[00:16:36] That's very dangerous. And there are
[00:16:38] specific things you need to do in order
[00:16:40] to prevent that. They're not hard. You
[00:16:42] just have to know to do them. So the
[00:16:44] risk here is not knowing what you don't
[00:16:46] know. That's the point of that video. It
[00:16:48] will elucidate the don't know what you
[00:16:50] don't know so then you do know and you
[00:16:52] don't make those [ __ ] mistakes.
[00:16:54] Simple things like bootstrapping some of
[00:16:56] your results, segmenting and then
[00:16:58] checking randomized order of things
[00:17:01] [snorts] using Monte Carlo simulations
[00:17:03] trained on your data to see different
[00:17:04] trajectories. All that kind of stuff is
[00:17:07] not difficult to do. Especially now with
[00:17:09] AI and project no code to do all of the
[00:17:12] stuff that I just said can easily be
[00:17:15] done in a single session. Whereas before
[00:17:17] even for me to code that stuff, it
[00:17:19] genuinely would take a while.
[00:17:25] That's what I'm talking about. This
[00:17:28] stuff is now open for business to
[00:17:32] everybody.
[00:17:34] So, we just talked about
[00:17:39] what this general project no code
[00:17:42] concept is, how it impacts
[00:17:45] your ability to move through something
[00:17:47] like the outlier strategy process. This
[00:17:49] is an example of what the database looks
[00:17:53] like. So, this is what we would call it
[00:17:54] a repo. And this this is the project.
[00:17:59] Mine looks
[00:18:02] close to this. I've changed it a little
[00:18:05] bit over time. This was captured a
[00:18:06] little bit earlier, but yeah, this is
[00:18:09] generally fine fine itself.
[00:18:13] Now,
[00:18:14] the whole point here is it's just a
[00:18:18] series of files. That's all. And in
[00:18:20] those series of files, you organize them
[00:18:22] however logically makes sense to you.
[00:18:24] The one thing to note and you should
[00:18:26] listen to AI as you go through this is
[00:18:28] there's some conventions that are
[00:18:29] normal. Like for example, the the
[00:18:32] claw.md
[00:18:34] that actually realistically shouldn't go
[00:18:36] in the docs folder. That should be under
[00:18:37] the root folder because that's where
[00:18:39] claude knows to look for it. That
[00:18:41] doesn't mean that you can't put it here,
[00:18:42] but then it means you'll have to direct
[00:18:44] claude to it, right? There's all these
[00:18:46] little kind of things like that that
[00:18:47] you'll learn on your own over time. And
[00:18:49] these are the kind of things
[00:18:50] realistically for the Pro Plus members
[00:18:52] that we're going to work through as you
[00:18:54] guys are building it alongside me in the
[00:18:56] Zoom workshops. The whole point for that
[00:18:58] is just these little gimmies and
[00:19:00] gotchies. But again, it's not
[00:19:01] gatekeeping. It's not I'm not even
[00:19:03] trying to convert anybody to pay. That's
[00:19:04] literally not it. It's just to let them
[00:19:06] know what's coming. This is all [ __ ] you
[00:19:07] can figure it out on figure out on your
[00:19:09] own. Just takes a little while. That's
[00:19:11] all. But you can absolutely do it for
[00:19:12] free. No subscription to nothing. That's
[00:19:15] what it's all about. being faster to
[00:19:18] iterate.
[00:19:19] Now, let's get into what really matters
[00:19:22] here. Understanding some of the
[00:19:25] different models available, what they
[00:19:27] are, how they work, strengths and
[00:19:29] weaknesses. So, if I look at the project
[00:19:34] as I wrote it, I primarily used Claude
[00:19:39] Claude code
[00:19:42] chat GPT via codeex. And we'll talk
[00:19:44] about all of these
[00:19:46] There are strengths and weaknesses to
[00:19:50] all of these models that you're going to
[00:19:53] learn and understand so that you can
[00:19:54] make a decision. This is your first
[00:19:56] homework item. Other second homework
[00:19:58] item. First homework item is watch that
[00:19:59] video. The second homework item is again
[00:20:03] if you intend to attempt to use the
[00:20:06] guide and all that kind of stuff to
[00:20:08] build your own research node, you're
[00:20:11] going to have to pick an AI agent at
[00:20:13] least one. What I would look to do
[00:20:16] personally is have two. And I'll explain
[00:20:19] why in a little bit. Three is better. I
[00:20:21] I literally have all of them. And one of
[00:20:24] the reason why the this project has
[00:20:26] taken me so much time, it's a tremendous
[00:20:30] amount of time
[00:20:32] over the last 2 weeks is primarily I
[00:20:37] spent a lot of time giving the same
[00:20:39] prompt to multiple agents to running
[00:20:43] code between agents to see what they
[00:20:45] would pick up. Again, my goal wasn't
[00:20:48] just to like build it for me. it was to
[00:20:51] document stuff throughout that entire
[00:20:53] process to be able to help you. But
[00:20:56] there's a a lot of small little nuances
[00:20:59] with stuff like that. But again, it's
[00:21:01] all stuff that you can easily figure out
[00:21:03] on your own. It'll just take a little
[00:21:06] time and a little bit of interaction.
[00:21:08] But [snorts] the the three on the left,
[00:21:10] those are the primary that I used and
[00:21:14] the two on the left specifically. And
[00:21:16] then I did not use Deepseek at all. The
[00:21:18] reason why I put it in here is just
[00:21:19] because I know it's cheaper to access
[00:21:21] for people. So, you can know it exists.
[00:21:24] I have nothing to say about its
[00:21:26] capability in this context because I did
[00:21:28] not use it. Did not use it at all.
[00:21:31] Here's a general comparison between
[00:21:33] these different models. Claude literally
[00:21:36] just launched 48. Most of what I built
[00:21:38] was built with 47 and now I've
[00:21:41] transitioned obviously to using 48. What
[00:21:44] I'm giving you here [snorts] are on the
[00:21:47] lefth hand side standard benchmarks. So
[00:21:50] these are tests that are given to the
[00:21:52] models. So it's not like you know Claude
[00:21:56] analyzes Claude and just you know
[00:21:59] jerryrigs the numbers so Claude looks
[00:22:01] better. It's the actual strengths and
[00:22:04] weaknesses
[00:22:05] of the models themselves. Now one thing
[00:22:09] to note is specifically with stuff like
[00:22:12] agentic coding and coding in general
[00:22:16] claude code tends to be really really
[00:22:20] solid.
[00:22:22] Codeex
[00:22:24] is getting really good. So I think if
[00:22:29] you're not sure between clawed code and
[00:22:32] codeex is like your primary engine, I
[00:22:35] genuinely don't think either one is
[00:22:37] going to steer you that wrong. The
[00:22:39] better solution is a combination of
[00:22:41] both.
[00:22:44] This just gives you a quick qualitative
[00:22:47] overview of really what they're good at.
[00:22:51] The cost side of it doesn't really
[00:22:53] matter to you in the near term. doesn't
[00:22:56] doesn't matter too much, but you'll have
[00:22:59] that for reference.
[00:23:01] Let's talk about what AI is so that you
[00:23:06] understand the strengths and weaknesses.
[00:23:08] I had a member in the the Discord, which
[00:23:11] is free for everybody to join. This is
[00:23:12] actually a free member. I had a member
[00:23:14] in the Discord that was complaining
[00:23:17] about using I forgot which AI model to
[00:23:21] test a strategy and they were
[00:23:24] effectively saying like hey you know I'm
[00:23:26] giving it this and it's not working and
[00:23:28] they were you know not not happy with
[00:23:30] that. They were kind of you know saying
[00:23:33] that it doesn't work and my immediate
[00:23:37] instinct was that they were [ __ ]
[00:23:40] something up. The reason why that was my
[00:23:42] immediate instinct is because I know
[00:23:45] well enough because at that point I had
[00:23:47] been working on project no code for a
[00:23:50] bit. I know well enough what they can do
[00:23:52] and what they described was not
[00:23:54] difficult. So that immediately tells me
[00:23:57] it's user error. It is a problem in how
[00:24:01] we're prompting and it's a problem in
[00:24:03] how we're using the tool which is what
[00:24:06] we need to align on so that we have a
[00:24:09] better relationship in this process.
[00:24:12] So if you think of
[00:24:16] what AI generally is, it's a force
[00:24:19] multiplier.
[00:24:21] You still need to be the thinking,
[00:24:25] planning,
[00:24:27] oversight
[00:24:28] on the entire thing. AI will be able to
[00:24:31] help you a lot with this whole thing,
[00:24:34] but you still have to be engaged and
[00:24:40] logically think through stuff because it
[00:24:42] is not perfect and you have to remember
[00:24:44] that. So using AI in this kind of thing
[00:24:48] does not like remove you from the
[00:24:50] process and it does not mean that you
[00:24:53] just kind of sit back, turn AI on and
[00:24:55] hope it o all goes well. It won't. I
[00:24:58] guarantee you it won't.
[00:25:01] But what you can do is iterate with AI.
[00:25:06] You can go back and forth, explore
[00:25:08] ideas. That's when it's strong.
[00:25:13] So this is an overview for those that
[00:25:16] don't know on like what an LLM is, large
[00:25:19] language model. It's trained on text and
[00:25:24] it's effectively like really good at
[00:25:27] predicting stuff. So the way to think
[00:25:30] about some of the errorprone pieces are
[00:25:34] when you introduce ambiguous terms and
[00:25:40] not clarifying enough what you are
[00:25:45] attempting to accomplish
[00:25:48] context window. That's probably one of
[00:25:50] the most important things that I could
[00:25:51] talk about in this today with you guys.
[00:25:55] For those that don't know, whenever you
[00:25:57] use AI, there is a context window. So,
[00:26:03] I'll literally pull over what's running
[00:26:05] right now. This is in Claude Code right
[00:26:07] now. And what I'm having it do is
[00:26:12] facilitate data transfer essentially.
[00:26:15] So, you can see Claude Code here, me
[00:26:17] here. But I want to show you this thing
[00:26:20] at the bottom here. You see this little
[00:26:23] blue blue circle? You see, see it says
[00:26:26] context. Context right now is at 550K of
[00:26:28] 1 million. 1 million is huge by the way
[00:26:30] relative.
[00:26:33] This context includes both my inputs and
[00:26:39] Claude's inputs.
[00:26:41] What happens is as you go back and
[00:26:44] forth, it consumes context. Context is
[00:26:49] the ability for Claude to follow or
[00:26:52] whatever AI agent you're using. Ability
[00:26:56] to follow everything that's going on
[00:27:00] without error or with less error.
[00:27:04] The problem is if you run out of
[00:27:07] context, you need to do something
[00:27:10] because you can't chat anymore. It
[00:27:11] literally won't let you. So to fix that
[00:27:16] some models claw does it um codeex does
[00:27:20] it or chatpt does it where you can
[00:27:22] compact the chat. Compacting the chat
[00:27:27] essentially takes all the prior context
[00:27:30] and it crunches it down in its memory
[00:27:32] base to a summary. What happens when you
[00:27:35] summarize? You lose a lot of detail. How
[00:27:38] do we circumn this? because we're
[00:27:41] working on something that's going to go
[00:27:43] through multiple context windows and
[00:27:46] it's going to take multiple chats. The
[00:27:48] way you fix this is actually really easy
[00:27:51] and I found a fantastic system that
[00:27:56] works exceedingly well.
[00:27:59] Here's what it is. What you do is set up
[00:28:04] first,
[00:28:05] and Claude will do this by itself when
[00:28:07] you introduce it to the environment, but
[00:28:10] you set up a Claude markdown file. MD,
[00:28:13] MD. For those that don't know what MD
[00:28:15] is, it's like a text file on steroids.
[00:28:18] That's all. MD Markdown.
[00:28:20] This becomes the internal turnover for
[00:28:24] Claude. So, any time that I open up a
[00:28:28] new Claude terminal inside of here, I
[00:28:31] reach out to Claude,
[00:28:33] this
[00:28:35] is now going to reference this.
[00:28:38] So, all of the things that I'm working
[00:28:40] on, any big decisions, all that kind of
[00:28:43] stuff, I capture in here. And when I say
[00:28:48] I, I direct Claude to capture in there.
[00:28:52] Then I have a bigger document,
[00:28:55] the no code SOP and then the road map.
[00:28:59] The SOP in the military standard
[00:29:02] operating procedure. The way to think of
[00:29:04] that that is like literally everything
[00:29:05] in the kitchen sink. So every single day
[00:29:08] before I log off I have any any chat
[00:29:12] that I operated with in claude code or
[00:29:14] claude or any of them that day update
[00:29:17] the SOP.
[00:29:19] The purpose for that is understanding
[00:29:22] that the claw.md file, it can only be
[00:29:25] 40,000 characters. Sounds like a lot.
[00:29:28] It's not. Especially on a big project.
[00:29:30] You're going to be fighting for space.
[00:29:32] You don't want to lose all of the
[00:29:34] detail. All of the very specific
[00:29:36] decisions you made, when you made them,
[00:29:38] why you made them, what they impact. You
[00:29:41] don't want to lose that. All of it in
[00:29:44] total is captured in the SOP. What makes
[00:29:47] the SOP useful is the AI model can't
[00:29:52] read the whole thing. It literally can't
[00:29:54] get through the whole thing. There's way
[00:29:56] too many characters. It would use the
[00:29:58] entire context window just trying to get
[00:30:00] through the document.
[00:30:02] But what it can do is efficiently move
[00:30:04] through the SOP. The way we efficiently
[00:30:07] move through the SOP is by having a
[00:30:08] table of contents up top so that it can
[00:30:11] skip down to the relevant sections. So
[00:30:14] for example, let's say tomorrow I'm
[00:30:16] working on something and the model wants
[00:30:19] to do something and I say like hey check
[00:30:21] that section in the SOP to make sure
[00:30:23] that there are no conflicts with this
[00:30:25] design decision. An example of that is I
[00:30:29] actually found a way to compress a lot
[00:30:32] of the files a lot that I'm using. So I
[00:30:34] actually don't need quite as much
[00:30:36] storage as I have.
[00:30:39] Originally what I was doing was mixing
[00:30:42] internal external. You'll see in the
[00:30:44] video on Sunday how it all works. But
[00:30:47] the update actually to that video that's
[00:30:48] going to come out on Sunday is that I
[00:30:51] don't need that much.
[00:30:53] So what I'm doing well what I did
[00:30:56] previously is let's say I have two 28
[00:31:00] terbte external hard drives. I would
[00:31:03] have more than that but two of them in
[00:31:05] this example. You can pull them
[00:31:07] together. All that means is that the
[00:31:10] machine is going to view it as one
[00:31:12] thing, one drive. But there's
[00:31:16] risks to that. If, for example, if one
[00:31:19] of those hard drives dies, everything on
[00:31:22] both of them is dead. So it I use it as
[00:31:27] an expansion if you need the space. But
[00:31:29] there's risk now that I don't need that
[00:31:32] much space. I'm going to undo that. So,
[00:31:35] I'm going to split those two 28 TBTE
[00:31:38] drives apart, use them for different
[00:31:41] things. And then I have another pool
[00:31:42] that's using three hard drives. I'm
[00:31:44] going to split that one apart. And but
[00:31:47] that impact stuff. So, I have data on
[00:31:50] all of them. So, what I'm going to do is
[00:31:53] use, which I'm doing right now, I'm
[00:31:54] using AI to comb through, figure out
[00:31:58] what's on all of them, and then to work
[00:32:01] on a remigration plan to unpool the
[00:32:04] drives. What it's doing is it's going
[00:32:06] into the SOP, and it's reviewing all the
[00:32:08] prior decisions that have been made. And
[00:32:11] in there, it now knows what lives where,
[00:32:14] what the risk is. Right now, it's making
[00:32:16] sure that everything is fully duplicated
[00:32:18] before I begin that process. I have
[00:32:21] written nothing in the SOP. Nothing. All
[00:32:27] clawed code. All of it.
[00:32:31] So, the purpose behind this little segue
[00:32:36] is that you have to be very aware of
[00:32:39] your context windows because let's say
[00:32:43] for example that you're chatting along,
[00:32:46] you're having a great time with Claude,
[00:32:49] Codeex, whatever. And full disclosure,
[00:32:51] I'm not sponsored by any of them. I wish
[00:32:53] I were. It would be a sick sponsor. I
[00:32:54] [ __ ] should reach out to them. Be
[00:32:56] honest. Giving them a lot of lot of
[00:32:59] credit here. should reach out to them,
[00:33:01] but I'm not. So, I'm not sponsored. I
[00:33:04] guess it does reduce conflict of
[00:33:06] interest, which is good.
[00:33:08] And
[00:33:11] you're chatting away.
[00:33:13] If you're not paying attention to that
[00:33:15] context window and you run into the
[00:33:17] context window, you now have a problem.
[00:33:20] The problem is twofold. First one here,
[00:33:24] recall called context rot starts to get
[00:33:28] broken apart. If your prompts are huge,
[00:33:32] lengthy things, it's not good. You can
[00:33:36] have big prompts, but they need to be
[00:33:38] logical and as concise as possible. And
[00:33:41] if you have a whole ton of those, even
[00:33:44] though the context window might be a
[00:33:46] million tokens long in this sense, the
[00:33:49] context that's in like the first 25K,
[00:33:52] that's not going to be super accessible,
[00:33:55] super clear. So, you don't want to wait
[00:33:57] until you hit the 1 million tokens
[00:33:59] before you compact or before you move
[00:34:01] into a new chat. You want to make sure
[00:34:04] that the AI is giving a good turnover in
[00:34:07] all of your documentation. And then what
[00:34:09] I do is I have AI in the chat itself
[00:34:13] create a markdown file and I just say
[00:34:16] create a comprehensive markdown turnover
[00:34:18] file for everything that we worked on
[00:34:20] specifically where we landed on key
[00:34:22] decisions open action items that we're
[00:34:25] working on now what's in flight for the
[00:34:28] next agent to be able to pick up
[00:34:30] seamlessly I have it make its own and
[00:34:34] that is how you do a good job managing
[00:34:38] ing your context window. This is l I I
[00:34:43] firmly believe this that a a really big
[00:34:46] part of how well this project and just
[00:34:49] your use in general of AI is is how well
[00:34:53] you manage the context window so that
[00:34:56] it's maximizing
[00:34:58] its capability without running out of
[00:35:03] direct information on what you're
[00:35:05] currently working on and being able to
[00:35:07] turn on it. Because the other thing that
[00:35:09] you will notice is that if you get
[00:35:10] really deep in a context window, it'll
[00:35:12] slow down. It'll bog way down because
[00:35:14] it's trying to chew through all of that.
[00:35:17] Okay, I do need to talk quickly about
[00:35:21] chat models versus coding agents.
[00:35:23] They're two different things. So, Claude
[00:35:27] is not the same as Claude code. Same
[00:35:31] company, similar idea, different things.
[00:35:35] It's really important to know the
[00:35:38] difference between these because the way
[00:35:41] that I've tested all different
[00:35:44] combinations. I tried writing code or
[00:35:48] dispatches, not even code, dispatches in
[00:35:52] claude, feed it to chat GPT, the chat
[00:35:55] model, and then feed it from chat GPT to
[00:35:58] Claude code to draft the original
[00:36:01] dispatch and feed that into codeex and
[00:36:03] like literally every combination
[00:36:04] thereof. I would have claude code
[00:36:07] generate a code line of script, whatever
[00:36:10] it is for what I needed to do. I then
[00:36:12] feed that into chat GPT, feed that back
[00:36:14] into codeex, go back to claud and
[00:36:16] iterate on all of these to figure out
[00:36:18] what works the best. There are strengths
[00:36:21] and weaknesses to both. What I would say
[00:36:24] at the high-end level first to
[00:36:26] understand the differences between
[00:36:28] these, this is literally just a chat
[00:36:29] model. It lives in the app on your
[00:36:31] computer. You can give it access to
[00:36:33] folders and context so that it knows
[00:36:35] what's going on. But this is what you're
[00:36:38] used to working with. This might be new
[00:36:40] to people. So this actually works in
[00:36:45] your environment. So for me, I'm
[00:36:48] primarily using VS Code to kind of
[00:36:50] coordinate everything, but it can be
[00:36:53] just in a Python shell. It can be really
[00:36:56] anywhere that you want to set up your
[00:36:59] infrastructure.
[00:37:01] It can be in command lines, whatever.
[00:37:04] But I find having everything generally
[00:37:06] consolidated in VS Code is really nice.
[00:37:08] I can run Python in there. I can run
[00:37:10] Jupiter in there. I can run terminals,
[00:37:12] shell commands, everything. That's super
[00:37:15] useful. Now, the coding agent, it can
[00:37:19] directly access stuff. So, when it says
[00:37:23] the same brain, I agree with it, except
[00:37:26] there are differences in how they think
[00:37:30] slightly. I've noted at least. Again,
[00:37:32] this is 47 for Claude. I do not know
[00:37:35] about 48. 48 could have improved and you
[00:37:37] might be able to skip all that entirely.
[00:37:38] This shit's moving fast. But
[00:37:42] understanding the difference between
[00:37:43] these two is really useful so that you
[00:37:46] can implement them effectively.
[00:37:49] All right. So this gives you a side
[00:37:53] byside breakdown of what these things
[00:37:55] are, how they work, all that kind of
[00:37:57] stuff. This is for your reference. Just
[00:38:00] understand the way that you generally
[00:38:03] want to use these big planning
[00:38:05] decisions, architecture, all that kind
[00:38:06] of stuff. You can use the chat model to
[00:38:08] start, feed it into the coding agent to
[00:38:11] review and then operationalize.
[00:38:13] Operationalization
[00:38:15] always is going to come from the coding
[00:38:17] agent or from the chat model feeding you
[00:38:21] to execute something or the coding
[00:38:24] agent. You can skip the middleman on a
[00:38:27] lot of smaller tasks that you don't need
[00:38:29] to use the chat model. I use the chat
[00:38:31] model way and way less now. I use it for
[00:38:34] other things. the chat model built this
[00:38:36] [ __ ] deck. So I use it for other
[00:38:38] stuff at this point because most of like
[00:38:43] the big planning decisions and all that
[00:38:45] stuff that's all done and now I'm at you
[00:38:48] know refinement of the space. So it's
[00:38:50] all being done in the agent but in the
[00:38:52] beginning the chat model is useful. All
[00:38:55] right
[00:38:57] so this gives you an idea on how you can
[00:39:02] implement these. I already literally
[00:39:03] just gave you a preamble between these,
[00:39:05] but I want to emphasize step three.
[00:39:10] You're still here. You have to be
[00:39:13] involved. You have to pay attention to
[00:39:16] what's going on. This is where you stand
[00:39:19] to [ __ ] up the most if you skip this.
[00:39:23] Cannot emphasize that enough.
[00:39:28] Have to be involved. Okay,
[00:39:31] this gives you an idea on how you can
[00:39:34] interact with your AI model. A good
[00:39:37] thing to do is to give it a lens to look
[00:39:40] through. So you can say you are a option
[00:39:44] strategist. This is if you're doing
[00:39:46] research. You could say you're a full
[00:39:48] stack engineer with front-end, backend,
[00:39:51] and experience and you're going to help
[00:39:53] me build an options research database.
[00:39:56] Again, the prompt that I give you in the
[00:39:58] quick start guide, it's not even a
[00:40:00] prompt. It's like a series of prompt.
[00:40:01] Shreyj can tell you in the chat. It's
[00:40:03] like I don't know how long. It's several
[00:40:05] pages of a prompt, but I split the
[00:40:08] prompt into phases for you so that you
[00:40:10] can more easily navigate, you know, the
[00:40:12] different conversations and sections,
[00:40:14] but giving good context is important.
[00:40:19] So the cick the the the the crux here is
[00:40:25] you can use it to brainstorm. You don't
[00:40:28] always have to tell it exactly what to
[00:40:31] do if you don't know. You can literally
[00:40:34] instruct it to plan or brainstorm with
[00:40:38] you and it'll give you different coas
[00:40:40] courses of action pros and cons. You can
[00:40:42] weigh them out, ask questions as you
[00:40:45] should. Okay. So Shay J says it's 17.
[00:40:48] So, the the prompt that I'm providing to
[00:40:51] to you guys for building and mirroring
[00:40:54] this project, the prompt itself is 17
[00:40:56] [ __ ] pages. It's huge, but it's
[00:40:59] specifically designed to give this right
[00:41:02] the important level of context that you
[00:41:05] can feed it and have a good result.
[00:41:09] This is a breakdown of some of the
[00:41:13] places that this thing will fail you. I
[00:41:17] really want to focus actually on the
[00:41:20] last two being here
[00:41:25] and here.
[00:41:27] First, it's very agreeable. What I do in
[00:41:30] my clawed MD file is I immediately
[00:41:34] instruct it to not be agreeable. So,
[00:41:37] every single chat that I open, I do not
[00:41:40] want it to be agreeable. I want it to be
[00:41:42] as objective as humanly possible and
[00:41:45] seek to actively punch holes in what I'm
[00:41:49] thinking. That's way more valuable to
[00:41:50] me. That's in the Claude MD file. You
[00:41:53] should earmark that. In general, the
[00:41:55] chats are going to try to be generally
[00:41:57] agreeable. We don't want that. It's just
[00:42:00] like how we operate inside the outlier
[00:42:02] community for everybody. It's not about
[00:42:05] like trying to tear people down or build
[00:42:07] people up. This is just objective
[00:42:10] analysis. sharpening of skills. It's the
[00:42:13] same [ __ ] This is the last thing.
[00:42:16] It accelerates judgment. It doesn't
[00:42:18] replace it. It's sometimes going to
[00:42:20] suggest things that might not actually
[00:42:22] make sense. That's why if you're unsure
[00:42:25] what those things are, you use another
[00:42:28] model. Now, once you get more familiar
[00:42:30] with this stuff, you'll start to be able
[00:42:32] to correct it in flight. So, for
[00:42:33] example, you could be downloading
[00:42:35] something from an API and then you can
[00:42:38] see that it's trying to write it to a
[00:42:40] folder that you're not using or
[00:42:42] something like that. Then you can
[00:42:44] immediately you would know like, oh no,
[00:42:46] don't write it to there. That's not
[00:42:47] where this stuff is. You should write it
[00:42:48] to here. But you might not know that in
[00:42:50] the beginning, right? You might not have
[00:42:52] that context. So, in the beginning, you
[00:42:54] should use multiple chats or agents to
[00:42:57] validate [ __ ] because again, this is how
[00:43:00] I'm showing you to protect yourself
[00:43:03] against what you don't know. That's the
[00:43:06] whole point. So, just be aware of these.
[00:43:10] This is the general workflow that you
[00:43:15] can literally implement from day one.
[00:43:19] The big thing that you're going to start
[00:43:20] with is the quant builder. Really, what
[00:43:25] project no code is is a it is a literal
[00:43:29] quantitative database to do like very
[00:43:33] legitimate quantitative research. You
[00:43:36] become your own quant just like whatever
[00:43:38] that I forgot the name of the movie. Was
[00:43:40] it the big short? No. Yes. Yeah. The big
[00:43:44] short. This is my quant. Well, it's
[00:43:47] [ __ ] gonna be you. You are the quant.
[00:43:51] All right, so that wraps up the overview
[00:43:55] section. What I want to do is have a
[00:43:57] conversation with you guys. So, in the
[00:44:00] chat, if there's anything at all that
[00:44:03] you want to revisit, if there's
[00:44:05] questions you have, because we're not
[00:44:08] going to have another live stream as a
[00:44:09] broad group until next Friday. So, the
[00:44:12] video is going to come out Sunday. It'll
[00:44:14] give you access to the document, but I
[00:44:15] want to make sure that you are
[00:44:17] comfortable, ready to rock and roll at
[00:44:20] the onset. So, throw anything that you
[00:44:23] want to get at in the chat and give me
[00:44:25] one second. I will be right back while
[00:44:27] you do that.
[00:45:23] All right. What do you guys have? I'm
[00:45:26] going to go through the chat now. Sorry
[00:45:27] I didn't go through it before. I wanted
[00:45:29] that to be packaged. I'm actually going
[00:45:30] to break it out as its own video.
[00:45:33] Um, so we got Reese. Reys is doing a
[00:45:37] little bit of a workout. That's sick.
[00:45:39] Robert, what's up, man? Good to see you.
[00:45:40] Same thing with Mark Level. Good to see
[00:45:43] you as well.
[00:45:45] Um, Shrey. Okay, so Shrey is here. Shre
[00:45:48] says, "Can confirm the doc is
[00:45:50] high-grade, way more than what I
[00:45:52] expected for a quick start guide. Glad
[00:45:55] it would be available for everyone."
[00:45:57] Yeah,
[00:45:58] I'm stoked on that. And yeah, really
[00:46:00] what ended up happening was when I built
[00:46:03] it, I wanted I really wanted to have
[00:46:06] like a good prompt road map for people
[00:46:09] to follow cuz that's the way you [ __ ]
[00:46:10] this up. If you have generally good
[00:46:12] prompts to follow, then it legitimately
[00:46:15] is kind of hard to [ __ ] this up. So,
[00:46:17] yeah, I'm actually really really stoked
[00:46:20] on that.
[00:46:22] Hey, James, what's up? Good to see you.
[00:46:23] Same thing. Hey, Lauren. I'm actually
[00:46:25] really excited, Lauren, specifically for
[00:46:27] you on on this. I really really hope
[00:46:31] that you're planning to to participate
[00:46:34] and do it. I think it will be really
[00:46:36] helpful for you. Specifically in terms
[00:46:39] of stuff like figuring out how long to
[00:46:41] hold something, that's applicable to
[00:46:43] everybody by the way. But if you think
[00:46:45] of something like trend following, when
[00:46:47] you're trend following, one of the
[00:46:49] biggest decisions that you have to make
[00:46:51] is how do you take profits? If you take
[00:46:53] profits too fast, then you end up
[00:46:55] missing out on a move and you're like,
[00:46:57] "Fuck, I didn't want to miss out on the
[00:46:58] move." move. If you take profits too
[00:47:00] slow, then you give up a [ __ ] ton of
[00:47:02] profits that otherwise you're like,
[00:47:04] "Shit, I wish I took them." So, with
[00:47:07] project no code, you can literally
[00:47:10] answer that. You can have a very good
[00:47:13] idea on specific to that profit
[00:47:16] mechanism, specific to that strategy
[00:47:18] that you're running, what kind of
[00:47:20] management plan generally makes the most
[00:47:22] sense. And the thing to remember is that
[00:47:24] when we say things like generally makes
[00:47:26] the most sense, the entire purpose of
[00:47:28] that is we're not looking to overfit.
[00:47:30] We're not looking for each one to be
[00:47:31] maximized. It's impossible. But what
[00:47:34] we're saying is for this specific
[00:47:35] strategy, what bears out best in the
[00:47:38] long run across a lot of samples and
[00:47:41] then that's how you use that's what you
[00:47:43] use to make a decision.
[00:47:46] So I think it would be really good for
[00:47:47] you. Uh, level says first question. Do I
[00:47:51] need to get a separate computer for
[00:47:53] this? So, on Sunday, that video actually
[00:47:59] has a breakdown. Give me one sec. Um,
[00:48:02] I'll just move you guys over to that
[00:48:03] screen. I just have to go through the
[00:48:04] the slides really quick because I can
[00:48:06] pull that one up for you that has
[00:48:10] uh PC requirements. Where we at?
[00:48:14] Where we at? Here. So this is
[00:48:19] more or less like a a minimum starting
[00:48:23] point, but I would I would run run the
[00:48:28] quick start guide. When you get that,
[00:48:30] you literally can run that by claude or
[00:48:32] chatt and you could say like, hey, I'm
[00:48:35] looking to do this. What kind of machine
[00:48:37] do I need? What what hardware do I need?
[00:48:40] Here's the thing. The storage component
[00:48:43] is very real. When you start getting
[00:48:48] more and more data, you can compress it.
[00:48:50] You can move things into what are called
[00:48:51] parquet files, which are very, very
[00:48:53] efficient, by the way. But it's still
[00:48:55] not an insignificant storage size. Plus,
[00:48:59] you have to remember the redundancy
[00:49:02] because what I you don't want to just
[00:49:04] have your database and all your data on
[00:49:05] one spot. It's a massive mistake. I
[00:49:08] literally I have it now triplicated.
[00:49:11] It's in three spots. And the reason
[00:49:13] being is again if you're really trying
[00:49:16] to treat this as a standalone database,
[00:49:19] you don't want to have one, if that
[00:49:23] fails, you're completely [ __ ] Two is
[00:49:25] reasonable, but the military planner in
[00:49:29] me also knows that sometimes both of
[00:49:31] those can get [ __ ] at the same time.
[00:49:33] So, we go to three. And that's the whole
[00:49:36] point of having like redundant storage.
[00:49:40] And to give you context right now, I'll
[00:49:42] literally pull up my drives. So right
[00:49:44] now in my staging drive, it's about 9
[00:49:49] terabytes of data in the staging drive.
[00:49:53] And in the backup, so the way that I'm
[00:49:56] built, I'll literally show you again the
[00:49:58] the video on Sunday. Some of this will
[00:50:00] be duplicative, but this is how I'm
[00:50:02] built.
[00:50:03] So what I have is this is like my main
[00:50:06] computer. This is for the main computer.
[00:50:09] This is the option research engine. So
[00:50:12] this is 4 terb of internal SSD. It's
[00:50:15] fast. That's the whole point. I want
[00:50:18] this to be super quick cuz I don't want
[00:50:20] to be writing tables and stuff like that
[00:50:22] and that be slow. This is my hot
[00:50:26] storage, the O pool, option research
[00:50:29] pool. The reason why I include pool in
[00:50:32] the name is so that I know this is a
[00:50:36] pulled drive. This is two 4 TBTE SSDs
[00:50:41] that are pulled together to create seven
[00:50:44] and a quarter usable space. This is the
[00:50:47] hot storage. This is the staging area.
[00:50:50] What's happening right now as we speak
[00:50:52] is the entire database sands some raw
[00:50:56] files and stuff is moving from RAID
[00:51:00] alpha onto the pool. RAID alpha is
[00:51:04] another series of pool drives and this
[00:51:08] is the first spot that everything is
[00:51:11] stored in its entirety.
[00:51:14] Then RAID poolool bravo is a separate
[00:51:17] drive. Same this is a complete backup of
[00:51:22] everything. So you can see the sizes of
[00:51:25] everything as it sits. What'll end up
[00:51:28] happening is I'm actually going to break
[00:51:32] Raidool alpha apart. I'm going to break
[00:51:35] RaidPool Bravo apart because as you can
[00:51:38] see I don't need 45 terabytes. I really
[00:51:41] am not using that much. I only need like
[00:51:43] 10 plus. So, what I'm going to do is in
[00:51:47] RAID pool alpha, I will have a 28 terbte
[00:51:51] drive and then I will have an 18 terbte
[00:51:55] pulled with a 10 terbte to make another
[00:51:58] 28 or so. And that will be the warm
[00:52:02] storage for everything. And then the
[00:52:04] cold storage will be a 28 terbte. And
[00:52:08] then I have another 18 terabyte that
[00:52:10] will just be duplicative for now until I
[00:52:12] start I start wanting to build more
[00:52:14] research and all that kind of stuff.
[00:52:16] Then I'll dance things around. So this
[00:52:18] gives you like an exact idea. You don't
[00:52:21] need this much. But even in terms of
[00:52:24] like how much stuff I downloaded as far
[00:52:26] as data, you don't need to go that far
[00:52:28] either. I am I am obsessive and I'm an
[00:52:32] extremist. I definitely have always been
[00:52:34] an extremist. So I'm doing everything in
[00:52:37] the kitchen sink. In terms of data, I'm
[00:52:40] literally over a billion rows of data
[00:52:43] now. It's a unbelievably large data set.
[00:52:47] But I want to be able to show you guys
[00:52:51] using this kind of tool. How does the
[00:52:54] implied volatility surface for S&P SPX
[00:52:57] options shift as we go through an
[00:53:00] election cycle versus a non-election
[00:53:03] cycle or as we go through a presidential
[00:53:05] election cycle versus a congressional or
[00:53:08] how they behave around FOMC, right? Like
[00:53:12] all these weird generally nuanced
[00:53:14] questions. I like to be able to explore
[00:53:17] all of them. That's what I do in my
[00:53:19] personal database. But again, I've
[00:53:21] already told you guys I'm taking this
[00:53:23] really seriously. And this this is
[00:53:26] really going to be what I'm going to
[00:53:27] lean on as much as I can. And if I
[00:53:30] can't, if I find that it's not suitable
[00:53:32] for any reason, which I don't see any
[00:53:34] reason why that would be the case based
[00:53:35] on what I see so far, then I will
[00:53:37] migrate back to my machine in a
[00:53:38] heartbeat. It's like no doubt in my mind
[00:53:42] because at the end of the day, I need to
[00:53:43] make money trading. Like that's my top
[00:53:45] priority. But in this scenario, I don't
[00:53:48] see why that both of those can occur at
[00:53:50] the same time where I continue to be,
[00:53:52] you know, equally successful as I tend
[00:53:53] to be, but then also like pivot to this
[00:53:57] setup literally as a demonstration to
[00:54:00] you guys to lead by example that it's
[00:54:03] doable and you can use it to produce
[00:54:05] good results. It's not the thing itself
[00:54:07] that's going to produce good results.
[00:54:08] It's still you, the trader. But that's
[00:54:11] the point because historically like my
[00:54:14] trading performance, it was based on
[00:54:16] something that only I had access to,
[00:54:18] which is my database, my research. It's
[00:54:21] stuff that people could still recreate
[00:54:22] on their own. But now I'm taking that
[00:54:25] one step further and I'm li literally
[00:54:27] giving everybody access to kind of the
[00:54:29] hanger that you need in order to do all
[00:54:32] of this.
[00:54:34] So a really long bouncing around answer
[00:54:37] to do you need a new computer? But it'll
[00:54:41] depend on what kind of machine you have.
[00:54:43] The one thing I will say is everything I
[00:54:46] built in here is wrapped around Windows.
[00:54:49] That's what I have. That doesn't mean it
[00:54:51] won't work in a Mac. I don't see any
[00:54:53] reason why it wouldn't, but a lot of the
[00:54:54] stuff that I'm doing is in like
[00:54:56] PowerShell and I don't know the Mac
[00:54:58] alternatives to that stuff. I know it
[00:55:00] has it. So, you can do it there. And
[00:55:02] then if you're in Linux, you probably
[00:55:04] don't need any of this stuff. You're
[00:55:05] probably already doing all of this on
[00:55:06] your own. Now the so that covers
[00:55:11] operating system and then storage. For
[00:55:13] context on storage, I literally started
[00:55:16] on a 4 terbyte SSD because I knew my new
[00:55:18] I had a new computer coming before I
[00:55:20] started this and I was I wanted to be
[00:55:23] able to migrate easily. Like that's very
[00:55:25] reasonable to get a lot of data up
[00:55:28] front. Stock data is really really
[00:55:31] cheap. Not in terms of price also in
[00:55:34] terms of price but in terms of storage.
[00:55:36] It's really really cheap. You can get
[00:55:38] minute level entire universe and it does
[00:55:42] not take that much space. What starts to
[00:55:44] take a lot of space is if you also get
[00:55:46] like quotes and trades which you can do.
[00:55:48] I'm doing but that takes more space but
[00:55:52] like you can easily now one thing I will
[00:55:55] note that Sunday doesn't go into
[00:55:56] explicitly this is kind of like a quick
[00:55:59] rambling of some best practices.
[00:56:01] genuinely you should take notes
[00:56:04] is
[00:56:06] the um
[00:56:09] the one of the risks that you come when
[00:56:11] you're pulling data is survivorship
[00:56:13] bias. You have to make sure you you
[00:56:15] don't do that because there will be a
[00:56:16] lot of names that become delisted
[00:56:20] and you need to track those. So what
[00:56:21] that means is you're going to have
[00:56:23] stocks that you know launched in 90 that
[00:56:25] died in 99 or 2000. You want to make
[00:56:28] sure that you really capture all of
[00:56:31] those. So, just keep that in mind that
[00:56:34] when you're pulling data, you don't want
[00:56:35] to just use current, you know, metrics,
[00:56:38] everything based on current volume or
[00:56:41] liquidity metrics because you're going
[00:56:42] to have a lot of survivorship bias on
[00:56:44] [ __ ] that died. So, keep that in mind.
[00:56:47] The the biggest thing in this whole
[00:56:50] project that I could emphasize though is
[00:56:52] this, your memory. So, my new computer
[00:56:56] has 96 gigs of DDR5,
[00:57:00] and you do want something with a lot of
[00:57:04] RAM. And I would say like 32 gig is like
[00:57:08] legit minimum. If you don't have more
[00:57:13] than that, I still think you could get
[00:57:15] by, but is going to be really
[00:57:17] constrained and really slow. So, if you
[00:57:22] don't have that, that would be a very,
[00:57:26] very meaningful upgrade to get, which by
[00:57:28] the way, like laptops have that. So, you
[00:57:32] don't have to get like a PC tower like I
[00:57:34] have. Again, it's better for expansion,
[00:57:36] heat, all that stuff. It's definitely
[00:57:38] better, but you don't have to. You can
[00:57:40] get a laptop that exceeds this.
[00:57:42] Actually, let's do like shopping really
[00:57:44] quick. I'm just curious.
[00:57:46] um uh pre-built
[00:57:49] ECs. One thing I will generally direct
[00:57:52] people towards is um
[00:57:58] [ __ ] I forgot what I was going to say.
[00:58:03] The window popped up.
[00:58:05] Oh, gaming gaming stuff. The reason why
[00:58:09] is I call them the nerds but it's really
[00:58:12] a
[00:58:13] expression
[00:58:15] of love. The nerds are really really
[00:58:20] into power like really really power.
[00:58:25] And one note to keep in mind as well is
[00:58:32] uh my new computers from Origin just for
[00:58:35] context. not sponsored by them, but I
[00:58:37] use them really for convenience. I do
[00:58:40] not like building my own computer. It's
[00:58:41] not that hard to do, but it is just not
[00:58:44] my preference. And then for my laptop, I
[00:58:47] have a G14,
[00:58:49] which is a Asus ROG, which is the nerds,
[00:58:52] the gaming people. But I am purposefully
[00:58:56] not using AMD.
[00:58:59] I'm using Intel, the Ultra 9 285K.
[00:59:04] The reason is AMD is really really good
[00:59:07] for gaming. It's the place I would go
[00:59:09] for gaming. My laptop has u AMD in it
[00:59:13] for that exact reason cuz they have like
[00:59:15] 3D cores and stuff. I don't want to go
[00:59:17] like super nerd in case this doesn't
[00:59:18] [ __ ] mean anything to anybody. It's
[00:59:20] still good to listen to by the way
[00:59:21] because you're just going to expand your
[00:59:23] own context window. But Intel works
[00:59:27] really really well for multiple tabs and
[00:59:31] a lot of multitasking and stuff like
[00:59:34] this. So querying a database, all those
[00:59:36] kind of things, Intel does an
[00:59:39] exceptional job at. So for my, you know,
[00:59:42] standard day-to-day computer, I have the
[00:59:44] Ultra 9. Let's just see. Um,
[00:59:49] let's see what Now this isn't Origin.
[00:59:52] The reason why I'm not using Origin is
[00:59:53] Origin is a little bit more expensive.
[00:59:55] It's kind of like a a boutique, but I'm
[00:59:58] just super curious like what uh No, no,
[01:00:03] no. I want pre-built. I don't want Let
[01:00:06] me find
[01:00:09] Let me find some pre-built stuff. Well,
[01:00:11] we'll go to Origin. I mean, I use them
[01:00:14] for mine. Let's see.
[01:00:20] Let's see what their pre-builts are.
[01:00:27] All right.
[01:00:30] Uh, do they have a filter?
[01:00:35] So, this is 32 gig.
[01:00:38] Oh, wait. That's not what I'm looking.
[01:00:40] Yeah. So, that this has a [ __ ] 5080
[01:00:43] in it.
[01:00:45] It's an FE, but it's still a 5080.
[01:00:50] This is an insanely good computer and
[01:00:51] it's three grand.
[01:00:55] That's actually kind of sick. I'm not
[01:00:56] going to lie.
[01:01:01] The Millennium, this is the the case,
[01:01:06] the chassis that I have,
[01:01:10] but mine mine I purposely do a little
[01:01:13] bit of a custom build. So, here you're
[01:01:16] looking at like three grand. I want to
[01:01:18] see if there's any other
[01:01:21] look at some gaming PCs.
[01:01:24] What can we filter by? Here we go. So,
[01:01:27] graphics card. It's actually like not
[01:01:30] the end of the world, but let's see
[01:01:35] between the Intels. Oops.
[01:01:41] So, the topofthe line card here is
[01:01:43] pretty expensive, which by the way, you
[01:01:45] don't have to get an Intel Ultra 9. The
[01:01:48] the performance difference is not that
[01:01:51] significant.
[01:01:54] So, the sevens are like three grand. And
[01:01:56] again, these are higherend PCs. So, let
[01:01:59] me see if I can find some cheap ones.
[01:02:06] products,
[01:02:08] gaming PCs.
[01:02:10] We love us some nerd stuff.
[01:02:16] Uh
[01:02:18] ones are topline stuff.
[01:02:22] I think the Yeah, I power I think is the
[01:02:24] cheaper one.
[01:02:28] So here you can kind of go through and
[01:02:30] find
[01:02:33] Yeah. Yeah. So you literally can limit
[01:02:35] by price.
[01:02:38] That's perfect.
[01:02:42] I would not want like an ultra 5. I
[01:02:45] would do either the i9, i7, the ultras.
[01:02:48] Like that's fine. So you're looking at
[01:02:50] like two grand. That's ultimately what I
[01:02:53] see here. And that's 32 gigs of DDR5,
[01:02:57] which is good. And it comes with a 5070,
[01:02:59] which is good. So, the point that I'm
[01:03:02] making here is that this is an
[01:03:03] investment if you don't have a machine
[01:03:05] capable, but it's the kind of thing that
[01:03:08] I mean, these, you know, last you for
[01:03:09] years, so it's something that you'll be
[01:03:11] able to use for tons of stuff. And I do
[01:03:14] think you'll be able to you could
[01:03:15] conceivably get by with less. I just
[01:03:18] think it would be a little bit um
[01:03:23] Yeah, it would be a little bit
[01:03:27] slow.
[01:03:29] Okay.
[01:03:30] So that's hardware requirements in a
[01:03:33] nutshell. Let me continue through what
[01:03:36] you guys got. Uh Joseph says comes to
[01:03:40] recency bias and what Bloomberg had in
[01:03:42] the closing bell. A book has some
[01:03:44] critical concepts on the generational
[01:03:46] term of AI. Yeah. Yeah. That's
[01:03:48] completely completely fair.
[01:03:53] Um, Ben says, "How much do you think
[01:03:58] required Eric's expert expertise that
[01:04:01] Joe No Trades would fail at?"
[01:04:04] Well, the research requires definitely
[01:04:07] more expertise in order to do a good
[01:04:09] job. Like that's
[01:04:12] full stop for sure. In order to build
[01:04:16] the thing that I built, you don't need
[01:04:19] any expertise. I had no expertise really
[01:04:21] going into it with using AI. The only
[01:04:24] expertise I had was all the self-taught
[01:04:26] stuff from making my own DB and then
[01:04:29] coding to to operate it. But even that
[01:04:32] was at a very very low level. So for for
[01:04:36] like the the building side of this, you
[01:04:39] really do not need any expertise. Like
[01:04:42] that's the whole point of AI. AI is the
[01:04:44] expert. And I would argue if you're less
[01:04:48] of an expert, then that's an even
[01:04:51] stronger argument for having multiple AI
[01:04:55] tools
[01:04:56] because then you'll be able to use them
[01:04:58] to fact check and bounce off of one
[01:05:00] another so that you're in a in a good
[01:05:02] place.
[01:05:04] That said, in order to come up with like
[01:05:07] research and to know what questions to
[01:05:10] ask and where to look, Yeah. Like that's
[01:05:13] experience and that's where you you need
[01:05:15] to have experience. The only way you're
[01:05:17] going to build that experience is again
[01:05:19] by doing stuff like this and iterating
[01:05:20] on it. But it would be
[01:05:24] unbelievably foolish for me to expect
[01:05:26] people to like immediately come online
[01:05:29] doing what I do at a performance level.
[01:05:32] Um just because you have this that's an
[01:05:35] like holistically unreasonable
[01:05:36] expectation. But that's that shouldn't
[01:05:39] be the target for anybody either. So
[01:05:42] yeah, I I do not think that the build
[01:05:46] requires my expertise. I don't even
[01:05:49] think that the research part requires my
[01:05:51] expertise to begin with if you have a
[01:05:53] healthy
[01:05:55] expectation. But yeah, like if your
[01:05:57] expectation is you download this and
[01:06:00] then you start churning out, you know,
[01:06:02] 30% compound annual growth rate for 20
[01:06:06] years.
[01:06:08] I mean, objectively, probably not, but
[01:06:13] It is certainly the kind of thing that
[01:06:14] you can use to move you in the correct
[01:06:16] direction
[01:06:18] for sure.
[01:06:20] Justice says, "How do I bear the
[01:06:22] marginal EV extra abstractly speaking is
[01:06:25] what I've found participants are trying
[01:06:28] to venture forwards.
[01:06:30] I don't totally follow."
[01:06:34] Uh Shay says, "What are some beginner
[01:06:36] tips say for data handling, hygiene or
[01:06:40] broadly?" It's a good question, Trey.
[01:06:42] And there's a couple things that I would
[01:06:45] highlight in this project specifically.
[01:06:49] It's
[01:06:51] to be really, really slow in the
[01:06:55] beginning. And the reason why you want
[01:06:57] to be slow is you want to like think
[01:06:59] through stuff before you actually action
[01:07:03] on it. A way you can think of this is
[01:07:07] say for example
[01:07:09] you instead tell AI that you know you
[01:07:15] want to build this database and then AI
[01:07:18] says okay I'm going to build the
[01:07:19] database right a lot of times AI wants
[01:07:22] to immediately do what you want it to do
[01:07:25] but you really should plan a little bit
[01:07:28] what that can look like is when you tell
[01:07:31] AI like yeah I want to you know walk
[01:07:33] down the path path of project no code
[01:07:35] and build my own research database.
[01:07:39] Brainstorm
[01:07:40] with me and then when it brainstorms
[01:07:43] it'll give you a suggested structure for
[01:07:45] example. Then in that suggested
[01:07:47] structure you should say things like
[01:07:50] brainstorm how to optimize this poke
[01:07:52] holes in issues that we might run into
[01:07:54] the future with this kind of setup and
[01:07:56] suggest alternatives.
[01:07:58] So working on prompt engineering is
[01:08:01] probably the biggest tip in order to
[01:08:02] make this successful. And one of the
[01:08:04] best possible ways you could work on
[01:08:06] prompt engineering is to literally ask
[01:08:08] AI how to use it best. That's what I
[01:08:12] would think of. The other thing I would
[01:08:15] say is when you start pulling stuff,
[01:08:20] make sure you validate quickly. So, what
[01:08:23] that means is let's say that you're
[01:08:24] going to pull 4,000 tickers via an API.
[01:08:28] What I would do is a smoke test and
[01:08:31] instead of writing a script that pulls
[01:08:34] 4,000 from the API, I would say pull 25.
[01:08:39] Run that, see how everything goes, and
[01:08:41] then pull the rest. Make sure that the
[01:08:44] data is as you think it is. Make sure
[01:08:46] that you point AI towards the correct
[01:08:48] API documentation. you can literally
[01:08:51] just paste the website for it to look
[01:08:52] at. But all of those small things will
[01:08:56] really really pay dividends in terms of
[01:08:59] having a smoother process.
[01:09:02] The other thing I would say on top of
[01:09:04] all of that
[01:09:06] is
[01:09:08] focus on one thing first. I had this
[01:09:11] weird thing where AI literally kept
[01:09:14] trying to get me to like run queries and
[01:09:18] stuff, which is cool, but I needed to
[01:09:22] keep it on task to build out the
[01:09:25] database, right? Like for me, it was
[01:09:27] build the database first. Now, you have
[01:09:29] to run some queries in order to make
[01:09:31] sure everything works. That's totally
[01:09:32] cool. have those kind of tests. But
[01:09:36] making sure that you're keeping AI on
[01:09:38] point is something I didn't expect to do
[01:09:41] quite as much that was useful. And then
[01:09:44] the last thing I would say on top of all
[01:09:46] of that, this gives you the engine to do
[01:09:50] research. You still have to understand
[01:09:54] how to conduct good research.
[01:09:58] And realistically on the YouTube channel
[01:10:00] there are a couple really good resources
[01:10:02] for that. There's things like the
[01:10:03] outlier strategy process that gives you
[01:10:06] in a nutshell how to conduct a research
[01:10:08] process and then the same thing with
[01:10:10] that back testing video as a requirement
[01:10:12] that gives you context on how to
[01:10:14] actually conduct research which is
[01:10:16] really really important that is not
[01:10:18] immediately solved in this context
[01:10:21] because realistically if you come into
[01:10:23] this you build this and then you're like
[01:10:25] yo AI find me edge
[01:10:28] that's not going to [ __ ] work man you
[01:10:31] have to still complete the observations,
[01:10:35] explore things, and understand the
[01:10:37] correct questions to ask. The way that
[01:10:39] you do that is by developing your own
[01:10:41] context window. And once that's built,
[01:10:44] then you will be able to ask good
[01:10:46] questions that make sense, that kind of
[01:10:48] stuff. [snorts] So to summarize all of
[01:10:51] that, I think planning is really
[01:10:54] important, using AI to help you plan,
[01:10:56] but also like thinking a little bit
[01:10:58] deeper than solving the immediate tasks.
[01:11:01] I think having good documentation that
[01:11:04] we referred to earlier, right? Like
[01:11:07] having the SOP and all that kind of
[01:11:09] stuff built in is non-negotiable in my
[01:11:11] opinion. Having a grasp of conducting
[01:11:15] good research is really, really useful.
[01:11:19] Making sure that you're conducting smoke
[01:11:23] tests so that you're not, you know,
[01:11:26] 3,000 tickers deep on an API poll. then
[01:11:30] you find that there's some sort of
[01:11:32] glaring error, writing error, whatever
[01:11:34] that's [ __ ] up in all of it. Like,
[01:11:37] that's a massive problem. So, those
[01:11:40] would be like four really, really big
[01:11:42] things. All right,
[01:11:45] what else we got?
[01:11:49] Um,
[01:11:54] I'm just catching up.
[01:12:02] Uh, Ben says, "Those that can access
[01:12:04] commissary, you can get no tax and
[01:12:06] sometimes lower prices on stuff." It's a
[01:12:08] great reminder. So, there's probably
[01:12:10] several veterans in my community, and
[01:12:13] you definitely should check out the
[01:12:15] commissary. The other thing to think
[01:12:16] about the commissary, too, is like you
[01:12:18] can you don't always have to physically
[01:12:19] go to it. You can still have [ __ ]
[01:12:20] shipped to your house. So,
[01:12:24] it's a great call out and like no tax on
[01:12:27] stuff like this, especially if you're
[01:12:28] getting like a $2,000 machine. Like,
[01:12:30] that's that's impactful. Completely
[01:12:32] agree.
[01:12:38] Uh, let me see.
[01:12:42] Uh, Gemini says, "I would love your
[01:12:44] thoughts on what you think about the
[01:12:46] wild semis and tech run in the last two
[01:12:48] months. If you think this could last or
[01:12:50] you see severe downside,
[01:12:52] um, let me make sure that we're all
[01:12:55] clear on the project no code and AI
[01:12:58] stuff and then if we're good then I'm
[01:13:01] happy to talk about that a little bit,
[01:13:02] but I just want to stay on ask here.
[01:13:08] The other thing really quick, actually I
[01:13:11] have a a couple quick models to to show
[01:13:15] you guys. So, what I did is I created a
[01:13:20] script that shows me S&P and I'm just
[01:13:26] looking at skew and term structure. So,
[01:13:29] I can see what the term structure is.
[01:13:34] And then here, what I'm doing is
[01:13:36] actually measuring variance, risk,
[01:13:38] premium across different terms.
[01:13:42] This is all done with Claude. Claude
[01:13:46] wrote the scripts outright. This is an
[01:13:49] example of using a Claude chat to create
[01:13:54] the scripts and then plugging those into
[01:14:01] a PowerShell by myself. So all all I'm
[01:14:05] doing is saying go do these things.
[01:14:08] This is an example
[01:14:11] of where I had Claude do it itself.
[01:14:15] [snorts]
[01:14:16] So the environment that we have here is
[01:14:20] you can populate Claude in a terminal
[01:14:23] down here. The way that works is you
[01:14:26] just literally start with a PowerShell
[01:14:28] and you just type in Claude. Now, one
[01:14:31] useful note is you'll notice at the
[01:14:34] bottom I have by bypass permissions on
[01:14:37] that's generally just useful so that you
[01:14:41] don't have to, you know, confirm as much
[01:14:43] stuff cuz otherwise that can slow stuff
[01:14:45] down. But this is one spot that you can
[01:14:48] access claude. And then in here you
[01:14:50] could have it do whatever you want. I'm
[01:14:53] having one literally go through right
[01:14:55] now and clean up all my documentation.
[01:14:59] So you can access claude code here. You
[01:15:02] can also access claude code up here in
[01:15:06] an actual like chat like this. And then
[01:15:10] this is also the same area that you can
[01:15:13] access codeex which is here. And then
[01:15:16] the other the other tool that you can
[01:15:18] access in something like VS code is
[01:15:20] actually the the git version of these.
[01:15:24] So, Git allows you to access, you know,
[01:15:27] some of the the different chat tools and
[01:15:30] stuff like that. So, in general, most of
[01:15:34] these
[01:15:36] what I like to do is run clawed code not
[01:15:41] in this. I run clawed code in the app
[01:15:45] itself that I showed you. And the reason
[01:15:48] why I do that is it makes it easier for
[01:15:50] me to multitask. So, I'll have Claude
[01:15:54] code, which is literally the same thing
[01:15:55] as operating it in here. I'll have
[01:15:58] Claude code in the web or in the desktop
[01:16:02] app. And a lot of times I'll have Claude
[01:16:05] Code create dispatches
[01:16:08] for individual Claude Code terminals.
[01:16:11] This allows me to compartmentalize
[01:16:13] things. Now, you don't have to do it.
[01:16:15] You could do it in the Cloud Code chat
[01:16:16] itself, but I like doing it in the
[01:16:18] terminals. It doesn't really matter what
[01:16:21] you choose to do. I would say kind of,
[01:16:24] you know, tinker around and find what
[01:16:26] you prefer the most. But that's just
[01:16:29] like a a brief overview of, you know,
[01:16:32] where you can access the different tools
[01:16:34] and then a sample workflow.
[01:16:41] Uh, Mamba says, did you implement noise
[01:16:43] reduction checkpoints? Another way to
[01:16:46] effectively clear unrequested huge cash.
[01:16:50] Yeah. So what I I just use gating and
[01:16:54] all that is is whenever I create a plan
[01:16:58] with claude or codeex I have it
[01:17:01] institute
[01:17:03] gates and I would say execute up until
[01:17:07] you know x gate then request
[01:17:09] confirmation or review or whatever. Then
[01:17:13] once you have it, execute to the next
[01:17:15] gate because you do not want to have to,
[01:17:20] you know, dance well really sit in front
[01:17:22] of it and ask it to do everything or ask
[01:17:26] it to prompt you to do everything. It
[01:17:27] just take forever. So I gate things and
[01:17:31] I'll just use kind of gated prompts and
[01:17:35] rollouts.
[01:17:38] Um I think this thing actually made
[01:17:40] visuals. Yeah, that's actually sick. So
[01:17:44] Claude made these for us.
[01:17:48] I haven't looked at them yet.
[01:17:51] So we know implied V runs richer than
[01:17:53] realized. I think that generally makes
[01:17:56] sense. The average risk premium is about
[01:17:58] 0.96 points. So this is using 30-day.
[01:18:01] This is actually awesome. So again, if
[01:18:04] you're, let's say that you're selling
[01:18:07] premium and you want to ask yourself a
[01:18:10] question like, "Huh, I wonder what tenor
[01:18:15] has the most risk premium." You
[01:18:18] literally could have Claude run a grid
[01:18:20] search on which tenor tends to have and
[01:18:24] carry the best, richest risk premium
[01:18:28] or the most consistent, right? It
[01:18:30] doesn't necessarily have to be the
[01:18:31] highest. the highest models also have
[01:18:33] bigger draw downs or something like
[01:18:34] that. So you could give it a prompt like
[01:18:38] do a grid search to identify which
[01:18:40] teners tend to have the most risk
[01:18:42] premium prompt one you could see the
[01:18:44] result to that. Then you could say
[01:18:46] prompt two find the teners that have the
[01:18:49] least
[01:18:52] worst I don't like that that have the
[01:18:55] best maximum draw down metric. So, which
[01:19:00] one would have the lowest maximum draw
[01:19:02] down if you're selling a straddle in
[01:19:04] that term? And then you can ask it to
[01:19:07] combine them. Do a grid search for which
[01:19:10] tenor has the most risk premium embedded
[01:19:13] in it on average that also includes the
[01:19:18] best draw down protection, effectively a
[01:19:20] compound annual growth rate, and have it
[01:19:23] build it for you.
[01:19:26] That's a really easy way to build on
[01:19:28] this. One thing to note is in terms of
[01:19:30] my convention, the convention that I use
[01:19:34] is I have like a workshop section. This
[01:19:38] is where I'm testing stuff. And then a
[01:19:40] research section. Research is where
[01:19:43] defined things are going to live that
[01:19:48] I'm going to maintain going forward. So
[01:19:50] there will be like a risk premium or an
[01:19:52] SPX risk premium thing or like an SPX
[01:19:55] zerodte thing. Those will have you know
[01:19:59] their spot in research. Workshop is like
[01:20:02] more temporary stuff. This is where I'm
[01:20:04] going to like explore things, get an
[01:20:07] idea and I organize them so that there's
[01:20:10] an archive at top. So if it's something
[01:20:12] that you know I looked at, don't really
[01:20:13] care about, don't like that much, I
[01:20:15] archive it. Don't delete it. There's no
[01:20:17] reason to. The readme is for AI and it
[01:20:22] gives them instructions on how to
[01:20:25] conduct studies, tests, how I want them
[01:20:29] to organize the library. So the way that
[01:20:32] the library gets organized is each test
[01:20:36] gets its own folder and then everything
[01:20:39] is baked into the folder and then
[01:20:42] everything gets a spec sheet. So the
[01:20:44] spec is the build. What what are we
[01:20:46] actually testing? It's kind of like a
[01:20:48] strategy outline the way to think of it.
[01:20:50] And then I have a script. This is in
[01:20:54] Jupiter. And then any visuals that are
[01:20:58] made, I'll have it document those. So
[01:21:01] this is actually something I posted on X
[01:21:03] not that long ago. And I effectively
[01:21:07] this is a a great use case for project
[01:21:10] no code. All I did was look at S&P and I
[01:21:14] said, "How frequently are we within
[01:21:17] these different distances of all-time
[01:21:20] highs?" Because a lot of times people
[01:21:22] get really antsy when we're at all-time
[01:21:25] highs. They're calling for a crash. But
[01:21:28] the reality is most of the time we're
[01:21:31] within 10% of all-time highs. Over 60%
[01:21:35] 55% within 5% of all-time highs. So the
[01:21:40] the funny thing is is like if you look
[01:21:43] most of the time that's where we are but
[01:21:47] a lot of people don't really
[01:21:50] know that but it's the exact kind of
[01:21:52] thing that you can do. You can do that
[01:21:55] exact style of research which is super
[01:21:58] duper cool.
[01:22:00] Ben says, "So if someone started at at I
[01:22:05] want to sell credit spreads to collect
[01:22:07] premium, would that be broad to extract
[01:22:11] usefulness or do you think AI could give
[01:22:13] good advice?" I do not think that that
[01:22:16] would be sufficient. I also do not think
[01:22:19] that that's a good way to think about
[01:22:21] it. Anyways, if a person was thinking
[01:22:24] like that, I would recommend them
[01:22:26] specifically to watch my videos on the
[01:22:30] outlier strategy process specifically.
[01:22:34] It's always bad to start with a
[01:22:37] structure. It's always bad. It's never a
[01:22:40] good thing to start with. I want to
[01:22:43] trade X structure. It's broken. It's
[01:22:47] backwards. The market doesn't care what
[01:22:50] structure you prefer to trade. That
[01:22:52] doesn't equal edge. It's making the
[01:22:55] problem really hard to solve
[01:22:58] unnecessarily. So, conversely,
[01:23:02] the problem is way better posed as I
[01:23:08] want to attempt
[01:23:10] to capture
[01:23:12] variance risk premium. Literally just
[01:23:15] like we looked at I want to capture
[01:23:18] variance risk premium.
[01:23:20] Brainstorm with me different ways
[01:23:23] to capture variance risk premium. That's
[01:23:27] a better prompt that still honestly has
[01:23:29] holes in it, but that's just I would
[01:23:31] consider more accessible to people.
[01:23:36] The other thing to remember BT Dubs and
[01:23:40] this is why the the people that say like
[01:23:43] perpetual selling I always want to sell
[01:23:47] premium it's not good right because you
[01:23:52] can see like there's not an
[01:23:54] inconsequential number of days where
[01:23:56] there's not risk premium like not an
[01:23:59] inconsequential number of days
[01:24:02] which is actually kind of important to
[01:24:04] to note.
[01:24:06] BT Dubs like 68% of the time from 0 from
[01:24:12] ' 07 to present well to the 15th of May
[01:24:15] I should say. Like again it's an
[01:24:18] important note. So like if you're in the
[01:24:20] bucket of I want to sell credit spreads
[01:24:22] or I want to sell premium to collect
[01:24:24] income
[01:24:27] 32%
[01:24:29] of the time you're selling at bad
[01:24:30] points. And depending on how bad those
[01:24:33] bad points are, that could really [ __ ]
[01:24:36] up what you're actually collecting on
[01:24:38] risk premium. One of the best things,
[01:24:40] again, a good research question here is
[01:24:43] how do I identify the [ __ ] rich
[01:24:46] periods?
[01:24:47] So, not when it's at, you know, 96
[01:24:51] points of risk premium. How do I find
[01:24:54] when there's two two points of risk
[01:24:56] premium plus? I want to find those days
[01:24:59] and play there. It's actually again that
[01:25:02] that's like a direct map to start
[01:25:05] looking for edge
[01:25:07] for free available to everybody. That
[01:25:09] kind of thing.
[01:25:12] Bend says, "Right, but I had someone say
[01:25:15] exactly that and just start doing it."
[01:25:19] Yeah. I mean, it'll do anything, right?
[01:25:22] You could say like, "I want to learn how
[01:25:23] to backflip." And it'll show you. Just
[01:25:26] cuz just cuz you give it a prompt and it
[01:25:28] does something literally doesn't mean
[01:25:30] anything. But again, this goes back and
[01:25:34] it violates an important thing that we
[01:25:37] talked about before.
[01:25:40] This
[01:25:42] right AI is not something that knows the
[01:25:47] market. So if you give it a prompt like
[01:25:50] that, sure it's going to give you
[01:25:52] something back. It wants to please you.
[01:25:55] it wants to complete the task but that
[01:25:57] doesn't make it good. So yeah that's
[01:26:00] again it's it's a bad prompt because the
[01:26:04] market doesn't the AI model doesn't have
[01:26:07] some sort of expertise on edge in the
[01:26:10] market at all.
[01:26:14] So yeah I would I would not do that.
[01:26:20] All right gang I'm super stoked. Stay
[01:26:23] tuned for the video that launches on
[01:26:26] Sunday. And if you have any questions in
[01:26:30] the meantime, you can hit me up in the
[01:26:31] Discord. For the pro members, we have
[01:26:34] market prep as always on Sunday. And
[01:26:36] then for the Pro Plus members, we have a
[01:26:39] Zoom workshop on Monday. I will probably
[01:26:42] try to open up a seat or two to a couple
[01:26:45] community members. So stay tuned for the
[01:26:48] standard giveaway for that. And if you
[01:26:52] do want to ride along, this first
[01:26:54] session is going to be a little bit more
[01:26:55] of a prep session for the Pro Plus
[01:26:58] members. And then after that is when
[01:27:00] I'll have like the the actual build
[01:27:04] workshop sessions. So in that time
[01:27:07] frame,
[01:27:08] um, if you want to come right along,
[01:27:11] even if you don't feel like being a Pro
[01:27:12] Plus member into perpetuity, but you
[01:27:14] just want more support while you do it,
[01:27:16] we still have seats available. So
[01:27:18] there's your there's your pitch, but all
[01:27:21] of it will be accessible on Sunday for
[01:27:24] free for everybody. So there's the anti-
[01:27:25] pitch. Be an outlier.
[01:27:29] See you guys later.