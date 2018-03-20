#This file will take the sentiment_data csv and clean it. Meaning that the sentiment data does not have 
#the sentiment values added up per state. 

#Importing files for use in this file 
from csv import writer
import math
import numpy as np
import pandas as pd

class Clean_CSV():

    #Initing the csv file to be used.
    # def __init__(self):
    #     self.data = pd.read_csv('sentiment_data.csv')

    #This method will be building the new CSV that will have the mean's of sentiment values by state.
    def new_csv(self):
        #not 100% sure why but when this line is above, in the init method, the new_csv method does not 
        #work. 
        self.data = pd.read_csv('sentiment_data.csv')
        states = ['alabama', 'alaska','arizona','arkansas', 'california', 'colorado', 'connecticut',
         'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas',
         'kentcky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota','mississippi'
          ,'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 
        'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania',
        'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 
        'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']
        #probably need an outer loop where I search through the day values and then increment by one. 
        #or do a search by state and day where I increment the day by one and cut it off at the max value?
        #Opening the csv file where I will append the data. 
        with open("final_data.csv", "a") as csv_file:
            csv_writer = writer(csv_file)
            #This variable will hold the current day of the data. I have to manually increment it by one 
            #for each day that I run this program. If this was a full fledge program I would use a datetime
            #stamp and have it increase by one each day. 
            day = 7
            #Loop to go through all of the states above looking for the mean on each state. 
            for state in states:
                state_info = self.data.loc[self.data['state'] == state.title()]
                #excetion handling to deal with situations where an error occurs. 
                try:
                    state = state_info.iloc[0][1]
                except IndexError:
                    print('Error, state not present, Program will continue running')
                avg = state_info['sentiment'].mean()
                #When the avg comes back as a number, it means that its NOT a NAN and thus data is 
                #inserted into CSV. 
                if math.isnan(avg) != True:
                    #Inserting the data. 
                    csv_writer.writerow([day, state, avg])




# csv = Clean_CSV()
# csv.test()
# csv.new_csv()
