#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import matplotlib.pyplot as plt, mpld3
import json 
import requests

#importing personal code
from data import *


#Setting up Flask
app = Flask(__name__)

#This route takes the user to the home page
@app.route('/')
def landing():
    return render_template('home.html')

@app.route('/my/data/endpoint')
def get_d3_data():
    data = Data()
    data_file = data.convert_csv_for_d3()
    return data_file.to_csv()

@app.route("/json")
def json():
    data = Data()
    data_file = data.convert_json_for_d3()
    # return data_file
    return data_file.to_json()


#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)