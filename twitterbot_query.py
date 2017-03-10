# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

SCREEN_NAME = "WallStJesus"
KEYWORD = "$BAC"

def twtr1():
    for tweet in tweepy.Cursor(api.search, q=KEYWORD, lang="en").items(1):
        try:
            print tweet.text.encode('utf-8')
            print tweet.user.screen_name # <- gives user name
            print tweet.user.name # <- gives nickname
            print tweet.user.id # <- gives user id
            print tweet.created_at # gives tweet creation time
            print tweet.user.time_zone
            print tweet.geo
            print tweet.coordinates
            print tweet.user.location
            print tweet.user.created_at # <- gives account creation time
            print tweet.user.lang
            # print tweet.user.id_str # <- gives user id
            # print tweet.id
        except tweepy.TweepError as e:
            print(e.reason)
twtr1()

# Collect 200 tweets with KEYWORD, then select the ones from screen_name
def twtr2():
    for tweet in tweepy.Cursor(api.search, q=KEYWORD, lang="en").items(200):
        try:
            if tweet.user.screen_name == SCREEN_NAME:
                print tweet.text.encode('utf-8')
                print tweet.user.screen_name
                print tweet.created_at
                print tweet.user.time_zone
        except tweepy.TweepError as e:
            print(e.reason)
twtr2()

# Collect 200 tweets from screen_name, then select the ones with KEYWORD
def twtr3():
    for tweet in api.user_timeline(screen_name=SCREEN_NAME, count=200):
        if KEYWORD in tweet.text:
            try:
                print tweet.text.encode('utf-8')
                print tweet.user.screen_name
                print tweet.created_at
                print tweet.user.time_zone
            except tweepy.TweepError as e:
                print(e.reason)
twtr3()
