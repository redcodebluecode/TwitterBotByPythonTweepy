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

def twtr():
    for tweet in tweepy.Cursor(api.search, q=KEYWORD, lang="en").items(1):
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
twtr()

#################################################################
# not working
# def twtr2():
#     raw_tweets = tweepy.Cursor(api.search, q=KEYWORD, lang="en").items(50)
#　    for tweet in raw_tweets:
#         if tweet['user']['screen_name'] == SCREEN_NAME:
#             print tweet
# twtr2()

#################################################################
# not working
# def twtr3():
#     raw_tweets = tweepy.Cursor(api.search, q=KEYWORD, lang="en").items(50)
#     for tweet in raw_tweets:
#         load_tweet = json.loads(tweet)
#         if load_tweet['user']['screen_name'] == SCREEN_NAME:
#             print tweet
# twtr3()

#################################################################
for tweet in tweepy.Cursor(api.search, q=KEYWORD, lang="en").items(200):
    if tweet.user.screen_name == SCREEN_NAME:
	    print tweet.text
	    print tweet.user.screen_name
	    print tweet.created_at
	    print tweet.user.time_zone
