import re
import random
import twitter
import unicodedata

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

for account in accounts:
	statuses = api.GetUserTimeline(screen_name=account)
	print "Processing " + account
	for tweet in statuses:
		tweets.append(process(tweet.text))

tree = {}
cur = tree

for tweet in tweets:
	for word in tweet:
		if word in cur:
			cur = cur[word]
		else:
			cur[word] = {}
			cur = cur[word]
	cur['END_TWEET'] = ""
	cur = tree

def genTweet():
	cur = tree
	tweet = ""
	while True:
		nex = random.sample(cur.keys(),1)[0]
		if nex == 'END_TWEET':
			break
		tweet += " "
		tweet += nex
		cur = cur[nex]
	return tweet

x = genTweet()
while len(x.split(" ")) < 10:
	x = genTweet()
