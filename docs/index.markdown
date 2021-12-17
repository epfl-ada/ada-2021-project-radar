---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: post
# layout: home
banner: "/assets/images/banners/trump_clinton.jpeg"
---

_"I've just received a call from Secretary Clinton"_, said Donald Trump late in the night of Nov 8, 2016. The result of the 58th Presidential election, an intense battle between Donald Trump and Hillary Clinton, remains a major upset around the world and came as an unpredictable surprise to many. But was it? What can be seen and understood from this election, if we only look at all quotes by them found on the internet during this historic election year? This could give a glimpse into the running of a major democratic election system, and the importance that speech and its representations have in making citizens turn for one party or another. Media biases have deep implications in our lives, and have evolved to be more extreme in this noisy world. Considering this, and using only quotes by these two candidates, we will try to understand how they ran their political campaigns.
 
Although not impossible to predict, very few Americans would have believed that Donald Trump would sit in the White House just a few years ago. 

## Background
### The Dataset
This data story is based on [Quotebank](https://zenodo.org/record/4277311#.Ybwv_i8w1B0), a corpus of close to 200 million quotes extracted from the Internet using state of the art technology. 
The dataset ranges from August 2008 to April 2020 with quotes extracted from more than 377 000 web domains.

This investigation only uses **quotes of the year of 2016**, where the predicted **speaker is either “Hillary Clinton” or  “Donald Trump”**. It is important to note that Quotebank ran into technical issues during the scraping of 2016 quotations which resulted in 3 periods with very few extracted quotes. For this analysis, any quote found inside of these periods was removed. After this and a few other (more trivial) filtrations, **140 000 quotes** remain to be used for the analysis. The dataset contains a disproportionately high share of Trump quotations. The distribution of quotes is presented in the two graphs below.

<div>{%- include plots/quotes_date_distributiion_plot.html -%}</div>
<div>{%- include plots/pie_chart_unique.html -%}</div>


### Caveats
The reader is encouraged to keep the distribution of quotes in mind, such as each speaker's share, as the report will refer to this and its implications throughout the data story. It is essential to highlight a few caveats:

Quotations could have been falsely assigned to the candidates during the Quotebank extraction process.
Quotations might not have been said by the speaker for other reasons. (Fake News, human error, etc.)
The content of a quote does not necessarily allow us to draw a conclusion about a person's belief and speech.

As a result of these caveats we encourage everyone to take this report for what it is:  

_An interesting (and fun) investigation into what conclusions **could** be drawn based on what the Internet quoted Hillary Clinton and Donald Trump with during the 2016 election year._

## Media bias
Do media outlets portray Trump and Clinton differently?
Coverage: Did the outlets report different quotes at a given point in time? For a given outlet, was the average valence of reported quotes the same for the two candidates?
Bias: Does the bias of the news outlets correlate with our previous findings?
### What is the bias?
Before diving into any analysis on Trump and Clinton’s speech, it is important to assess the bias in our dataset, which in our case is a list of quotes coming from various media outlets, potentially plagued with bias over two highly polarizing figures. Since our speakers are politicians, we should know if our quotes come from mostly left- or right-leaning outlets. The _AllSides_ news outlet presents news articles _in context_ --- by keeping note of the general political bias of news outlets. We will use their data in this part, which we obtained on [Kaggle](https://www.kaggle.com/supratimhaldar/allsides-ratings-of-bias-in-electronic-media).

Our quotes come from nearly __5 200 different websites__, while the AllSides database contains about __400 media outlets__, each with an assigned bias (“Left”, “Left-center”, “Right”...) and information on how many people agree with this rating. You can go rate the outlets yourself on their [website](https://www.allsides.com/media-bias/media-bias-ratings#ratings).
Though their ratings are informed by other things than public ratings, this should still raise your eyebrow: it is likely that the only people giving ratings come from a certain political side, which would _bias_ our bias ratings, ironically.


<div>{%- include plots/bias_distribution.html -%}</div>

| Bias     	| Median confidence* |
|--------------|------------|
| Left     	| 2.24   	|
| Left-center  | 0.97   	|
| Center   	| 0.90   	|
| Right-center | 1.08   	|
| Right    	| 1.97   	|

*The confidence is #Agree / #Disagree

About 39% of the outlets are classified as “Center”, 38% as “Left-center” or “Left”, and 23% as “Right-center” or “Right”. Also, perhaps expectedly, the ratings are less equivocal when the outlet is more extreme.
### Can we detect media bias?
Now that we collated the bias data with our quotes, the intriguing question is how the sentiment of quotes relates to the bias of the media outlet. __Perhaps a left-wing outlet would quote more negative quotes from Trump, and more positive quotes from Hillary?__

<div>{%- include plots/mb_valence_hist2d.html -%}</div>

From this plot, it seems that there is little difference between how our candidates are quoted by different media __difficult to make a conclusion__. Important limiting factors are the sentiment analysis tool, which fails to grasp the subtle meaning of sentences the way a human can, and our media bias database which allows us only to look at a fraction of the outlets in the quotes dataset.

(Show examples of negative quotes scoring high and neutral and positive quotes scoring low and neutral)
 
 

## Political topics
Did Clinton and Trump address political issues differently?

We want to track the different political topics that the candidates focused on according to the content of their quotes. From this we aim to learn the importance of the topics in an absolute relative context but also in regards to when a certain topic might have been very present and then. disappeared for some time. We furthermore want to see if there might be a candidate which sparked a topic or at least started talking/being quoted about it first. Two approaches are used to classify quotes:

1. Extracting and finding topics using Machine Learning (LDA).

2. Specifying topics by building a regular expression (regex). Done both for topics suggested by the LDA model as well as for a known topic to extract matching quotes.


### Topics extracted by the LDA
Several different LDA models were trained with the goal of finding topics which might  have been significant in 2016 during shorter periods of time but today are not well remembered. Due to the nature of the dataset this came with significant challenges since the entire data set as one big  piece of  text  was too large, but at the same time the individual documents (quotes) were too small. By grouping the quotes per day we created subdocuments for LDA to train on which yielded some pretty  interesting topics as listed in the table below, including the number of matching quotes.

|Topic Title| # Matching Quotes |
|    ---    |         ---       |
|Ted  Cruz|  719|
|Obamacare|  290|
|Healthcare|  438|
|Guns & Shootings| 1928|
|FBI Probe of 2016|  376|
|Russia| 2105|
|Khan Speech at the DNC|  342|
|Ted Cruz and JFK Conspiracy|   16|
|Crooked Hillary|  301|
|Trump praises Saddam Hussein|  147|
|Abortion|  231|

Out of the table above all topics were detected by our LDA model (and more). Some are about events many still remember, such as the FBI probe, which first reached the public in September of  2016. But some topics were a lot more short term and some of us in the team do not remember hearing about them before. An example of this is a short scandal which involved Trump “promoting” a conspiracy theory which  claimed that the father of  Ted Cruz’ (a rival republican candidate) was involved in the JFK assasination. Another one is a scandal which involved Donald Trump commenting in negatively about a US soldier who got killed in combat and happened to have been a muslim. The parents held a speech at the Democratic National Congress (DNC), which got a lot of attention at the time but few remember in hindsight. 

Since most quotes are very short our model did a terrible job at assigning them to a topic, which is why we decided to opt for regular expressions instead which performed significantly better. Below we present a selection of some interesting topics as mentioned throughout 2016.


<div>{%- include plots/ted__cruz.html -%}</div>

<div>{%- include plots/ted_cruz_and_jfk_conspiracy.html -%}</div>

<div>{%- include plots/guns_and_shootings.html -%}</div>

<div>{%- include plots/fbi_probe_of_2016.html-%}</div>


## Language
How does the quoted language of Clinton and Trump differ?

Intellectuality: Did they express different levels of intellectuality (more complicated words; more colloquial words)?
Sentiment: Did they address certain topics or people more positively or negatively?
Pronouns: How do the candidates use pronouns and what pronouns do they prefer?
### Intellectuality
Jokes were often made that, despite his world-class education, candidate Trump would only use simple words during his campaign. Some surmised that this might be an attempt to appeal to a broader audience, the regular American Joe, while others considered that his vocabulary simply was not mature enough.

Are these jokes accurate? __Was Clinton’s language more sophisticated than Trump’s?__

#### Syllables
First we looked for a simple predictor of language intellectuality: the __number of syllables__. We collated all of the quotes in our dataset together and counted the number of syllables in each word, not distinguishing when the same word appeared several times.

<div>{%- include plots/syllables.html -%}</div>

Here are some of the words we found in the quotes:
(give 3 words per class or so)

Though the syllable counting is done using course heuristics, there seems to be little difference between the two candidates. Maybe we ought to go deeper?

#### Language level
Instead of measuring word complexity using syllables, we can directly look at the English level classification of words used. The Common European Framework of Reference, or CEFR, is the grading system Europeans use to judge the __proficiency of English speakers__. The grades go from Basic (A1 and A2) to Independent (B1 and B2) to Proficient (C1 and C2).
In particular, English words can be given a CEFR rating: for example, “support” has level B2, which means we expect that a speaker with level B2 can use the word “support”.

Similarly to the syllables study, we took the list of all words and obtained their CEFR level from this [website](https://www.englishprofile.org/american-english).

Let us look at the distribution of words on the website first:

<div>{%- include plots/cefr.html -%}</div>

and now, after taking the language level of all the words in our quotes (notice some words might be counted more than one time):

<div>{%- include plots/cefr_candidates.html -%}</div>

where NA means the word did not exist in the CEFR dataset.

Again, the two distributions seem quite close, which runs counter to the hypothesis that Trump tended to use simpler words during the 2016 campaign. Further, the distribution looks somewhat like that of the CEFR dataset.

For Trump:

| NA   	| A1  	| A2	| B1	| B2	| C1   	| C2         	|
|----------|---------|-------|-------|-------|----------|----------------|
| lot  	| people  | will  | go	| talk  | campaign | able       	|
| american | country | know  | say   | deal  | allow	| voter      	|
| gon  	| want	| think | very  | put   | tough	| administration |
| trump	| good	| can   | would | state | attack   | radical    	|
| become   | well	| so	| make  | run   | debate   | founder    	|

For Clinton:

| NA   	| A1  	| A2	| B1	| B2   	| C1   	| C2    	|
|----------|---------|-------|-------|----------|----------|-----------|
| lot  	| people  | will  | go	| support  | campaign | voter 	|
| american | more	| can   | say   | talk 	| stand	| racist	|
| trump	| want	| know  | make  | put  	| attack   | able  	|
| become   | country | think | just  | together | security | reform	|
| nominee  | well	| work  | would | run  	| race 	| commander |


So far, the intellectuality route has not led us very far in distinguishing the discourse of our two candidates. Our next attempt is to look at sentimentality.



### Sentiment Analysis
This section compares the underlying sentiment of quotes uttered by Donald Trump versus Hillary Clinton towards typical political campaign issues such as immigration and health care, as well as specific topics that we have extracted in the Topic Extraction section.


**Method**

Our approach consists of filtering the quotes for a specific topic and performing sentiment analysis on each filtered quote.

In order to perform the sentiment analysis, we use NLTK’s Pre-Trained Sentiment Analyzer’s VADER (Valence Aware Dictionary and sEntiment Reasoner), which is well suited for analyzing short sentences.

For each quote, we get a “compound score” ranging between -1 and 1 (-1 being the most negative and +1 the most positive score). In order to understand the distribution of the sentiment for each candidate towards the selected topic, we plot the results on a histogram. We combine this histogram with a boxplot for each candidate, which enables us to better compare their distribution.

To better understand and compare the opinion of each candidate on the topic of interest, we use the polarity score of each quote to classify it as “negative” (score < -0.05), “neutral” (-0.05 < score < 0.05), or “positive” (score > 0.05). We then aggregate the results and, after normalizing them by the total number of quotes for each speaker (since the number of quotes is not the same for each candidate), plot them or a categorical bar chart.

#### Campaign Type
Before diving down into individual topics, we perform sentiment analysis over the whole dataset to get a general feel of the type of campaign that Donald Trump and Hillary Clinton ran.

When classifying the quotes as Negative, Neutral and Positive, we see that, even though there are slight differences between both candidates (Hillary Clinton has slightly more positive quotes than Donald Trump), both candidate’s quotes tend to be generally more positive than negative (about 10% more). 
<div>{%- include plots/sentiment_class_.html -%}</div>

According to the Inquiries Journal’s article *[“Comparing the Effectiveness of Positive and Negative Political Campaigns”](http://www.inquiriesjournal.com/articles/1311/comparing-the-effectiveness-of-positive-and-negative-political-campaigns)* by Gregory Peter, it seems that candidates have a better chance to win if they run a *positive* campaign rather than a *negative* campaign. 
This article describes a positive campaign as one where “a candidate focuses primarily on relevant issues, their own views, their own experiences, and their own virtues, without attacking their opponent in an attempt to gain votes.” On the other hand, “a negative campaign is one where a candidate uses attack ads and rhetoric to deliberately frame his opponent as foolish, inexperienced, irresponsible, disconnected, or evil as a means of presenting him or herself as a more desirable alternative to said opponent.”

From our analysis, it seems like both Hillary Clinton and Donald Trump have taken this into consideration in their campaign by uttering more positive statements than negative.



#### Immigration
The immigration topic was one of the most controversial topics in the 2016 election. Donald Trump promised to build a wall and deport illegal immigrants, while Clinton pledged to protect and integrate some illegal immigrants.

When analyzing the sentiment of quotes related to immigration, we can notice a difference between Donald Trump’s and Hillary Clinton’s sentiment: 45% of Hillary Clinton’s quotes related to immigration are positive, and 38% are negative. In contrast, 38% of Donald Trump’s quotes are positive, and 47% are negative. 

<div>{%- include plots/sentiment_class_immig.html -%}</div>


#### Obamacare 
Better known as Obamacare, the Affordable Care Act (ACA) was a policy enacted by President Obama in 2010 that was intended to improve access to health insurance for US citizens.
This ACA was one of the dominant issues of the 2016 presidential campaign. While Clinton pledged to “build” on Obamacare, Trump vowed to repeal the law.

Our sentiment analysis on this topic reflects this trend: 71% of Clinton’s quotes about Obamacare are positive, versus only 44% for Trump. On the other side of the spectrum, 12% of Clinton’s quotes are negative, versus 39% for Trump.

<div>{%- include plots/sentiment_class_obama.html -%}</div>


#### Target of Quotes
In terms of personal targets by the two candidates through their quotes, our analysis shows polar opposite views on political figures such as Bernie Sanders and Elizabeth Warren, two prominent socialist figures, as well as for more right-leaning figures Sarah Palin and Mitt Romney. However, it is interesting to note that overall, we saw that Trump expressed much more negativity towards his own political party members than did Clinton.

<div>{%- include plots/sentiment_class_Eliza.html -%}</div>
<div>{%- include plots/sentiment_class_Berni.html -%}</div>

**Conclusion**

While sentiment analysis on text can be helpful to show patterns, one must be very careful in its interpretation. Some aspects of the text might not be captured or interpreted correctly by the machine. For example, the tone, the sarcasm, or the negation of sentences can cause some misclassifications.

Also, the choice of keywords when filtering the quotes is critical. For example, quotes containing words or expressions about the same general topic but with opposite meanings can skew the results.
For example, if we take the topic of abortion and decide to analyze quotes containing either the words “pro-life” or “pro-choice,” the results of a speaker that is against abortion will be postive for the first keyword, and negative for the second. Therefore, if we look at the aggregated results, we will think this person is as positive as he or she is negative about this topic, which does not reflect the truth. 
To avoid this confusion, we selected quotes with keywords that belong to a specific side of the spectrum for each topic.



### Use of pronouns

A large part of analyzing someone's speech is not only about what they say, but how they say it. Indeed, people reveal who they are through their own words. Now besides content words such as nouns, regular & action verbs, and modifiers (adjectives and adverbs) that describe what a speaker is talking about, there is a separate class of words called style or function words (including pronouns) that, on their own, do not signify anything.

However, it turns out these function words are very good at indicating the current emotion of the speaker as well as how they think since they are processed differently in the brain. For instance, when someone is depressed, they will use the pronoun "I" more frequently in conversation*. There are also gender differences when it comes to function words: women tend to use more first-person words such as "I" or "we" whereas men prefer to use articles like "a" and "the".

Another interesting finding relates to the social class differences in language patterns. People from higher social classes tend to use more articles and prepositions compared to their lower class counterparts which use more pronouns and auxiliary verbs. This difference is known to be statistically significant.

How do these differences fare between Hillary Clinton and Donald Trump? As we can see, one noticeable difference is that Trump uses the first person pronoun “I” often, while Clinton employs the pronoun “we” more frequently.

As we’ve seen from the social difference of the use of pronouns, does Donald Trump target the lower and middle classes better? The heartland of America? It certainly helped Trump in his case, since listeners feel closer to the speaker when the word "I" is used more often instead of “we”. Yet, political advisors usually suggest to use  "we" more, which unfortunately creates the opposite effect: for example, during John Kerry's 2004 Presidential run, advisors clearly directed him to use “we” rather than “I”. However, it is very likely that knowing this wouldn't have changed the outcome in 2004 nor in 2016. Language is a powerful reflection of a person's personality and character but does not change a person on its own.

This is in fact a counterintuitive finding as well since, as a male, Donald Trump would be statistically much more likely to use more articles and nouns and less likely to use pronouns than Hillary Clinton, his female adversary. Donald Trump's high social status also does not account for this pronoun use by the Republican candidate.

<div>{%- include plots/pronoun_frequency.html -%}</div>

#### “Crooked Hillary”?

Trump famously popularized the harsh phrase "Crooked Hillary" to denote the dishonesty that he perceived from his opponent. But was there some basis for this statement? It turns out, deception can also be captured by language to some degree, and language analysis is almost as accurate as lie detectors. Most people, when telling the truth about an important situation, will more often use the pronoun "I" (which is in fact the single best predictor of a person's honesty*) as well as more negative emotion. However, in our case, Clinton used both less "I" and less negative emotion than Trump for most pronouns! This gives some evidence for the validity of Trump's nickname for Clinton, cruel as it may be…
	Trump also uses much more negative emotion words in sentences that use pronouns as can be seen above, especially for sentences containing “she”! Trump is known to have misogynist tendencies and now we see why, however this inordinate amount of negativity goes to show his level of honesty as well.

<div>{%- include plots/pronoun_sentiment.html -%}</div>

*Taken from Pennebaker, James W. The Secret Life of Pronouns. Bloomsbury Publishing.

## Conclusion
We studied the 2016 US presidential campaign of Hillary Clinton and Donald Trump through the quotes reported on the Internet.

Throughout our analysis, we searched for clues that might indicate how both conducted their campaigns, based on who quoted them, what they talked about and how they talked.

From the media bias side, we could not find a difference between how the two candidates were quoted, but our media bias dataset was perhaps not appropriate for a quotes dataset with such a variety of sources. In future work, we might try to impute the bias of all sources by comparing the quotes they report.

We found some very interesting topics from the LDA model we trained, some of which none of us remembered or had heard of. The regular expressions we built to extract quotes for some of the topics showed interesting patterns, such as Trump’s obsession with Ted Cruz, as well as more short term trends such as the DNC speech. Overall we are satisfied with the model performance but hope to find better ways to more scientifically classify quotes.

From the language side, it is a mixed bag: it seems that both candidates are similar in terms of intellectuality, while in terms of pronouns, there are clear differences in usage between the two, for example Clinton uses “she” in positive sentences more often.

In sum, while it is difficult to draw strong conclusions from our analysis, we have extracted some interesting information from the quotes database. Trump spoke more on certain topics (including conspiracy theories), and this might have given him the edge and put him over the top.


