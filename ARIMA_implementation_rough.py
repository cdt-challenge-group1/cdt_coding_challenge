#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:45:37 2019

@author: do19150
"""

import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt

def ARIMA_predict():
    #import the data set into a pandas DataFrame
    data = pd.read_csv('Insert name of data path', index_col=0)
    prices = data["Price"]

    #Initialise the parameters for the ARIMA model (p,d,q).
    order = (1,1,1)
    model = ARIMA(prices, order)

    #Fit the model to the data provided
    fit = model.fit()

    #Forecast the next price
    price_prediction = fit.forecast()[0]
    price_std = fit.forecast()[1]

    return price_prediction, price_std, prices

