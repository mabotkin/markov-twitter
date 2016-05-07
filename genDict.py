import re
import random
import twitter
import unicodedata
from pickle import dump

keyIn = open("keys.txt").read().splitlines()
api = twitter.Api(consumer_key=keyIn[0],consumer_secret=keyIn[1],access_token_key=keyIn[2],access_token_secret=keyIn[3])

accounts = open("accounts.txt").read().splitlines()

tweets = []

def process(text):
	text = text.replace("\n"," ")
	text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
	escapes = ''.join([chr(char) for char in range(1, 32)])
	text = text.translate(None,escapes)
	#text = " ".join(filter(lambda x:x[0]!='@', text.split()))
	return text.split(" ")

def genDict():
	for account in accounts:
		statuses = api.GetUserTimeline(screen_name=account)
		print "Processing " + account
		for tweet in statuses:
			tweets.append(process(tweet.text))
	dic = {}
	prev = ""
	for tweet in tweets:
		for word in tweet:
			if prev in dic:
				dic[prev].append(word)
			else:
				dic[prev] = []
				dic[prev].append(word)
			prev = word
	fout = open('dict.pkl','wb')

	dump(dic,fout,protocol=2)

	fout.close()

