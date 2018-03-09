#This file will contain the class to pull in the the tweets from the twitter api. 

#importing third party libraries for this project. 
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json

#importing personal libaries for the project. 
#This file will contain all of the keys for the twitter API. 
from keys import *
from clean import *
from lang import *


class Tweets():

    def __init__(self):
        self.oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
        self.twitter_stream = TwitterStream(auth=self.oauth)
        self.iterator = self.twitter_stream.statuses.filter(track="Trump", language="en")

    def get_tweet(self):
        #Creating the clean object
        clean = Clean()
        #Creating the language sentiment object
        sentiment = Language_Analysis()
        #setting a count 
        count = 0
        #interating through all of the tweets. 
        for tweet in self.iterator:
            if count != 4:
                #Getting the location of the tweet. 
                tweet_location = json.dumps(tweet['user']['location'])
                print(tweet_location)

                #Getting the text of the tweet.
                tweet_text = json.dumps(tweet['text'])
                print(count)
                print(tweet_text)
                print('---------------------')
                #Turning the tweet to a list
                tweet_list = clean.turn_to_list(tweet_text)
                #cleaning the tweet. 
                tweet_list = clean.clean_tweet(tweet_list)
                tweet = clean.tweet_to_string(tweet_list)
                print(tweet)
                #Getting the language analysis of the tweet. 
                sent_value = sentiment.examine_tweet(tweet)
                # print(type(sent_value))
                
                # input()
                
                # print(json.dumps(tweet['text']))
                #print(json.dumps(tweet['user']['location']))
            #breaking out of the loop when the counter reaches my specified number. 
            else: 
                break 
            count += 1



test = Tweets()
test.get_tweet()


#Getting authorization from the API. 
#oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
#twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()
#iterator = twitter_stream.statuses.filter(track="Trump", language="en")


# for tweet in iterator:
#   #print(json.dumps(tweet['id'])) 
#   print(json.dumps(tweet['text']))
#   print(json.dumps(tweet['user']['location']))
#   input()