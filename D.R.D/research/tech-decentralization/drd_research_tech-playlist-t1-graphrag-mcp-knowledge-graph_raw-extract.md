# RAW EXTRACT — Build an Agentic GraphRAG System in 1 Hour (MCP + Knowledge Graph)

## Source Metadata
- **Title:** Build an Agentic GraphRAG System in 1 Hour (MCP + Knowledge Graph)
- **URL:** https://www.youtube.com/watch?v=LnCXoIr0Mw8
- **Tier:** 1
- **Extracted:** 2026-06-09
- **Domain:** tech-decentralization / agentic-systems
- **Playlist:** Pandora Tech Playlist — PLWKcfqsabTLUxfC7OFs7UZ8EIJ6hjY_M8
- **Word Count:** ~10551

## Transcript (timestamped)

[00:00:00] Heat. Heat. [music]
[00:00:07] [music]
[00:00:14] [music]
[00:00:20] [music]
[00:00:28] >> [music]
[00:00:34] [music]
[00:00:40] >> All right. Hi everyone. Thank you so
[00:00:42] much for taking the time to join us for
[00:00:45] another episode in the databases for AI
[00:00:49] series. Um, so if you are a builder
[00:00:53] working on building rag applications,
[00:00:56] maybe you've already started dabbling on
[00:00:58] the side of graph rag applications
[00:01:01] or you're just interested in graphs like
[00:01:03] a lot of us are, then you are in the
[00:01:06] right place today because we are going
[00:01:09] to be showing you how to build an
[00:01:12] agentic graph rag system in less than an
[00:01:15] hour. Uh, so my name is Melissa. I am a
[00:01:19] Neptune specialist solutions architect
[00:01:21] and I am going to be your host for
[00:01:23] today's episode. I am also here with our
[00:01:27] super special guest Ian. Um if Ian you
[00:01:29] want to quickly introduce yourself.
[00:01:32] >> Hello everyone. My name is Ian. Uh I'm a
[00:01:34] graph architect with the Amazon Neptune
[00:01:37] service team.
[00:01:39] >> Awesome. Thank you Ian. Um so yeah as a
[00:01:43] Neptune specialist solutions architect
[00:01:45] um I get a lot of inquiries from
[00:01:48] customers uh people using Neptune on
[00:01:51] everything graph and Neptune related but
[00:01:53] it feels like lately a lot of the asks
[00:01:57] and questions that we get are really
[00:02:00] centered around how do we make our rag
[00:02:03] applications more accurate? How do we
[00:02:05] give them more context? How do we kind
[00:02:08] of capture some of the missing semantics
[00:02:11] and bits that a pure rag search might
[00:02:14] miss? And so kind of the traditional
[00:02:17] answer to that has been using graph rag.
[00:02:21] And just as a little recap, so if you've
[00:02:24] tuned in to some of our previous
[00:02:26] episodes on this databases for AI
[00:02:29] series, you might have seen that we've
[00:02:32] done some previous episodes covering
[00:02:34] graph in general. We talked a little bit
[00:02:37] about graph rag, what is it, why you
[00:02:39] might need it, when it would be a great
[00:02:41] fit. Um, and we'll post the links in the
[00:02:44] chat just in case you want to catch up.
[00:02:47] But just as a really quick recap to kind
[00:02:50] of set the stage for agentic graph rag,
[00:02:53] what we're going to be talking to about
[00:02:55] today, I just wanted to chat a little
[00:02:57] bit about what graph rag is really
[00:03:00] quickly. Um so if you're familiar with
[00:03:03] just your standard rag pipeline um it's
[00:03:06] actually very similar to how a graph rag
[00:03:09] architecture would look like. Um so here
[00:03:12] right we are again still starting with
[00:03:14] our data sources. We're going to load
[00:03:16] them, chunk them, generate embeddings,
[00:03:19] stick those embeddings into our vector
[00:03:21] store, but we're really enriching this
[00:03:24] process with a graph that will help
[00:03:27] provide additional context to the flow
[00:03:31] that helps capture
[00:03:33] not necessarily similar information,
[00:03:36] right? It could be dissimilar
[00:03:37] information, but it can still be
[00:03:40] relevant to the original question,
[00:03:44] right? And that's really the value that
[00:03:46] graphreg works. And uh one of my
[00:03:48] favorite examples that I always like to
[00:03:50] show of course is our sales prospects in
[00:03:53] example core. Um and this
[00:03:55] [clears throat] is a really great simple
[00:03:57] example that kind of captures the value
[00:03:59] ad of the graph in the graph rag flow.
[00:04:03] And as an example here, we might have a
[00:04:05] repository of articles, about example
[00:04:09] corp, about the sales, about the
[00:04:12] distributors that it uses. And right if
[00:04:16] we generate some chunks for it and we're
[00:04:17] trying to answer this question with the
[00:04:19] standard vector rag flow right we see
[00:04:22] that um a chatbot might pull from this
[00:04:27] do the vector search and we're going to
[00:04:29] match on the most semantically similar
[00:04:31] chunks which are going to be these blue
[00:04:32] ones. Um, and while this is semantically
[00:04:35] similar and we can derive an answer from
[00:04:39] this, right, that sales are going to be
[00:04:41] great, we actually see as a human that
[00:04:43] we're missing some extra context on the
[00:04:45] bottom. And so these are really the
[00:04:47] extra bits of information that are
[00:04:49] crucial and might be missed as part of
[00:04:52] just a standard vector flow.
[00:04:55] Um, so I just really wanted to quickly
[00:04:57] set the stage with that extra context
[00:04:59] about graph rag because we've been
[00:05:01] talking a lot about just graph rag as an
[00:05:04] architecture. We've been talking about
[00:05:06] more generally how we can connect a
[00:05:08] graph to agents to kind of query graphs
[00:05:11] with agents, but today we're really
[00:05:13] going to be putting all of those
[00:05:15] different components together into what
[00:05:18] we call agentic graph rag. And so I
[00:05:22] think that really brings our question to
[00:05:25] you Ian of on like I feel like graph rag
[00:05:28] has been such a hot topic lately. Uh we
[00:05:32] understand kind of generally the gaps
[00:05:34] that graph rag helps bridge from the
[00:05:37] standard vector rag but now we're moving
[00:05:39] on to agentic graph rag. So I guess how
[00:05:43] do you define agentic graph rag and what
[00:05:46] are the gaps that agentic graph rag
[00:05:49] covers that graph rag alone might not
[00:05:52] necessarily address.
[00:05:55] >> Yeah I think [laughter]
[00:05:57] agentic graph rag or any agentic
[00:05:59] solution is is us effectively adding a
[00:06:02] layer of additional intelligence over
[00:06:04] the top of our rag solutions. So we're
[00:06:07] providing some domain expertise. We're
[00:06:10] actually creating systems that can apply
[00:06:15] some domain expertise to solve really
[00:06:17] really complex problems. So graph rag
[00:06:20] out of the box or traditional vector rag
[00:06:23] there's not a lot of intelligence in
[00:06:24] there. You know you you said that that
[00:06:26] graph rag is really really useful in
[00:06:29] finding some of that super relevant
[00:06:30] information where we've got to chase
[00:06:32] down some connections in the data. We
[00:06:35] can use vector rag to find stuff that's
[00:06:36] really similar to the question that's
[00:06:38] being asked. We can use the graph to
[00:06:40] chase down additional connections, find
[00:06:42] some of that non-obvious content and
[00:06:45] combine these two sets of information
[00:06:47] and produce a good answer. So
[00:06:49] effectively with Rag, we're finding some
[00:06:51] content and then we're handing it off to
[00:06:54] an LLM with a prompt and saying, you
[00:06:56] know, given this evidence, please answer
[00:06:59] this question. But there's not a lot of
[00:07:01] intelligence there.
[00:07:03] um we are actually having to build an
[00:07:05] application or build a set of retrievers
[00:07:07] that know how to go hunt for that
[00:07:10] information. Um and then really we're
[00:07:12] just presenting
[00:07:14] the LLM with everything that we've
[00:07:16] found.
[00:07:18] Well, when we think about how we as
[00:07:20] experts in the real world solve
[00:07:22] problems, we tend to adopt a more
[00:07:25] iterative or incremental approach. We
[00:07:27] come with a whole bunch of strategies to
[00:07:29] solve a problem. And so we may start
[00:07:33] solving a specific problem by gathering
[00:07:36] some information, you know, reviewing
[00:07:38] what the initial situation looks like
[00:07:40] and then based out on our understanding
[00:07:42] of how things stand, we'll pick and
[00:07:45] choose amongst some other strategies in
[00:07:46] order then to be able to further develop
[00:07:49] a solution to the problem. That's how we
[00:07:51] behave as as real experts.
[00:07:54] And I think what we're all trying to do
[00:07:56] today in building uh genai applications
[00:08:01] is incorporate some of those expert
[00:08:04] behaviors into our systems. And that's
[00:08:06] where an agentic approach can help where
[00:08:09] the agent is effectively behaving like
[00:08:12] an expert. And we're furnishing that
[00:08:15] agent with a whole set of tools and
[00:08:18] capabilities and bits of domain
[00:08:19] knowledge. And then we're saying, "Hey,
[00:08:21] look, here's a really complex problem
[00:08:23] that I want you to solve. You work out
[00:08:25] how you're going to solve it. Take
[00:08:27] advantage of these tools, apply some of
[00:08:29] this knowledge, this domain knowledge,
[00:08:31] and come back with the answer."
[00:08:34] >> And so, in adding Sorry, go on.
[00:08:37] >> Oh, no. I was just going to say, um,
[00:08:39] just wanted to jump in quickly with
[00:08:41] Reginaldo's comments. Um, he brings up a
[00:08:44] good point about the data freshness. Um
[00:08:47] I think that is also a common question
[00:08:50] that we get even in just the regular
[00:08:52] graph rag flow about how do we keep
[00:08:54] things up to date. So it would be
[00:08:56] awesome if as we kind of go through this
[00:08:58] kind of if we could touch on the
[00:09:00] freshness aspect and then how we keep
[00:09:02] the graph subsequently up to date as
[00:09:04] part of this flow as well.
[00:09:07] >> Yeah. Yeah. I mean that that's that's
[00:09:09] really important isn't it? Because when
[00:09:10] we are again as as humans and human
[00:09:14] experts trying to solve a problem, we
[00:09:16] want access to the latest information.
[00:09:18] Um and therefore we want to be able to
[00:09:19] trust that whatever tools or whatever
[00:09:22] sources of information we have available
[00:09:24] to us are giving us good honest fresh
[00:09:28] data. So I think as we go through a few
[00:09:31] demos we'll we'll talk about ways in
[00:09:33] which we maintain that data and keep it
[00:09:36] fresh. Um, but obviously it's it's it's
[00:09:40] super relevant to be able to produce
[00:09:43] accurate and timely and comprehensive
[00:09:47] solutions to problems. We need access to
[00:09:49] that that really relevant information.
[00:09:51] Yeah.
[00:09:52] Um, and I think when we talk about
[00:09:55] agentic graph rag, we're effectively
[00:09:57] saying as part of an agentic solution,
[00:10:00] we can add some graph rag capabilities.
[00:10:02] We can take advantage of an underlying
[00:10:05] graph and of the ways in which we've
[00:10:07] represented all the stuff that's of
[00:10:09] interest to us as a set of connected
[00:10:11] data. We'll take advantage of that in
[00:10:14] order to chase down those connections,
[00:10:16] find fresh, relevant, non-obvious
[00:10:20] information, and allow the agent to take
[00:10:23] advantage of these capabilities. It's
[00:10:25] beginning to to work its way iteratively
[00:10:27] through solving a problem.
[00:10:28] >> Yeah.
[00:10:30] >> Awesome. So, this this sounds awesome.
[00:10:32] Um, I I guess my question would be if
[00:10:35] I'm starting from kind of ground zero,
[00:10:38] like I don't I maybe I don't have a
[00:10:40] graph yet, like what's the easiest way
[00:10:43] to kind of get this going?
[00:10:47] So I think I'm I'm going to create a
[00:10:51] very simple distinction between what we
[00:10:54] might call a knowledge graph and other
[00:10:59] graph solutions that effectively index
[00:11:02] textual content. And a knowledge graph
[00:11:05] on the one hand is uh a very faithful
[00:11:08] representation of the stuff that's
[00:11:10] really of interest to us. And what we'll
[00:11:12] see in a minute is a a demo, a fraud
[00:11:15] demo where we have a graph data set that
[00:11:19] represents
[00:11:21] uh accounts and transactions and bits of
[00:11:23] identity information associated with
[00:11:25] those accounts.
[00:11:27] And to get started there, there's
[00:11:30] actually still quite a bit of effort
[00:11:32] involved because as a builder, I've got
[00:11:35] to think, well, what's an ideal
[00:11:38] representation of my domain? How am I
[00:11:40] going to model it as a graph? Um, what
[00:11:43] kinds of questions do I expect to be
[00:11:45] able to ask and answer out of that
[00:11:47] graph? There's a bit of upfront
[00:11:50] information architecture effectively,
[00:11:52] but the end result is I've got a really
[00:11:55] really powerful data set that rep
[00:11:58] represents the stuff that I'm really
[00:12:00] interested in and I can ask some very
[00:12:01] very complex questions of it.
[00:12:04] Um, and I think on the Neptune side, we
[00:12:06] do have some tooling that can help
[00:12:09] all of our builders get started modeling
[00:12:12] those domains and creating queries and
[00:12:16] visualizations of them.
[00:12:19] But as I say, I'm going to call that a
[00:12:21] knowledge graph. There's lots of
[00:12:22] different ways of describing knowledge
[00:12:23] graphs, but that's that's my simple
[00:12:25] version of it. It's, you know, kind of
[00:12:26] faithful representation of the stuff in
[00:12:28] our domain that we're really really
[00:12:30] interested in.
[00:12:32] >> Awesome. Separately
[00:12:34] there is um we'll often have a lot of
[00:12:38] information in unstructured or
[00:12:41] semistructured documents in text
[00:12:43] documents or markdown files or even JSON
[00:12:46] documents things like that.
[00:12:49] And one of the easiest ways of getting
[00:12:52] started building firstly a graph rag
[00:12:54] solution and then an agentic graph rag
[00:12:56] solution based off this kind of content
[00:12:59] is to take advantage of either things
[00:13:03] such as the Neptune bedrock integration
[00:13:05] that will allow you to automatically
[00:13:06] ingest all of this data and create a
[00:13:10] kind of graph rag capability. That's a
[00:13:12] fully managed uh capability that we
[00:13:15] offer through Bedrock through Bedrock
[00:13:17] knowledge bases
[00:13:19] or and again in one of the demos we'll
[00:13:21] be seeing uh this in a little more
[00:13:23] detail. We have an opensource graph rag
[00:13:26] toolkit that will actually allow you to
[00:13:28] ingest all of those unstructured and
[00:13:31] semistructured documents. And the
[00:13:33] toolkit will automatically build for you
[00:13:35] a graph. It's not a knowledge graph.
[00:13:38] It's a it's a graph that provides a very
[00:13:41] powerful index over all of that textual
[00:13:44] content.
[00:13:46] Um, and then the toolkit actually
[00:13:48] provides you then with a query engine
[00:13:49] that allows you to begin to ask
[00:13:51] questions of your data. And what we'll
[00:13:54] see a bit later on is how that toolkit
[00:13:57] also includes some features that will
[00:14:00] automatically create a set of tools that
[00:14:03] you can use in an Aentic solution. So if
[00:14:06] you've got unstructured or
[00:14:07] semi-structured data, the easiest way to
[00:14:09] get started is either through Bedrock
[00:14:11] knowledge bases or via the graph rack
[00:14:14] toolkit. Um if you're wanting to build
[00:14:17] one of these more highfidelity knowledge
[00:14:20] like graphs, um there are perhaps some
[00:14:22] other tools that we can talk about or we
[00:14:24] can link to at the end of the show that
[00:14:26] can help you with some of that modeling
[00:14:28] um and application and information
[00:14:30] architecture.
[00:14:32] >> Awesome. And just to kind of jump in on
[00:14:34] this, um, thank you Reginaldo for your
[00:14:37] question talking a little bit about how
[00:14:39] Neptune ties into the architecture that
[00:14:41] Ian was just discussing. So does Neptune
[00:14:44] have any similarity search capabilities
[00:14:47] or do you have to map those nodes in an
[00:14:50] external vector database? So depending
[00:14:53] on the architecture that you want to
[00:14:55] build, I think there's a couple options
[00:14:56] here, right Ian?
[00:14:58] >> There that there are. Yes. Yeah.
[00:15:00] [snorts]
[00:15:01] So um firstly you know for for people
[00:15:04] watching who aren't necessarily hugely
[00:15:06] familiar with Neptune just say that
[00:15:09] Neptune is Amazon's managed graph
[00:15:11] database but actually has two different
[00:15:13] engines. There's the Neptune database
[00:15:15] engine which you can think of as uh kind
[00:15:18] of SQL for it's an online transactional
[00:15:21] graph database for storing very very
[00:15:23] large data sets.
[00:15:25] Um and then separately we have another
[00:15:28] engine called Neptune Analytics which is
[00:15:31] a memory optimized graph engine.
[00:15:35] Neptune Analytics
[00:15:37] also allows you to store vector
[00:15:40] embeddings as part of the graph. So if
[00:15:43] you're building a solution that uses
[00:15:44] Neptune Analytics, you can model all and
[00:15:47] model everything as a graph, store it in
[00:15:49] Neptune Analytics. You can also generate
[00:15:51] embeddings. You have to do that
[00:15:53] externally perhaps via bedrock, but you
[00:15:56] can then store those embeddings within
[00:15:58] the graph. And you can use the graph
[00:16:00] query languages that we supply with
[00:16:02] Neptune Analytics to conduct a vector
[00:16:06] similarity search and use that as the
[00:16:08] starting point for a graph query that
[00:16:11] then chases down all of those
[00:16:12] connections in the graph. uh or you can
[00:16:15] begin a normal graph traversal and then
[00:16:18] when you find stuff in the graph that
[00:16:19] you're really interested in, if they
[00:16:21] have embeddings associated with them or
[00:16:23] attached to them, you can use that to
[00:16:25] drive similarity search. So that's one
[00:16:28] approach. Neptune Analytics allows you
[00:16:30] to combine graph and vector similarity
[00:16:33] search in the same underlying
[00:16:35] technology.
[00:16:38] um a separate approach and this is the
[00:16:40] the the approach that we've adopted in
[00:16:42] that open-source toolkit is to create a
[00:16:46] logical distinction between a graph
[00:16:48] store and a vector store and then have
[00:16:51] put APIs over the two of them so that I
[00:16:54] could query the vector store find stuff
[00:16:57] that's of interest by way of similarity
[00:16:59] search and then use those results to
[00:17:02] drive a graph search in the graph
[00:17:07] And again in the toolkit the toolkit
[00:17:09] actually supports multiple backends. It
[00:17:11] supports Neptune database, Neptune
[00:17:13] Analytics, S3 vectors, open search, uh
[00:17:17] Postgress with the PG vector extension.
[00:17:21] Depending upon which of those backends
[00:17:23] you choose, it may be, you know, if
[00:17:25] you're using Neptune Analytics,
[00:17:28] the graph store and the vector store
[00:17:29] will actually be pointed at the same
[00:17:31] underlying instance.
[00:17:34] Does that help answer the question?
[00:17:38] >> Yeah, I think you covered that
[00:17:39] perfectly. Yeah. So, uh just to
[00:17:42] summarize,
[00:17:43] Bedrock knowledge bases graph rag. If I
[00:17:45] wanted to go that route, I can use that
[00:17:47] with Neptune Analytics and that would be
[00:17:49] an all-in-one package. And then if I
[00:17:51] wanted to mix and match my stores, the
[00:17:54] graph toolkit would be a good option for
[00:17:56] that. and it would handle it would
[00:17:59] handle for me the kind of mapping
[00:18:01] between the nodes in the graph to the
[00:18:04] corresponding vectors in the open
[00:18:06] search. So uh yeah it would be handled
[00:18:08] for me so I don't have to think about
[00:18:10] that too much
[00:18:11] >> actually and I think that's a really
[00:18:12] important point. So you know we we've
[00:18:14] talked about the Neptune Bedrock
[00:18:17] integration and the toolkit and in both
[00:18:19] cases
[00:18:21] these
[00:18:22] service on the one hand open source
[00:18:24] library on the other are doing that
[00:18:26] mapping on your behalf. But if you're
[00:18:28] building your own graph rag solutions um
[00:18:32] and you're wanting to combine vector
[00:18:35] search with graph search you do have to
[00:18:37] think about how you're going to map
[00:18:39] backwards and forwards between the two.
[00:18:41] So the results that returned from a top
[00:18:44] case similarity search should ideally
[00:18:47] have some reference to nodes in the
[00:18:48] graph that you can use to then begin a
[00:18:51] graph traversal or a graph query.
[00:18:55] >> So I guess when we think about how the
[00:18:57] graph rag toolkit fits in with a gentic
[00:19:01] graph rag I I guess I'm mentally trying
[00:19:04] to figure out like what's the connection
[00:19:07] if we want to do a gentic graph rag.
[00:19:10] uh how does that work if we're choosing
[00:19:13] to use the graph toolkit to build this
[00:19:15] out?
[00:19:17] >> So [snorts] um let's let's think about
[00:19:20] the the the kind of the overall
[00:19:22] architecture of an agentic solution. As
[00:19:24] I say, what we're wanting to do here is
[00:19:27] is what you're wanting is to build a
[00:19:30] system or an application where we've
[00:19:33] incorporated some domain knowledge, some
[00:19:36] expertise. we're actually having the
[00:19:38] system behave like an expert.
[00:19:41] The way we've done that for decades is
[00:19:44] to hardcode all of that kind of
[00:19:47] decision-making logic into the
[00:19:49] application. But then we find that
[00:19:51] that's a rather fragile way of solving
[00:19:53] the problem. It works today really
[00:19:56] really well as long as we're prepared to
[00:19:57] to to follow those steps. but something
[00:20:01] out there in your the business changes,
[00:20:03] some new requirements emerge, and we've
[00:20:05] got to go and revise and update that all
[00:20:07] over again. With an agentic solution,
[00:20:10] we're effectively saying, "Look, here's
[00:20:12] a an LLM based agent that we're going to
[00:20:16] furnish or give um some instructions,
[00:20:21] some domain expertise that describe how
[00:20:23] it ought to behave. And we're also going
[00:20:26] to give it some tools that it can use to
[00:20:29] solve the problem. So we're giving it
[00:20:30] some knowledge and the tools that it can
[00:20:34] use based on that knowledge and then
[00:20:36] we're going to let it solve the problem.
[00:20:38] It's going to work out its own
[00:20:41] stepby-step approach to solving the
[00:20:43] problem and it may make a couple of
[00:20:45] steps forward and come back and solve.
[00:20:47] The way in which the graph rag toolkit
[00:20:49] can help here is it can automatically
[00:20:54] create what I'm calling domainspecific
[00:20:58] tools I tools that are intimately
[00:21:01] related to the underlying data set and
[00:21:05] it can expose those tools to the agent.
[00:21:09] Now many agentic solutions are not only
[00:21:12] going to have a graph as part of the
[00:21:16] underlying tool set. They may very well
[00:21:18] have many other tools that are pointed
[00:21:20] to other different backends.
[00:21:23] But where we've introduced the toolkit
[00:21:25] in order to provide some graph
[00:21:27] capabilities to the agent, the toolkit
[00:21:30] is making it really really easy to
[00:21:33] automatically generate tools that are
[00:21:37] descriptive or representative of our
[00:21:39] domain. they kind of naturally
[00:21:42] incorporate lots of knowledge about our
[00:21:44] domain because the toolkit is
[00:21:46] automatically introspecting the
[00:21:48] underlying data and saying hey I think
[00:21:52] this underlying data set represents a
[00:21:55] set of uh runbooks or a set of policy
[00:21:58] documents so hey look I've got a
[00:22:01] knowledge base or I've got a tool here
[00:22:03] that knows all about runbooks to solve
[00:22:06] problems x y and zed
[00:22:08] and we're advertising that to the agent
[00:22:11] and then the agent given a problem if it
[00:22:13] thinks it's appropriate to take
[00:22:15] advantage of that tool those runbooks or
[00:22:18] those policy documents it will
[00:22:20] automatically invoke it. So that's how
[00:22:22] the toolkit is making this stuff really
[00:22:24] really easy. It's automatically creating
[00:22:26] tools that you can incorporate into an
[00:22:28] agentic solution.
[00:22:32] >> Awesome.
[00:22:34] Cool. So should we check this out in
[00:22:37] action? I'm super excited to see how
[00:22:39] this all works. Um, I've worked with the
[00:22:41] Graphrack toolkit before, but not from
[00:22:45] the custom domain tool perspective. So,
[00:22:47] >> right be interested to see how it all
[00:22:49] comes together.
[00:22:51] >> Yeah. And so I I think you know when
[00:22:54] when Melissa and I were discussing how
[00:22:57] we'd like to to tackle some of these
[00:22:59] issues previously, we kind of identified
[00:23:02] three different ways in which you can
[00:23:05] incorporate a graph and graph
[00:23:08] capabilities into your agentic solutions
[00:23:10] today. Um so we're going to go through
[00:23:13] those three different approaches.
[00:23:15] Um it's not necessarily either or you
[00:23:18] know that each approach is relevant for
[00:23:20] a specific set of problems but the great
[00:23:23] thing about agentic solutions is we can
[00:23:27] always add more tools. We can always
[00:23:29] present the agent with more tools. So
[00:23:30] you can actually combine or mix and
[00:23:33] match the three different approaches
[00:23:35] that we're going to look at today.
[00:23:37] So, what we're going to look at first of
[00:23:39] all are um two examples of
[00:23:44] building tools that we give to an agent
[00:23:49] um that are pointed at one of those
[00:23:51] knowledge graphs. One of those things I
[00:23:52] was talking about earlier where we've
[00:23:53] got a really highfidelity representation
[00:23:57] of a specific domain. somebody has
[00:23:59] actually invested the time to create a
[00:24:01] good information architecture and have
[00:24:04] built and populated and kept fresh a
[00:24:07] data set around a specific domain. And
[00:24:09] this is going to be a a fraud demo and I
[00:24:11] think in previous live live streams
[00:24:14] we've actually used some of the the
[00:24:16] fraud demo example uh previously.
[00:24:20] Um, so we'll look at that first. And
[00:24:22] then the third example is this example
[00:24:25] where we've got this unstructured and
[00:24:27] semi-structured textual content that
[00:24:29] we've ingested into the toolkit. And
[00:24:32] we're going to show how the toolkit just
[00:24:33] automatically
[00:24:35] infers, oh, these are the kind of tools
[00:24:38] that I can create and hand off to an
[00:24:40] agent.
[00:24:42] All right.
[00:24:44] So, I'm going to
[00:24:47] >> and for those that are interested in
[00:24:48] following along, uh, we do have all of
[00:24:52] the examples and some of the fraud
[00:24:55] examples that Ian is mentioning from the
[00:24:57] past episodes. Uh, we'll post those
[00:25:00] links into the chat as well, so you will
[00:25:02] have access to kind of run through all
[00:25:05] of these on your own as well. So,
[00:25:11] >> cool. So let's let's start with this uh
[00:25:13] this this fraud example. Um so here I've
[00:25:16] just got a simple diagram that
[00:25:19] illustrates the underlying graph data
[00:25:21] model for this fraud data set. So I said
[00:25:24] this is this is somebody's applied some
[00:25:26] careful information architecture here in
[00:25:29] order to design a graph model that's
[00:25:32] really really useful for helping
[00:25:35] identify things like fraud rings. So you
[00:25:37] can see that in our underlying graph
[00:25:39] data, we're going to have lots of
[00:25:40] different accounts
[00:25:42] um and many transactions where those
[00:25:45] accounts have transacted with merchants.
[00:25:48] And each account is associated with one
[00:25:52] or more bits of identity information. So
[00:25:54] as we onboard accounts, we'll capture
[00:25:56] things like a physical address, person's
[00:25:58] date of birth, an email address, and so
[00:26:00] on. And for the purposes of a fraud demo
[00:26:03] application, we typically take those
[00:26:06] bits of identity information and pull
[00:26:08] them out and represent them as separate
[00:26:10] nodes because that allows us to find
[00:26:14] accounts that are sharing multiple bits
[00:26:17] of identity information. And that's
[00:26:19] often a key clue that
[00:26:25] we're looking at people who are or
[00:26:26] groups of people who are behaving in a
[00:26:28] fraudulent manner. Okay, so that's the
[00:26:30] underlying data.
[00:26:37] Um,
[00:26:38] this diagram or this this visualization
[00:26:41] here um is just showing some small
[00:26:45] subset of the data that's in our
[00:26:47] underlying graph. So you can see all of
[00:26:49] the things that are red here. These are
[00:26:51] different accounts. Different bits of
[00:26:53] identity information are in blue. So,
[00:26:55] we've got things like uh email address,
[00:26:57] date of birth, telephone number,
[00:27:00] um and then we've got all the different
[00:27:02] transactions where those accounts have
[00:27:05] bought services or products from
[00:27:07] different merchants. So, that's just to
[00:27:09] give you a sense of the underlying data
[00:27:10] that we're working with.
[00:27:14] Okay. Now, the first approach that we
[00:27:17] can take if we're wanting to incorporate
[00:27:20] some fraud detection capabilities into
[00:27:23] our agentic solution or we're building
[00:27:25] an agentic solution that is responsible
[00:27:27] for identifying and uh assessing
[00:27:31] potentially fraudulent behavior. The
[00:27:33] first way we can do that is to create an
[00:27:38] agent and give it some knowledge. Say,
[00:27:41] hey, look, you're an agent. you're
[00:27:43] responsible for detecting fraud and
[00:27:45] you've got access to a graph database
[00:27:48] and a graph data set that represents all
[00:27:50] this information. So, we're being very
[00:27:52] explicit. We're actually telling the
[00:27:53] agent something about the underlying
[00:27:56] data. We're saying when you're given a
[00:27:59] problem to solve,
[00:28:01] you're free to write whatever query you
[00:28:04] want against this underlying data in
[00:28:07] order to solve that problem or to answer
[00:28:09] a specific question. So we're
[00:28:11] effectively allowing the agent to act
[00:28:13] like uh a good data engineer or uh a
[00:28:18] database specialist.
[00:28:20] Okay. So that's the first approach we're
[00:28:21] going to take.
[00:28:25] Um and to to do that we're going to use
[00:28:29] uh another piece of software called the
[00:28:34] Amazon Neptune MCP server.
[00:28:38] So, the Amazon Neptune MCP server
[00:28:40] available on GitHub Labs. It's really
[00:28:43] easy to set up and you'll see that
[00:28:44] that's exactly what I'm doing in this
[00:28:47] cell here.
[00:28:49] I'm creating a local instance that's up
[00:28:52] and running on this notebook instance of
[00:28:54] the Amazon Neptune MCP server. And I've
[00:28:58] told that server where my graph database
[00:29:01] resides. I've given it the graph
[00:29:02] endpoint of that data set. And so this
[00:29:06] MCP server can now be offered by way of
[00:29:09] a client to an agent.
[00:29:13] So
[00:29:15] very simple code to create a client that
[00:29:18] will allow an agent to interact with
[00:29:20] that MCP server. And that MCP server in
[00:29:23] turn will forward queries to the
[00:29:27] underlying graph database.
[00:29:32] The next thing I have here is a prompt.
[00:29:35] So this is that that prompt that I'm
[00:29:36] going to give my agent. And you can see
[00:29:38] we're telling it this is how I want you
[00:29:40] to behave. You're a fraud investigation
[00:29:42] agent. So we're telling it a little bit
[00:29:43] about its role.
[00:29:45] And then we're providing it with some
[00:29:48] additional guidance. And the interesting
[00:29:49] thing here is we've got two different
[00:29:51] kinds of guidance. We've got some
[00:29:52] guidance about it behaving
[00:29:56] like a uh a database specialist. We're
[00:30:00] telling it how to write good graph
[00:30:02] queries.
[00:30:04] But the second part of the prompt, we're
[00:30:07] also giving it a bit of domain expertise
[00:30:10] around
[00:30:11] the fraud investigation domain. So we're
[00:30:15] saying when you're asked questions, you
[00:30:16] should be doing things such as
[00:30:18] identifying shared resources, things
[00:30:20] like shared devices, shared IP
[00:30:22] addresses.
[00:30:24] You should try and trace transa
[00:30:25] transaction flows and money movement
[00:30:27] patterns. So we're we're actually
[00:30:30] telling in the prompt we're we're giving
[00:30:32] the agent some domain expertise
[00:30:36] and we're also giving it some expertise
[00:30:38] about how to behave like a good database
[00:30:41] specialist.
[00:30:42] All right.
[00:30:46] In this cell here, we're then going to
[00:30:48] create the agent itself.
[00:30:51] So we create an agent.
[00:30:54] We give it the tools that are made
[00:30:56] available by way of that MCP client. And
[00:30:59] in this case, that Amazon Neptune MCP
[00:31:03] server exposes a couple of tools. One is
[00:31:05] a tool that allows you to get the
[00:31:06] underlying graph schema. And another is
[00:31:09] a tool that allows you or the agent to
[00:31:12] actually run graph queries.
[00:31:17] So let's run.
[00:31:19] Okay. So Oh. Ah, yeah. Didn't
[00:31:24] can create my prompt,
[00:31:27] right?
[00:31:36] Let's restart and do this again.
[00:31:38] >> I love [snorts] Jupyter Notebooks.
[00:31:40] [laughter]
[00:31:41] If you all haven't worked with Jupyter
[00:31:42] Notebooks before, they're a lot of fun.
[00:31:45] Um if you're curious about the interface
[00:31:47] that Ian is showing and uh I guess we
[00:31:52] saw a little bit of a visualization
[00:31:54] earlier um we actually have this
[00:31:56] opensource package called graph notebook
[00:32:00] that's on our GitHub that actually
[00:32:01] extends the Jupyter notebooks uh with
[00:32:05] some Neptune specific magics that just
[00:32:07] make it a lot easier to like generate
[00:32:09] some of the visuals that we saw earlier.
[00:32:11] Um, so ever since we introduced that, I
[00:32:14] feel like all of us tend to lean on the
[00:32:17] notebooks for doing everything Neptune
[00:32:19] graph related.
[00:32:20] >> Yeah, it's it's [snorts]
[00:32:22] pros and cons, but it's a nice
[00:32:24] interactive environment for
[00:32:25] experimenting both in terms of writing
[00:32:27] queries um and taking advantage of a lot
[00:32:30] of that uh software and the SDKs that we
[00:32:33] make available. Okay, so I've got it
[00:32:34] running now. So we've created an agent.
[00:32:37] I've given it the tools that were made
[00:32:39] available by way of that MCP server.
[00:32:42] I've given it the prompt with all of
[00:32:43] that domain expertise in it. And then
[00:32:46] I've also given it a question. Find
[00:32:48] accounts linked by shared contact
[00:32:49] details or devices that indicate a
[00:32:52] single fraudulent actor.
[00:32:55] Um, and now this print out here towards
[00:32:59] the top, we can actually see the agent
[00:33:01] beginning to run.
[00:33:03] As I say, we want to build agents that
[00:33:05] behave like experts that iteratively and
[00:33:07] incrementally begin to solve a problem
[00:33:10] based on their current understanding of
[00:33:12] the state of the world. So, it's going
[00:33:14] to make an initial query, get back some
[00:33:16] results, interpret those results, decide
[00:33:19] what to do next, and then potentially
[00:33:21] run some additional graph queries.
[00:33:24] So, you can see the agent saying, I can
[00:33:25] help you find those accounts. It
[00:33:27] initially gets the graph schema just to
[00:33:29] confirm that the graph looks exactly how
[00:33:32] we've promised it's going to look and
[00:33:34] then it begins to run a number of graph
[00:33:38] queries against the underlying data. And
[00:33:41] what's happening here is the agent knows
[00:33:44] enough about the query language that we
[00:33:46] use against Neptune query language
[00:33:48] called Open Cipher. it knows enough to
[00:33:51] be able to actually author queries on
[00:33:53] the fly that it can then run against
[00:33:55] that underlying data.
[00:33:58] So you can see how many we've got five
[00:34:01] queries here I think that it's run one
[00:34:03] after another gets the results back
[00:34:04] makes some decisions advances its
[00:34:07] problem solving a little further runs
[00:34:09] another query and so on and then finally
[00:34:12] it presents us with some results. So in
[00:34:15] the end this is a rag like solution but
[00:34:20] the agent has more interactively sourced
[00:34:24] all of that evidence and then finally
[00:34:27] created a response
[00:34:29] based upon that evidence.
[00:34:32] So it said here's the the high-risk
[00:34:34] fraud cluster lots and lots of details
[00:34:38] even recommended actions that we should
[00:34:40] take next. Okay. So quite a
[00:34:42] comprehensive answer and all we had to
[00:34:44] do was give it the prompt that told it a
[00:34:46] little bit about the database or the
[00:34:47] data schema and a little bit of
[00:34:50] knowledge about the the fraud domain.
[00:34:53] Yeah, I see this as super helpful
[00:34:55] especially for if I was a fraud
[00:34:58] investigator from the business side and
[00:35:00] I don't want to know how to write any
[00:35:03] graph queries myself then I can just ask
[00:35:06] natural language questions and get
[00:35:08] something back which is super cool but
[00:35:11] also that kind of brings me to the
[00:35:12] question of how do I prevent malicious
[00:35:16] people from let's say deleting certain
[00:35:20] data or augmenting the data writing in
[00:35:24] bad data, things like that,
[00:35:27] >> right? Um, so I think firstly we have to
[00:35:30] ensure that
[00:35:33] uh the tools that we're running and the
[00:35:34] environments in which they're running
[00:35:37] have sufficient permissions to be able
[00:35:39] to get the job done but no more. And one
[00:35:43] of the things that we'd be really
[00:35:44] careful of in this kind of context is
[00:35:47] ensuring that our notebook environment
[00:35:49] can read the graph but it can't write or
[00:35:53] delete data.
[00:35:56] Okay. If we're wanting to create an
[00:35:57] investigative tool where we don't
[00:35:59] necessarily want to use the tool to
[00:36:03] create data and we want to pro
[00:36:06] definitely prevent anybody from deleting
[00:36:08] data, then we would use IM permissions
[00:36:11] to ensure that this environment only has
[00:36:14] the read data permission against the
[00:36:16] underlying graph. And then those
[00:36:19] permissions will flow all the way
[00:36:20] through that MCP server
[00:36:24] and any query that the agent may come up
[00:36:27] with. And we all know that agents can be
[00:36:28] quite creative. We know that LLMs can be
[00:36:31] quite creative and can often try and do
[00:36:34] things that exceed their
[00:36:35] responsibilities. But if the agent here
[00:36:38] were to invent a query that thought
[00:36:41] perhaps I do need to delete some data
[00:36:42] and issues a delete request.
[00:36:46] As long as we've provisioned the
[00:36:48] environment such that it can only read
[00:36:50] data that will be refused.
[00:36:54] >> Okay. So one of the ways here is firstly
[00:36:57] securing the environment in which we're
[00:37:00] running the agent in order to to prevent
[00:37:03] it doing anything malicious against the
[00:37:05] the underlying data.
[00:37:07] >> Awesome. Also just wanted to jump in
[00:37:09] here with a couple quick questions from
[00:37:11] the chat. So Lauren is asking if this is
[00:37:15] available for us to try out ourselves.
[00:37:17] So yes, we do have a GitHub repo where
[00:37:21] we post a lot of samples around Neptune
[00:37:24] and generative AI which we just posted
[00:37:26] in the link into the chat. So check that
[00:37:29] repo later this week and we'll have that
[00:37:31] updated with these examples for you to
[00:37:33] play around with.
[00:37:35] Also wanted to bring up a question from
[00:37:38] Reginaldo which I think is a good
[00:37:39] transition point as to what we've been
[00:37:42] talking about around you know once we
[00:37:44] start moving this flow to production
[00:37:47] you know can we write the queries
[00:37:49] ourselves or can we really rely on the
[00:37:53] agent and the LLM to make sure that it
[00:37:55] comes up with like the logically correct
[00:37:58] version of someone's natural language
[00:37:59] question.
[00:38:00] >> Right. Yeah. I think that that I mean
[00:38:04] that naturally does lead into the the
[00:38:07] second demo here where we're going to
[00:38:09] impose a little more control over the
[00:38:11] kinds of tools that we expose to the
[00:38:12] agent. Um but just to emphasize I mean
[00:38:15] this this MCP client and the the uh the
[00:38:18] Amazon Neptune MCP server are available
[00:38:22] uh via GitHub and you can install them
[00:38:26] exactly as I've installed them here. And
[00:38:28] so you could use these today against
[00:38:31] your own wellformed graph. If you've got
[00:38:33] an existing graph database, an existing
[00:38:35] Neptune graph, you can use this today um
[00:38:38] in order to have the agent write
[00:38:40] queries. Um the downside is as we saw
[00:38:44] the agent was running several different
[00:38:46] queries.
[00:38:48] Um I actually have some logging where we
[00:38:50] actually see the underlying queries. And
[00:38:51] what I sometimes see is that the agent
[00:38:54] might first author a query where the
[00:38:56] syntax isn't quite correct
[00:38:58] >> and it runs it against the database and
[00:39:00] then it gets a response back and says,
[00:39:01] "Oh, I'm going to try again and I'm
[00:39:02] going to modify the query." So, it can
[00:39:06] be quite hesitant in moving forwards and
[00:39:08] solving the problem. Um, it's a great
[00:39:11] way of getting up and running very very
[00:39:13] quickly. But it may be that as we begin
[00:39:15] to move some of our solutions into
[00:39:17] production, we want as builders to take
[00:39:21] a little more control over the kinds of
[00:39:23] tools that were exposed to the agent and
[00:39:26] the ways in which those tools behave.
[00:39:29] So the second example I've got here and
[00:39:32] this again is running against that
[00:39:34] underlying fraud data set.
[00:39:38] But here
[00:39:40] as an application developer, I've
[00:39:42] created a couple of very domain specific
[00:39:45] tools.
[00:39:47] So you can see I've got one here, the
[00:39:49] tool called find fraud ring candidates
[00:39:53] and a second one called calculate fraud
[00:39:55] ring exposure. So these are these look
[00:39:57] just like normal Python methods and you
[00:40:00] can
[00:40:03] and you can see that each method
[00:40:05] encapsulates
[00:40:07] a graph query.
[00:40:09] In this first one, we're running
[00:40:12] actually a graph algorithm, the Louain
[00:40:13] graph algorithm in order to find
[00:40:19] uh potentially fraudulent groups of
[00:40:23] fraudulent actors. and we're returning
[00:40:26] those results. And this second query,
[00:40:30] again, it's using the open cipher query
[00:40:31] language, but given a list of account
[00:40:34] IDs, it's traversing the graph, finding
[00:40:36] all of those different transactions, and
[00:40:38] summing the results.
[00:40:40] So, this allows us to control exactly
[00:40:42] the kind of behaviors and the kinds of
[00:40:44] queries that the agent can run against
[00:40:48] our underlying data set.
[00:40:50] So, we've moved some of that knowledge
[00:40:52] from the prompt, which we saw in the
[00:40:53] first example, back into the code, but
[00:40:57] we're we're then exposing
[00:41:00] these methods or these functions as
[00:41:02] tools to the agent. And again, the key
[00:41:05] thing about an agentic solution is we're
[00:41:08] not being overly prescriptive about the
[00:41:10] order in which the agent performs a
[00:41:13] process. We're just saying, look, you're
[00:41:15] this kind of expert. Here's a set of
[00:41:17] tools that you can use. You think about
[00:41:20] the order in which you want to apply
[00:41:22] them, which tools you want to use. You
[00:41:24] pick and choose. You go ahead solve the
[00:41:26] problem the best way you think
[00:41:28] appropriate.
[00:41:31] >> And I also see this um we've got another
[00:41:34] comment from Assan about if we wanted to
[00:41:36] integrate to an app like a web app um
[00:41:40] how can we secure it so queries are
[00:41:43] synthesized and only valid questions are
[00:41:45] answered. So this looks like it would be
[00:41:46] a great approach for that because you
[00:41:48] can have a lot more controls over like
[00:41:52] what exact queries are being run. It
[00:41:53] looks like with this.
[00:41:55] >> Yes. Yeah. I I as a an application
[00:41:58] developer or a a data engineer um have a
[00:42:02] lot more control over the kinds of query
[00:42:05] capabilities that I want to expose to
[00:42:06] the agent. So I'm definitely not going
[00:42:08] to include queries here that will change
[00:42:11] or corrupt the data. I'm not going to
[00:42:13] include any queries that delete data.
[00:42:17] What it does mean is that I need that
[00:42:21] graph database expertise though I need
[00:42:23] to understand the domain, the the graph
[00:42:26] data model and I also need to know how
[00:42:29] to author good queries that can
[00:42:32] effectively implement these kinds of
[00:42:34] capabilities. With that first solution,
[00:42:36] we were just letting the agent write the
[00:42:38] best queries it could come up with in
[00:42:40] order to solve the problem. Now we've
[00:42:42] moved that responsibility back to me,
[00:42:44] but I've now created a couple of domain
[00:42:46] meaningful tools that we can give to the
[00:42:48] agent and just say, you know, you go
[00:42:50] ahead solve the problem the way you you
[00:42:52] see fit.
[00:42:55] So again, we're going to create a little
[00:42:57] uh local
[00:42:59] MCP server. We're going to give it these
[00:43:02] two tools.
[00:43:06] >> So the setup is slightly different,
[00:43:08] >> but we're still creating a client. Go
[00:43:10] on. Oh, sorry. Uh, Ian, I thought it was
[00:43:12] going to take longer to run some of
[00:43:14] these steps because we got a couple
[00:43:15] questions in the chat. I just wanted to
[00:43:16] pop up really quickly. Um, one was just
[00:43:19] about the query language. So, um, we're
[00:43:22] using Open Cipher today, but the Neptune
[00:43:25] MCP server also supports Gremlin, um, as
[00:43:29] Neptune database supports both query
[00:43:31] languages today. So,
[00:43:34] that
[00:43:34] >> Yeah, that's that's that that's correct.
[00:43:36] So if you're using Netune database as
[00:43:38] your underlying graph store, then you
[00:43:41] have access to both Open Cipher and
[00:43:43] Gremlin query languages for these kind
[00:43:45] of property graphs. If you're using
[00:43:47] Neptune Analytics today, Neptune
[00:43:49] Analytics
[00:43:50] supports Open Cipher for querying the uh
[00:43:54] the property graph data model. So yeah,
[00:43:57] all the examples that we're using today
[00:43:58] have been written using Open Cipher.
[00:44:00] >> Yes. And then one more question from
[00:44:03] Siobhan Shu asking if we could do this
[00:44:06] agentic graph ragra flow with agent
[00:44:09] core. So um at the moment I believe
[00:44:12] we're just showing it running locally.
[00:44:14] Is that right Ian?
[00:44:15] >> Yes. Yeah. And again notebooks great
[00:44:18] place to to experiment. Um give you a
[00:44:21] very nice interactive environment where
[00:44:23] I can just build out or or flesh out the
[00:44:26] skeleton of a an overall solution. But
[00:44:29] putting this into production, um, I I'd
[00:44:32] use things like agent core in order to
[00:44:33] to properly host and manage and monitor
[00:44:36] a lot of the the agentic components
[00:44:38] within my solution.
[00:44:42] Um, okay. So, we've created those tools.
[00:44:46] Um, stood up a server that exposes those
[00:44:48] tools. Um, this code should look very
[00:44:52] familiar [snorts] because we're creating
[00:44:53] an agent. Uh, we're telling it which
[00:44:56] model we want it to use for its own
[00:44:57] intelligence. And this is going to be
[00:44:59] Claude Sonet 4. Uh we're giving it those
[00:45:01] tools.
[00:45:03] Um we're giving it a very very simple
[00:45:06] system prompt. You're a helpful
[00:45:07] assistant. Answer the user question
[00:45:10] based on the evidence in the search
[00:45:11] results. This is a very very generic
[00:45:13] system prompt. But then the problem
[00:45:15] we're asking it to to solve is please
[00:45:17] can you identify the largest potential
[00:45:19] fraud ring and then list its members and
[00:45:21] calculate its exposure.
[00:45:24] So we'll create that agent. Oh yeah,
[00:45:27] here we go. So, I'll help you identify
[00:45:30] the largest potential fraud ring.
[00:45:34] So, it uses the first tool, tool number
[00:45:36] one, f find fraud ring candidates. Comes
[00:45:40] back with some results. Now, let me
[00:45:42] calculate the exposure for this fraud
[00:45:44] ring. Okay, so you can see again the
[00:45:48] agent,
[00:45:49] it knows the tools that it has at its
[00:45:51] disposal. It's been given a problem to
[00:45:53] solve and it chooses the most
[00:45:56] appropriate tools to help solve that
[00:45:58] problem. Really gave it two tools and it
[00:46:00] used both tools. But it could be that
[00:46:02] there are much wider array of fraud
[00:46:06] detection and fraud analysis tools that
[00:46:08] we were making available to the server.
[00:46:12] Okay, so that's the first two demos and
[00:46:16] that's been running against this fraud
[00:46:18] data set. And as I mentioned earlier,
[00:46:20] this is a very well-modeled fraud data
[00:46:23] set that's pretty representative of a
[00:46:27] set of accounts and merchants and
[00:46:28] transactions and so on. And we've had
[00:46:30] two different approaches to being able
[00:46:32] to build an agentic solution that takes
[00:46:35] advantage of being able to find all of
[00:46:37] those connections in the the underlying
[00:46:39] data.
[00:46:40] >> Yeah. first approach.
[00:46:41] >> Oh, sorry, Ian. I I've got a little bit
[00:46:44] of lag, but um just before we move on
[00:46:46] from the two examples, I just wanted to
[00:46:48] kind of quickly tie it back to
[00:46:50] Reginaldo's comment earlier on the data
[00:46:53] freshness. So, because both of these
[00:46:55] examples, we are reading from kind of
[00:46:58] that well structured knowledge graph. In
[00:47:00] this case, we could have like a separate
[00:47:03] pipeline that just updates the graph in
[00:47:06] real time if we wanted to, right? So we
[00:47:07] don't really have to uh at least from
[00:47:09] the agent perspective, it doesn't have
[00:47:11] to care too much about the data
[00:47:13] freshness because we are just constantly
[00:47:15] updating the graph.
[00:47:17] >> Yes. Yeah, that that [snorts] that's a
[00:47:19] really really good point here that um
[00:47:21] we're building an agent that's pointed
[00:47:23] at this fraud data set. What's building
[00:47:26] the fraud data set? Well, there are
[00:47:28] probably some other parts of an
[00:47:29] application, other pipelines, other
[00:47:32] systems that as the organization
[00:47:35] onboards new accounts begins to add new
[00:47:38] nodes into the graph, add those bits of
[00:47:41] identity information and as we learn
[00:47:43] about transactions, as transactions flow
[00:47:46] um through the organization, again,
[00:47:49] there'll be some other pipeline or
[00:47:51] application that's populating and
[00:47:53] updating the graph. So that's what's you
[00:47:56] know some other process is ensuring that
[00:47:58] the graph is constantly up to date. The
[00:48:00] agent can then do its job knowing that
[00:48:04] the data it has access to is as fresh as
[00:48:06] possible.
[00:48:11] Um okay so we're now going to turn to
[00:48:14] our third example and this is an example
[00:48:16] that uses the graph rag toolkit
[00:48:18] something I mentioned earlier. The graph
[00:48:20] toolkit is an open-source library for
[00:48:23] building
[00:48:24] graph enabled Genai applications.
[00:48:28] The graph toolkit allows you to ingest
[00:48:32] unstructured and semistructured textual
[00:48:35] content. So things like PDFs, text
[00:48:38] files, markdown files, and also some
[00:48:40] semistructured content. It may be JSON
[00:48:43] documents, things like that.
[00:48:46] It allows you to ingest all of this and
[00:48:48] it will automatically build for you a
[00:48:51] graph that effectively indexes all of
[00:48:54] this textual content. So we're not
[00:48:57] building what I called earlier a
[00:48:58] knowledge graph. We're building a graph
[00:49:01] what I call a lexical graph which is
[00:49:04] effectively a fancy graph index over all
[00:49:07] of that textual content.
[00:49:11] But the toolkit also exposes a query
[00:49:14] engine API that allows you to ask
[00:49:17] natural language questions
[00:49:20] and then it has some retrieval
[00:49:22] strategies
[00:49:23] that have been prepopulated with very
[00:49:26] well-written graph queries to go find
[00:49:30] all of that relevant textual content.
[00:49:32] And again, the benefit of using the
[00:49:34] graph here is we can always use vector
[00:49:36] search to find the semantically similar
[00:49:39] information. And that's usually core to
[00:49:41] answering any good question. But the
[00:49:44] graph will also help us find some of
[00:49:46] that non-obvious connected information
[00:49:49] that lies elsewhere in other documents.
[00:49:51] We can combine all that information to
[00:49:53] get a very comprehensive answer. All
[00:49:55] right. So that's what the graph rag
[00:49:57] toolkit allows you to do. It allows you
[00:49:58] to build the kind of graph rag
[00:50:00] application that Melissa was showing at
[00:50:04] the outset of the the live stream.
[00:50:07] Now there are a couple of other things
[00:50:09] in the toolkit that are super useful for
[00:50:11] us here when we're building agentic
[00:50:12] solutions. The first is it supports out
[00:50:15] of the box this concept of
[00:50:16] multi-tenency.
[00:50:17] So I can create separate lexical graphs
[00:50:22] completely and wholly distinct from one
[00:50:23] another in the same underlying graph
[00:50:26] database.
[00:50:28] Now you could use that because you've
[00:50:29] got your own different tenants,
[00:50:31] different users and they all want their
[00:50:32] own separate graphs. But another way in
[00:50:34] which you can use it is to ingest
[00:50:37] specific kinds of documents or specific
[00:50:39] domain information into a particular
[00:50:42] tenant. So you're applying a kind of
[00:50:44] divide and conquer approach so that you
[00:50:46] have different lexical graphs
[00:50:48] representing different bodies of textual
[00:50:51] content. Okay.
[00:50:54] So multi-tenency allows us to ingest
[00:50:57] into different lexical graphs in the
[00:50:58] same underlying instance. So we can
[00:51:01] divide and conquer based on different uh
[00:51:03] different kind of bodies of knowledge.
[00:51:06] The second important feature here is as
[00:51:09] we're ingesting all of this information,
[00:51:12] we're effectively building to the side a
[00:51:14] kind of inferred schema for the
[00:51:17] underlying domain semantics for that
[00:51:19] data. Right?
[00:51:22] combined together. This means that we
[00:51:25] can take that inferred schema. We can
[00:51:29] sample some of the data and we can
[00:51:31] automatically generate a description of
[00:51:34] that graph
[00:51:36] that we could formulate as a tool
[00:51:39] description.
[00:51:41] All right. So the example I've got here
[00:51:43] is two different data sets in two
[00:51:45] different lexical graphs residing in the
[00:51:47] same database instance.
[00:51:50] One of those data sets is information
[00:51:52] about it's kind of aircraft information.
[00:51:55] It's information about different light
[00:51:57] aircraft models, the manufacturers, the
[00:52:00] history of those different aircraft and
[00:52:02] so on. That's information that was
[00:52:03] sourced from Wikipedia.
[00:52:06] The second data set that I have is a set
[00:52:10] of air aircraft incident reports
[00:52:14] from the National Transportation Safety
[00:52:16] Board. So these are kind of
[00:52:18] semistructured documents that describe
[00:52:21] aviation incidents that have occurred
[00:52:23] over the last few years.
[00:52:25] So you can see these two bodies of
[00:52:27] information are related but they're
[00:52:28] somewhat distinct. One is all about the
[00:52:30] history of the aircraft and the
[00:52:32] manufacturers and the other is very
[00:52:34] specific information about specific
[00:52:36] incidents.
[00:52:38] So I've previously ingested all of that
[00:52:39] information using the toolkit into two
[00:52:42] different tenants.
[00:52:45] Um,
[00:52:46] what I'm going to show here
[00:52:49] is that inferred schema for just one of
[00:52:52] those data sets.
[00:52:56] So I said as we're ingesting the data,
[00:52:59] we're actually building to the side this
[00:53:01] kind of inferred schema for the data. So
[00:53:04] we can see that what we have are things
[00:53:06] like aircrafts and facilities and
[00:53:08] manufacturers and then different kinds
[00:53:10] of relationships that connect instances
[00:53:12] of these things. So in the underlying
[00:53:15] data set we will have information about
[00:53:17] specific aircraft and about specific
[00:53:20] manufacturers and they'll be connected
[00:53:21] by way of lots and lots of different
[00:53:23] relationships. Okay.
[00:53:31] So what I'm going to do here
[00:53:35] is
[00:53:38] start an MCP server. And the toolkit has
[00:53:42] some methods that will automatically
[00:53:44] create for you an MCP server. When it
[00:53:48] creates that MCP server,
[00:53:50] the toolkit introspects all those
[00:53:53] different lexical graphs, takes the
[00:53:56] schemas for each graph, samples the data
[00:53:58] for each graph, and uses that to
[00:54:01] generate a description of the contents
[00:54:04] of the graph.
[00:54:06] So that's just taken place here.
[00:54:09] Let's just grow the screen a bit.
[00:54:15] I'm going to create a client again that
[00:54:16] can point to my MCP server.
[00:54:23] And look, these are the tools that were
[00:54:25] automatically created on my behalf by
[00:54:29] the toolkit based on its understanding
[00:54:32] of the contents of those different
[00:54:34] graphs. So the first tool is called
[00:54:36] aircraft and its domain is general
[00:54:38] aviation and aircraft knowledge base. So
[00:54:41] it's quite wordy but it gives a kind of
[00:54:45] a detailed description of this is the
[00:54:47] kind of information that you'll find in
[00:54:50] this specific knowledge base. And notice
[00:54:52] it doesn't even describe it as a graph.
[00:54:54] It just says hey I'm a tool that knows
[00:54:57] all about aviation and aircraft.
[00:55:01] And you could use it for doing things
[00:55:02] such as tracing aircraft lineage and you
[00:55:07] could use it for ex answering these
[00:55:09] kinds of questions. So it's just
[00:55:11] providing some examples to help the
[00:55:12] agent understand when it might be
[00:55:14] appropriate to use this specific tool.
[00:55:18] The second tool is called NTSB
[00:55:21] and this is about again this is a tool
[00:55:23] that says hey I'm a knowledge base that
[00:55:26] knows all about aviation safety and
[00:55:28] accident investigations. So if you want
[00:55:31] to know about specific incidents, I'm
[00:55:33] the tool to use.
[00:55:38] So
[00:55:40] familiar piece of code again, we're
[00:55:41] going to create an agent. We're going to
[00:55:43] give it those tools, the aircraft
[00:55:45] knowledge base and the air aviation
[00:55:47] incident knowledge base.
[00:55:50] A very simple system prompt, but quite a
[00:55:53] complex question that we wanted to
[00:55:54] answer. What safety issues and accident
[00:55:57] patterns do Kit Fox series experimental
[00:56:01] aircraft demonstrate? And how do these
[00:56:03] compare to the design features and
[00:56:06] manufacturing specifications provided by
[00:56:09] Denny Aircraft? I mean, that to me
[00:56:11] sounds like quite a complex question
[00:56:12] that might require us to delve into both
[00:56:16] of those data sets and pick and choose
[00:56:19] and mix and match and marry up lots and
[00:56:20] lots of bits of information.
[00:56:23] All
[00:56:26] right.
[00:56:27] So what we'll see here, we don't see a
[00:56:29] lot of details of what's going on behind
[00:56:31] the scenes, but effectively the agent to
[00:56:34] answer this particular question is going
[00:56:37] backwards and forwards
[00:56:40] taking advantage of both of those tools,
[00:56:42] asking a question, getting back the
[00:56:45] results, interpreting the results,
[00:56:47] deciding what it wants to do next, what
[00:56:48] it needs to learn next, and so on until
[00:56:51] it feels as though it's satisfactory
[00:56:54] accumulated enough information to
[00:56:56] properly answer the question.
[00:56:58] So it goes backwards and forwards and
[00:57:00] behind the scenes it's actually asking
[00:57:01] natural language questions. The agent is
[00:57:03] posing natural language questions to
[00:57:05] those knowledge bases because it doesn't
[00:57:06] know that there's a graph behind the
[00:57:08] scenes. There's no graph query language
[00:57:09] that it knows of. It's just asking
[00:57:12] natural language questions.
[00:57:15] And then we can see here that it's
[00:57:17] finally accumulated enough information
[00:57:18] to create a pretty comprehensive answer
[00:57:23] about the origins and the design and so
[00:57:26] on.
[00:57:28] >> Awesome. Yeah, thanks so much Ian for
[00:57:30] taking us through this demo. I think
[00:57:31] this really ties together all the
[00:57:34] different pieces. So, uh, the previous
[00:57:36] two examples we saw with the Neptune MCP
[00:57:40] server being able to connect that up to
[00:57:43] more of a structured, uh, knowledge
[00:57:45] graph. And then here, you know, we could
[00:57:48] layer on to those previous two examples,
[00:57:50] another MCP server and set of tools that
[00:57:53] would expose what the graph toolkit
[00:57:56] provides for the graph side of things,
[00:57:58] which I think is super cool. Um, one
[00:58:01] last question I wanted to put up on the
[00:58:03] screen. um before we start to close out
[00:58:07] is from William. Uh he's asking what AWS
[00:58:11] service do we use for the rag vector
[00:58:14] database. Uh also no worries being late
[00:58:16] to the party. We'll have all the
[00:58:18] recordings posted to YouTube and all of
[00:58:20] our samples are going to be on the
[00:58:22] GitHub links that we posted uh by this
[00:58:25] Friday. Um but as far as the vector
[00:58:28] store here, graph toolkit supports both
[00:58:32] Neptune analytics which has its own
[00:58:34] vector index or you can also use other
[00:58:37] vector stores in conjunction with it. Um
[00:58:40] I'm sorry Ian for your example were you
[00:58:42] using Neptune database plus something
[00:58:44] else?
[00:58:45] >> Uh this is using Neptune Analytics. So
[00:58:47] Neptune Analytics is both the graph
[00:58:49] store and the vector store. The toolkit
[00:58:51] also supports as you say uh other
[00:58:53] backend vector stores that includes open
[00:58:55] search postgress with the PG vector
[00:58:57] extension and S3 vectors. Um and we
[00:59:00] always welcome contributions to add new
[00:59:03] connectors.
[00:59:05] >> Awesome. Perfect.
[00:59:07] >> Thank you. Well, thank you so much Ian
[00:59:09] for taking the time to show us all of
[00:59:11] this today. Um before we close out, are
[00:59:14] there any like last thoughts or closing
[00:59:16] thoughts you wanted to share with the
[00:59:17] audience?
[00:59:20] Um, well, I I liked your term layer. I
[00:59:22] mean, the point is we're giving you lots
[00:59:26] of different options for creating tools
[00:59:29] that you can hand over to your agents.
[00:59:31] You can keep on adding new tools to your
[00:59:34] agents, not just graphback tools, but
[00:59:36] others, and those agents become more
[00:59:38] powerful, more specialized, behave more
[00:59:41] like experts over time.
[00:59:44] >> Awesome.
[00:59:45] Well, with that, um, everyone again,
[00:59:48] thank you so much for joining us and
[00:59:51] yeah, thank you Ian for sharing all your
[00:59:54] knowledge with us and yeah, hope to see
[00:59:56] you all on next week's episode of
[00:59:58] Databases for AI. Thank you.
[01:00:00] >> Wonderful. Thank you. Thanks, Melissa.
[01:00:02] Thanks, everyone.
[01:00:11] >> [music]

---
*RAW — not yet passed through D.R.D deconstruction. Do not integrate into department files.*
