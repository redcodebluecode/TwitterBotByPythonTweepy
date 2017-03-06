# Reference：https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library

# Add all import statements at top of file
import tweepy
from time import sleep

# Import our Twitter credentials from credentials.py
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file helloworld.txt (or your chosen file) for reading
my_file = open('helloworld.txt', 'r')

# Read lines one by one from my_file and assign to file_lines variable
file_lines = my_file.readlines()

# Close file
my_file.close()

# Create a for loop to iterate over file_lines
for line in file_lines:
# Add try ... except block to catch and output errors
    try:
        print(line)
	# Add if statement to ensure that blank lines are skipped
        if line != '\n':
            api.update_status(line)

	# Add an else statement with pass to conclude the conditional statement
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
# Add sleep method to space tweets by 5 seconds each
    sleep(5)
