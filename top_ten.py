import sys
import json #convert JSON string into Python data structure

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def getKey(item):
    return item[1]

def main():
    tweet_stream = open(sys.argv[1])
    list_of_tweets=[]
    for line in tweet_stream:
        list_of_tweets.append(json.loads(line))

    #load hashtags to a dictionary
    hashtags = {}

    for tweet in list_of_tweets:
        if 'entities' in tweet:
            if 'hashtags' in tweet['entities']:
                #print "FOUND hashtag"
                entities = tweet['entities']
                hashtag = entities['hashtags']
                if len(hashtag) != 0:
                    hashtag = hashtag[0]
                    hashtag = hashtag['text']
                    if hashtag in hashtags:
                        hashtags[hashtag]=hashtags[hashtag]+1
                    else:
                        hashtags[hashtag]=1

    sorted_hashtags = [(k,v) for v,k in sorted([(v,k) for k,v in hashtags.items()],reverse=True)]
    #trick from http://bytesizebio.net/2013/04/03/stupid-python-tricks-3296-sorting-a-dictionary-by-its-values/

    for i in range(0,10):
        print (sorted_hashtags[i])[0],
        print (sorted_hashtags[i])[1]


if __name__ == '__main__':
    main()
