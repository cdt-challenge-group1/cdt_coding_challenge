#!/usr/bin/python3

import gatherData as quandl
import yahoo_data as yahoo
from os import path
import pickle
import pandas as pd
from pandas.tseries.offsets import BDay, DateOffset
import datetime

def updateData():
	data = None
	f = None
	if not path.isfile("data.dat"):
		f = open("data.dat", "wb")
		data = quandl.requestData()
		pickle.dump(data, f)
	else:
		f = open("data.dat", "rb")
		data = pickle.load(f)
	f.close()

	diff_days = pd.date_range(data[0][-1], datetime.datetime.today(), freq=BDay()).size

	if diff_days - 1 > 0:
		yahoo_data = yahoo.get_yahoo_data(diff_days)
		dates = data[0] + yahoo_data[0]
		close = data[1] + yahoo_data[1]
		data = (dates, close)

	with open("data.dat", "wb") as f:
		pickle.dump(data, f)

	return data

# get the stored data, if there is none, store as much data as we can
# find first. Data is updated before returning using yahoo
def getData():
	updateData()

	f = open("data.dat", "rb")
	data = pickle.load(f)
	f.close()

	return data

# update stored data from eni using yahoo finance
# if there is no stored data then download the whole of eni
if __name__ == "__main__":
	updateData()
