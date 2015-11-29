#Simple Twitter Sentiment Analysis

### `tweet_sentiment.py`: derive the sentiment of each tweet
Compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet. The file `AFINN-111.txt` contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score. Each word or phrase that is found in a tweet but not found in `AFINN-111.txt` should be given a sentiment score of 0. See the file `AFINN-README.txt` for more information. 

### `term_sentiment.py`:derive the sentiment of new terms
A script that computes the sentiment for the terms that do not appear in the file `AFINN-111.txt`. A naive way of doing this is the following. We know we can use the sentiment-carrying words in `AFINN-111.txt` to deduce the overall sentiment of a tweet. Once you deduce the sentiment of a tweet, you can work backwards to deduce the sentiment of the non-sentiment carrying words that do not appear in `AFINN-111.txt`. 

### `frequency.py`: compute term frequency
A Python script `frequency.py` to compute the term frequency histogram of the livestream data harvested. 

### 'top_ten.py': Top ten hashtags
A Python script `top_ten.py` that computes the ten most frequently occurring hashtags from the data.
