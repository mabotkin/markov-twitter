import schedule
import time
import os
import main
import genDict

def job():
	main.post()

def update():
	genDict.genDict()

schedule.every().hour.do(job)
schedule.every().day.at("00:05").do(update)

while 1:
	schedule.run_pending()
	time.sleep(1)
