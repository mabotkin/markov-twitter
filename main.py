import re
import random
import twitter
import unicodedata
import language_check
from pickle import load

keyIn = open("keys.txt").read().splitlines()
api = twitter.Api(consumer_key=keyIn[0],consumer_secret=keyIn[1],access_token_key=keyIn[2],access_token_secret=keyIn[3])

accounts = open("accounts.txt").read().splitlines()

tweets = []

def proofread(text):
	tool = language_check.LanguageTool('en-US')
	matches = tool.check(text)
	text = language_check.correct(text,matches)
	text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
	return text

def genTweet():
	dic = load(open("dict.pkl","rb"))
	tweet = ""
	last = random.choice(dic[random.sample(dic.keys(),1)[0]])
	tweet += last
	tweet += " "
	while len(tweet) < 140:
		prevtweet = tweet
		word = ""
		if last in dic:
			word = random.choice(dic[last])
		else:
			word = random.choice(dic[random.sample(dic.keys(),1)[0]])
		if word == "&amp;":
			last = word
		else:
			tweet += word
			tweet += " "
			last = word
	prevtweet = prevtweet[:-1]
	if len(prevtweet) >= 140:
		return genTweet()
	prevtweet = proofread(prevtweet)
	return prevtweet

def post():
	tweet = genTweet()
	try:
		api.PostUpdate(tweet)
	except:
		tweet = genTweet()
		api.PostUpdate(tweet)
	return tweet
#fout = open("log.txt","w")
#fout.write(tweet + "\n")
#fout.close()
