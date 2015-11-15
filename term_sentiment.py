import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

    #this part loads the sentiment scores
    afinnfile = sent_file
    scores = {} #empty dictionary
    for line in afinnfile: # 'line' seems to be a built-in object...
        term, score = line.split("\t")
        scores[term] = int(score)
    #print scores.items()

    #this part loads the twitter stream
    list_of_tweets = []; #creat a list to store tweets.each element is a dict
    score_of_tweets = []; #another list to store the score of each tweet
    for line in tweet_file:
        list_of_tweets.append(json.loads(line))
    #print(len(list_of_tweets))

    #try to come up with a score...
    for i in list_of_tweets:
        if 'text' in i:
            rating = 0
            tweet = i["text"]
            wordlist = tweet.split() #becomes a list of words
            for word in wordlist:
                if word in scores:
                    rating = rating + scores[word]
            score_of_tweets.append(rating)
            #print rating
            #stdout.write(str(rating)+"\n")            
            #print "[Tweet]:" + tweet + "\n"
            #print "[Score]:" + str(rating) + "\n" #don't forget to convert int to str
        else:
            score_of_tweets.append(0);
            #print 0
            #print("There's no text in this tweet\n") #some of the tweets have no text
    #print score_of_tweets

    #assign sentiment to words not in dic
    new_word = {}; #to store word and score
    j = 0; #just a counter
    for i in list_of_tweets:
        if 'text' in i:
            tweet = i['text']
            wordlist = tweet.split() #tweet becomes a list of words
            for word in wordlist:
                if word not in scores:
                    if word not in new_word:
                        new_word[word]=score_of_tweets[j]
                    else:
                        new_word[word]=new_word[word] + score_of_tweets[j]
        j = j + 1

    #print the score of new words
    for word in new_word:
        print word +' '+str(new_word[word])



if __name__ == '__main__':
    main()
