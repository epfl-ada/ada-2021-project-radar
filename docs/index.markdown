---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: post
# layout: home
banner: "/assets/images/banners/trump_clinton.jpeg"
---

*"I've just received a call from Secretary Clinton,"* said Donald Trump late in the night of Nov 8, 2016. The result of the 58th Presidential election, an intense battle between Donald Trump and Hillary Clinton, remains a major upset around the world. But was it? What can be seen and understood from this election, using only quotes by these candidates in the media? This could give a glimpse into the running of a major democratic election system, and the importance that speech and its representations have in making citizens turn for one party or another. Media biases have deep implications in our lives, and have evolved to be more extreme in this noisy world. We will analyze how Trump and Clinton's words quoted in media outlets relate to the polarization seen during the 2016 U.S. election.


## Research questions 

### Media bias
Do media outlets portray Trump and Clinton differently?

- **Coverage:** Did the outlets report different quotes at a given point in time? For a given outlet, was the average valence of reported quotes the same for the two candidates?
- **Bias:** Does the bias of the news outlets correlate with our previous findings?

### Political issues
Did Clinton and Trump address political issues differently?

- **Topics:** Did they address the same topics?
- **Trendsetter:** Did they address the topics at the same time? If not, who discussed it first?
- **Intellectuality:** Did they express different levels of intellectuality (more complicated words; more colloquial words)?
- **Sentiment:** Did they address certain topics or people more positively or negatively?

### Sentiment Analysis
This section compares the underlying sentiment of quotes uttered by Donald Trump versus Hillary Clinton towards typical political campaign issues such as immigration and health care, as well as specific topics that we have extracted in the Topic Extraction section.


#### Method
Our approach consists of filtering the quotes for a specific topic and performing sentiment analysis on each filtered quote.

In order to perform the sentiment analysis, we use NLTK’s Pre-Trained Sentiment Analyzer’s VADER (Valence Aware Dictionary and sEntiment Reasoner), which is well suited for analyzing short sentences.

For each quote, we get a “compound score” ranging between -1 and 1 (-1 being the most negative and +1 the most positive score). In order to understand the distribution of the sentiment for each candidate towards the selected topic, we plot the results on a histogram. We combine this histogram with a boxplot for each candidate, which enables us to better compare their distribution.

To better understand and compare the opinion of each candidate on the topic of interest, we use the polarity score of each quote to classify it as “negative” (score < -0.05), “neutral” (-0.05 < score < 0.05), or “positive” (score > 0.05). We then aggregate the results and, after normalizing them by the total number of quotes for each speaker (since the number of quotes is not the same for each candidate), plot them or a categorical bar chart.

#### Analysis
##### Campaign Type
Before diving down into individual topics, we perform sentiment analysis over the whole dataset to get a general feel of the type of campaign that Donald Trump and Hillary Clinton ran.

When classifying the quotes as Negative, Neutral and Positive, we see that, even though there are slight differences between both candidates (Hillary Clinton has slightly more positive quotes than Donald Trump), both candidate’s quotes tend to be generally more positive than negative (about 10% more). 
<div>{%- include plots/sentiment_class_.html -%}</div>

According to the Inquiries Journal’s article *[“Comparing the Effectiveness of Positive and Negative Political Campaigns”](http://www.inquiriesjournal.com/articles/1311/comparing-the-effectiveness-of-positive-and-negative-political-campaigns)* by Gregory Peter, it seems that candidates have a better chance to win if they run a *positive* campaign rather than a *negative* campaign. 
This article describes a positive campaign as one where “a candidate focuses primarily on relevant issues, their own views, their own experiences, and their own virtues, without attacking their opponent in an attempt to gain votes.” On the other hand, “a negative campaign is one where a candidate uses attack ads and rhetoric to deliberately frame his opponent as foolish, inexperienced, irresponsible, disconnected, or evil as a means of presenting him or herself as a more desirable alternative to said opponent.”

From our analysis, it seems like both Hillary Clinton and Donald Trump have taken this into consideration in their campaign by uttering more positive statements than negative.



##### Immigration
The immigration topic was one of the most controversial topics in the 2016 election. Donald Trump promised to build a wall and deport illegal immigrants, while Clinton pledged to protect and integrate some illegal immigrants.

When analyzing the sentiment of quotes related to immigration, we see a clear difference between Donald Trump’s and Hillary Clinton’s sentiment: 60% of Hillary Clinton’s quotes related to immigration are positive, and only 22% are negative. In contrast, only 47% of Donald Trump’s quotes are positive, and 37% are negative. 

<div>{%- include plots/sentiment_class_immig.html -%}</div>


##### Obamacare 
Better known as Obamacare, the Affordable Care Act (ACA) was a policy enacted by President Obama in 2010 that was intended to improve access to health insurance for US citizens.
This ACA was one of the dominant issues of the 2016 presidential campaign. While Clinton pledged to “build” on Obamacare, Trump vowed to repeal the law.

Our sentiment analysis on this topic reflects this trend: 71% of Clinton’s quotes about Obamacare are positive, versus only 44% for Trump. On the other side of the spectrum, 12% of Clinton’s quotes are negative, versus 39% for Trump.

<div>{%- include plots/sentiment_class_obama.html -%}</div>


#### Conclusion
While sentiment analysis on text can be helpful to show patterns, one must be very careful in its interpretation. Some aspects of the text might not be captured or interpreted correctly by the machine. For example, the tone, the sarcasm, or the negation of sentences can cause some misclassifications.

Also, the choice of keywords when filtering the quotes is critical. For example, quotes containing words or expressions about the same general topic but with opposite meanings can skew the results.
For example, if we take the topic of abortion and decide to analyze quotes containing either the words “pro-life” or “pro-choice,” the results of a speaker that is against abortion will be postive for the first keyword, and negative for the second. Therefore, if we look at the aggregated results, we will think this person is as positive as he or she is negative about this topic, which does not reflect the truth. 
To avoid this confusion, we selected quotes with keywords that belong to a specific side of the spectrum for each topic.


<!-- 
#### All
<div>{%- include plots/quotes_count_per_speaker_.html -%}</div>
<div>{%- include plots/sentiment_class_.html -%}</div>
<div>{%- include plots/sentiment_hist_.html -%}</div>

##### Abortion
<div>{%- include plots/quotes_count_per_speaker_abort.html -%}</div>
<div>{%- include plots/sentiment_class_abort.html -%}</div>
<div>{%- include plots/sentiment_hist_abort.html -%}</div>

##### Economy 
<div>{%- include plots/quotes_count_per_speaker_econo.html -%}</div>
<div>{%- include plots/sentiment_class_econo.html -%}</div>
<div>{%- include plots/sentiment_hist_econo.html -%}        </div>

##### Immigration
<div>{%- include plots/quotes_count_per_speaker_immig.html -%}</div>
<div>{%- include plots/sentiment_class_immig.html -%}</div>
<div>{%- include plots/sentiment_hist_immig.html -%}</div>

##### Obamacare
<div>{%- include plots/quotes_count_per_speaker_obama.html -%}</div>
<div>{%- include plots/sentiment_class_obama.html -%}</div>
<div>{%- include plots/sentiment_hist_obama.html -%}</div> -->



- **Pronouns:** How do the candidates use pronouns and what pronouns do they prefer?


