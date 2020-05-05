#!/usr/bin/python3

from ARIMA_implementation_rough import ARIMA_predict
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tseries.offsets import BDay, DateOffset
import datetime

DELAY_COST = 30000
NUM_BARRELS = 750000

if __name__ == "__main__":
    prices, predicted_stdevs = ARIMA_predict()
    print('Price today:', prices[1][-2], 'Predicted price tomorrow:', prices[1][-1])
    price_today = prices[1][-2]
    price_prediction = prices[1][-1]

    # For now, we check only 1 day ahead, so if today's price is higher, dock today
    if price_today >= price_prediction:
        dock_today = True
    # If the prediction is higher, check whether the delay cost is worth it
    elif (price_prediction * NUM_BARRELS) - DELAY_COST > (price_today * NUM_BARRELS):
        dock_today = False
    else:
        dock_today = True

    print('~~~~~~~~~~~~~~~~~~~~~~')
    if dock_today:
        advice = 'The boat should dock today'        
        
    else:
        advice = 'The boat should wait to dock'
    print(advice)
    print('~~~~~~~~~~~~~~~~~~~~~~')

    ys = prices[1]
    xs = prices[0]
    
    textout = '\n'.join((r"Today's price=%.2f" %price_today,r"Tomorrow's prediction=%.2f" %price_prediction,advice))
    
    errors = ([0] * (len(prices[0]) - len(predicted_stdevs))) + predicted_stdevs
    fig = plt.figure(figsize=(10,5))
    #print([x.strftime("%Y-%m-%d") for x in xs[-10:]])
    plt.errorbar([x.strftime("%Y-%m-%d") for x in xs[-10:]], ys[-10:], yerr=errors[-10:], elinewidth=2, uplims=True, lolims=True, ecolor="red")
    plt.xticks(rotation=70)
    plt.ylabel('Price (USD/Barrel)')
    plt.xlabel('Date')
    plt.title('Predicted Oil Price')
    plt.text(([x.strftime("%Y-%m-%d") for x in xs[-10:]][-2]),(price_prediction+3),textout)
    plt.tight_layout()
    plt.savefig("prediction_graph_output.svg", dpi=150)
