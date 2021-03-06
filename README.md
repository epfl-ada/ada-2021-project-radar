# Trump vs Clinton: the 2016 Presidential election through their own words

[Our Data Story](https://epfl-ada.github.io/ada-2021-project-radar/)

## Abstract

"I've just received a call from Secretary Clinton," said Donald Trump late in the night of Nov 8, 2016. The result of the 58th Presidential election, an intense battle between Donald Trump and Hillary Clinton, remains a major upset around the world. But was it? What can be seen and understood from this election, using only quotes by these candidates in the media? This could give a glimpse into the running of a major democratic election system, and the importance that speech and its representations have in making citizens turn for one party or another. Media biases have deep implications in our lives, and have evolved to be more extreme in this noisy world. We will analyze how Trump and Clinton's words quoted in media outlets relate to the polarization seen during the 2016 U.S. election.

## Research questions answered on the Website

### _Media bias_: Do media outlets portray Trump and Clinton differently?

1. **Coverage**: Did the outlets report different quotes at a given point in time? For a given outlet, was the average valence of reported quotes the same for the two candidates?
2. **Bias**: Does the bias of the news outlets correlate with our previous findings?

### _Political topics_: Did Clinton and Trump address political issues differently?

1. **Topics**: What topics got discussed?
2. **Focus**: Who focused on which topic?

### _Language_: How does the quoted language of Clinton and Trump differ?

1. **Intellectuality**: Did they express different levels of intellectuality (more complicated words; more colloquial words)?
2. **Sentiment**: Did they address certain topics or people more positively or negatively?
3. **Pronouns**: How do the candidates use pronouns and what pronouns do they prefer?

## Additional datasets

### Media bias

- It would be interesting to find a dataset ranking news outlets by popularity. So far the closest we've come to finding one is [here](https://www.similarweb.com/fr/top-websites/united-states/category/news-and-media/)
- It would help to find a dataset to match a URL to the news outlet name
- Media bias data ([AllSides](https://www.kaggle.com/supratimhaldar/allsides-ratings-of-bias-in-electronic-media))


### Language

- **Datasets for common English words**
  - English [adjectives](https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913)
  - English [verbs](https://www.wordexample.com/list/most-common-verbs-english/)
  - NLTK stopwords

#### Intellectuality

- Using [The EnglishProfile website](https://www.englishprofile.org/american-english) we assigned each word in American English to a CEFR level (A1 to C2), so we scraped it with [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) for the data we need; the cleaning is detailed in the notebook.

## Methods

### Media bias

- Compute the positivity score of quotes (using the NLTK library), and use this to observe whether for a given outlet, quotes from one candidate are more positive than the other.
- Using the AllSides data, look at whether the difference in positivity score correlates with the bias of the outlet.
- Consider for each quote, the average bias of the outlets which reported it.

### Political topics

In identifying political topics we went with a hybrid approach which was different from what we planned for, but the data did not allow something else (we know of):

- **Extract quotes using LDA**
- **Assign topics to quotes using regular expressions**

### Language

#### Intellectuality

- Measure intellectuality of words by the number of syllables. For this, the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) allows us to divide words into phonemes and the [syllables package](https://pypi.org/project/syllables/) uses heuristics which is a bit less precise but much faster.
- Evaluate the average English level of a speaker in terms of the CEFR level associated with each word they use, using the CEFR level dataset.
- Evaluate words based on their commonality in the English language.
- It might also be interesting to count the number of unique words across the whole quotes uttered.
- If we can find an appropriate dataset, we could measure the proportion of formal versus colloquial words.

#### Sentiment

We categorized the quotes as "negative", "neutral" or "positive". 
- Using existing libraries such as [NLTK Pre-Trained Sentiment Analyzer](https://www.nltk.org/api/nltk.sentiment.html), as they usually are very efficient and will allow us to focus on the data analysis rather than the technical implementation of the algorithms.

- Perform sentiment analysis on the target of quotes using NLTK. For instance, Trump calling Clinton "Crooked Hillary" would be a negative statement about Presidential candidate Clinton.

#### Pronouns

- Use regular expressions to get the number of times that "I", "we", "they", "them" were uttered.

## Timeline
This was our schedule which we partly complied with, but as expected not everything went according to plan, but we reached our goals nonetheless.

![](./assets/gantt.png)

## Organization

- **Auguste**: Language intellectuality, media bias analysis, organisation of codebase.
- **Francis**: Project management, sentiment analysis, data visualisation and web integration.
- **Dean**: Website setup, political topics analysis and data visualisation.
- **Leonard**: Sentiment analysis, natural language processing.

