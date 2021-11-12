# ADA-2021: Project RADAR

**Team:** RADAR

**Topic:** Trump vs Clinton: the 2016 Presidential election through their own words

We will evaluate this milestone according to how well these steps have been done and documented, the quality of the code and its documentation, the feasibility and critical awareness of the project. We will also evaluate this milestone according to how clear, reasonable and well thought-through the project idea is. Please use the second milestone to really check with us that everything is in order with your project (idea, feasibility, etc.) before you advance too much with the final Milestone 3! There will be project office hours dedicated to helping you.


--- 

# Trump vs Clinton: the 2016 Presidential election through their own words

## Abstract

“I’ve just received a call from Secretary Clinton,” said Donald Trump late in the night of Nov 8, 2016. The result of the 58th Presidential election, an intense battle between Donald Trump and Hillary Clinton, remains a major upset around the world. But was it? What can be seen and understood from this election, using only quotes by these candidates in the media? This could give a glimpse into the running of a major democratic election system, and the importance that speech and its representations have in making citizens turn for one party or another. Media biases have deep implications in our lives, and have evolved to be more extreme in this noisy world. We will analyze how Trump and Clinton’s words quoted in media outlets relate to the polarization seen during the 2016 U.S. election.

## Research Questions

> A list of research questions you would like to address during the project.

### Media bias: Do media outlets portray Trump and Clinton differently?
- Do media outlets quote the two candidates equally much?
- What type of quotes do they use for the different candidates?
- Does the bias of the news outlet correlate with the quotes they report?

### Political topics: Did Clinton and Trump both address the same political issues?
- How did they address the topics? 
- Was there a candidate that started a topic? “Trend Setter”...
- Did they address issues when they were being discussed in general?

### Language: How does the quoted language of Clinton and Trump differ?
- Did they use different language registers (more complicated words; more colloquial words)?
- Did they express different levels of valence (more positive or negative?)
- Pronouns are powerful. “Yes WE can...”. How do the candidates use pronouns and what pronouns do they prefer?

### Further Ideas
- Which speakers mention the candidates, and what do they say about them?



## Proposed additional datasets
> List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.

### Media bias
- It would be interesting to find a dataset ranking news outlets by popularity. So far the closest we’ve come to finding one is [here](https://www.similarweb.com/fr/top-websites/united-states/category/news-and-media/)
- It would help to find a dataset to match a URL to the news outlet name
- Media bias data ([AllSides](https://www.kaggle.com/supratimhaldar/allsides-ratings-of-bias-in-electronic-media))

### Political topics
It would be interesting to use data which helps us understand what happens outside of the small universe of Trump and Clinton quotes so that we can put the data in context.

- Scraping Newspapers for political topics (CNN, Breitbart, Fox, etc)
    - Two of us are comfortable using web scraping frameworks.
    - Paywalls could be a problem but the titles are usually open and include the topic of an article. Otherwise we have the internet archive.
    - Services such as Cloudflare could cause problems.

- Dataset of political topics of importance to citizens of the US.
    - Polling services such as Gallup, YouGov, Statista, Pew, etc. have plenty  of historic data.


### Language

- CEFR language levels data:  [This site](https://www.englishprofile.org/american-english) assigns each word in American English to a CEFR level. We scraped the data we needed with [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/). The cleaning is detailed in the notebook.

## Methods

### Media bias
We would build a dataset containing, for each major outlet, all the quotes they reported, detailed by candidate. We would then use sentiment analysis (similarly as in Levels of Valence) to categorize quotes based on their positivity score (using the NLTK library). This would also allow us to see the different amount of quotes by each candidate in media outlets and visualize the difference.

### Political topics
In identifying political topics we will go with a hybrid approach:

1. Quotes covering the most prominent topics such as

    There are many extensive lists of prominent political topics and issues during the election online ([Pew 2016](https://www.pewresearch.org/politics/2016/07/07/4-top-voting-issues-in-2016-election/)). Regex' should allow us to find most quotes regarding a topic.
    
    Examples: Guns, Health Care, Obamacare (see Notebook for PoC), Abortion, etc

2. Find less obvious topics or subtopics by analysing the quote content.

    An example could be a specific shooting or scandal which is usually only talked about for some days or 1-2 weeks, but not the entire election cycle.
    - Using EDA by iteratively filtering out certain words starting with pronouns, adjectives, etc. and slowly moving down until we can see a pattern emerging with only meaningful words. We then classify and remove topics step by step until we hopefully end up with a new set of less prominent topics.
    - Using a ML approach such as LDA.



## Proposed timeline


## Organization within the team
> A list of internal milestones up until project Milestone 3.



## Questions for TAs (optional)

- 

## Notebook containing initial analyses and data handling pipelines

Notebook: [Milestone2.ipynb](./Milestone2.ipynb)

