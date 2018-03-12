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
            state = "al"
        elif 'alaska' in tweet_location or 'ak ' in tweet_location:
            state = "ak"
        elif 'arizona' in tweet_location or 'az ' in tweet_location:
            state = "az"
        elif 'arkansas' in tweet_location or 'ar ' in tweet_location:
            state = "ar"
        elif 'california' in tweet_location or 'ca ' in tweet_location:
            state = "ca"
        elif 'colorado' in tweet_location or 'co ' in tweet_location:
            state = "co"
        elif 'connecticut' in tweet_location or 'ct ' in tweet_location:
            state = "ct"
        elif 'delaware' in tweet_location or 'de ' in tweet_location:
            state = "de"
        elif 'florida' in tweet_location or 'fl ' in tweet_location:
            state = "fl"
        elif 'georgia' in tweet_location or 'ga ' in tweet_location:
            state = "ga"
        elif 'hawaii' in tweet_location or 'hi ' in tweet_location:
            state = "hi"
        elif 'idaho' in tweet_location or 'id ' in tweet_location:
            state = "id"
        elif 'illinois' in tweet_location or 'il ' in tweet_location:
            state = "il"
        elif 'indiana' in tweet_location or 'in ' in tweet_location:
            state = "in"
        elif 'iowa' in tweet_location or 'ia ' in tweet_location:
            state = "ia"
        elif 'kansas' in tweet_location or 'ks ' in tweet_location:
            state = "ks"
        elif 'kentcky' in tweet_location or 'ky ' in tweet_location:
            state = "ky"
        elif 'louisiana' in tweet_location or 'la ' in tweet_location:
            state = "la"
        elif 'maine' in tweet_location or 'me ' in tweet_location:
            state = "me"
        elif 'maryland' in tweet_location or 'md ' in tweet_location:
            state = "md"
        elif 'massachusetts' in tweet_location or 'ma ' in tweet_location:
            state = "ma"
        elif 'michigan' in tweet_location or 'mi ' in tweet_location:
            state = "mi"
        elif 'minnesota' in tweet_location or 'mn ' in tweet_location:
            state = "mn"
        elif 'mississippi' in tweet_location or 'ms ' in tweet_location:
            state = "ms"
        elif 'missouri' in tweet_location or 'mo ' in tweet_location:
            state = "mo"
        elif 'montana' in tweet_location or 'mt ' in tweet_location:
            state = "mt"
        elif 'nebraska' in tweet_location or 'ne ' in tweet_location:
            state = "ne"
        elif 'nevada' in tweet_location or 'nv ' in tweet_location:
            state = "nv"
        elif 'new hampshire' in tweet_location or 'nh ' in tweet_location:
            state = "nh"
        elif 'new jersey' in tweet_location or 'nj ' in tweet_location:
            state = "nj"
        elif 'new mexico' in tweet_location or 'nm ' in tweet_location:
            state = "nm"
        elif 'new york' in tweet_location or 'ny ' in tweet_location:
            state = "ny"
        elif 'north carolina' in tweet_location or 'nc ' in tweet_location:
            state = "nc"
        elif 'north dakota' in tweet_location or 'nd ' in tweet_location:
            state = "nd"
        elif 'ohio' in tweet_location or 'oh ' in tweet_location:
            state = "oh"
        elif 'oklahoma' in tweet_location or 'ok ' in tweet_location:
            state = "ok"
        elif 'oregon' in tweet_location or 'or ' in tweet_location:
            state = "or"
        elif 'pennsylvania' in tweet_location or 'pa ' in tweet_location:
            state = "pa"
        elif 'rhode island' in tweet_location or 'ri ' in tweet_location:
            state = "ri"
        elif 'south carolina' in tweet_location or 'sc ' in tweet_location:
            state = "sc"
        elif 'south dakota' in tweet_location or 'sd ' in tweet_location:
            state = "sd"
        elif 'tennessee' in tweet_location or 'tn ' in tweet_location:
            state = "tn"
        elif 'texas' in tweet_location or 'tx ' in tweet_location:
            state = "tx"
        elif 'utah' in tweet_location or 'ut ' in tweet_location:
            state = "ut"
        elif 'vermont' in tweet_location or 'vt ' in tweet_location:
            state = "vt"
        elif 'virginia' in tweet_location or 'va ' in tweet_location:
            state = "va"
        elif 'washington' in tweet_location or 'wa ' in tweet_location:
            state = "wa"
        elif 'west virginia' in tweet_location or 'wv ' in tweet_location:
            state = "wv"
        elif 'wisconsin' in tweet_location or 'wi ' in tweet_location:
            state = "wi"
        elif 'wyoming' in tweet_location or 'wy ' in tweet_location:
            state = "wy"
        elif 'dc' in tweet_location:
            state = "dc"
        else:
            state = None
        return state

    #This method will turn the location to a list. 
    # def location_to_list(self, tweet_location):
    #     loc_list = tweet_location.split()
    #     return loc_list

    # This method will convert the strings in the loc_list to lowercase to help with matching in the 
    # match_location function. 
    # def list_lower_case(self, loc_list):
    #     lower_case = []
    #     count = 0
    #     while count < len(loc_list):
    #         loc = loc_list[count].lower()
    #         lower_case.append(loc)
    #         count += 1
    #     return lower_case

    #This method will clean the location portion of the tweet. 
    # def match_location(self, tweet_list):
    #     if "Alabama" in tweet_list or 'AL' in tweet_list:


































