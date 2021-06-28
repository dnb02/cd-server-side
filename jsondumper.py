import praw
import json
import os

clientSecret = os.environ.get('REDDIT_SECRET_KEY')
password = os.environ.get('BOTT_PASSWORD')
reddit = praw.Reddit(client_id='WvfB2YOqYcUlMg',client_secret=clientSecret,username='jsonbot',password=password,user_agent='prawtryv1')
with open('dump.json') as inp:
	dumpValue=json.load(inp)
selftext = str(dumpValue)
title = "-json-dump-"
reddit.subreddit("jsondump").submit(title, selftext=selftext)