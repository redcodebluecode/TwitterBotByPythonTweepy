# Reference: https://dototot.com/write-twitter-bot-python-tweepy-tweet-list-users/

# Import Tweepy, sleep, credentials.py
import tweepy, sys, time
from time import sleep
from random import randint
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def mention(handle_list,greetings):
    name_list = handle_list
    f = open(name_list, "r")
    h = f.readlines()
    f.close()
    for i in h:
        try:
            i = i.rstrip()
            m = i + " " + greetings
            s = api.update_status(status=m)
            nap = randint(1, 5)
            time.sleep(nap)
        except tweepy.TweepError as e:
            print(e.reason)    
mention("handles.txt", "Hello! Nice to meet you!")

def send_dm(handle_list,direct_message):
    f = open(handle_list, "r")
    h = f.readlines()
    f.close()
    for i in h:
        try:
            i = i.rstrip()
            api.send_direct_message(screen_name = i, text = direct_message)
            nap = randint(1, 5)
            time.sleep(nap)
        except tweepy.TweepError as e:
            print(e.reason)
send_dm("handles.txt", "Hello! This is my direct message to you.")
