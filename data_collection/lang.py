#This file will contain the class to do the sentiment analysis on the tweet. 

#importing the textblob library. 
from textblob import TextBlob


class Language_Analysis: 

  def examine_tweet(self, tweet):
    #This will get the parts of speech taging 
    blob = TextBlob(tweet)
    blob.tags 
    #Getting the noun phrases
    blob.noun_phrases 
    #This will get the exact value that I need.  
    value = blob.sentiment[0]
    return value


    
# test = Language_Analysis()
# test.examine_tweet(textFour)
                    








#### SCRAP Code down here. 
#This one returns 0, 0.25, 0
# text = """RT @AnnCoulter: No wonder Guillermo del Toro  refuses to go back to Mexico!  
# He better hope Trump builds a really big wall! https://t.co/vZ\u2026"""  

# #This one returns 0, 0.25
# textTwo = """RT No wonder Guillermo del Toro refuses to go back to Mexico! He better hope Trump 
# builds a really big wall!"""

# textThree = "I'm great! I have a great life! Everyone loves me"



# for sentence in blob.sentences:
#     sent = sentence.sentiment.polarity
#     print(sent)