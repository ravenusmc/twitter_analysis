#This file will take the sentiment_data csv and clean it. Meaning that the sentiment data does not have 
#the sentiment values added up per state. 

#Importing files for use in this file 
from csv import writer
import math
import numpy as np
import pandas as pd

class Clean_CSV():

    #Initing the csv file to be used.
    def __init__(self):
        self.data = pd.read_csv('sentiment_data.csv')

    #This method will be building the new CSV that will have the mean's of sentiment values by state.
    def new_csv(self):
        states = ['alabama', 'alaska','arizona','arkansas', 'california', 'colorado', 'connecticut',
         'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas',
         'kentcky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota','mississippi'
          ,'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico', 
        'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania',
        'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont', 
        'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']
        #probably need an outer loop where I search through the day values and then increment by one. 
        #or do a search by state and day where I increment the day by one and cut it off at the max value?
        with open("final_data.csv", "a") as csv_file:
            csv_writer = writer(csv_file)
            # csv_writer.writerow(["day", "state", "avg"])
            day = 6
            for state in states:
                state_info = self.data.loc[self.data['state'] == state.title()]
                # state_info = self.data[(self.data['state']== state.title()) & (self.data['day']== 1)]
                #excetion handling to deal with situations where an error occurs. 
                try:
                    state = state_info.iloc[0][1]
                except IndexError:
                    print('Error, Program will continue running')
                avg = state_info['sentiment'].mean()
                if math.isnan(avg) != True:
                    csv_writer.writerow([day, state, avg])



# csv = Clean_CSV()
# csv.new_csv()