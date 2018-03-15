#This file will contain the class to do the sentiment analysis on the tweet. 

#importing the textblob library. 
from textblob import TextBlob


class Language_Analysis: 

  #This method will actually get the sentiment value
  def examine_tweet(self, tweet):
    #This will get the parts of speech taging 
    blob = TextBlob(tweet)
    blob.tags 
    #Getting the noun phrases
    blob.noun_phrases 
    #This will get the exact value that I need.  
    value = blob.sentiment[0]
    return value



                    