#This file will clean the text of the tweet

from csv import writer

class Clean():

    #This method will turn the tweet to a list
    def turn_to_list(self, tweet):
        tweet_list = tweet.split()
        return tweet_list

    #This method will clean the tweet and pull out values that I believe may 
    #affect the analysis.
    def clean_tweet(self, tweet_list):
        count = 0
        while count < len(tweet_list):
          if tweet_list[count][0:2]  == 'RT':
            del tweet_list[count]
          elif tweet_list[count][0:5] == 'https':
            del tweet_list[count]
          elif tweet_list[count][0] == '@':
            del tweet_list[count]
          else: 
            count += 1
        return tweet_list

    #This will turn the tweet back to a string from a list so that it can be placed into the 
    #sentiment anaylis program. 
    def tweet_to_string(self, tweet_list):
        tweet = ' '.join(tweet_list)
        return tweet

    #This method will ensure that the location portion of the tweet is all lowercase. 
    def location_to_lowercase(self, tweet_location):
        tweet_location = tweet_location.lower()
        return tweet_location

    #This method will place the location by state. I wrote this by hand. It was not fun. 
    def location_to_state(self, tweet_location):
        if 'alabama' in tweet_location or 'al ' in tweet_location:
            state = "alabama"
        elif 'alaska' in tweet_location or 'ak ' in tweet_location:
            state = "alaska"
        elif 'arizona' in tweet_location or 'az ' in tweet_location:
            state = "arizona"
        elif 'arkansas' in tweet_location or 'ar ' in tweet_location:
            state = "arkansas"
        elif 'california' in tweet_location or 'ca ' in tweet_location:
            state = "california"
        elif 'colorado' in tweet_location or 'co ' in tweet_location:
            state = "colorado"
        elif 'connecticut' in tweet_location or 'ct ' in tweet_location:
            state = "connecticut"
        elif 'delaware' in tweet_location or 'de ' in tweet_location:
            state = "delaware"
        elif 'florida' in tweet_location or 'fl ' in tweet_location:
            state = "florida"
        elif 'georgia' in tweet_location or 'ga ' in tweet_location:
            state = "georgia"
        elif 'hawaii' in tweet_location or 'hi ' in tweet_location:
            state = "hawaii"
        elif 'idaho' in tweet_location or 'id ' in tweet_location:
            state = "idaho"
        elif 'illinois' in tweet_location or 'il ' in tweet_location:
            state = "illinois"
        elif 'indiana' in tweet_location or 'in ' in tweet_location:
            state = "indiana"
        elif 'iowa' in tweet_location or 'ia ' in tweet_location:
            state = "iowa"
        elif 'kansas' in tweet_location or 'ks ' in tweet_location:
            state = "kansas"
        elif 'kentucky' in tweet_location or 'ky ' in tweet_location:
            state = "kentucky"
        elif 'louisiana' in tweet_location or 'la ' in tweet_location:
            state = "louisiana"
        elif 'maine' in tweet_location or 'me ' in tweet_location:
            state = "maine"
        elif 'maryland' in tweet_location or 'md ' in tweet_location:
            state = "maryland"
        elif 'massachusetts' in tweet_location or 'ma ' in tweet_location:
            state = "massachusetts"
        elif 'michigan' in tweet_location or 'mi ' in tweet_location:
            state = "michigan"
        elif 'minnesota' in tweet_location or 'mn ' in tweet_location:
            state = "minnesota"
        elif 'mississippi' in tweet_location or 'ms ' in tweet_location:
            state = "mississippi"
        elif 'missouri' in tweet_location or 'mo ' in tweet_location:
            state = "missouri"
        elif 'montana' in tweet_location or 'mt ' in tweet_location:
            state = "montana"
        elif 'nebraska' in tweet_location or 'ne ' in tweet_location:
            state = "nebraska"
        elif 'nevada' in tweet_location or 'nv ' in tweet_location:
            state = "nevada"
        elif 'new hampshire' in tweet_location or 'nh ' in tweet_location:
            state = "new hampshire"
        elif 'new jersey' in tweet_location or 'nj ' in tweet_location:
            state = "new jersey"
        elif 'new mexico' in tweet_location or 'nm ' in tweet_location:
            state = "new mexico"
        elif 'new york' in tweet_location or 'ny ' in tweet_location:
            state = "new york"
        elif 'north carolina' in tweet_location or 'nc ' in tweet_location:
            state = "north carolina"
        elif 'north dakota' in tweet_location or 'nd ' in tweet_location:
            state = "north dakota"
        elif 'ohio' in tweet_location or 'oh ' in tweet_location:
            state = "ohio"
        elif 'oklahoma' in tweet_location or 'ok ' in tweet_location:
            state = "oklahoma"
        elif 'oregon' in tweet_location or 'or ' in tweet_location:
            state = "oregon"
        elif 'pennsylvania' in tweet_location or 'pa ' in tweet_location:
            state = "pennsylvania"
        elif 'rhode island' in tweet_location or 'ri ' in tweet_location:
            state = "rhode island"
        elif 'south carolina' in tweet_location or 'sc ' in tweet_location:
            state = "south carolina"
        elif 'south dakota' in tweet_location or 'sd ' in tweet_location:
            state = "south dakota"
        elif 'tennessee' in tweet_location or 'tn ' in tweet_location:
            state = "tennessee"
        elif 'texas' in tweet_location or 'tx ' in tweet_location:
            state = "texas"
        elif 'utah' in tweet_location or 'ut ' in tweet_location:
            state = "utah"
        elif 'vermont' in tweet_location or 'vt ' in tweet_location:
            state = "vermont"
        elif 'virginia' in tweet_location or 'va ' in tweet_location:
            state = "virginia"
        elif 'washington' in tweet_location or 'wa ' in tweet_location:
            state = "washington"
        elif 'west virginia' in tweet_location or 'wv ' in tweet_location:
            state = "west virginia"
        elif 'wisconsin' in tweet_location or 'wi ' in tweet_location:
            state = "wisconsin"
        elif 'wyoming' in tweet_location or 'wy ' in tweet_location:
            state = "wyoming"
        else:
            state = None
        return state




































