# Reference: https://dototot.com/write-twitter-bot-python-tweepy-unfollow-non-followers-command-line/

# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
SCREEN_NAME = "SophieBot10000"

# Unfollow non-followers
followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)
 
for f in friends:
    if f not in followers:
        print "Unfollow {0}?".format(api.get_user(f).screen_name)
        answer = raw_input("Y/N?")
        if (answer == 'y') or (answer == 'Y'):
            api.destroy_friendship(f)
        else:
            pass
			
# Follow new followers
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print follower.screen_name
