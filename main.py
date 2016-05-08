import re
import random
import twitter
import unicodedata
from pickle import load

keyIn = open("keys.txt").read().splitlines()
api = twitter.Api(consumer_key=keyIn[0],consumer_secret=keyIn[1],access_token_key=keyIn[2],access_token_secret=keyIn[3])

accounts = open("accounts.txt").read().splitlines()

tweets = []


def genTweet():
	dic = load(open("dict.pkl","rb"))
	tweet = ""
	last = random.choice(dic[random.sample(dic.keys(),1)[0]])
	tweet += last
	tweet += " "
	while len(tweet) < 140:
		prevtweet = tweet
		if last in dic:
			word = random.choice(dic[last])
		else:
			word = random.choice(dic[random.sample(dic.keys(),1)[0]])
		tweet += word
		tweet += " "
		last = word
	return prevtweet[:-1]

def post():
	tweet = genTweet()
	api.PostUpdate(tweet)
	return tweet
#fout = open("log.txt","w")
#fout.write(tweet + "\n")
#fout.close()
