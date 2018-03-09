#This file will clean the text of the tweet

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

    #This method will turn the location to a list. 
    def location_to_list(self, tweet_location):
        tweet_location_list = tweet_location.split()
        return loc_list

    #This method will convert the strings in the loc_list to lowercase to help with matching in the 
    #match_location function. 
    #def list_lower_case(self, loc_list):

    #This method will clean the location portion of the tweet. 
    # def match_location(self, tweet_list):
    #     if "Alabama" in tweet_list or 'AL' in tweet_list:




if "LA" in one or "Jefferson," in one:
































