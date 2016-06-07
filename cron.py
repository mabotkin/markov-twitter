import schedule
import time
import os
import main
import genDict

def job():
	genDict.genDict()
	print "Regenerated Markov Chain"
	print "Tweeted: " + str(main.post())

schedule.every().hour.do(job)

job()
while 1:
	schedule.run_pending()
	time.sleep(1)
