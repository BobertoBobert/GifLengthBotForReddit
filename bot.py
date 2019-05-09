#!/usr/bin/python
import praw
import re
from test import submissionHandling
reddit = praw.Reddit('bot1')


subreddit = reddit.subreddit('MetaMakesNamesEasier')



for submission in subreddit.stream.submissions():
	print('Title: ' + submission.title)
	print(submission.url)
	submissionHandling(submission)
	print("\n\n--------------------\n\n")
