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
        data_container = []
        #interating through all of the tweets. 
        #use "w" to write for a new file, "a" to append to add new data
        with open("sentiment_data.csv", "w") as csv_file:
            csv_writer = writer(csv_file)
            #The below line should be commented out depending on whether I'm appending or not. 
            csv_writer.writerow(["day", "state", "sentiment"])
            for tweet in self.iterator:
                if count != 2000:
                    day = 5
                    #Getting the text of the tweet.
                    #Using exceptions to catch when the tweets have errors. 
                    try:
                        tweet_text = json.dumps(tweet['text'])
                        # print(tweet_text)
                        # input()
                    except KeyError:
                        print('Error, but program will continue to function')
                    #Turning the tweet to a list
                    tweet_list = clean.turn_to_list(tweet_text)
                    #cleaning the tweet. 
                    tweet_list = clean.clean_tweet(tweet_list)
                    t_text = clean.tweet_to_string(tweet_list)
                    #Getting the language analysis of the tweet. 
                    sent_value = sentiment.examine_tweet(t_text)
                    #Getting the location of the tweet as well as more exception handling.  
                    try:
                        tweet_location = json.dumps(tweet['user']['location'])
                    except KeyError:
                        print('Error, but program will continue to function')
                    tweet_location = clean.location_to_lowercase(tweet_location)
                    state = clean.location_to_state(tweet_location)
                    print('Currently the program has analyzed: ', count, ' tweets.')
                    if state != None:
                        state = state.title()
                        csv_writer.writerow([day, state, sent_value])
                #breaking out of the loop when the counter reaches my specified number. 
                else: 
                    break 
                count += 1



tweet = Tweets()
tweet.get_tweet()
