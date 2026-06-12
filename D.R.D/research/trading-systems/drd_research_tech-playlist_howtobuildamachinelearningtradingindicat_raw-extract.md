# RAW EXTRACT — How To Build a Machine Learning Trading Indicator in Python

- **Video ID:** gyE3bYPsvu8
- **Duration:** 17:51
- **Word count:** ~3,645

---

[00:00:00] Hi, and welcome back. In this video, I'm
[00:00:03] going to show you a machine learning
[00:00:04] indicator using a classifier for trend
[00:00:06] predictions. This table shows the
[00:00:08] prediction results on validation data,
[00:00:10] meaning on new unseen data, and the
[00:00:13] total accuracy is around 52% for this
[00:00:15] particular example. This is going to be
[00:00:18] dependent on the model we're going to
[00:00:20] use. Also, we have access to the
[00:00:22] separate accuracies for the three trend
[00:00:24] categories that we considered in our
[00:00:27] simulation in this experiment. So, first
[00:00:29] we have the ranging price, category
[00:00:31] zero, downtrend, category one, and the
[00:00:33] uptrend that we labeled category two. If
[00:00:36] you are into machine learning
[00:00:38] classifiers, and you've already used and
[00:00:40] you are already familiar with this field
[00:00:43] and related metrics, the ROC curves show
[00:00:45] positive signs of predictability,
[00:00:47] meaning the forecasting, although not
[00:00:50] perfect at this stage, is still
[00:00:52] capturing a signal about the future of
[00:00:54] the trend. And this is how the signal
[00:00:56] looks like on the chart. So, here we
[00:00:57] have um
[00:00:59] false bearish signal because the price
[00:01:01] went up afterwards. Here we have a
[00:01:03] bullish signal. We didn't really have an
[00:01:05] uptrend afterwards, although we have one
[00:01:07] day of a green candle. This is daily
[00:01:10] time frame, by the way, so each candle
[00:01:11] represents one day. These two signals
[00:01:14] are bearish signals, and they are good
[00:01:16] because for the coming uh four or five
[00:01:19] days, we have a downtrend. So, this is a
[00:01:21] really wide range. It could have been a
[00:01:23] really good uh trade right here. And
[00:01:25] this is an excellent bullish signal as
[00:01:27] well detected by the model because the
[00:01:29] price went straight up afterwards. So,
[00:01:32] if you notice we're trying to use the
[00:01:33] model to pick entry points at candles
[00:01:35] where we can enter with maximum chances
[00:01:38] of profit. So, now I will show you how I
[00:01:40] trained the machine learning model, so
[00:01:42] you can reproduce the same results. And
[00:01:44] if you are here for the coding part, the
[00:01:46] Python code I'll be using is available
[00:01:48] for download from the link in the
[00:01:49] description of this video, so you can
[00:01:51] download it for free and run this
[00:01:53] experiment from your side. Our quick
[00:01:55] plan is the following. First step is to
[00:01:57] get the data, add some technical
[00:01:59] indicators. I have added more than 20
[00:02:01] indicators as input features ranging
[00:02:03] from momentum indicators, oscillators,
[00:02:05] trend detection, volatility, and
[00:02:07] volume-based indicators. We will go
[00:02:09] through the details later on in this
[00:02:11] video. Then we need to label the data. I
[00:02:14] will also show you how I did this
[00:02:15] step-by-step in details looking into the
[00:02:17] average closing price of future candles
[00:02:20] and comparing it with the current
[00:02:21] candle. Then we train the machine
[00:02:23] learning model on the training data set.
[00:02:26] We will evaluate its prediction metrics
[00:02:28] on the test data and the validation data
[00:02:30] or using unseen data set. And finally, I
[00:02:32] will show you how the indicator looks
[00:02:34] like on the trading chart, so we can
[00:02:36] analyze its potential for trading
[00:02:38] strategies.
[00:02:39] Now, for the labeling, we will choose a
[00:02:42] fixed time horizon, meaning we will look
[00:02:44] into how the price changes in a fixed
[00:02:46] number of candles in the future. Imagine
[00:02:49] this is the current candle, and it
[00:02:51] closes at this price level. We will
[00:02:54] define a threshold area in number of
[00:02:56] pips or a percentage of the price. We
[00:02:59] will look into the future considering a
[00:03:01] fixed number of bars. Next, we compute
[00:03:03] the average closing price of these
[00:03:05] candles, and we check if the difference
[00:03:08] with the original closing price of the
[00:03:10] current candle exceeds the threshold
[00:03:12] boundaries. In this example, the average
[00:03:14] is still within the threshold area, so
[00:03:16] we have a ranging market, and the label
[00:03:19] of this current candle is zero. If the
[00:03:21] average of future prices crossed above
[00:03:24] the threshold area, we have an uptrend,
[00:03:27] and the label is two. In the opposite
[00:03:29] direction, if the average closing price
[00:03:31] of the future candles is below the
[00:03:33] threshold, and the label is set to one.
[00:03:35] So, at the end we will get a data set
[00:03:38] with all the input features, but also
[00:03:40] the labels. We can compute the multiple
[00:03:42] labels in this case, changing the number
[00:03:45] of future bars and the threshold width,
[00:03:48] so we can optimize our labeling method
[00:03:50] as well. We will be using a grid search
[00:03:52] approach to compute those different
[00:03:54] labels using different thresholds and
[00:03:56] different future candles. Now, just as a
[00:03:59] side note, this is not a look-ahead
[00:04:01] bias. This is a labeling technique, a
[00:04:04] labeling approach. It allows the model
[00:04:06] to peek into the future just during the
[00:04:08] learning or training phase. But these
[00:04:10] values are not provided to the model
[00:04:13] during the prediction or the testing
[00:04:15] phase or the validation phase. Now, we
[00:04:17] can move on to the Python code, train
[00:04:19] the model, apply predictions, and have a
[00:04:21] look at the results. So, this is our
[00:04:23] Jupyter notebook file. First of all, I'm
[00:04:25] importing whatever is needed, so I'm
[00:04:27] using Wi-Fi for the data to import the
[00:04:29] data, then scikit-learn and XGBoost,
[00:04:32] matplotlib for plotting, and so on. I'm
[00:04:36] downloading the data for now. You can
[00:04:37] change the label to
[00:04:39] download different stocks, the date, the
[00:04:41] starting date, and so on. So, this is
[00:04:43] just to download the data. We will get a
[00:04:45] data frame that looks like this. We have
[00:04:47] the close, high, low, open, and the
[00:04:49] volume
[00:04:50] and the date for each of those rows.
[00:04:52] Then we have the feature engineering
[00:04:55] part or technical indicators added using
[00:04:57] pandas_ta technical analysis. So, this
[00:05:01] is just a helper function that we're
[00:05:03] going to use later on now to merge the
[00:05:06] indicators into our original data frame,
[00:05:09] and then one function named
[00:05:10] add_indicators
[00:05:13] is going to compute the indicators, the
[00:05:15] momentum indicators,
[00:05:17] and the RSI with different length. For
[00:05:20] example, we are using RSI length 5, 10,
[00:05:24] and 15. This is why it's in a for loop,
[00:05:27] so it's going to add three different
[00:05:28] columns. We have the ROC 10, momentum
[00:05:30] 10.
[00:05:31] Uh we're going to merge these together.
[00:05:33] We have the CCI 20,
[00:05:35] uh WR 14, and so on, the MACD as well.
[00:05:39] Uh we're also adding simple and
[00:05:41] exponential moving averages with length
[00:05:44] 5, 10, and 20, as you can see here. And
[00:05:47] the um
[00:05:48] volume W moving average, volume-weighted
[00:05:52] uh moving average 20, and so on. So, I'm
[00:05:54] not going to list all of these. You can
[00:05:56] add all kind of indicators here. You can
[00:05:58] add your custom indicators. This is
[00:06:00] where you can experiment by adding as
[00:06:03] many indicators that you want and
[00:06:05] probably applying some dimensionality
[00:06:06] reduction later on if needed. And now
[00:06:09] our data frame will look like this. On
[00:06:11] top of the original columns, we'll get
[00:06:13] the additional columns of the technical
[00:06:15] indicators we just added. Now, for the
[00:06:17] label, we're going to compute the
[00:06:19] average closing price of future uh
[00:06:21] candles using a certain look-ahead and
[00:06:24] negative look-ahead. For example, for
[00:06:25] the future five candles by default, and
[00:06:27] then there's a threshold of 0.01, so
[00:06:30] that's a percentage of the current
[00:06:32] price.
[00:06:33] If the price went above by a certain
[00:06:36] percentage above the threshold, then we
[00:06:38] have a return two. It's a bullish uh
[00:06:41] trend, let's say, bullish future trend.
[00:06:43] Otherwise, if the average of the future
[00:06:45] closing prices of the future candles
[00:06:48] is below the threshold, it's uh
[00:06:50] downtrend, so we return one in this
[00:06:52] case. Otherwise, we return zero. We
[00:06:54] don't have a clear trend. It's a ranging
[00:06:56] market. So, we can uh I put this into a
[00:07:00] function so-called generate label, so we
[00:07:02] can change the look-ahead into uh let's
[00:07:06] say from five candles to 10 candles in
[00:07:09] the future, 15 candles in the future,
[00:07:10] and so on. And also, we can change the
[00:07:13] threshold.
[00:07:14] And also, we can change which part of
[00:07:17] the candle we're looking at using the
[00:07:19] closing price by default for for this
[00:07:21] example. So, here you can see that we're
[00:07:24] using a grid search approach. The
[00:07:27] look-aheads we're going to test are two
[00:07:29] candles in the future, four, six, eight,
[00:07:31] and 10 candles. And we're checking only
[00:07:34] two thresholds, either 1 or 2%. You
[00:07:37] might want to add more values here to
[00:07:39] make the test more complete, but it's
[00:07:41] going to cost you more compute time. And
[00:07:43] now in the data frame, we can see that
[00:07:45] we have the original columns, open,
[00:07:48] high, low, and close, and the volume. We
[00:07:50] have the indicators, but we also have
[00:07:52] different labels that you can see here.
[00:07:55] So, that's label, let's say, two candles
[00:07:58] in the future with a threshold of 1%
[00:08:01] change,
[00:08:02] uh two candles, 2% change, four candles
[00:08:05] in the future, 1%, 2%, and so on. So, we
[00:08:08] can see that we have all the labels of
[00:08:11] the grid that we have defined in these
[00:08:13] two lines right here. Then we're going
[00:08:15] to split the data into training,
[00:08:17] testing, and validation or validation
[00:08:19] and testing. You might want to name it
[00:08:21] differently depending on which book
[00:08:22] you've been reading recently, but
[00:08:24] anyway, we're splitting these into three
[00:08:27] um slices. Uh you might want to use 60
[00:08:29] 20 20 or 80 10 10%. It's not that
[00:08:33] important, really. When it's working,
[00:08:34] it's working. When it's not working,
[00:08:36] we'll know that it's not working. Then
[00:08:38] we're defining the um baseline XGBoost
[00:08:42] performance. So, we're defining the
[00:08:44] model first of all with the
[00:08:46] hyperparameters. We're not going to
[00:08:48] fine-tune the hyper parameters at this
[00:08:50] point. We're just trying to check which
[00:08:54] of the labels in this data frame
[00:08:57] will provide the best result. And the
[00:09:00] way we're going to do this is that we're
[00:09:02] going to train and test the
[00:09:04] model
[00:09:06] on all of the labels. So, we're going to
[00:09:08] use all of the labels, and we're going
[00:09:10] to concatenate the results in this list.
[00:09:13] Remember, this is a for loop. It's going
[00:09:15] to loop over all the labels. It's going
[00:09:17] to split the data, train the model, test
[00:09:20] the data. This is the training training
[00:09:22] here with the fitting function, then
[00:09:24] it's going to predict on the testing
[00:09:25] part
[00:09:26] or the validation part again. Then it's
[00:09:28] going to compute the accuracy, the F1
[00:09:31] score, and we're going to append the
[00:09:32] results in the results list. Then we
[00:09:34] sort the list of these labels for for
[00:09:38] one same model, actually, uh depending
[00:09:41] on either accuracy or the F1 score. So,
[00:09:44] this way we can see how the label is
[00:09:46] affecting the same model using the same
[00:09:48] data. So, we can have an accuracy of
[00:09:51] 0.86, which means actually nothing
[00:09:54] because if the model is
[00:09:56] uh very not sensitive, let's say, and
[00:10:00] it's predicting uh category zero by
[00:10:02] default, like this category.
[00:10:05] We're going to easily get uh something
[00:10:07] above 60% of accuracy cuz most of the uh
[00:10:11] candles are not uh labeled either one or
[00:10:15] two. So, I have the tendency to look
[00:10:18] both at the F1 score and the accuracy
[00:10:20] together as a first glance. But, anyway,
[00:10:23] the good thing good news is that we can
[00:10:24] try all of these. So, now that we can
[00:10:27] choose which label we are going to use,
[00:10:29] so probably you will want to use either
[00:10:31] the highest accuracy or the highest F1
[00:10:33] score. In this case,
[00:10:36] you can say, let's say the best label is
[00:10:38] the maximum among among the results
[00:10:41] using the F1 score, for example. I've
[00:10:43] used the F1 score maximum. So, that's
[00:10:45] going to be this model right here. 10
[00:10:48] candles in the future, a change above
[00:10:51] 2%. You can also uh if you want, you can
[00:10:53] also override this. So, uh you can
[00:10:55] uncomment this line and choose whatever
[00:10:57] label you want to experiment on.
[00:11:00] So, now that we have chosen the label
[00:11:03] that we're going to use, we can uh tune
[00:11:05] the hyper parameters of our machine
[00:11:07] learning model.
[00:11:08] So, this is where it's happening. We're
[00:11:10] also using a grid search approach. So,
[00:11:13] these are the hyper parameters and we're
[00:11:15] providing a range or few values for each
[00:11:17] of these parameters. And then we're
[00:11:19] going to test the um model with the
[00:11:22] different parameters using our best
[00:11:24] choice of the uh label. We're using the
[00:11:26] grid search function, providing this
[00:11:28] dictionary where we have different
[00:11:30] values for different hyper parameters.
[00:11:32] So, that's around 810 fits for this
[00:11:35] example. It's going to repeat this job
[00:11:38] 810 times in order to provide the best
[00:11:41] set of hyper parameters. And now we have
[00:11:43] a total accuracy of 76% for now. And
[00:11:46] then we can see the um classification
[00:11:48] report. We can see that for the category
[00:11:50] zero, which is not of interest, to be
[00:11:52] honest, for us. This is a ranging
[00:11:55] market, so that's not
[00:11:56] uh our purpose. 73% precision. Unless if
[00:12:00] you want to apply this for a ranging
[00:12:02] market strategy, that might be
[00:12:04] interesting. Then we have category one,
[00:12:06] which is the downtrend prediction with a
[00:12:08] precision of 16% and the bullish
[00:12:11] prediction is 62%, so that's a bit more
[00:12:14] uh accurate in this case, a bit more
[00:12:15] precise. We have the recall and we have
[00:12:18] the F1 score for these two. Now, if we
[00:12:20] test the uh model, the machine learning
[00:12:22] model, on new and unseen data, let's say
[00:12:24] the validation
[00:12:25] set that we haven't used so far, we're
[00:12:27] losing the precision that we uh got on
[00:12:30] the bullish part. The bearish part is
[00:12:33] somehow kept the same. We kept the uh F1
[00:12:35] score, we we kept the uh recall, and we
[00:12:38] kept somehow the
[00:12:40] And also the category zero is kept as
[00:12:42] is. So, this is again, we're not using
[00:12:45] the best label. I've chose the label
[00:12:46] with the best or the highest F1 score.
[00:12:49] We could try with the highest accuracy
[00:12:51] or just choose something which has a
[00:12:53] compromise in between. If we check the
[00:12:55] classification reports of these
[00:12:57] different labels, we might want to
[00:12:58] choose a label manually, which will
[00:13:00] probably provide better results. Now,
[00:13:02] there is a way to make the model a bit
[00:13:04] more selective and improve the results,
[00:13:06] improve the precision. Instead of making
[00:13:09] the model predict a category straight
[00:13:11] away, we're going to extract the
[00:13:13] probability for each of these
[00:13:14] categories, the predicted probability by
[00:13:16] the model. And in this case, we're going
[00:13:18] to set our threshold manually. So, if
[00:13:21] the
[00:13:22] of a certain category is above, let's
[00:13:24] say, a threshold 55% or 0.55.
[00:13:28] In this case, we're going to confirm
[00:13:29] that this is a bearish sell, for
[00:13:31] example, or a bullish in the case in the
[00:13:34] other case. So, we have two thresholds,
[00:13:36] one for the category one, a bearish, and
[00:13:39] one for the bullish category. Then we
[00:13:41] can use this function
[00:13:44] in order to uh extract the um
[00:13:46] probabilities. And then we're going to
[00:13:48] compute the um predicted categories
[00:13:51] based on the new thresholds that we uh
[00:13:53] we have set. So, in this case, we can
[00:13:55] see that we have few predictions in the
[00:13:57] bullish category. We have few
[00:13:59] predictions in the bearish category as
[00:14:01] well.
[00:14:02] And we have category zero as well, so
[00:14:04] it's populated with a precision of 68%.
[00:14:07] So, this is how we can play with the
[00:14:10] model parameters, prediction
[00:14:11] probability, the hyper parameters, and
[00:14:14] the labels that we've started with in
[00:14:16] the beginning. We can also improve the
[00:14:18] uh indicators that we started with in
[00:14:21] the data frame at the beginning of this
[00:14:22] video. Another interesting thing that we
[00:14:24] can use is SHAP. It's a library where we
[00:14:26] can compute the um effect, actually, the
[00:14:30] weight uh of each of the indicators that
[00:14:33] we have used on the results and for each
[00:14:37] of the classes. You can see that we have
[00:14:39] three colors, so each color is for one
[00:14:41] class, class one, two, and zero. And
[00:14:43] this graph is going to show for each of
[00:14:45] the indicators, each class, how much is
[00:14:48] it affected uh by the indicator itself
[00:14:52] in terms of predictability or
[00:14:53] forecasting. So, we can see that the
[00:14:55] simple moving average 20 is affecting
[00:14:58] mostly the pink category, which is the
[00:15:01] bullish class two signals.
[00:15:03] Uh it's also affecting this green thing,
[00:15:05] which is class zero and class one. I
[00:15:07] could say in a very equilibrate way. You
[00:15:10] don't have a lot of uh bias in here.
[00:15:13] Instead, this one, for example, the NVI,
[00:15:15] you can see that it's mainly the blue
[00:15:17] category, which is the bearish signal.
[00:15:20] And so on. We obviously tend to keep in
[00:15:23] the data frame the uh indicators that
[00:15:26] are going to have the highest effect as
[00:15:28] a stacked effect on the three different
[00:15:31] categories. So, this is just to provide
[00:15:33] an idea that some of the indicators are
[00:15:36] contributing a lot to the predictions
[00:15:38] and some others are contributing much
[00:15:40] less. And now we can plot the uh
[00:15:43] indicator itself. So, I'm going to show
[00:15:45] you here in red triangles, we have the
[00:15:48] labels. So, this is how our label uh our
[00:15:51] labeling worked. And then we have the um
[00:15:54] purple points are the generated or the
[00:15:56] forecasted uh signals.
[00:15:59] And as you can see, in some cases, we
[00:16:01] have opposite signals. This is really
[00:16:03] bad because we have a bearish uh
[00:16:05] prediction here while the label is
[00:16:07] bullish. Here we have bullish signals,
[00:16:10] bullish labels, and the model is
[00:16:11] predicting bearish. But, sometimes,
[00:16:13] actually, in this case, for example,
[00:16:16] it's predicting a good bearish signal
[00:16:18] and it's capturing actually the exact
[00:16:21] moment where we could have entered with
[00:16:23] a good return. It's at the closing price
[00:16:25] of this one. It's a good bearish signal.
[00:16:28] Here as well, we have a good prediction,
[00:16:30] as you can see. Uh this one as well is a
[00:16:32] good signal, a bearish signal. This as
[00:16:35] well, here, they are good bearish
[00:16:37] signals. So, in total, we have some good
[00:16:40] predictions and some bad predictions,
[00:16:42] and this obviously can be improved, but
[00:16:44] you have now the uh this Jupiter
[00:16:46] notebook is a good frame to start with.
[00:16:49] You have the visualization part, you
[00:16:50] have the starting part, you have the
[00:16:52] different labeling parts, and so on. And
[00:16:54] just to make sure that we're not uh
[00:16:57] totally working in the blind, the ROC
[00:16:59] curves actually here, they show a
[00:17:02] positive pulse. So, the model is not
[00:17:05] totally dead. It's not a random model.
[00:17:07] It's not randomly uh choosing between
[00:17:10] uh zero, one, or two. It's actually
[00:17:12] showing a positive predictability
[00:17:14] potential when it's showing these curves
[00:17:16] above this middle line, which somehow
[00:17:18] represents a totally random model. So,
[00:17:21] this is a good news. It can definitely
[00:17:22] be improved. And this will be it for
[00:17:24] this one. I hope you guys liked it and
[00:17:26] found the information helpful. I know
[00:17:27] it's not a full trading strategy that's
[00:17:29] going to print money overnight. Please
[00:17:31] don't trust me in the comments section.
[00:17:33] This content is mainly dedicated for
[00:17:35] people who are learning
[00:17:37] to code their own strategies, to put
[00:17:40] them into a Python, backtest these, and
[00:17:43] include complex indicators using AI,
[00:17:45] machine learning, and so on. Until our
[00:17:47] next one, trade safe and see you next
[00:17:49] time.