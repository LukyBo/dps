# Designed by: Lukas Bock
#-------------
# Created on: 14.07.2021
# ------------
# Version: Python 3.7.6, Spyder 4.0.1
# -------------
# Description: 
# This schript is used to visualise historically the number of accidents per category and 
# to forecast the values for the future. The method is applied to a data set which contains 
# the monthly values for traffic accidents in Munich until the end of 2020.
# ------------
# Input: 
#   Input data (csv file) -> (Input/Monatszahlen_Verkehrsunfälle.csv)

# %% Import libraries and functions

# Import libraries
import pandas as pd
import MyPlots
from prophet import Prophet
import pickle
