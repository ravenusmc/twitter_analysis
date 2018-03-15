#The purpose of this file is to build the CSV file that I will use to build the data visualization 

#importing files that will help the program run
from clean_csv import *
from lang import *
from tweet import *


def main():
    #Creating the objects that will be used in this program. 
    tweet = Tweets()
    clean = Clean_CSV()
    #Letting the user know that the program is starting
    print('Program Starting')
    #This method will get all of the tweets, analyze them and then place them into a csv file
    tweet.get_tweet()
    #This method will average the sentiment values by state and move that data into a new CSV file
    clean.new_csv()
    #Letting the user know that the program has finished running
    print('Program Finished')


main()