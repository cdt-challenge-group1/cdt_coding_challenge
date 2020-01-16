#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:45:37 2019

@author: do19150
"""

import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
import quandl_data as qd
from pandas.tseries.offsets import BDay, DateOffset

def ARIMA_predict():
    #import the data set into a pandas DataFrame
    #data = pd.read_csv('Insert name of data path', index_col=0)
    data_days = 60
    quandl_data = qd.get_quandl_data(data_days)
    
    # quandl has missing data do predict extra days
    diffDays = pd.date_range(quandl_data[0][-1], pd.datetime.today(), freq=BDay()).size
    print("Predicting %d missing days" % diffDays)

    # predict the missing number of days and then the current day so that the prediction is for tomorrow not
    # for the day after the data has days for
    #Initialise the parameters for the ARIMA model (p,d,q).
    order = (5,1,0)
    model = ARIMA(quandl_data[1], order=order)

    #Fit the model to the data provided
    fit = model.fit()
    date = pd.datetime.today() - BDay(diffDays)
    predicted_stdevs = []
    for i in range(diffDays):
        #Forecast the next price
        price_prediction = fit.forecast()[0][0]
        price_std = fit.forecast()[1][0]
        
        datestr = date.date().strftime("%Y-%m-%d")
        quandl_data[0].append(datestr)
        quandl_data[1].append(price_prediction)
        predicted_stdevs.append(price_std)
        date += BDay(1)
    
    #Forecast the next price
    price_prediction = fit.forecast()[0][0]
    price_std = fit.forecast()[1]
        
    return price_prediction, price_std[0], quandl_data, predicted_stdevs

