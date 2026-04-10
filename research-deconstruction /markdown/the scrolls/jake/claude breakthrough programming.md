Tab 1
## What this video covers
Hi everyone. In this video, we're going
to dive into my concepts around folder
as a workspace and architecture, what it
means to use AI in a way that will
actually probably last the next decade,
and what I think the industry is
actually moving towards.
Now, if you've seen any of my other
videos, I'm sure you've seen screenshots
or snippets of crazy folder structure
I'm doing where I'm routing Claude to
different folders, my markdown files,
using skills at certain times, creating
animations or code with it. I have all
sorts of different ways I'm doing it,
but I don't think I have a video out
there that really dives into how I
structure it and teaching you to do
that. And I decided to go ahead and
create a kind of template folder to walk
you through all of this. This is
something you could use to be able to
apply to any of your workflows, build
through it, understand it, and kind of
explore, you know, building your own
version of this. Now, throughout this
video, I'm actually going to teach some
concepts along the way for people who
are not familiar with maybe VS Code,
which is the workspace I'm working in.
Don't worry, you don't need VS Code to
do the things I'm showing you. You can
do it within claude, but I just want to
describe like what markdown is, what it
means to have an IDE, all of these
things. And if you are familiar with
## The problem with how most people use AI
these, you're a software engineer, you
probably are. Don't worry, I'm still
going to be diving into the specifics,
and I think you're going to get a lot of
out of this either way. However,
sometimes it's also nice to just dive
back into the fundamentals. So, let me
paint a little scene for you. Right now
most people if they are even using AI
which fun fact about 84% of the nation
is still not fully using it but log in
and use claude or chatt or Gemini and
they're typing things they're diving in
um maybe they get something back they
start another conversation start over
and sometimes they're able to share
context between conversations right like
chat GPT and claude can do that I can
say you know tell me a software stack
for Vigilor which is a software that I
was working on for another company and
it's able to go and look through our
older conversations, which is nice.
That's a little bit of extra there, but
it's still not, you know, it's not able
to look at files, have persistence,
things like that, and you're constantly
having to make these huge prompts. Maybe
you have some sort of prompts that you
save and throw in or documents, and
you're throwing it in, and then you have
to start a new conversation, throw it
in, start a new conversation, you hit a
wall, there's too many tokens, right?
All sorts of problems there. And don't
get me wrong, there's some really good
prompt engineering techniques out there.
But at the end of the day, AI can only
hold so much in a single information or
chat area. And even further, that's not
your workflow. Having to have it create
a whole bunch of stuff and then re-edit
it again, it's it's not sustainable.
It's not scalable. Now, for those of you
who don't understand why they struggle
so much, essentially AI reads
everything, all of your sentence, and
measures it by something called tokens.
A token is roughly three quarters of a
word or a single word. Sometimes the
word hamburger could be three tokens.
Hamburger. Hamburger. The term comes
from NLP research in the '9s. A bunch of
researchers needed a unit smaller than a
word because language doesn't all break
the same way, right? So, they borrowed
token from linguistics, which borrowed
it from old English taken, which means a
sign or a symbol. A token is just the
smallest meaningful chunk of a sentence
or a word. There's only so much tokens
an AI can have in its context window
## What tokens are and why context windows matter
before it starts failing. When people
say context window, they mean how many
tokens the AI can see at once. And that
window is in fact finite. So if you dump
everything into one file, an AI writing
a blog post is also reading your video
production notes. You're burning tokens
on stuff that doesn't matter. So instead
of building one big file, you want to
separate your thoughts, your ideas, your
work into separate areas. This is
something I created for all of us. It's
called a workspace blueprint. Here you
have three workspaces. And again, this
is an example. You don't always have to
do this, but each one handles a
different kind of work. One for the
community, right? Maybe I have this one
for working on content and docs in the
community production, right? What am I
building? Where are scripts? Maybe I'm
creating animations. Writing room, maybe
I need to have some sort of process of
thinking or I have a client list or
insert as many things as I have there.
And we're going to dive deeper into it.
This is a space that does the job well
because you can circumn and AI seeing
everything and only direct it to what
you want. Let me explain how that
actually works though. So, I'm going to
show you inside of VS Code, which is an
IDE, basically a developer environment
that allows people to kind of look at
folders in a different way. Okay. So,
instead of having to click into the
folders like you just saw here, I can
just open the folders and see everything
and open the files without having to
doubleclick the files, right? So,
instead of having to doubleclick this
text document and opens another window,
I can just bounce between them. It's
much cleaner, much easier. Even if
you're not into code, it looks
overwhelming. I promise you, all of this
is just natural language. This literally
reads like a document. So, this is a
Markdown file. If you haven't seen them
before, markdown is just a text file
with some lightweight formatting, right?
You have dashes for bullets. You have
hashtags or pound symbols, if everyone
else remembers when they were just
called that, for headers. Um, you have
all sorts of stuff like asterisks for
bolding or doing things in that way. And
there's a lot of programs that can
actually run this to look a certain way.
In fact, your claude does exactly that.
If you look when you're talking to an
AI, it's writing in markdown already.
These boldings, these lines, all of
these things. Watch what happens when I
## The workspace blueprint: three workspaces for three kinds of work
copy this. All of that formatting
disappears when I paste it into here.
And it turns into markdown because
that's how it's making it look like
that. Markdown is just a good way to
format text. If you're curious, there's
a man named John Gruber. He actually
created this in 2004. The whole idea was
write something that's readable as plain
text but can also render into a
formatted document. He named it markdown
as a play on markup language which is
the same stuff that HTML right the stuff
that builds websites uh hypertext
markdown language and all it does is
mark stuff down with tags. Markdown
strips all the tags and absurdity away
and makes it look like something simple
like this. But again, you're probably
not here for this. you're here for the
file system. So let's move on to that
next step. So in this specific folder,
which is an example, it runs on
essentially three layers. And there's a
reason for each one. If you look at my
clawed MD, my clawed markdown file, this
is something that my AI will read every
time it's in any one of these folders.
So this is something that the AI will
always have and always reads. Imagine
it's you're just copying and pasting
this into claude code or into claude
## What VS Code is and why I use it (you dont have to)
every time you open it. Now you can
actually just type in to claude read the
claw.md. In this case it's claude code.
You could be working inside of claude
co-work as well which is again a video I
have on how to install and it can
operate inside of folders in case the VS
code is too much for you. Um but just
read the cloud imd and tell me what this
is. Before you had to copy and paste do
all these things. it had to read the
entire every file that's in here. In
this case, it reads the cloud.md and
immediately without having to read
everything else understands the product,
the process, what's going on, my writing
room, my production, my community. It
knows where to find it, what the file
names are, all from just a single text
prompt that allows it to understand
where to go, what to do, what are these
areas. But let me describe this a little
simpler for those of you who might, you
know, feel like this is a bit
overwhelming. Layer one in this is the
map. This is what loads automatically,
right? It's looking at it. So, you put
the stuff the agent always needs to
think about. Folder structure, naming
conventions, where files go. Think of
this as the floor plan. You walk into
any room, the floor plan is on the wall,
and the agent knows where to go. Now
layer two is where the floor pan tells
you to go. It's the actual rooms. What
is your task? Go here. I want to write a
blog post. Well, then you need to go to
## Markdown explained: what it is, where it came from, why it matters
here and read this context or this
markdown file. If you want to build a
demo or a video, you need to go here and
read this context or markdown file. And
this could be one that you wrote by hand
or it could be one that you told Claude
to wrote. And we're going to dive into
that here shortly. Layer three is the
actual workspace itself. Where do you
want your files going? What content are
you doing? If you're writing stuff,
where do you want the events to be?
Where do you want newsletters to be?
Where do you want social to be? And it's
just a file system. Again, if you don't
want to work inside of here, you can
actually just go straight into the
folder and just create new folders. New
text document. That can be a prompt,
that can be a context, right? It's that
simple. And you can just you can just
edit it without any of this. Look, my uh
my claw.md this is what it looks like in
if you open up Notepad. Same thing. And
nothing breaks when you edit it. You can
type whatever you want in here. It's
just English. Now, it's good to have it
uniform and well, but that's the idea
here. Most people are only doing one of
these layers, maybe two. The reason you
want to actually have these three layers
is it stops the narrow funnel of AI
doing too much all at once without
allowing you to edit every single part
but still give you the ability to
automate the entire process. So again,
the router, the initial claw MD or
whatever you're naming it is loaded when
you start any task. The workspace is
loaded when you're in the workspace.
When you want to do production, it's
only reading stuff that's in production
as it needs to. When you're doing stuff
in the writing room, it's only writing
it when you're in the writing room. For
example, go to writing room. Let's start
making something. Very little prompting,
almost terrible prompting. Yet, the
agent without wasting a whole bunch of
tokens and going through everything
immediately goes to the context file
that I have in writing room that
describes what it is. describes what to
load and what not to load and just
describes the folder structure and what
the process is. First I understand the
topic, then I find the angle, then I
write it, then I catch problems. You can
also incorporate skills into this,
## The CLAUDE.md file: the first thing every AI reads
right? So you can download the humanizer
skill which is an actual GitHub I
recommend you all check out or like doc
co-authoring skill which is another set
of markdown files or even Python scripts
and tutorials that someone else build to
do a certain task. And this is where
this whole process is different than
just running skills. You're putting
skills inside of a thought process. And
as you can see right here, we're in the
writing room. Clean slate, no drafts in
progress. Voice is loaded. Style is blog
post. What do you want me to make? From
one single prompt, we've gotten it in
there. But while that's going on, I can
open up another cloud and I can say,
"Hey, I want to do some work in
production." And it's going to go in
there and I can do whatever work I want
to do in production, right? I want to
maybe make some designs. I want to
create some sort of code for workflows
in there. But the real fun happens is
when you're building stuff in production
with one of your cloud code instances,
you're writing a script and you can say,
"Hey, take the script from writing room
and let's make an animation out of it in
production." It's moving that file. It's
going to go there. Now, it's going to
notice that I don't have any scripts in
there when I send this out. But if I did
have a final in there, it's going to go
look for it, right? There's no scripts.
Boom. It didn't waste a whole bunch of
tokens. It didn't do anything, but it
immediately knew, oh, well, we have to
write a script first. Or if you have a
script somewhere else, you can upload
it. You see, most apps or frameworks or
aantic things require you to build an
agent for each of these. I need a
writing room agent. I need this agent. I
need this agent. But the way in which
you approach each task is always
different. Why not just have Claude code
become the agent you need when you're
working in the workspace? And you see
## The three layer routing system explained
from there you get the most important
part of this process is just good
routing in English language. Again, this
is all just English, right? File, folder
names, titles. It's describing what you
want, right? This right here is the most
important pattern in the whole system.
It's just a simple table that tells the
AI, "For this task, read these files.
Skip those files. You might need these
skills." Without this, the AI either
reads everything and runs out of the
room and just does all sorts of stuff
you don't want it to do using way too
many tokens, or it guesses wrong about
what matters or just doesn't hit what
you need, or you can't edit what it
creates along the process. This table
eliminates all of those problems. This
this system here gets rid of all of
that. Now, let's go ahead and zoom in a
little bit here and actually really look
at this kind of folder structure. Walk
through this pipeline. Imagine you're
sitting here and you open up production
and you go to workflows, right? So, you
know, you're doing some sort of
animation production or insert whatever
it is that this folder is as a separate
workspace as part of a larger task flow
that you're doing. Production has a
pipeline in itself as well. Four stages.
You have to do a brief. You need a spec,
which a specification, a build, and an
output. I have a brief, some sort of
script that I want to do. I have a spec
that's generated from that brief, and
then it goes into the builds and it
builds out the animations. And then
finally, you have the output. More
## Layer 1: Top level identity and navigation
importantly, this allows me to have one
MD file, right? So for my production, I
can have a context for this file system
that is generating different types of
sub aents or ways to look at it. Again,
I'm not even worried about agents. I'm
just worried about what the workspace
is, what I want to do in these
workspace. If I want to understand, look
up technical standards, look up design
rules, I can find that because I might
have that in a doc, right? So, I have
components or maybe some way I like to
design these systems with my color
designs, my headers, my quality. And
again, these are all just generated from
English, super short docs. These are
visual philosophy or what type of tech
you want to use. And it doesn't always
have to read that, but maybe during the
brief stage, it does. Right? When you're
sitting there and you're going through
and you're loading the brief, well, I
need to make sure you look at this text
standards when you're making the brief.
If it's loading the spec, I need to make
sure it looks at the design system and
our component library. And then maybe it
does need to load the deck as well. And
you can swap this around super easily
just by looking at it. This is
traditional function calling software
routing. This has existed for decades
and decades. But now it gets to be
natural language, English. Now, at this
point, many of you are like, "Oh, well,
you're just making a bunch of skills."
Technically, yes. Now, for those of you
who don't know what skills are, again, I
mentioned them earlier. I I talked about
this idea that you can download them
from everywhere. There's PowerPoint
skills and I have other um videos on
this, but at the end of the day, skills
## Layer 2: Workspace level context files
are a process that someone else figured
out and designed a set of packages or
folders just like I'm doing here to tell
Claude how to do something. Thing is,
skills aren't just markdown files with
instructions. Some are just that, but
skills work best when they're wired into
a system. One important note too is this
is where the difference between it's
just skills we're creating here and it's
a system. You're actually putting skills
inside of your MD. So in this case I
have in my context for production I have
the fire outlook what I want to do but
also right this is where you can call to
call skills or MCP servers. If you don't
know what an MCP, it's model context
protocol. I think that deserves an
entire video in itself, but just think
of it as a way that the AI can talk to
other apps and services easier. It's
designed to just kind of plug and play
it in rather than you have to create all
these custom integrations. At certain
points, we might want the front-end
design skill or a web app testing skill
or a PDF skill. Or I might want to give
Claude the opportunity to look up a
skill, find a new skill, or even
possibly create one. You can wire up to
15 skills, 20 skills, 100 skills into a
workspace, or you can perfectly add the
skills where you would need them inside
the workspace rather than having them
loaded at all times. That's the whole
## Layer 3: Skills, MCP servers, and plug and play tools
idea here is about plugandplay and
routing. One other sneaky thing I do to
like completely ignore like databases or
anything like that in my claude MD the
main file at the beginning that shows
you know every AI or every agent that
comes into this workspace can see my
entire folder structure and navigation I
just add naming conventions right so if
a file is going to be outputed a certain
way it needs to name it for blog drafts
it needs to be like file name where it's
at is it draft is it v2 is it v3 example
API off guide draft, right? Or same for
newsletters. Here's the year and day and
then here's what it's kind of is, right?
2026 03 launch week MD. So the AI knows
to organize and move stuff which comes
in handy when instead of having to
navigate through these files or have an
agent that's connected to some sort of
you know SQL database or vector database
or query or Postgress or anything like
that. I could just say hey pull
my uh O demo
demo v2 and build a spec from it. It
immediately knows without me doing
anything to look where that v2 demo
script would be because it knows how to
find it. It knows to pull it. Then it
knows to read the docs associated with
specs and then start building it. I have
zero code technically speaking running
any sort of Python injection or
framework or database. This is tools
that people are building right now.
They're building apps and crazy Python
stuff which in some very bespoke cases
might be useful but most of the time for
most people you don't need all that
extra stuff to get the process and the
job done. The job to be done is more
important than this kind of rigid
architecture that so many people are
building. You see the folder becomes
your app. This is your UI. What's
## Naming conventions that replace databases
simpler UI than a folder? And the best
part is I don't even need to technically
click on anything. I could just talk
with my voice to AI, have it do all the
text work for me. The next stage of
this, I promise you, within six months,
everyone's going to be doing this, is
just talking to your folder setup. It's
going to be designed and set up to be
this way. It's going to be around yours,
which leads into a good final point. How
do you make this yours? This template
uses a fake idea with fake process,
right? Fake blog posts and demos. If
you're a content creator, writing room
might become your script lab. Production
becomes your edit bay. Uh whatever
community becomes a distribution hub.
And you're going to remove and change
these rules to edit your platform. Maybe
your tone and voice inside of these,
right? So what is your audience? That's
what you want to hear. It's working
developers, two to eight years of
experience, technical decision makers,
developer advocates. It might be
something completely different. You
might be in construction or real estate,
but this is roughly what you would be
doing across all of them. And the best
part is all you need is one subscription
to Claude Code and you can generate a
hundred quote unquote apps that are just
folders creating what you need.
Obviously, it's much more complicated
once you get into breaking down your
workflow. But if you're a developer, if
you're a freelancer, right, just swap
## How to make this yours: content creators, freelancers, developers
design for engineering and docs or
intake and production and delivery,
right? This workspace changes lightly.
But the three layer routing system, the
idea that you go from, hey, look at this
area. This is what you're going to to
lower level context ones to lower level
skills is the idea here. It's just
layered. This isn't a prompt trick. This
isn't some sort of crazy infrastructure.
It's folders and markdown files with the
understanding of advanced software
engineering. Every conversation after
that, the AI knows where it is, what to
load, what tools to use, and where to
put the work in. Now, there is a lot of
history behind my thinking. I didn't
just randomly come up with this. And
there's a lot of people who are already
doing this. And the reason they're doing
this is because it works. I'm writing a
very large research paper right now that
goes into the history of programming,
rules of transparency, rules of
composition, um, all the way back down
to 1972 and then I'm bringing it forward
and applying all this stuff to modernday
AI, what it means to have humans in it.
And I specifically talk about the layers
that we could actually have. And I
actually go into a five layer
architecture in the paper, but
realistically, most of you just need to
understand the three main layers that we
talked about here. I will be making
videos on this. However, it is in the
main chat. Um, if you want to download
this and give it to Claude so that it
can tell you about it rather than having
to read through it, I highly recommend
## The research paper behind all of this
that. In fact, I urge you to do it
because some of this is kind of
technical information. I'm being nerdy.
I'm being structured in it. But this is
layering out what the next decade is
looking like. And this isn't because I'm
predicting the future. It's because I'm
learning from the past, from the last
200 years of software engineering. And I
mean 200 when I say that and applying it
to AI. I want to teach the concepts that
last, not the concepts that are replaced
next month. I understand that some of
this might be in a little fast. It might
be a little confusing. I'll keep making
deeper dives. Give me feedback on what
you didn't understand. How did I move
too fast? I want to make these better
every day. Again, I'm making these on my
own. So hopefully this all gave you a
good idea. If you do want access to any
of these files or worker templates, um I
am giving them already to my VIP and my
uh premium accounts. It's my one way of
like the work, right, to be able to
support this. So, if you're able to
## Where to get the template
subscribe, amazing. If it actually is
that much of a financial challenge,
please reach out to me. I can try to see
if I can get you something, you know,
quick and easy for you. Um but at the
end of the day, go go check it out. Go
check out all my other courses that I'll
be doing. And again, as always, happy
learning.

Tab 2
So, David had a great question. We were
kind of talking about, you know, making
animations with Claude Code and he uh,
you know, watched my initial video and
then also kind of set up some really
great animations himself, which I
absolutely love. Um, obviously there's
always more tweaking that you can do and
I'm creating videos on how to do that.
But he had this idea of creating a
front-end UI that allows him to control
Claude, right? Right now he's using VS
Code which is what I tell you know tell
people to install and it's a great place
to kind of use it but he wanted
something a little bit better that he
could like monitor or observe how the
agents are kind of working. Now the
problem is is whenever you're using
claude code or claude CLI is you can use
your subscription you can use your
entropic subscription so it doesn't cost
as much. If you did API calls for all of
this, it'd be really expensive. But with
a subscription, it's not as expensive.
But as soon as you're building a front
end, it's a lot easier quickly, or at
least you would think, to use, you know,
anthropic calls because then it's kind
of clunky to control Claude code through
your own front end. However, there are
ways to get around this. And so I went
and actually had Claude do a little bit
of digging to see what some open source
files are out there for. And there's
actually some really great open- source
repos that are already out there where
you can control claude uh through this
like kind of downloadable front end and
it can even track usage if you are using
the front end as well as this other one
where you're able to do it through your
mobile. Now there are ways to actually
control claude code remotely uh and I've
actually installed that where I use it
through my phone. So I'm going to make a
video on all of that. But I wanted to
make a quick video real quick on this
idea of like me actually researching it
and and processing like what it could
look like because I'm actually going to
go ahead and develop a front end
specifically for this where essentially
you can access it, but on top of that it
might be able to make kind of like a web
service for you or some sort of like um
uh like a web you're able to navigate
the folders not just like simple folders
like this which is how I currently do it
but maybe something like a mind map or
webnap. Um, and so I'm I actually told
Claude how, you know, hey, this is my
idea. Let's not reinvent the wheel.
Let's use what they're doing in these
open- source areas. Let's look at each
of those repos. But also, I used my own
build that I have personally on my
computer here, right? This is my
animation workflow, how I go from
scripts to animations. And there's a lot
here. And don't worry, I have a course
that's going to be breaking all of this
down in detail. But at the end of the
day, I wanted to share kind of my Claude
MD, right? because I give Claude the
same markdown file before I'm ever using
it, which shows the file structure,
shows all of this stuff. In this case
though, I'm working backwards. I'm
giving Claude my my structure, my file,
saying, "Hey, what if we made a front
end directly around this folder system
and around what I'm trying to do here
around my script design, around my areas
here, and uh kind of working with it on
this area." And so it's come up with
some really good ideas for the
architecture around it and understanding
it. So what I'm actually going to do is
I'm not going to have Claw build it in
the desktop. Sometimes I use the desktop
one just because it has, you know, a lot
of memory and it's easier to use. I'm
actually going to have it make a PRD
document. Now a PRD document is a
product requirements document, right?
PRD doc is really something useful. It's
used in software programming, things
like that. It describes what kind of
stacks you need, right? what your
integrations might be, what you're
trying to do, targeting, right? Things
like that. And Claude understands what
PRDs are. But I specifically say a PRD
make a PRD markdown of this for clawed
code as in it will read it that
describes what we are trying to do and
breaks down steps
and
structure for early phase to late phase,
right? So, just trying to get it to kind
of break it into steps rather than build
the whole thing at once. And what this
is going to do is it's going to give me
a document that then I can go in and
read and edit. Now, I have a background
in software, so it makes it easier for
me to know, oh, I don't really want to
use that software. Oh, it's being too
complicated there. But you can actually
feed this into another version of Claw
and have it act as that auditor. Uh, and
it can kind of redo it there, which is
really cool. So, immediately it's going
to do that. It's for this. It's I'm the
owner, right? Right? And it gives this
all descriptions. When this is done, I
can download it, drop it into my
workspace, and actually have it build
the front end inside of this workspace
just by simply opening up my my next
thing plot code and saying, "Hey, read
the PRD for the front and once I drop it
in here, it's immediately going to be
able to see that and move that in
there." So, pretty cool. Just wanted to
make a quick update video on this. Um,
I'll make a course on both of these very
# I'm Building a Custom Front End for Claude

Tab 3
## What I'm building and why
All right, I figured I would record my
work process. This is less of a lecture
video and more of just kind of almost
like a live stream. So, basically what
I'm thinking is I should make a front
end for this, but I don't want to make a
front end that calls Claude because then
we have to use API fees. I want to make
a front end that lets me navigate all of
my work here, right? Because I can take
scripts and I can take them and turn
them into, you know, full animations.
Um, and I want to be able to, you know,
have my workflow to create these
animations, but have it where it's much
more organized and cleaner. Kind of like
how there's a front end for when my
animations are done and I can look at
them and look through them. But, you
know, something a little bit cleaner
there. And I found a couple GitHub repos
that already do that. Cloud CLI, Cloud
Code Web, and Op code do similar things,
but they're not really doing everything
that I wanted. So, I went ahead and
created a large PRD, right? product
requirements document um that describes
it to Claude code so it always knows
where we are, right? Hey, here's the
repos that I was talking about. Here's
the stacks that those repos have. You
can have Claude create these PRDs for
you as well. Um and kind of like what I
liked about them, but what I wanted to
cut, right? We want to get rid of most
of the frontends on these other repos
because at the end of the day, I just I
don't know. I didn't I didn't I wasn't
vibing with them, I guess, is the
question. I don't uh which where's the
I'm sure I have it. Here we go. Yeah, I
just they weren't fitting what I wanted.
They didn't look I don't know. It just
this isn't my workflow. I'd rather just
sit and work inside of VS Code in the
folders instead of use these types of
friends. This one was okay, but I didn't
need all this crazy choice. I didn't
need Enthropic and all these things. I
wanted something for me in my area and
I'll make it modular later. But they had
a lot of really good ideas inside of
this as well as like the way they were
doing things. So that's kind of what uh
I was going to kind of build and look at
here. So the first thing I did is um I'm
inside this workspace because this has a
lot of the information and processes. So
I built a new folder that says front
end, right? And so that way, you know, I
have my my stuff is already all here
that I can reference later or I can have
Claude go running as context easier
without rather than me having to upload
it. Um, but I just dropped my PRD in
here and it went through and described
it. Right, here's what the workspace
looks like. I'm thinking this is a
pretty good architecture. Uh, I went
through and edited a little bit cuz I
have Claude generate a lot of this, but
I was thinking about, okay, I want a
workflow map as well. So, we create like
## The PRD and workspace setup
nodes and stuff and you know, have you
ever seen like mind maps and web maps
where you can look through? Well, I want
a similar thing, but in that thing be
able to edit these folders. So like I
start at script lab. I create a short
form script, right? And I get all these
different scripts. Then that moves into
my animation studio and my animation
studio creates all sorts of things and
processes, right? Uh and goes through a
workflow where I go into a spec and I
build that and then that turns into a
render which is then, you know,
something that I can actually uh you
know build so to speak um or look at the
animations from. And so that's something
I want to map visually rather than just
stare at, you know, a folder structure.
And this is great. It organizes it well,
but I think it could be even better. Um,
and so that's kind of what I want to do
with all of this. Maybe even have a
chat, right? Just a panel right there
that you see much similar to this. And
again, we're relying on Claude's code's
infrastructure. We're not creating a
separate app. We're not using anything
doing anything craziness. We're just
making something better, a better
interface for how I want to work with
claude code. Um, now we've got the idea
of a panel, right? So, it's like, okay,
I want to have maybe my workflow map on
the left, file editor in the middle, and
claude code on the right. And being able
to open multiple chats is going to be
super important there. Um, and being
able to collapse them. And again, this
is why it's important to do a PRD
because you can lay all this out and
edit it. If you didn't like this, you
don't want Claude to just run out and
start building stuff. you want it to be
right from the get-go and then it
expands on what you like. Um, so I'm
going to look at pipeline definitions.
I'm going to look at um kind of okay,
here is probably what has worked well in
the past. Here's the root path. So, this
is built off of my actual workflow here.
And this is a JavaScript. You don't
necessarily need to write it like this.
You could write it where it looks
something more like quad code, right?
like, hey, to write a script, I'm in
this folder. To learn script structure,
go to this folder. That's another way
you could do that. However, if we're
going to put it in a front end, we're
actually going to need some sort of
front end style image or or or code, uh,
you know, React or anything like that,
but JavaScript is a really common one
that everyone uses. And again, you can
ask Claw to build something like this.
And I'm going to be making um more
courses that dive deeper into what
JavaScript is, what Python is, like how
do you read this? But at the end of the
## Why existing repos didn't work
day, you'll start to learn that all
programming languages are roughly the
same. They have some sort of definition
and then they have a description for
that definition and then that
description and definition can be paired
with others which are then sent to other
descriptions and definitions so that you
can then look at stuff. It's the same
thing here, right? You have a folder and
in that folder you have definitions,
right? Right? So you have a description
of what is should be in there and then
you have things that work inside of that
folder. This is the same thing here but
written out programmatically.
Very simplifying a lot of this but
that's kind of the idea here. Um I'm
also giving the idea of like what I
want. I want to be able to click nodes.
I want to be able to click sub stuff. So
instead of me just clicking like this,
the same exact thing's happening, but
it's like a really pretty, you know,
visual design or something like that.
Um, and I'm gonna keep it clean and
minimal. Um,
matrix maybe. No, I don't know if I want
to add matrix. So, anything I add here
is what's going to be for I I want to
think more about my visual style,
honestly, but I think it's good where it
is. Um, and after that, it's just simple
things like that. Here's the steps that
I want you to take, right? Make sure
you're removing all these features. The
first thing we're going to do is
actually look at and clone these repos.
So, when I say clone a repo, that means
literally downloading someone else's
code or GitHub. And again, I'm making
videos on what GitHub is, what Git is as
well. Uh, so keep an eye out for those,
but someone already did a lot of work
and then they put it up on GitHub and
then I can come in and actually look at
it, see what their code is. So, my goal
is to actually download this, strip away
everything that I don't like uh of both
of these and kind of create something
from it, right? Don't reinvent the
wheel. Make a better wheel. Uh, clean up
the wheel. Make the wheel yours. And I'm
doing that through steps. And that's why
I have this here. The PRD is saying this
is what we need to do first before we
start building anything. Um, we're going
to add in O tokens and things like that,
which basically what this is doing is
## Workflow maps and the panel layout
it's just allowing it to connect to the
cloud CL2. Basically, someone had come
up with a really good session
persistence. So, if I sit here and see
all of this, I have persistence in here.
This is an extension for VS Code.
Someone had to build every single one of
these buttons in. So, we want to rebuild
some of these or just in this case take
them from someone else who's already
built them, right? Um, and the idea by
the end of that is have something like
that's clean there. Then we're going to
move into actually implementing the
front end. Then at the end, I'm actually
implementing the workflow because I
think that's going to be the hardest.
And at a certain point, Claude's going
to run out of tokens. I might even want
to start a whole other Claude process.
So, um, yeah, I'm going to go ahead and
nail that down and kind of work on it. I
already did partially do that, right?
So, I asked Claude, "Hey, read this PRD
and make sure you're up to speed on
everything." Um, and you understand it,
right? And it's like, cool, got it.
Here's the idea. I kind of liked it, but
I wanted to make sure that it understood
what I really wanted, right? I wanted to
clean and edit stuff. I want to have
control over files and routing. Uh,
other ones are annoying. I literally say
that. Um, I want to be able to automate
things, swap files around. I just want
to make sure you understand this. The
abstract goal isn't a prettier claw
front end. It's a control surface that I
can fluidly switch, right, between I'm
driving or Claude's driving. That's such
a good way to put it. I love that. Um,
and that's the idea, right? Is sometimes
I want to edit every individual file,
but sometimes I just want to automate
the whole thing, but trust that it's
automating it the way I want. Um, so I'm
gonna say that's perfect.
Let's go ahead and start. And um, in
this case, again, this version of Cloud
Code is really nice because it's using
my folders, my files, my text as these
prompts, right? These are essentially
just bunch of prompts that are being fed
into it. But in this case, I don't have
## I'm driving or Claude's driving
to write this out. It's actually
referencing that file. And it's a uh
almost it's not a stateless prompt. Um
when when I say stateless, right,
imagine your memory. You have something
that's in memory, right? You downloaded
it. It has a state on your computer.
It's sitting there and it's held well.
In this case, when you're sending
prompts to claude, as soon as you leave
that conversation or you start to the
next one, it's gone. It's stateless. It
doesn't have its original structure in
the same way. This makes a prompt exist
permanently. So, I can always reference
it. I can redo it. I can tell Claude to
check it out again. We can restart very
quickly. That's why it's nice having
markdown files because they don't take a
lot of memory, which is a really great
one. They take less tokens than a PDF or
a DOC file, and they're really easy for
AI to read. They are very uh well
trained to understand markdown styles.
And if I do want to do something with
this markdown file, I can actually
upload it to Google Docs or something
like that and it will turn all of these
into formatting. Like it'll bold these.
It'll make these bigger because that's
how markdown's designed to be. And
that's what I'm going to make my front
end work on. It's going to be allowing
me to use markdown in that way. So, I
think that's pretty cool. I'm going to
let this kind of rip through. As you can
see, it's currently Let me actually
explain this for for some of you who
aren't familiar with it. What's
happening is it's going to enter plan
mode and there's plan mode and then
there's execution mode. Um, usually it
## Claude Code plan mode and sub-agents
chooses on its own, but you can affect
it and change it right here. Uh, it's
going to go through and it's going to
plan what our plan is, which is really
good. This is what we want it to do
because now it's going to create
individual plans off of this. And if
you're using um 4.6, right? So, if I
type /model, I can switch model. Um, if
you're using 4.6 or the default, which
is usually 4.6, six, it actually also
creates something called sub agents
where it saves kind of time and says,
"Hey, let me send an agent to go study
the workspace. Let me send something
else other than this main one to save on
tokens to go study and fetch these
things." And as you can see, the tool is
going, "Oh, I need to do this. Let me
look at this. Let me understand how all
of this is structured." Right? Claude is
acting as the uh kind of what do you
call it? manager of these agents
automatically. Um, and then it's doing
some bash commands. So, a bash is
literally just right if I was to sit
here and open up a terminal and type
something in say like, oh, fine. Or if I
could even run claw again right here,
it's just doing a command of some sort.
So, in this case, it's doing a bash
command, which is just searching for,
hey, look for structure this, right?
This is where it's trying to find some
sort of file. Hey, we're going to script
lab. So, it's actually going through.
And this is why this is really
important. I did this conversation
inside of my actual workspace instead of
a separate folder. Because if I did it
in a separate folder, it wouldn't be
able to pull context from my actual
workflow, the things that's working. So,
as I'm building this front end, it's
able to reference the thing that we're
building the front end on, but only
referencing it when I tell it to. I'm
not saying, "Hey, go read everything
here." I'm saying, "Hey, there's certain
processes at certain steps. Go reference
parts of it." Right? It's all about
breaking it down and putting it into
control. And it's doing that a couple
different times here or there. It's
doing a web fetch. It immediately went
and it found um this JSON package for
the clawed code UI. Right? So, what this
is going to do is basically how is it
structured? How is it delivering it?
Let's pull that from these people who've
already done the hard work and actually
get that together. Um, which I think is
nice.
Uh, oops, wrong one. From there, let's
see. It's just doing a whole bunch of
web fetches. So, it's pulling individual
files rather than the entire repo
itself, which actually is better than
what I told it to do originally. Uh, so
that's pretty cool. Uh, originally I was
just going to say clone the repo, but it
## Why workspace context matters
makes a lot more sense for it just to
search through the repo and then only
download what we need or just straight
up copy and paste it. Now, it's sending
another agent to go implement another
part of it. Um, it looks like it's doing
a find command to look for some sort of
parts inside of it. Uh, let's see, Max.
Yep, it's trying to find certain parts
of the cloud code web app, the actual
aspect. And then it's going back and
looking. So, this is now onto the next
GitHub repo, the other one that I wanted
to pull from, and it's pulling for this.
And as you can see, if we had been using
Cloud before and I just gave basic
things, it kind of responds quickly. But
because we have an entire PRD that it's
following, right? And I said, "Hey, you
can go and do your thing, it's going to
go through and do all of this and it
might stop at certain points to ask for,
you know, help, but this is how you get
Claude to like work for a long time on
its own and kind of trust its outputs."
And of course, we can watch what it's
doing, uh, which is really nice. So, um,
I'll go ahead and post another video
here soon on kind of what we are doing
or what is actually being done. Um, this
is probably going to be thrown into
session two of one of these courses. I'm
kind of making these as I go and seeing
where they go. Uh, you shouldn't have
paid to see this. This should be free.
Uh, that's the paid ones. I want to be
more structured, have workbooks, be like
an actual college course, which I do
teach college courses. that's a real
thing uh as well. So, that's the other
side of this. If you're feeling rushed
or confused by anything I'm doing, don't
## Free vs paid content, what's coming next
worry. I'm going to break every little
concepts of these down into individual
courses for you to be able to really
catch up and understand. But for those
of you who already kind of understand
all of this, I wanted to show what I do
on a daily basis. This is something I I
work with every day. So, yeah, have a
wonderful time. See you everyone. or I
guess I'll update you on the next
session.
