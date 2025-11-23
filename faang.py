#! /usr/bin/env python

# datetime
import datetime as dt

# Yahoo Finance API data
import yfinance as yf

# Setting the DataFrame. This includes the data for the FAANG companies at a period of 5 days and 60 minute intervals
df = yf.download ('META AAPL AMZN NFLX GOOG', period = '5d', interval = '60m')


# The dataframe is created from data from the past five working days, and so today's date is being used
today = dt.datetime.today()

# This formats today into an order that suits the file output name
today_format = today.strftime("%Y.%m.%d_%H.%M.%S")

# This brings together the data and format name into a folder specifically created for the outputs
df.to_csv("data/" + "faangdata_" + today_format + ".csv")