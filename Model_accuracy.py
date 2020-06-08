#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:39:16 2020

@author: do19150
"""

from statsmodels.tsa.arima_model import ARIMA
from gatherData import requestData
import numpy as np

#for date in past.

#load data to date

dates, close = requestData()

pred = []
actual = []
difference = []
correct_advice = []
financial_impact = []

n = 2000
o=(1,1,1)

for i in range(n):
    
    p = close[0:-(n-i)]
    
    nextday = close[-(n-i)]
    
    #build model
    model = ARIMA(p, order=o)
    fit=model.fit(disp=0)
    
    #create prediction
    prediction = fit.forecast()[0][0]
    
    pred.append(prediction)
    actual.append(nextday)
    difference.append(np.absolute(prediction - nextday))
    
    #if prediction is wait, was it correct
    if prediction - 0.04 > p[-1]:
        if nextday - 0.04 > p[-1]:
            correct_advice.append(1)
        else:
            correct_advice.append(0)
            
        financial_impact.append((nextday - (p[-1]+0.04)))
            
    #if prediction is sell, was it correct
    else:
        if nextday - 0.04 > p[-1]:
            correct_advice.append(0)
        else:
            correct_advice.append(1)
            
        financial_impact.append((p[-1] - (nextday - 0.04)))
            
#Accuracy of model in advice given
advice_accuracy = np.average(correct_advice) * 100
profit_per_day = np.average(financial_impact)
average_difference = np.average(difference)


print('The model gives the correct advice %2.2f per cent of the time.' %advice_accuracy)
print('The average absolute difference between the predicted and actual price is %.4f US$ per barrel.'%average_difference)
if profit_per_day > 0:
    print('The use of our model gives an average profit of %.2f US$ per barrel per day.' %profit_per_day)
else:
    print('The use of our model gives an average loss of %.2f US$ per barrel per day.' %np.absolute(profit_per_day))  
    
#Output accuracy information to textfile.
labels = ['Advice Accuracy','Daily Profit','Average Price Difference']
results = [advice_accuracy,profit_per_day,average_difference]
output = np.array((labels,results),dtype=str)
np.savetxt('Model_Accuracy_Results.csv',output,fmt='%s',delimiter=',')
    
