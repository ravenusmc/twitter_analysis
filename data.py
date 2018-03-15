import csv
import geopandas as gpd
import numpy as np
import pandas as pd



#This class will handle all of the data manipulation
class Data():

    #This method will allow the csv file to be used by D3.js.
    def convert_csv_for_d3(self):
        self.data = pd.read_csv('tweet_data.csv')
        data = pd.DataFrame(self.data)
        return data

    #This method will allow the csv file to be used by D3.js.
    def convert_json_for_d3(self):
        # self.__data = pd.read_json('us-states.json')
        self.data = gpd.read_file('us-states.json')
        df = self.data
        return df