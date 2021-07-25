# Designed by: Lukas Bock
#-------------
# Created on: 14.07.2021
# ------------
# Version: Python 3.7.6, Spyder 4.0.1
# -------------
# Input: 
#   results from 'main'
# ------------
# Output: 
#   plots
# ------------

# %% Import libraries

import matplotlib.pyplot as plt



def historically_data(df_alk, df_flucht, df_verkehr):
    x = df_alk["ds"]
    fig, ax = plt.subplots()  # Create a figure and an axes.
    ax.plot(x,df_alk["y"], label='Alkoholunfälle')  # Plot some data on the axes.
    ax.plot(x,df_flucht["y"] , label='Fluchtunfälle')  # Plot more data on the axes...
    ax.plot(x, df_verkehr["y"] , label='Verkehrsunfälle')  # ... and some more.
    ax.set_xlabel('Time in years')  # Add an x-label to the axes.
    ax.set_ylabel('Number of accidents')  # Add a y-label to the axes.
    ax.set_title("Historically data accidents")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.savefig("historically_data.svg", format="svg")