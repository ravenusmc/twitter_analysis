#This file will contain code that I'll test things out on. None of the code in this file will actually 
#be placed into the project. It's simply a place to test ideas. 

from textblob import TextBlob

tweet_one = """RT @AnnCoulter: No wonder Guillermo del Toro  refuses to go back to Mexico!  
He better hope Trump builds a really big wall! https://t.co/vZ\u2026"""

tweet_two = """No wonder Guillermo del Toro  refuses to go back to Mexico!  
He better hope Trump builds a really big wall!"""

########

tweet_three = """@amjoyshow @MichaelAvenatti This is what is going to get Trump impeached. 
Republican's aren't going to be able to i\u2026 https://t.co/afjcQFhOxf"""

tweet_four = """This is what is going to get Trump impeached. 
Republican's aren't going to be able to"""

######

tweet_five =  """RT @NatCookResists: Everyone, have your walking shoes 
ready!\ud83d\udea8\ud83d\udea8\ud83d\udea8\n\n#JohnDowd 
is calling for an end to the Mueller investigation \ud83d\ude30\n\n#AMJOY #Sa\u2026"""

tweet_six =  """Everyone, have your walking shoes 
ready! is calling for an end to the Mueller investigation"""


blob = TextBlob(tweet_six)
blob.tags 
#Getting the noun phrases
blob.noun_phrases 
#This will get the exact value that I need.  
value = blob.sentiment[0]
print(value)

#Value for tweet_one: 0.16666666666666666
#Value for tweet_two: 0.16666666666666666

#Value for tweet_three: 0.5
#value for tweet_four: 0.5

#Value for tweet_five: 0.0
#value for tweet_six: 0.25


