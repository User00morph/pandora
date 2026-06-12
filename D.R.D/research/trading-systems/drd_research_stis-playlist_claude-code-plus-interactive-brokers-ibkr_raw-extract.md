# RAW EXTRACT — Claude Code Plus Interactive Brokers IBKR

- **Video ID:** q4TyQ7akK-U
- **Duration:** 9:42
- **Words:** ~1,678

---

[00:00:00] Hi guys, in this video I will show you
[00:00:03] how to integrate cl code with
[00:00:06] interactive broker so you can use clo
[00:00:08] code to de to create and develop your
[00:00:11] algorithmic trading strategy. This form
[00:00:14] of integration shall not be used by
[00:00:17] retail investors who wants to access
[00:00:19] their perform their portfolio using a
[00:00:22] code. This is not what is that for. This
[00:00:25] integration is primarily used for
[00:00:27] algorithmic trading. There are two form
[00:00:30] of integrations. I will walk you through
[00:00:33] both of them and I will let you to
[00:00:35] decide which one is more suitable for
[00:00:37] your particular use case. Without
[00:00:39] further ado, let's jump in. The first
[00:00:42] method of integration is called direct
[00:00:44] method. With this method, you are
[00:00:47] setting up cloud code on your local
[00:00:49] machine together with interactive broker
[00:00:52] gateway. Interactive broker gateway is
[00:00:54] the small Java application which ups and
[00:00:58] running and it's actually used for
[00:01:01] authorizing your request to interactive
[00:01:03] broker API without interactive broker
[00:01:07] gateway your request to the API they
[00:01:10] will not be authorized they will not be
[00:01:12] executed because uh this setup runs
[00:01:16] locally it doesn't require any form of
[00:01:19] investments it's free to use and the
[00:01:22] only require requirements that you have
[00:01:23] to be aware of is that your interactive
[00:01:27] broker gateway must be up and running
[00:01:30] 24/7. So your computer must be up and
[00:01:33] running 24/7. Your your internet must be
[00:01:37] stable and reliable. So your algorithmic
[00:01:40] trading strategy is up and running
[00:01:42] correctly.
[00:01:44] and uh interactive broker gateway every
[00:01:47] now and then multiple times a day it's
[00:01:49] going to be sending you authorization
[00:01:51] request on your phone to step
[00:01:53] verification and you need to approve
[00:01:55] them every now and then without your
[00:01:58] approval cloud code will not be able to
[00:02:00] execute anything and everything is going
[00:02:03] to be broken you have to keep that in
[00:02:05] mind so you need to keep an eye on your
[00:02:07] phone 24/7 as well there will be no
[00:02:10] deployment management you will not have
[00:02:13] a stage in production ction and
[00:02:15] development environment. You're going to
[00:02:16] have the environment and this is why
[00:02:20] this form of setup is not really
[00:02:23] production ready. It's good for testing
[00:02:26] for throwing ideas but this is it and
[00:02:29] there will be no feedback loop. What is
[00:02:33] the feedback loop? Feedback loop is uh
[00:02:36] when you're developing algorithmic
[00:02:38] trading strategy you need to ensure that
[00:02:43] you your trading strategy meets the
[00:02:46] certain targets. So the return of your
[00:02:48] strategy is certain the draw down is
[00:02:52] certain and the performance P&L and the
[00:02:56] win rate there as well certain you do
[00:02:59] that by running all the back test for
[00:03:01] different time periods and you recording
[00:03:03] that as the performance metrics. After
[00:03:07] doing alteration in your algorithmic
[00:03:10] trading strategy, you need to ensure
[00:03:12] that all your new changes they have not
[00:03:15] broken the strategy. And the way you are
[00:03:18] actually ensuring that is by rerunning
[00:03:21] the back tests once again. And uh with
[00:03:24] this form of integration, there is no
[00:03:27] back testing ability and there is no
[00:03:28] feedback loop whatsoever. So you will be
[00:03:32] able to run the code will be able to run
[00:03:35] the trading strategy but it will not be
[00:03:38] able to back test your strategy. It will
[00:03:40] not be able to do much and you will be
[00:03:43] blind. That's why I quite quickly
[00:03:46] disregarded this this method of
[00:03:49] integration for myself and I moved to
[00:03:51] the advanced method. Advanced method
[00:03:55] uses Quan connect as the integration
[00:03:59] provider. Quan connect is the world's
[00:04:02] leaders algorithmic trading platform and
[00:04:04] that's why I have chosen it. So you're
[00:04:07] setting up code on your local machine
[00:04:10] together with a lin CLI. Lin CLI is the
[00:04:14] CLI which is used by Quan connect and uh
[00:04:17] its only objective is to send requests
[00:04:19] to the Quan connect servers itself. Quan
[00:04:22] connect is going to be by itself
[00:04:24] integrated to the interactive broker API
[00:04:27] and all that integration is going to be
[00:04:30] handled by Quan connect. You don't have
[00:04:31] to worry about that. Everything is going
[00:04:33] to be up and running there 247.
[00:04:37] Of course, it's not free to use. You
[00:04:39] need to pay Quan Connect and the
[00:04:41] starting part package is 100 bucks a
[00:04:43] month and then you can add additional
[00:04:45] servers by demand. So, it's very
[00:04:48] scalable and it's very much production
[00:04:50] ready. It runs in a cloud in the servers
[00:04:53] nearby New York. So like the pin between
[00:04:57] your servers and the and the New York
[00:05:01] New York Stock Exchange is going to be
[00:05:03] minimal which is very great. Uh this
[00:05:06] form of connection maintains
[00:05:07] verification every there is two form of
[00:05:11] uh verifications approvals. One last
[00:05:14] seven days another one last
[00:05:16] indefinitely. With a seven days
[00:05:18] verification approval every week in a
[00:05:21] certain time, Quan Connect will send you
[00:05:24] a verification request on your phone.
[00:05:26] Once you approve it, it lasts for 7
[00:05:28] days. You can set it up indefinitely.
[00:05:31] It's up to you how you like to do it.
[00:05:33] It's also possible.
[00:05:35] uh because uh you are not going to be
[00:05:38] running direct using directly
[00:05:41] interactive broker API your strategy is
[00:05:45] going to be much more reliable. You will
[00:05:48] use the development tool provided by
[00:05:50] Quan connect and uh that Quan connect
[00:05:54] itself integrates with a different
[00:05:56] brokers different service providers and
[00:05:59] they actually maintaining that
[00:06:00] connection. So you don't have to worry
[00:06:02] about you just writing the code in their
[00:06:04] standard LS format and Quan connect
[00:06:07] handles the rest. Once again I have not
[00:06:11] been affiliated anyhow with Quan connect
[00:06:14] itself. I've started using them a week
[00:06:16] three weeks ago and I fallen in love
[00:06:19] with them. I love how they providing. I
[00:06:22] like like what they're doing. I it's
[00:06:24] very much reliable. It's very scalable
[00:06:26] and it's made for algorithmic trading at
[00:06:30] scale. So, and it actually provides
[00:06:33] deployment and access management. So,
[00:06:36] you're going to have the development,
[00:06:38] staging and production environment,
[00:06:40] everything up and running there in the
[00:06:42] cloud. And uh there's paper trading,
[00:06:45] there's a live trading. When you're
[00:06:47] deploying your envir your strategy,
[00:06:50] you're configuring environment the way
[00:06:52] you want it to be. Either it's going to
[00:06:54] be live environment, paper environment,
[00:06:56] a different broker environment. You're
[00:06:59] connecting each strategy to the certain
[00:07:01] environment which connect itself to the
[00:07:04] certain account on your broker which is
[00:07:06] very convenient. So you can have a
[00:07:08] multiple strategies which runs on a
[00:07:11] multiple accounts on your broker which
[00:07:14] for example right now I have one equity
[00:07:16] account, one futures account. They the
[00:07:20] strategies they're not overlapping with
[00:07:21] each other. They're not breaking each
[00:07:23] other and they're running independently.
[00:07:26] uh the Quan connect the power of Quan
[00:07:29] connect is that it provides you all the
[00:07:33] data back testing data for last 10 20
[00:07:37] years so when you are writing your
[00:07:40] strategy you actually running all the
[00:07:43] back tests then you're getting the
[00:07:45] reports I mean cloud code is getting
[00:07:47] reports from those back tests analyzes
[00:07:50] them and then it actually improves your
[00:07:52] trading strategy so what you can
[00:07:54] actually do you can say load code write
[00:07:58] me the trading strategy using these
[00:08:00] parameters iterate improve until you're
[00:08:03] going to find the suitable uh the best
[00:08:06] possible appro the criterias and let it
[00:08:09] run code will iterate run back test
[00:08:13] iterate run back test and find the
[00:08:16] solution for you that's why I think this
[00:08:18] is amazing setup in general the back
[00:08:21] testing is very reliable feedback loop
[00:08:24] is amazing in and you can iterate your
[00:08:27] trading strategy very fast. In the last
[00:08:30] three weeks, I have run more than a
[00:08:33] thousand different back tests. Uh in
[00:08:36] short, I've I've written more than a
[00:08:38] thousand different trading strategies. I
[00:08:40] will not be able to do that manually. I
[00:08:43] will not be able to analyze such a huge
[00:08:45] amount of data manually. But cloud
[00:08:47] connect together with uh cloud code,
[00:08:50] quan connect together with cloud code
[00:08:52] was able to do that.
[00:08:55] So if you want to have a production
[00:08:57] ready environment for your algorithmic
[00:09:00] trading, you need to stick to Quan
[00:09:03] Connect. It is just non-negotiable.
[00:09:06] They are the best in the market and
[00:09:08] there there is a reason for it. And uh
[00:09:11] I'm going if if you want to know how to
[00:09:15] set everything up, how to create your
[00:09:16] trading strategy, how to scale your
[00:09:19] trading strategy, how to properly back
[00:09:21] test and live test your trading
[00:09:23] strategy. I'm going to be opening the
[00:09:25] community for people like yourself. I'm
[00:09:27] going to drop the link in the
[00:09:29] description section down below. Feel
[00:09:31] free to check it out if you want to.
[00:09:33] Thank you very much for watching this
[00:09:34] video. I hope you find value in that and
[00:09:37] I hope to see you in the next one. Take
[00:09:38] care. Bye.