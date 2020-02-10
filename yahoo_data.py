#!/usr/bin/python3

import requests
import datetime
import xlrd
from bs4 import BeautifulSoup
import json

def get_yahoo_data(daysAgo = None):
	yahoo_url = ""
	if daysAgo == None:
		yahoo_url = "https://query1.finance.yahoo.com/v8/finance/chart/CLH20.NYM?region=GB&lang=en-US&includePrePost=false&interval=1d&range=10000000d&corsDomain=finance.yahoo.com&.tsrc=finance"
	else:
		yahoo_url = "https://query1.finance.yahoo.com/v8/finance/chart/CLH20.NYM?region=GB&lang=en-US&includePrePost=false&interval=1d&range=%dd&corsDomain=finance.yahoo.com&.tsrc=finance" % daysAgo

	data = requests.get(yahoo_url)
	if data.status_code != 200:
		raise ValueError("Failed to get data")
	print("Yahoo data is %d bytes" % len(data.content))
	data = json.loads(data.content)

	response = data["chart"]["result"][0]

	dates = []
	for timestamp in response["timestamp"]:
		dates.append(datetime.datetime.fromtimestamp(timestamp))
	
	close = []
	index = 0
	values = response["indicators"]["quote"][0]
	for value in values["close"]:
		if value == None:
			close.append(0)
			continue
			
		close.append(float(value))
		index += 1

	return (dates, close)
