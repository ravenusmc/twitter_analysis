# twitter_analysis
## Intro

This program will use a language sentiment analysis library, TextBlog, to analyze tweets from twitter in a particular subject. I will then take categorize as many tweets as I can from the state that they came from and include the language analysis of the tweet into the state information. 

Thus, a tweet from California that has a sentiment analysis of .54 will be placed into the tweets from CA and those sentiments will then be averaged. I will then hope to graph the data using D3.JS onto a map of the U.S and show how certain tweets will change over time. 

This project is a proof of concept. Its goal is to see if something like this would work and how it would look. As always, I'm up for the challenge! 


# Getting started
### Installing

1. Clone the repo
2. Run [sudo] pip3 install or pip3 install flask
3. Run python3 main.py to run the application
6. Visit localhost:5000 to see the application

### Technology Stack

1. Flask-0.12
2. Python-3.4
3. Pandas-0.18.1
4. Numpy-1.11.0
5. MySQL-5.6.26
6. D3.JS-3.5
7. TextBlob

### Operation

Once the program is downloaded, simply run the program as you would any other python program.
Then follow the address, which your console/terminal tells you to go to see the
website.

# Issues / Other

# Comments: 

First, I was going to include this information on a webpage on this project but decided to include it here for anyone that comes across this repo. Most of the Tweets came in looking something like this: 

RT @AnnCoulter: No wonder Guillermo del Toro  refuses to go back to Mexico!  
He better hope Trump builds a really big wall! https://t.co/vZ\u2026

Now, in using textblog I wondering if the RT or @ sign would through the sentiment analysis off. So I did a quick test of three tweets:

tweet_one = """RT @AnnCoulter: No wonder Guillermo del Toro  refuses to go back to Mexico!  
He better hope Trump builds a really big wall! https://t.co/vZ\u2026"""

tweet_two = """No wonder Guillermo del Toro  refuses to go back to Mexico!  
He better hope Trump builds a really big wall!"""

tweet_three = """@amjoyshow @MichaelAvenatti This is what is going to get Trump impeached. 
Republican's aren't going to be able to i\u2026 https://t.co/afjcQFhOxf"""

tweet_four = """This is what is going to get Trump impeached. 
Republican's aren't going to be able to"""

tweet_five =  """RT @NatCookResists: Everyone, have your walking shoes 
ready!\ud83d\udea8\ud83d\udea8\ud83d\udea8\n\n#JohnDowd 
is calling for an end to the Mueller investigation \ud83d\ude30\n\n#AMJOY #Sa\u2026"""

tweet_six =  """Everyone, have your walking shoes 
ready! is calling for an end to the Mueller investigation"""

Notice that in the even number tweets I cleaned up the tweet the best that I could. The sentiment analysis that I got back from each group was the following:

Value for tweet_one: 0.16666666666666666
Value for tweet_two: 0.16666666666666666

Value for tweet_three: 0.5
value for tweet_four: 0.5

Value for tweet_five: 0.0
value for tweet_six: 0.25

Thus, except for the last group, tweets five and six, text blog gave back the same analysis whether or not the tweet was cleaned up or not. I could carry this experiment out further but just wanted to see how much things differed between a clean and 'dirty' tweet. 

However, examining the tweets further, tweet five I would say is almost a negative tweet against Trump. Yet, it has a score of 0.0 and the cleaned version of 0.25. Tweet four is also what I consider a negative tweet against Trump and it has a score of 0.5. Thus, Text blog, in my case, does not seem 100% accurate. However, getting a bunch of tweets from one state, analysing them I hope to get a better picture of that state. Much like flipping a coin a trillion times you will eventually get 50% of the time heads and the other 50% tails. 
However, in the end, this project was a proof of concept and I think it worked out really well. 


# Preview

To see a video that talks about this project please go here:

Blog entry:
