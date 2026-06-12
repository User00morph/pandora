# RAW EXTRACT — MTP Backtesting Software Tutorial

- **Video ID:** -B3veSrnjGA
- **Duration:** 20:56
- **Words:** ~3,657

---

[00:00:00] All right, guys. This is my first
[00:00:02] tutorial of the new back testing tool
[00:00:04] for MTP. This is something you should
[00:00:07] definitely use and familiarize yourself
[00:00:08] with. This is much more powerful than
[00:00:12] the back testing we can do on Trading
[00:00:14] View. However, Trading View is still
[00:00:18] going to be useful for generating
[00:00:20] signals,
[00:00:22] seeing the signal on the chart, and
[00:00:24] sending alerts. But for back testing,
[00:00:26] this is really powerful. It's going to
[00:00:29] make back testing much more efficient
[00:00:31] and better at finding the optimized best
[00:00:34] parameters.
[00:00:35] It's also going to help us visualize and
[00:00:38] get data on a portfolio level. And this
[00:00:41] is the big reason why I commissioned
[00:00:42] this project. By the way, I'm spending a
[00:00:44] lot of money on this, but I think it'll
[00:00:46] pay back over the years. And please use
[00:00:49] it because I spent a lot of money so you
[00:00:52] didn't have to. Whatever you spent to
[00:00:53] access the software is very, very small
[00:00:55] compared to what I'm spending.
[00:00:59] But now we can see on a portfolio level.
[00:01:02] So um in the in the discord there's the
[00:01:05] uh the login credentials. So let me walk
[00:01:08] through essentially how it works. Now it
[00:01:12] allows us to choose a number of assets
[00:01:14] and we've just put in the biggest major
[00:01:17] ones. Uh S&P 500,
[00:01:20] the NASDAQ, the Japanese stock market,
[00:01:23] the European stock market, Bitcoin,
[00:01:25] gold, and silver. It lets us choose a
[00:01:27] start date. And you can see in here we
[00:01:31] have all our different parameters that
[00:01:32] we can choose from.
[00:01:35] Now, there's two ways you can use it.
[00:01:37] One is you can get optimized settings
[00:01:39] for the S&P 500, optimized settings for
[00:01:42] Bitcoin, optimized settings for gold.
[00:01:45] You can do that. But where I think it's
[00:01:47] more valuable is creating generalized
[00:01:50] settings that work on all of the assets.
[00:01:53] And maybe we just stick with those. This
[00:01:55] is a philosophical decision. If you
[00:01:57] learn about trading systems, you have to
[00:02:00] be wary of overfitting, which is when
[00:02:02] you your
[00:02:05] trading system is so close to exactly
[00:02:08] what happened in the past that it's
[00:02:09] unlikely to repeat in the future. And
[00:02:12] this allows us for the first time, we
[00:02:14] couldn't do this on Trading View, to
[00:02:16] create the best generalized settings
[00:02:19] that worked the same on all of these.
[00:02:21] So, I'm going to show you an example of
[00:02:23] how to do that and kind of walk you
[00:02:25] through. So, first I'm just going to I
[00:02:28] want to I want to date on the portfolio
[00:02:29] level. So, let's go ahead and put on um
[00:02:33] all of these different assets. Now, for
[00:02:36] the start date, I'm going to choose
[00:02:37] 1965. Why am I choosing 1965?
[00:02:42] Gold didn't really move before 1965.
[00:02:45] It was fixed to the dollar. It started
[00:02:47] to move a couple years later, but the
[00:02:50] period from say 1920 to 1965 is just the
[00:02:52] S&P 500. And we're trying to get an idea
[00:02:55] with gold and NASDAQ and silver and all
[00:02:58] these things. So I recommend starting
[00:02:59] around this time. Now for risk, you can
[00:03:03] choose a certain amount of capital to
[00:03:04] start with. Um just like on trading
[00:03:07] view, you can start with a percentage of
[00:03:08] equity or you can do fixed units, which
[00:03:10] is like contracts. Um percentage of
[00:03:13] equity or number of units. Now,
[00:03:16] strategy, we're going to come back to
[00:03:18] this because you're going to see it's
[00:03:20] going to automatically come up with the
[00:03:22] best most generalized settings. So, for
[00:03:24] optimization, we can optimize for a
[00:03:27] number of things. Sharp is like a smooth
[00:03:29] return. Sortino is related. I like
[00:03:32] Kalmar. Kelmar is basically the biggest
[00:03:36] return relative to the uh maximum draw
[00:03:38] down. KMAR is how do we make the most
[00:03:41] possible money regardless of the path
[00:03:45] sharp cares about was it a smooth path
[00:03:47] to make the money. I don't care. I just
[00:03:48] want to make money.
[00:03:50] I'm actually not sure what multivariant
[00:03:52] means. I'm going to need to ask. So when
[00:03:55] we go to parameter optimization, which I
[00:03:57] know it's the word optimization, but
[00:03:58] it's optimizing something that works
[00:04:00] generally on all these settings, right?
[00:04:02] or for all these assets, it's going to
[00:04:05] do
[00:04:06] n number of back tests. So we could pick
[00:04:11] 200, we could pick any number. It's
[00:04:12] going to do this many back tests and
[00:04:14] it's going to pick the best one.
[00:04:17] Now another way to prevent overfitting
[00:04:20] is rather than just pick the best
[00:04:22] parameter, I wanted to identify a range
[00:04:25] of 20 parameters, this is the number
[00:04:27] here that work and pick something in the
[00:04:29] middle. So the idea is if the stop loss
[00:04:33] works from
[00:04:35] three to 10, I wanted to pick six which
[00:04:39] is in the middle. So that way it's more
[00:04:42] likely even if three was the best
[00:04:44] possible one. If two was unprofitable,
[00:04:45] we don't want to do that, right? So now
[00:04:48] that we have our assets and the date set
[00:04:50] and our goal, we're optimizing for calm.
[00:04:53] We're going to do 200 back tests. and I
[00:04:55] wanted to do pick the 20 best parameters
[00:04:58] for each and pick the one in the middle.
[00:05:00] Um,
[00:05:02] we're going to hit optimize. Okay, so
[00:05:06] it's going to do this
[00:05:08] pretty quickly here.
[00:05:11] Okay, 20% done. So, it's going to be
[00:05:13] done in about 15 seconds. And what it's
[00:05:16] doing is it's running 200 back tests
[00:05:18] right now.
[00:05:21] And so it's picking these for our
[00:05:24] particular uh settings. It's picking
[00:05:27] these as the best parameters. And you
[00:05:30] can see now it filled that out on the
[00:05:31] left side. So we can take that into the
[00:05:33] back test. So it's saying a stop loss of
[00:05:36] seven, a TP of 49.
[00:05:39] Um look back for the stop loss 293 days.
[00:05:42] TP looking back 16 days.
[00:05:46] Pyramid of five. So min pyramid is
[00:05:49] interesting. This is a concept that's
[00:05:51] important which isn't on the trading
[00:05:53] view one yet. I might add it. But if you
[00:05:56] have min pyramid set to three, it
[00:05:58] doesn't take the first two trades.
[00:06:02] And this helps you because any bad asset
[00:06:05] can still make an occasional breakout,
[00:06:07] but only the best assets can get into a
[00:06:09] third breakout, right? So that protects
[00:06:11] you. And I think min pyramid would be
[00:06:13] useful if we were trading weak assets,
[00:06:15] but since we only trade the best, it
[00:06:16] doesn't matter as much. It's got the
[00:06:19] look back age. Um, I'll be updating
[00:06:21] this, but it's going to have uh
[00:06:23] conditional close. It's going to have
[00:06:26] moving average, stuff like that. We're
[00:06:27] going to add it. So, I'm going to hit
[00:06:29] walk forward optimize, too, and see how
[00:06:32] this changes things. What walk forward
[00:06:35] optimization does is
[00:06:38] it basically is testing a 10-year block
[00:06:41] at a time and then seeing how it
[00:06:44] performs.
[00:06:46] Basically, it's splitting the back test
[00:06:48] up into different uh regimes. So, the
[00:06:52] idea is it's going to help create
[00:06:55] I don't fully understand it if I'm being
[00:06:56] honest. I mean, I'm
[00:06:59] I'm like you. I'm kind of a normie. I
[00:07:01] didn't code this. I commissioned the
[00:07:02] code. But the developer thinks walk
[00:07:05] forward optimization is maybe the most
[00:07:07] important thing to prevent overfitting
[00:07:09] because it lets you create a system and
[00:07:12] then test on uh new data
[00:07:16] uh which wasn't seen. So okay so here we
[00:07:19] can see for instance let's look at max
[00:07:22] pyramid in the 1980s 10 pyramid was the
[00:07:25] best
[00:07:26] in the
[00:07:29] 2010s
[00:07:31] four pyramid was the best so it's going
[00:07:32] to pick something in between right so
[00:07:35] there was a time in the 1990s when a
[00:07:37] minimum pyramid of three was superior
[00:07:40] okay so this gives us some more
[00:07:42] information but anyways it's time to run
[00:07:44] the back test because the parameter
[00:07:47] optimization gave us the best settings
[00:07:49] for this particular.
[00:07:52] So now we can also Oh, there's one other
[00:07:55] thing. Relative weights. So I might say
[00:07:58] I want to run a bigger portion of gold
[00:08:03] and a little bit less NASDAQ
[00:08:06] to balance it a little bit more. And I
[00:08:08] want more Bitcoin. So I'm going to go
[00:08:10] back into parameter optimization.
[00:08:13] Oops. Now I'm going to go to parameter
[00:08:14] optimization and I'm going to optimize
[00:08:16] again. So it it can optimize based on
[00:08:19] relative weights. And depending on you
[00:08:20] see this it might it might also pick the
[00:08:22] best relative weights. So you can see
[00:08:25] how much faster this is than doing this
[00:08:27] on trading view. It's doing 200 trials
[00:08:31] and it's just picking it's like
[00:08:35] it's it's just not something a human
[00:08:36] could do. Okay. Okay. So now the the
[00:08:39] parameters changed slightly but not too
[00:08:41] much which is good because we want to
[00:08:42] see it's just generally good. Right? So
[00:08:46] here
[00:08:48] we went from 7 to six for the stop loss
[00:08:50] and we've been trading at five which is
[00:08:51] close enough. The pyramid max went from
[00:08:54] 5 to 7.
[00:08:56] TP went from 49 to 41. It's basically
[00:08:59] stayed mostly the same which is exactly
[00:09:00] what we want to see. Now we can run the
[00:09:02] back test.
[00:09:05] So there's different metrics again. Hey,
[00:09:07] it's not the best sharp ratio, but
[00:09:09] that's not what we're optimizing for,
[00:09:10] right?
[00:09:12] So, it can show the individual equity
[00:09:15] returns.
[00:09:17] Gold really
[00:09:19] carried significantly.
[00:09:22] That's interesting.
[00:09:24] So, we might want to increase some of
[00:09:26] these other ones. But anyways, we go to
[00:09:29] period returns.
[00:09:31] And this is starting to give us some uh
[00:09:34] better data of what to expect. So this
[00:09:35] with this particular back test, this is
[00:09:38] the distribution of of years. And we can
[00:09:41] see that for this back test, 70% of
[00:09:44] years were winning and 30% are losing.
[00:09:46] That might scare you guys, but this is
[00:09:48] one of the reasons I encourage you to
[00:09:49] stick with this. I've had losing years
[00:09:51] trading. We're going to have some losing
[00:09:52] years. Some of the winning years are
[00:09:53] going to be really big. With this
[00:09:55] particular back test, the average losing
[00:09:57] year was negative 112%.
[00:09:59] The average winning year was 47%. Which
[00:10:02] created an average year of 30%.
[00:10:05] Now, I'm going to show you. We'll try to
[00:10:07] optimize a bit more. I did find ways to
[00:10:09] get like 75 or 80% winning years, but
[00:10:11] there's going to be some losing years.
[00:10:13] But you can see the winning years are
[00:10:15] significantly bigger. And it also is
[00:10:17] going to give us data on different time
[00:10:20] frames. So,
[00:10:23] if I go to decade, look, it won 100 this
[00:10:25] particular back test. It won 100% of
[00:10:27] decades.
[00:10:29] The average decade is 22,000% return,
[00:10:32] which is 20x. So your 100,000 would turn
[00:10:35] into 2 million. But you can see that a
[00:10:39] lot of these years were like
[00:10:42] weaker like 400% 300 600% which is good
[00:10:47] but I'm going to show you how to get
[00:10:49] more insane returns. A lot of it was in
[00:10:50] the the 2020s because of Bitcoin in this
[00:10:52] back test. Now we can also look at days.
[00:10:57] We can look at at different uh period
[00:11:00] returns. See, winning days 48%, losing
[00:11:02] days 41%. This is data we didn't have on
[00:11:06] Trading View. So, you might think, well,
[00:11:09] I want to win every day. Well, this
[00:11:11] normal to lose about half the days and
[00:11:14] win slightly more days and your average
[00:11:15] winning day is a lot more is slightly
[00:11:17] more. Now, you might also be wondering
[00:11:20] why it doesn't add up to 100. It's
[00:11:22] because it doesn't trade every single
[00:11:23] day. So, we can also look at a week.
[00:11:29] Um
[00:11:32] 54% of weeks were winning with this back
[00:11:34] test. 50 42%. So it just compounds over
[00:11:38] time. The the longer the time frame, the
[00:11:39] better it does. 56% of winning months,
[00:11:45] 56% of winning quarters.
[00:11:48] So later on we're going to optimize this
[00:11:50] and you can look at trade data. Okay.
[00:11:52] Typically the win rate is around 50%.
[00:11:56] and the um win is a little bit less than
[00:11:59] two times
[00:12:02] uh bigger than the loss. So it's you
[00:12:05] know small expectancy but one of the
[00:12:08] beautiful things about the system is
[00:12:10] that it's likely to keep working forever
[00:12:12] relatively because we've done so many
[00:12:15] things to create it make it robust
[00:12:17] between in sample out of sample the walk
[00:12:20] forward parameter uh optimization
[00:12:23] testing sorry parameter sensitivity
[00:12:26] testing is what we call median parameter
[00:12:29] setting and then also uh running it on
[00:12:32] so many assets for so many decades It's
[00:12:34] it's really generalized. It's likely to
[00:12:35] keep working. So, there's a couple
[00:12:38] things we can do. One thing, if you want
[00:12:39] to juice the returns, you just risk
[00:12:41] more. So, I'm going to change 100% of
[00:12:43] equity to 200%. Also, there was right
[00:12:45] now is a 47% max draw down. Uh let's
[00:12:49] double and see what happens. Just
[00:12:51] increase that.
[00:12:55] So, now our max draw down is 76% which a
[00:12:58] lot of you guys maybe wouldn't want to
[00:12:59] handle. So, you might want to risk less.
[00:13:02] But you can see how that changes.
[00:13:08] The average year, the average winning
[00:13:10] year is now 100% gain. The average
[00:13:12] losing year is -22. So if you want to be
[00:13:15] more aggressive, this is how you could
[00:13:17] do it.
[00:13:19] So I want to play around with some
[00:13:20] things. We're going to have
[00:13:21] optimization, waiting optimization to
[00:13:23] give you an idea, but
[00:13:26] um
[00:13:28] just want to try some things like
[00:13:35] change the size a little bit
[00:13:40] 70% winning years.
[00:13:43] Uh I'm going to go back to parameter
[00:13:45] optimization now where we have calmar
[00:13:48] 200 trail trials. Just play with this
[00:13:52] increase the number of trials and
[00:13:53] parameters. This is going to make it
[00:13:55] take longer.
[00:13:58] So I'm just going to going to run it
[00:14:00] again. But you could just see how
[00:14:02] powerful this is and how useful this is
[00:14:05] going to be. It's running 300. It's
[00:14:06] running 300 back tests
[00:14:10] and it's picking the best one. That's
[00:14:12] the most. It's not picking the best one.
[00:14:14] It's identifying the 30 best parameters
[00:14:16] and picking something in the middle.
[00:14:19] Okay. So, this one change the min
[00:14:21] pyramid to one, which is quite
[00:14:23] interesting where it doesn't take the
[00:14:24] first breakout, only takes the second
[00:14:26] breakout. That's quite interesting.
[00:14:28] Let's see how this changes
[00:14:31] uh the back test. So, let's run a new
[00:14:33] back test.
[00:14:36] Okay. And see how much this improved
[00:14:39] things actually.
[00:14:41] So now we have 75% winning years.
[00:14:47] I'm going to change the risk again.
[00:14:48] Average losing year is negative9.
[00:14:50] Average winning year is 41.
[00:14:53] Um
[00:14:55] the sharp went up a lot or a little bit.
[00:14:58] So I'm going to try increasing the risk
[00:15:03] and seeing.
[00:15:06] That's great. Actually, this is kind of
[00:15:08] crazy. Again, you see how much gold
[00:15:10] carried this portfolio. So, I'm I'm
[00:15:12] interested in playing around with that a
[00:15:13] little bit.
[00:15:16] Uh, but
[00:15:18] I mean, this looks pretty good to me.
[00:15:20] Negative draw down a max 55%.
[00:15:24] 75% winning years. The average winning
[00:15:26] year is 60%. The average losing year is
[00:15:28] 13%. Again, most of you guys want to
[00:15:30] probably make money every year, but
[00:15:33] it's not so simple to do. It's also not
[00:15:35] necessary to grow wealthy.
[00:15:39] I'm just going to play with this a
[00:15:40] little bit more. I'm going to reduce
[00:15:41] Gold's position because it was
[00:15:46] um such an outsized
[00:15:49] part of uh that particular back test.
[00:15:52] So, I'm just going to try it.
[00:15:54] So, I'm going to run uh new settings.
[00:15:59] And again, you can instead of just doing
[00:16:01] this on the portfolio level, you could
[00:16:02] do it for individual assets and optimize
[00:16:04] for those. Whether that's going to get
[00:16:07] better returns or not, I don't know.
[00:16:09] Look how just changing reducing gold
[00:16:13] uh in the portfolio.
[00:16:16] The stop-loss multiple came down quite a
[00:16:18] bit. So, let's see. We'll run the new
[00:16:20] back test and see.
[00:16:24] Now, it was Bitcoin that's carried the
[00:16:25] most, not gold. So I don't necessarily
[00:16:28] want that much portfolio volatility
[00:16:31] but now we are up to 77% winning years
[00:16:35] losing years I mean this is really great
[00:16:38] right average winning year
[00:16:41] and the max draw down is 39%. Now I'm
[00:16:44] going to reduce Bitcoin more and uh run
[00:16:46] the back test again because
[00:16:49] the idea is that to increase winning
[00:16:51] years you you have a more balanced. So
[00:16:54] we're going to we're going to make it so
[00:16:55] it optimizes waiting too
[00:17:00] which is gives an idea of how many
[00:17:02] contracts to run.
[00:17:07] Okay.
[00:17:13] And then I'm going to do one more thing
[00:17:14] at the end. So let's run the back test
[00:17:16] again.
[00:17:19] Um,
[00:17:21] now the SPX is the biggest one in the
[00:17:24] curve. Let's see if this changes things
[00:17:27] similar. So I mean portfolio weighting
[00:17:29] doesn't necessarily need to change
[00:17:30] things that much. Now the last thing I'm
[00:17:33] going to do, so we have this percentage
[00:17:35] of equity. I'm going to change it to
[00:17:36] fixed units
[00:17:39] and units 10 I believe is essentially
[00:17:42] one contract. We'll start with say a
[00:17:45] $25,000 account
[00:17:48] and let's set to for 10 years ago and
[00:17:52] this will kind of tell us how much money
[00:17:53] we made
[00:17:55] if we traded this this way. So let's
[00:17:58] said 2015
[00:18:01] till now
[00:18:04] and let's run the back test.
[00:18:07] [laughter]
[00:18:08] It's showing a million dollar gain
[00:18:11] with a 61% draw down. So I mean this is
[00:18:16] how it would have looked
[00:18:19] uh by year.
[00:18:22] You know it's interesting. It's showing
[00:18:24] 59% for 2025 when I did 500% for 2025.
[00:18:30] But this just gives an idea of what's
[00:18:32] possible. But look,
[00:18:34] with this particular settings, it
[00:18:36] actually didn't
[00:18:39] uh basically didn't make anything from
[00:18:41] 2021, 2022, and 2023. It's interesting.
[00:18:45] It just went crazy in um December 2020.
[00:18:49] But that's the power of compounding.
[00:18:51] averaging 70% a year these years. Did
[00:18:54] 100% 100%.
[00:18:56] Um, so I do think I'm going to run one
[00:19:00] more parameter optimization
[00:19:03] for the past 10 years and see. But the
[00:19:05] idea is to use the thing that generally
[00:19:07] works the most.
[00:19:10] And I mean, I'm still happy to use a
[00:19:12] stop loss of around five. It kind of
[00:19:14] makes sense to me.
[00:19:18] Okay. So, let's run the back test
[00:19:22] and see
[00:19:24] 2 million. Okay. Now, I'm curious about
[00:19:26] the years. So, it's showing it's
[00:19:29] interesting. It shows a 5% return for
[00:19:31] 2025.
[00:19:34] Probably because silver was a small part
[00:19:36] of the portfolio, but some of these
[00:19:38] years were such big returns. I'm going
[00:19:41] to increase silver and see how that if
[00:19:44] that if it like picks that up because
[00:19:47] that's I mean
[00:19:49] the reason one of the reasons we did so
[00:19:51] well last year
[00:19:53] was because of silver.
[00:20:01] So let's check it out.
[00:20:07] All right, run the back test again.
[00:20:11] And that made things worse.
[00:20:16] Why doesn't it show a huge gain on
[00:20:18] silver? I think maybe it doesn't
[00:20:19] compound.
[00:20:22] I'm kind of confused.
[00:20:27] Still looks good. This This is now
[00:20:29] showing 100% winning years, so can't be
[00:20:32] too mad about that.
[00:20:38] That's probably because
[00:20:40] it goes down because it's not
[00:20:42] compounding.
[00:20:46] Okay. Anyways, hope you find this
[00:20:48] helpful and useful and please share
[00:20:51] performance returns you got with the
[00:20:53] group. Okay. Appreciate you on a well.