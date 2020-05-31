#!/usr/bin/python3

from ARIMA_implementation_rough import *
from update_data import *

"""
Test that the arima function returns an extra day than the input data
"""
def test_nextDayIsPredicted():
    data = getData()
    arima_data = ARIMA_predict()
    
    print(data[0][-10:])
    assert (len(data[0]) + 1) == len(arima_data[0][0])
