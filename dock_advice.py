from ARIMA_implementation_rough import ARIMA_predict
import logging

DELAY_COST = 0 # Replace this with actual delay cost

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

if __name__ == "__main__":
    price_prediction, price_std, prices = ARIMA_predict()
    print(price_prediction, prices)
    price_today = prices[1][-1]

    # For now, we check only 1 day ahead, so if today's price is higher, dock today
    if price_today >= price_prediction:
        dock_today = True
    # If the prediction is higher, check whether the delay cost is worth it
    elif price_prediction + DELAY_COST > price_today: 
        dock_today = False
    else:
        dock_today = True

    if dock_today:
        logging.info('The boat should dock today')
    else:
        logging.info('The boat should wait to dock')

