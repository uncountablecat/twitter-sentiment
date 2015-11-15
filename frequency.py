import sys
import json

def main():
	tweet_file = open(sys.argv[1])

	word_count = {}

	#load tweet stream into a list
	tweet_stream = []
	for line in tweet_file:
		tweet_stream.append(json.loads(line))

	for tweet in tweet_stream:
		if 'text' in tweet:
			content = tweet['text']
			wordlist = content.split()
			for word in wordlist:
				if word in word_count:
					word_count[word] = word_count[word]+1.0
				else:
					word_count[word] = 1.0

	num_words = 0.0
	for word in word_count:
		num_words = num_words + word_count[word]

	for word in word_count:
		print word + ' ' + str(word_count[word]/num_words)

if __name__ == '__main__':
	main()
