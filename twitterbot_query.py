# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, screen_name=USER, q="KEYWORD", since="2017-03-04", until="2017-03-05", lang="en").items(20):
    print('Tweet by: @' + tweet.user.screen_name + ' about KEYWORD: ' + tweet.text)
