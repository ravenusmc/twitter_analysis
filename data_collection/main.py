#The purpose of this file is to build the CSV file that I will use to build the data visualization 

#importing libraries for this project. 
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json

from test import *

print(name)

#Twitter API information. 
ACCESS_TOKEN = '2958973129-snuOBkA0uEncZrUJ6sPd8J43FnRrYO5ewUMIlK5'
ACCESS_SECRET = 'NM8s7gcF0RFrrakKqZgFi6nHJUDyFA1bYK5Q84VS2e7Rh'
CONSUMER_KEY = 'LZ7rRbyPtW27zw5aRbBF9f6zh'
CONSUMER_SECRET = 'i5uel1CC3Ozl6WymosCTuGSI8mPObUetoAII4tfy1yBadHQ7YC'

#Getting authorization from the API. 
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()
iterator = twitter_stream.statuses.filter(track="Trump", language="en")

tweet_count = 3
for tweet in iterator:
  tweet_count -= 1
  #print(json.dumps(tweet['id'])) 
  print(json.dumps(tweet['text']))
  print(json.dumps(tweet['user']['location']))
  input()