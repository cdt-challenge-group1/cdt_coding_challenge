import pandas as pd
from pandas.tseries.offsets import BDay
import datetime
import csv
import requests
from io import StringIO


def get_quandl_data(daysAgo=None):
    url = "https://www.quandl.com/api/v3/datasets/EIA/PET_RWTC_D\
            .csv?api_key=2Q1jAB4TAk3a2pKq925R"

    if daysAgo is None or daysAgo > 0:
        today = pd.datetime.today()
        agoDate = today - BDay(daysAgo + 1)
        fromDate = str(agoDate.date())
        toDate = str((today - datetime.timedelta(days=1)).date())
        url += "&start_date=" + fromDate + "&end_date=" + toDate

    data = requests.get(url)
    if data.status_code != 200:
        raise ValueError("Failed to get data")
    data = data.content

    returnDates = []
    returnPrices = []
    reader = csv.reader(StringIO(data.decode("UTF-8")))
    next(reader)
    for row in reader:
        returnDates.append(row[0])
        returnPrices.append(float(row[1]))

    returnDates.reverse()
    returnPrices.reverse()
    return (returnDates, returnPrices)

# print(get_quandl_data(30))
