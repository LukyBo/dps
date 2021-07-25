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


# load data
df = pd.read_csv('../Input/Monatszahlen_Verkehrsunfälle.csv', delimiter=';')


# Data cleansing and adaption
df = df[df.Month != 'Summe'] # Drop unnecessary rows
#df = df[df.Year != 2021]
df = df.sort_values(by ='Month' , ascending=True) # Sort values by time
df1 = df['Month'].str.extract('.*(\d{2})', expand = False) # Change Month Column to numbers between 1-12 and safe to df1
df = df.assign(Month=df1[:]) # Replace column 'Month' of df with column of df1
df["Month"] = pd.to_numeric(df["Month"]) # Change the non-numeric objects into integers
df[['Category', 'Accident-type']] = df[['Category', 'Accident-type']].astype(pd.StringDtype()) # Change the non-string objects into strings to be able to filter the df
df["Day"] = 15 # Create Column for days as datetime needs days as input
df['ds']=pd.to_datetime(df[['Year', 'Month', 'Day']]) # Obtain a datetime column to be able to visualise historically the number of accidents 
df.drop(['VORJAHRESWERT','VERAEND_VORMONAT_PROZENT','VERAEND_VORJAHRESMONAT_PROZENT', 'ZWOELF_MONATE_MITTELWERT', 'Day'],axis=1 ,inplace=True) # Drop unnecessary columns
df = df.rename(columns={'Value': 'y'}) # renamed the column for the later use in Model
df = df.loc[(df['Accident-type'] == 'insgesamt')]

# Create df for 'Alkoholunfälle'
df_alk = df.loc[(df['Category'] == 'Alkoholunf�lle')]

# Create df for 'Fluchtunfälle'
df_flucht = df.loc[(df['Category'] == 'Fluchtunf�lle')]

# Create df for 'Verkehrsunfälle'
df_verkehr = df.loc[(df['Category'] == 'Verkehrsunf�lle')]