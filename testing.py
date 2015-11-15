import sys
import json

def main():
	testing_file = open("testing.txt")
	for line in testing_file:
		diction = json.loads(line)
	print diction

if __name__ == '__main__':
	main()