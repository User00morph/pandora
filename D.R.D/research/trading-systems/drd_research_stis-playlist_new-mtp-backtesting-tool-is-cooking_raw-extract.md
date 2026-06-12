# RAW EXTRACT — New MTP Backtesting Tool is Cooking

- **Video ID:** y9nhEo_U-H0
- **Duration:** 13:31
- **Words:** ~2,170

---

[00:00:00] I currently owe my developer
[00:00:03] about $7,000 worth of software that I'm
[00:00:05] going to give to you for free. I've
[00:00:07] spent tens and tens of thousands of
[00:00:10] dollars on developer fees software in
[00:00:14] the last year and a half.
[00:00:16] And people ask why my stuff is so
[00:00:18] expensive at $1,500 a year. Like, it's
[00:00:21] so cheap. I've spent much more than you
[00:00:24] have to spend to get the same thing. A
[00:00:26] and I let people sell it, too. So miss
[00:00:30] me with that question. Anyways, let's
[00:00:32] get into it. So I'm still kind of
[00:00:35] playing around with this, but what it
[00:00:37] does is it lets me test a basket of
[00:00:40] assets. The S&P 500, Bitcoin, European
[00:00:44] stock market, gold, silver, NASDAQ, and
[00:00:46] Nikk225.
[00:00:48] I get to adjust the relative weights. I
[00:00:51] get to adjust the equity risked or the
[00:00:53] number of contracts
[00:00:56] and the strategy. I'm not going to give
[00:00:57] it all away, but here are the
[00:00:59] parameters. Stop loss, take profit,
[00:01:01] pyramid, breakout. There's a couple
[00:01:03] things I still want to add. It's going
[00:01:06] to let us optimize
[00:01:08] for a specific measure. Whether that's I
[00:01:12] like Calmar is uh equity is a max
[00:01:16] historical max return for per draw down.
[00:01:19] Basically, it looks at the max
[00:01:21] historical draw down and looks optimized
[00:01:23] for the best return. You can optimize
[00:01:25] for sharps, certino, cagr
[00:01:29] um the number of trials. So it it's
[00:01:31] going to run a bunch of back tests
[00:01:34] and then I can set it to optimize for a
[00:01:38] certain not optimize but take a median
[00:01:41] number of parameters and pick the best
[00:01:43] one in the middle. So let's try some
[00:01:45] things. Now I've set my date to 1965.
[00:01:48] The reason is gold wasn't really set
[00:01:51] free until around this time around 1970.
[00:01:54] So let's just start with this. Now if I
[00:01:57] want to optimize the parameters, I can
[00:01:59] just hit optimize. And you can see it's
[00:02:02] cued. There's 200 trials running
[00:02:06] calmar. And it's doing 200 back tests
[00:02:10] right now. And it's going to pick the
[00:02:12] best settings and it's going to spit it
[00:02:14] out. So there's a danger of overfitting.
[00:02:17] You guys understand? And one of the ways
[00:02:20] that we just reduced the danger of
[00:02:21] overfitting is it didn't pick the best
[00:02:23] out uh the best parameter. It found a
[00:02:26] range of the 20 best parameters and pick
[00:02:28] something right in the in the middle.
[00:02:31] We're also having data going back over
[00:02:34] 60 years. And another way that we're
[00:02:36] going to reduce optimization overfitting
[00:02:39] is by adding a bunch of uncorrelated
[00:02:41] assets and it trades all the assets
[00:02:44] exactly the same. So this is going to
[00:02:46] give us pretty robust and realistic back
[00:02:49] test of what we could potentially expect
[00:02:50] in the future. So here it will tell us
[00:02:54] for instance our stop loss is going to
[00:02:56] be almost 8 ATR. Our TP is going to be
[00:02:58] about 50. Um this this is how much
[00:03:04] I wonder what min pyramid means. I'm
[00:03:06] going to have to ask my developer on how
[00:03:08] old the breakout levels need to be. So
[00:03:11] right now we just have the S&P.
[00:03:13] So we can see our CAGR, Calmar,
[00:03:19] Sharp, and Sertino. And the Sharp's not
[00:03:22] very good, but it doesn't need to be to
[00:03:24] be a good system. I think it's sort of
[00:03:25] overrated.
[00:03:27] So just from the S&P right now, we have
[00:03:31] our average year is 10%. So this isn't
[00:03:34] really a big improvement over just buy
[00:03:36] and hold on the S&P 500, especially
[00:03:39] considering that we're going to be
[00:03:40] paying taxes on this. However, one thing
[00:03:43] we could do is simply risk more. So, I'm
[00:03:44] going to explain to you guys what risk
[00:03:46] premia is here. So, look, I'm going to
[00:03:48] do the exact same back test just with
[00:03:51] bigger size. What's going to happen now?
[00:03:55] Our average year is 35%. Our average
[00:03:57] winning year is 67%. Our average losing
[00:03:59] year is 29%.
[00:04:01] From draw down adjusted returns, this is
[00:04:04] not better than buy and hold. But it
[00:04:06] crushes buy and hold. Why? Simply
[00:04:08] because we tolerate a bigger draw down.
[00:04:11] Think about that
[00:04:13] here. Our max draw down was 78%.
[00:04:17] It's a lot more than the max draw down
[00:04:18] of just holding the S&P 500. So, it's
[00:04:21] difficult. A lot of people couldn't do
[00:04:23] that. But if we were to compound
[00:04:27] 35% a year,
[00:04:30] let's look at the uh we can go to decade
[00:04:33] on the decade view.
[00:04:38] How does this work? Decade.
[00:04:42] average decade would be about a 10x.
[00:04:46] Okay? So your 100,000 would be a million
[00:04:48] in 10 years and your million would be 10
[00:04:52] million. So in 20 years you could go
[00:04:54] from 100,000 to 10 million.
[00:05:00] Although
[00:05:07] you would have
[00:05:10] I'm kind of confused. All of these are
[00:05:12] showing winning decades,
[00:05:16] I guess.
[00:05:21] Yeah, I'm going to I'm going to converse
[00:05:23] with the the dev here right now.
[00:05:29] Okay.
[00:05:31] Why would this show a losing decade?
[00:05:34] Not showing
[00:05:37] losing decade. on the bar chart. Also,
[00:05:42] what is min pyramid mean? Okay, so let's
[00:05:47] add gold into the mix.
[00:05:51] There's other We're still going to add
[00:05:52] things by the way, but we're going to
[00:05:54] add gold. And then I'm going to optimize
[00:05:56] the parameters, okay,
[00:05:59] for the best return for whatever the
[00:06:02] maximum draw down is. So, it's running
[00:06:05] 200 trials and it's picking the
[00:06:09] parameters that are in the middle. Not
[00:06:10] the best parameters, but here we have
[00:06:13] stop loss of five, which is what we've
[00:06:15] been using in our group.
[00:06:18] And the stop loss ATR period of 102.
[00:06:20] We've been using 100. So, this doesn't
[00:06:23] really tell us that much actually. This
[00:06:24] is this is very close to this is very
[00:06:28] close to the settings that we've been
[00:06:29] using,
[00:06:32] but it's going to get helpful. So here
[00:06:34] we'll run the back test and notice by
[00:06:38] adding gold
[00:06:41] because of the uncorrelation the max
[00:06:43] draw down went from78 to 45%.
[00:06:47] Okay. Now let's go back to period
[00:06:49] returns. I'm only interested in decade
[00:06:52] and and year. If we go down to the
[00:06:55] daily, if we go down to the daily, it's
[00:06:58] just noise. 34% winning days, 29% losing
[00:07:02] days. Average winning days a little bit
[00:07:04] bigger. If you're trying to day trade
[00:07:06] consistently, this isn't for you and and
[00:07:09] it's very hard to do that. So, here we
[00:07:11] have weeks. We win more weeks than we
[00:07:13] lose. Now, we're starting to see edge
[00:07:15] once we go on the weekly. All right,
[00:07:17] let's go to month. Now, we're at 46% of
[00:07:21] months win, 34% lose. Average winning
[00:07:24] month is 8%, average losing month is
[00:07:25] ne5. Starting to look pretty good,
[00:07:27] right? Go to quarter.
[00:07:31] We win more quarters than we lose. The
[00:07:32] average winning quarter is much bigger.
[00:07:34] Now we go to the year. Okay. So here
[00:07:36] average year is 30% still. So we didn't
[00:07:40] really improve that but we did it on a
[00:07:42] much smaller draw down. Right? Average
[00:07:45] losing year 13%. And we got our winning
[00:07:47] years to 68%. So this is starting to
[00:07:49] look pretty good. Now in the decade it's
[00:07:52] one every decade. The average decade is
[00:07:56] a 10x and that could be increased. Once
[00:07:59] again, we could just increase the equity
[00:08:02] risk premia is the fundamental here.
[00:08:04] Okay. So now I'm just going to start
[00:08:07] adding more stuff. I'm going to add
[00:08:08] Bitcoin.
[00:08:10] I'm just going to add everything and
[00:08:11] kind of see. So I'm adding the the
[00:08:13] European stock market,
[00:08:15] NASDAQ, the Japanese stock market, and
[00:08:19] silver. So we're going to go parameter
[00:08:21] optimization.
[00:08:25] We can't, it's not set up to optimize
[00:08:29] um
[00:08:31] for equity
[00:08:34] yet
[00:08:36] or relative weight. So that's something
[00:08:37] we're going to come into. So here that
[00:08:40] actually changes stop-loss ATR multiple
[00:08:42] quite a bit. Something that notice I
[00:08:44] haven't even looked at the trade win
[00:08:45] rate. We have trade data. We can get
[00:08:47] into that.
[00:08:50] So interesting here. It's saying
[00:08:53] Max draw down on isgative8%.
[00:08:56] So I have a question about how this
[00:08:58] works.
[00:09:00] Um let's look.
[00:09:07] I think what happens
[00:09:11] is it splits the 100 up between all of
[00:09:13] these. I'm not sure. So let's let's
[00:09:15] change this to 200.
[00:09:18] I'm just going to increase the size and
[00:09:20] see.
[00:09:23] Okay, I see.
[00:09:26] So 500 implies leverage, right? So let's
[00:09:29] put it 500 C. So now we're seeing
[00:09:36] 77% winning years. So this starts to
[00:09:39] become a lot more comfortable to hold,
[00:09:41] right? Because you can make a ton of
[00:09:44] money. I'm going to jack this up even
[00:09:45] more. You can make a ton of money not
[00:09:47] lose like having a lot of losing years
[00:09:50] but it's uncomfortable.
[00:09:52] So this is quite good. So here let's
[00:09:55] look at period returns. Now we're at 73%
[00:09:57] winning years.
[00:10:00] We basically kept the average year the
[00:10:02] same but we have a higher sharp right
[00:10:09] essentially and our draw down is
[00:10:11] relatively the same. So let's go look at
[00:10:13] trade data.
[00:10:16] trades.
[00:10:17] So, it only has a 50% win rate.
[00:10:21] The 2452 trades, that's a sufficiently
[00:10:24] big sample.
[00:10:27] Average win, average loss, profit
[00:10:29] factor.
[00:10:31] Okay. So,
[00:10:38] um,
[00:10:42] yeah, this tells me a lot. Now, we could
[00:10:44] go in here and I would like to increase
[00:10:46] gold position size and I would like to
[00:10:50] reduce silver's position size. Why?
[00:10:51] Because it's just a good asset and it's
[00:10:53] relatively uncorrelated. So, I'm going
[00:10:55] to run the same equity size and see how
[00:10:57] this might change things.
[00:11:02] 77% winning years.
[00:11:05] This didn't really make much of a
[00:11:07] difference. Let's let's increase Bitcoin
[00:11:09] and see what happens. So, I'm I'm kind
[00:11:12] of interested for optimizing for
[00:11:18] that increased percentage of winning
[00:11:19] years and that actually made quite a big
[00:11:21] difference.
[00:11:24] Um, okay.
[00:11:28] Yeah, I mean this looks really good
[00:11:29] honestly at this point
[00:11:32] on a decade.
[00:11:35] Let's go back to the decade. So now
[00:11:38] we're at 5,000
[00:11:40] which is would be a 50x, right? So now
[00:11:43] your 100,000 turns to 5 million. Your 5
[00:11:46] million turns into
[00:11:51] um
[00:11:54] 250 million. Is that right? In 20 years,
[00:11:56] this would be 250 million.
[00:11:59] That said, you would need to sit through
[00:12:02] a 50% draw down at some point, and you
[00:12:04] would also be
[00:12:06] uh you would also be um
[00:12:11] paying taxes along the way. So, you
[00:12:13] wouldn't actually get a return quite
[00:12:14] like this. But now here we have trade
[00:12:17] data
[00:12:22] 50% win rate but the wins are twice as
[00:12:26] big as the losses. And again, to me, one
[00:12:31] of the things that I really like about
[00:12:34] this system is since it's based around
[00:12:36] getting paid for risk premia, which is
[00:12:39] compensation for taking risk, and it's
[00:12:42] not based around statistical arbitrage,
[00:12:44] something weird. And again, this is a
[00:12:48] optimized in a specific way. It's
[00:12:50] optimized to pick the most general
[00:12:52] parameter that works across a bunch of
[00:12:55] assets going back 60 years. So it's it's
[00:12:58] not optimized in the way it's like it's
[00:13:00] like extremely generalized, right?
[00:13:04] It's very likely to continue to work.
[00:13:06] Now adding new assets over time of I
[00:13:10] don't know the South Korean stock market
[00:13:12] or maybe Indian stock market or Africa
[00:13:14] emerges could be quite interesting. But
[00:13:18] um yeah, anyways, if you're interested,
[00:13:21] there's a link down below and I will
[00:13:25] uh uh can send you more info. So, just
[00:13:27] fill out that link and I'll hook you