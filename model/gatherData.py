#!/bin/python3

import requests
import datetime
import xlrd
from bs4 import BeautifulSoup


def requestData(daysAgo=None):
    """
    Request the price data from eni and return an array with tuples of
    the date and price for days less than daysAgo. The data does not contain
    prices for weekends so the number of prices returned may be less than
    daysAgo.
    """
    url = "https://www.eia.gov/dnav/pet/hist_xls/RWTCd.xls"
    # url2 = "https://uk.investing.com/commodities/crude-oil-historical-data"
    agoDate = None
    if daysAgo is not None:
        agoDate = datetime.datetime.now() -\
                  datetime.timedelta(days=daysAgo)

    data = requests.get(url)
    if data.status_code != 200:
        raise ValueError("Failed to get data")
    print("ENI data is %d bytes" % (len(data.content)))

    workbook = xlrd.open_workbook(file_contents=data.content)
    sheet = workbook.sheet_by_name("Data 1")
    # https://blogs.harvard.edu/
    # rprasad/2014/06/16/reading-excel-with-python-xlrd/

    dates = []
    close = []
    # The sheet starts at row 3
    for row_idx in range(3, sheet.nrows):
        # epoch = datetime.datetime
        # .strptime('1990-01-01T00:00:00+0000', "%Y-%m-%dT%H:%M:%S%z")
        # https://stackoverflow.com/
        # questions/26010455/convert-xldate-to-python-datetime
        date = datetime.datetime(*xlrd.xldate_as_tuple(
                                 sheet.cell(row_idx, 0).value,
                                 workbook.datemode))
        if agoDate is None or date >= agoDate:
            dates.append(date)
            close.append(float(sheet.cell(row_idx, 1).value))

    return (dates, close)
