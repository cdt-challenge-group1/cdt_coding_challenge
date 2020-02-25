#!/usr/bin/python3

import requests
import datetime
import xlrd
from bs4 import BeautifulSoup
import json
import re

def get_yahoo_data(daysAgo = None):
	# yahoo keeps changing their url, this will significantly
	# increase the data transfer to get the updated data
	# TODO: consider caching the url and only updating it when the fetch
	# fails with a 404.
	
	yahoo_chart_regex = re.compile("\"underlyingSymbol\":\"(.*?\.NYM)\"")
	data = requests.get("https://finance.yahoo.com/quote/CL=F/")
	if data.status_code != 200:
		raise ValueError("Failed to fetch yahoo finance page to find chart")
	print("Yahoo finance page is %d bytes" % len(data.content))
	
	# TODO: what if this match fails?
	print(data.content.decode("UTF-8"))
	chart_matches = yahoo_chart_regex.search(data.content.decode("UTF-8"))
	if chart_matches == None:
		raise ValueError("Failed to match chart name regex")
	yahoo_base_chart_url = chart_matches.group(1)
	
	if daysAgo == None:
		# we're not supposed to be able to query this many days so yahoo
		# might change their api to stop us at some point
		daysAgo = 10000000
	yahoo_url = "https://query1.finance.yahoo.com/v8/finance/chart/%s?region=GB&lang=en-US&includePrePost=false&interval=1d&range=%dd&.tsrc=finance" % (yahoo_base_chart_url, daysAgo)

	data = requests.get(yahoo_url)
	print(data.status_code)
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
