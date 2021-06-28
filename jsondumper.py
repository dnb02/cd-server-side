import praw
import json
import os

clientSecret = os.environ.get('REDDIT_SECRET_KEY')
password = os.environ.get('BOTT_PASSWORD')
reddit = praw.Reddit(client_id='WvfB2YOqYcUlMg',client_secret=clientSecret,username='jsonbot',password=password,user_agent='prawtryv1')
selftext = str({'k':'l','m':'j'})
title = "PRAW documentation"
reddit.subreddit("jsondump").submit(title, selftext=selftext)