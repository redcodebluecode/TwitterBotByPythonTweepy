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
# for tweet in tweepy.Cursor(api.search, screen_name=SCREEN_NAME, q=KEYWORD, since="2017-02-07", until="2017-03-05", lang="en").items(20):
    # print('Tweet by: @' + tweet.user.screen_name + ' about KEYWORD: ' + KEYWORD + tweet.text)
for tweet in tweepy.Cursor(api.search, q=KEYWORD, lang="en").items(20):
    print 'tweet:' + tweet + '/n tweet.text:' + tweet.text + '/n tweet.from_user:' + tweet.from_user + '/n tweet.screen_name:' + tweet.screen_name + '/n tweet.time:' + tweet.time
