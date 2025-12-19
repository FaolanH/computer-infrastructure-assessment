#! /usr/bin/env python

# shebang line above

# to run this file, open a new terminal and write './faang.py'


# ----- import modules -----


# listing files in a directory
import os

# datetime - formatting date and time date
import datetime as dt

# pandas - generating DataFrames and plotting them
import pandas as pd

import matplotlib

matplotlib.use('Agg')

# matplotlib.pyplot - having more plotting functionality
import matplotlib.pyplot as plt

# format the datetime of plots
import matplotlib.dates as mdates

# Yahoo Finance API data - the stock data being analysed
import yfinance as yf


# ----- setting up the data -----


# Setting the DataFrame. This includes the data for the FAANG companies at a period of 5 days and 60 minute intervals
df = yf.download ('META AAPL AMZN NFLX GOOG', period = '5d', interval = '60m')

# The DataFrame is created from data from the past five working days, and so today's date is being used
today = dt.datetime.today()

# This formats today into an order that suits the file output name
today_format = today.strftime("%Y.%m.%d_%H.%M.%S")

# This brings together the data and format name into a folder specifically created for the outputs
df.to_csv("data/" + "faangdata_" + today_format + ".csv")


# ----- sorting the data folder to find the most recent file -----


# List files in the data folder
datafiles = os.listdir('data/')

# sortdates Source: https://docs.python.org/3/howto/sorting.html

# Sort the list of files by date
datafiles.sort(reverse = True)

# latest file
datafiles [0]

# parse_dates documentation Source: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html#:~:text=as%20NaN%20values.-,parse_dates,-bool%2C%20list%20of
# calling the newest csv, generating two header rows and setting the NaN row as the index
df = pd.read_csv(f'data/{datafiles[0]}', header = [0,1], index_col = 0, parse_dates = True)


# ----- plotting the data -----


# Adding more functionality to the plot using fig,ax
fig, ax = plt.subplots()
# Using the company colours in the plot
colours = ('#A2AAAD', '#FF9900', '#34A853', '#0081FB', '#E50914')

date_formatter = mdates.DateFormatter('%d %b, %I:%M%p')  # %b = abbreviated month, %Y = 4-digit year
ax.xaxis.set_major_formatter(date_formatter)

# plotting all closing prices in the DataFrame
df['Close'].plot(color=colours, ax=ax, fontsize = 8);

# The DataFrame is created from data from the past five working days, and so today's date is being used
today = dt.datetime.today()

# This formats 'today' into an order that suits the file output name
today_format = today.strftime("%Y.%m.%d_%H.%M.%S")

# This brings together the data and format name into a folder specifically created for the outputs
plotname = "plots/" + "faangdata_" + today_format + ".webp"

# Save the figure into the plot folder as a webp which displays a higher quality image digitally with lower storage
fig.savefig(plotname, dpi = 500)

# to view the plot:
# - please navigate to the plots folder in this repository
# - scroll to the bottom to see the most recent plot
# (https://github.com/FaolanH/computer-infrastructure-assessment/tree/main/plots)