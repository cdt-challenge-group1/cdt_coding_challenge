from ARIMA_implementation_rough import ARIMA_predict
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tseries.offsets import BDay, DateOffset

DELAY_COST = 30000
NUM_BARRELS = 750000

if __name__ == "__main__":
    price_prediction, price_std, prices, predicted_stdevs = ARIMA_predict()
    print('Price today:', prices[-1][-1], 'Predicted price tomorrow:', price_prediction)
    price_today = prices[1][-1]

    # For now, we check only 1 day ahead, so if today's price is higher, dock today
    if price_today >= price_prediction:
        dock_today = True
    # If the prediction is higher, check whether the delay cost is worth it
    elif (price_prediction * NUM_BARRELS) + DELAY_COST > (price_today * NUM_BARRELS):
        dock_today = False
    else:
        dock_today = True

    print('~~~~~~~~~~~~~~~~~~~~~~')
    if dock_today:
        print('The boat should dock today')
    else:
        print('The boat should wait to dock')
    print('~~~~~~~~~~~~~~~~~~~~~~')

    ys = prices[1] + [price_prediction]
    xs = prices[0] + [(pd.datetime.today() + BDay(1)).strftime("%Y-%m-%d")]
    
    errors = ([0] * (len(prices[0]) - len(predicted_stdevs))) + predicted_stdevs + [price_std]
    fig = plt.figure(figsize=(20,10))
    plt.errorbar(xs, ys, yerr=errors, elinewidth=2)
    plt.xticks(rotation=70)
    plt.ylabel('Prices')
    plt.xlabel('Date')
    plt.title('Predicted Oil Prices')
    plt.savefig("prediction_graph_output.png", dpi=200)
