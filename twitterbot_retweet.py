# Reference: https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library

# Import Tweepy, sleep, credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For loop to iterate over tweets with #ocean, limit to 10
for tweet in tweepy.Cursor(api.search, q='#ocean').items(10):
    try:
# Print out usernames of the last 10 people to use #ocean
# Add \n escape character to print() to organize tweets
	    print('\nTweet by: @' + tweet.user.screen_name)
    
# Retweet tweets as they are found
        tweet.retweet()
		print('Retweeted the tweet')

# Favorite the tweet
        tweet.favorite()
		print('Favorited the tweet')

# Follow the user who tweeted
        if not tweet.user.following:
		    tweet.user.follow()
		    print('Followed the user')

        sleep(5)
		
	except tweepy.TweepError as e:
	    print(e.reason)
		
    except StopIteration:
	    break
