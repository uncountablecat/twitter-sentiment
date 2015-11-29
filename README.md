#Simple Twitter Sentiment Analysis

##Goal
*access the twitter Application Programming Interface(API) using python
*Derive the sentiment of each tweet
Compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet. The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
The file AFINN-111.txt contains a list of pre-computed sentiment scores. Each line in the file contains a word or phrase followed by a sentiment score. Each word or phrase that is found in a tweet but not found in AFINN-111.txt should be given a sentiment score of 0. See the file AFINN-README.txt for more information.
*analyze the relationship between location and mood based on a sample of twitter data

#Files
*tweet_sentiment.py : calculate sentiment of each tweet based on a given dictionary
*term_sentiment.py : use a certain algorithm to calculate sentiment of words that are not included in the given dictionary
*frequency.py : calculate the frequency of hashtags
*top_ten.py : find the top ten popular hashtags
