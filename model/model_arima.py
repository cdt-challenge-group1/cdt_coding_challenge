#!/usr/bin/python3

import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from pandas.tseries.offsets import BDay, DateOffset
import datetime
from abstract_prediction_model import *

class ModelArima(AbstractPredictionModel):
	def predict(self, data):
		# data has missing data so predict extra days
		diffDays = pd.date_range(data[0][-1], datetime.datetime.today(), freq=BDay()).size - 1

		# predict the missing number of days and then the current day so that the prediction is for tomorrow not
		# for the day after the data has days for
		#Initialise the parameters for the ARIMA model (p,d,q).
		order = (1,1,1)
		model = ARIMA(data[1], order=order)

		#Fit the model to the data provided
		fit = model.fit()
		date = datetime.datetime.today() - BDay(diffDays - 1)
		predicted_stdevs = []
		for i in range(diffDays):
			#Forecast the next price
			price_prediction = round(fit.forecast()[0][0], 2)
			price_std = fit.forecast()[1][0]
			
			datestr = date.date()
			data[0].append(datestr)
			data[1].append(price_prediction)
			predicted_stdevs.append(price_std)
			date += BDay(1)
			model = ARIMA(data[1], order=order)
			fit = model.fit()
		
		#Forecast the next price
		datestr = date.date()
		price_prediction = round(fit.forecast()[0][0], 2)
		price_std = fit.forecast()[1][0]
		price_prediction = fit.forecast()[0][0]
		data[0].append(datestr)
		data[1].append(price_prediction)
		predicted_stdevs.append(price_std)
		
		return data, predicted_stdevs
