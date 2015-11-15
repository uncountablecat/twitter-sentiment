import sys
import json #convert JSON string into Python data structure

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #stdout = open('score_output.txt','w') #a output object

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
    #tweet_stream = open("output.txt")
    list_of_tweets = []; #creat a list to store tweets.each element is a dict
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
            print rating
    	    #stdout.write(str(rating)+"\n")     	   
    	    #print "[Tweet]:" + tweet + "\n"
    	    #print "[Score]:" + str(rating) + "\n" #don't forget to convert int to str

    	else:
            print 0
    		#print("There's no text in this tweet\n") #some of the tweets have no text


if __name__ == '__main__':
    main()
