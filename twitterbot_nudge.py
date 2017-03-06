# Reference: https://dototot.com/write-twitter-bot-python-tweepy-tweet-list-users/

# Import Tweepy, sleep, credentials.py
import tweepy, sys
from time import sleep
from random import randint
from credentials import *

handles = sys.argv[1]
f = open(handles, "r")
h = f.readlines()
f.close()
 
for i in h:
    i = i.rstrip()
    m = i + " " + sys.argv[2]
    s = api.update_status(m)
    nap = randint(1, 60)
    time.sleep(nap)

# To run the python program
# python twitter_nudge.py handles.txt "Hello"
