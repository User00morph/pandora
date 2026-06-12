# RAW EXTRACT — CLI vs MCP: How AI Agents Choose the Right Tool for the Job

## Source Metadata
- **Title:** CLI vs MCP: How AI Agents Choose the Right Tool for the Job
- **URL:** https://www.youtube.com/watch?v=g9JIUM0MHgQ
- **Tier:** 1
- **Extracted:** 2026-06-09
- **Domain:** tech-decentralization / agentic-systems
- **Playlist:** Pandora Tech Playlist — PLWKcfqsabTLUxfC7OFs7UZ8EIJ6hjY_M8
- **Word Count:** ~2008

## Transcript (timestamped)

[00:00:00] Both CLI and MCP are ways for AI agents to interact with the outside world.
[00:00:06] Now CLI command line interface that's when an agent uses the CLI to run commands.
[00:00:13] It runs just regular terminal commands.
[00:00:19] What commands?
[00:00:21] Well commands like LS, like CAT, that's another one, Let's think of a few more grip, yeah, and...
[00:00:30] Let's say, curl.
[00:00:31] So these are the sort of commands it can run and they are the exact same commands a developer would type into a command terminal.
[00:00:40] Now MCP is a standardized protocol where dedicated servers expose structured tools.
[00:00:50] So these our tools, like let's one of them is read file, another one might be search files, and each tool has,
[00:01:04] well it has a name assigned to the tool like read file,
[00:01:09] it has a description which says what the tool does,
[00:01:15] written in English and then it has a JSON schema as well and that schema defines exactly what inputs it expects and what let's come back.
[00:01:27] There's a growing number of developers saying that MCP is an unnecessary complexity, that CLI tools can do the same job cheaper.
[00:01:39] And they do kind of have the numbers to back it up.
[00:01:42] So the argument goes a bit like this.
[00:01:45] AI models have been trained on millions of CLI examples, examples in their training data set from sources like stack overflow posts and man pages.
[00:01:56] So the model, it already knows how to use these commands and many more besides.
[00:02:03] I mean, we could just keep adding.
[00:02:04] Let's say we've got Git and then we've got Docker and then I could keep going on.
[00:02:10] It doesn't need a schema to tell it what flags to pass.
[00:02:14] That knowledge is baked in from the training.
[00:02:17] With MCP, every tool's schema gets loaded into the model's context window at the start of a conversation.
[00:02:27] And each one of those schema can cost hundreds of tokens.
[00:02:30] We're filling up a context window before the agent has even done anything useful.
[00:02:36] So, which side is right?
[00:02:38] Is MCP a useful abstraction tool or unnecessary context window filling bloat compared to the CLI?
[00:02:49] Let me show you two examples I carried out with an AI coding agent to illustrate the difference where the same operation was performed using CLI and MCP
[00:03:00] and you can try these very same exercises with the AI agent of your choice as well.
[00:03:06] So the first exercise is just simple file operations, so we've got a folder here with some markdown files
[00:03:12] and the agent has to do two things, it has to read one of the files notes.md And then it has to search both of them to try to find a specific word.
[00:03:23] Now I put in two separate requests to an AI coding agent, one requesting it use the CLI to do that task and the other requesting it use MCP.
[00:03:33] Now for the CL I approach, what happened was the agent ended up using two bash commands.
[00:03:41] So the first bash command it used was catnotes.md to dump the contents of a file to standard output.
[00:03:49] And then it used grep to search for the word agent across both Markdown files.
[00:03:56] Now, just a quick sidebar on these commands, if you're not a CLI person, cat, that's sure for concatenate.
[00:04:02] And here it's being used to print a single file and then grep that scans files line by line
[00:04:08] and spits out every line that matches the pattern and that minus N flag adds line numbers.
[00:04:14] So that's how the agent handled the CLI and it's worth pointing out the agent didn't need to look anything up to figure out which commands and flags to use.
[00:04:25] This was built into its training data.
[00:04:29] Now, when the agent adopted the MCP approach, it ended up using two tool calls from a particular MCP server called the file system server.
[00:04:47] Those two tools that it used from the MCP server
[00:04:49] were read file for reading from notes.md and then search files where we provided the string of the word that we wanted to search, which happened to be the word agent.
[00:05:05] Now, both approaches completed the task successfully and they both returned the same information, but the CLI commands, they were...
[00:05:13] They're a bit more compact and the model didn't need to know any schema to know that grep minus n was the right flag combination.
[00:05:22] Now the file system mcp server that advertises 13 tools, so I only actually used two.
[00:05:29] There were 11 more that weren't used and each one of those tools comes with a full JSON schema.
[00:05:36] That's a couple of thousand tokens of tool definitions loaded into the context window just so the agent could use two of them.
[00:05:45] So I think that is where some of the MCP is unnecessary complexity commentary kind of comes from, but honestly either would be fine in something this simple.
[00:05:56] It's when things scale up that the difference gets more notable.
[00:06:01] So let's think about something else.
[00:06:03] Let's think about Git, which is one of the most widely used developer tools on the planet.
[00:06:09] Now, an AI agent with Bash can run a bunch of Git commands,
[00:06:15] like it could run this command here to show the last 10 commits, and it could run Git status command to check the working tree.
[00:06:24] And the model knows Git cold, it knows the flags, it knows format strings, all from its training data.
[00:06:32] Now consider the MCP alternative, which this case, is the github mcp server.
[00:06:41] Now that...
[00:06:42] Doesn't ship 13 tools, that ships 80 different tools and every one of those tool definitions, the name, the description,
[00:06:51] the full JSON input schema with parameter types and descriptions,
[00:06:55] all of it, it gets injected into the model's context window at the start of the conversation
[00:07:01] and that adds up to approximately 55,000 tokens even if you only need one or two of those 80 tools and that.
[00:07:12] API pricing, those tokens are actual money.
[00:07:15] They eat directly into the context window space available for actual work
[00:07:19] and the model could have done those same Git operations with a couple of bash commands instead.
[00:07:26] So that is the CLI Camp's strongest argument.
[00:07:30] For local developer tools, MCP is paying a steep tax for knowledge the model already has.
[00:07:39] So is MCP Just dead weight.
[00:07:44] Well, let's try one more exercise.
[00:07:46] So this time, the task is to fetch a webpage at modelcontextprotocol.io and then just tell me what the main heading says plus a summary of the first few paragraphs.
[00:07:58] Now, first up was the...
[00:08:02] Approach and yes we're using MCP to fetch a page about MCP, a little meta.
[00:08:12] Now the agent used a single call to an MCP server and the server it used was called Fetcher.
[00:08:22] Now this is an MCP server built on a headless browser so it can render JavaScript and It made a single request using one tool that Fetcher has available.
[00:08:32] Which is just simply called fetch URL.
[00:08:36] And that had a link to the webpage, modelcontextprotocol.io.
[00:08:40] So the server launched a browser.
[00:08:42] It loaded this page, waited for it to render.
[00:08:45] It converted the result to readable text, and then it handed back the content.
[00:08:50] Now that used about 250 tokens and took but a couple of seconds.
[00:08:59] So that was MCP.
[00:09:02] The CLI approach started off good old simple curl, and this is where it gets painful.
[00:09:13] So the agent's first attempt was to use a curl minus s URL head minus 200 command,
[00:09:22] which is to fetch the raw HTML and just show the first 200 lines,
[00:09:26] but what came back was almost entirely JavaScript bundle code, because model context protocol dot is a next.js application.
[00:09:36] And the server doesn't send a finished HTML page.
[00:09:39] It sends a JavaScript application that builds the page in the browser and curl doesn't really run JavaScript.
[00:09:47] So all you end up getting is a skeleton and a pile of framework code.
[00:09:51] So at this point, the agent started improvising.
[00:09:55] It chained together text processing tools to try to strip the HTML tags and just filter out the JavaScript.
[00:10:03] That didn't work.
[00:10:05] So it tried to find page content embedded as JSON inside the source code that found fragments but it didn't find the full page.
[00:10:16] Then it wrote a Python script to reverse engineer the internal data format that Next.js uses to stream content to the browser.
[00:10:26] Reverse engineering a JavaScript's framework internals just to read a webpage.
[00:10:34] Now, when I ran this, it went through several more attempts before it finally got enough content to summarize the page.
[00:10:42] And it took several minutes and over 2,000 tokens, plus all that extra local processing on my poor laptop, all to get the same result.
[00:10:56] So what's the pattern here?
[00:10:58] Well, I think we can say that CLI, That wins when commands...
[00:11:05] Directly to jobs.
[00:11:06] So I'm thinking of jobs like file operations, like Git, like text processing and running scripts.
[00:11:12] Things where the command line has been solving the problem for decades and the model already knows the tools well.
[00:11:20] And also CLI tools they naturally compose with pipes
[00:11:23] so we can chain commands together in a single line which is something MCP can't do because each tool call is independent.
[00:11:33] But I think we can also make an argument for MCP.
[00:11:37] MCP wins when there is a gap between what the raw tool gives you and what you actually need, like my next.js web page example.
[00:11:48] And that extends to all sorts of other things as well.
[00:11:51] So for example, what about authentication?
[00:11:56] So authentication of Slack or Notion or databases?
[00:11:59] Well, with CLI...
[00:12:01] The agent is managing the OAuth tokens.
[00:12:04] It's looking up channel IDs.
[00:12:07] It's handling token refresh.
[00:12:09] Basically all of this stuff is quite manual.
[00:12:12] Now the AI agent is doing it, but it's still manually having to do so.
[00:12:18] Whereas MCP, the server, the MCP server takes care of all of that.
[00:12:23] So we could say this is actually server managed rather than the agent.
[00:12:29] Having to do it itself.
[00:12:30] The agent just says what it wants done.
[00:12:34] And I think also, if we look at this at an organization level, there are some differences as well.
[00:12:42] So MCP has some advantages here.
[00:12:44] When agents act on behalf of different employees, we might need per user access control.
[00:12:51] And we might need to not use share credentials.
[00:12:55] We, we may need audit trails.
[00:12:57] So we can actually track.
[00:12:59] What is being done.
[00:13:01] And those are hard things to bolt onto CLI after the fact, but MCP, that has it all built into the protocol.
[00:13:10] So MCP or CLI, you probably saw this coming, but the answer is to use both.
[00:13:19] The AI agent I tested uses both after all.
[00:13:22] It uses CLI and MCP side by side for differing tasks,
[00:13:27] CLI when the commands map to the job, mcp when the abstraction or the governance justifies it.
[00:13:36] The choice is up to the agent and the person prompting that agent
[00:13:41] and if the agent ever starts reverse engineering a javascript framework just to read a web page well that's a good sign it picked the wrong one

---
*RAW — not yet passed through D.R.D deconstruction. Do not integrate into department files.*
