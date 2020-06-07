#!/usr/bin/python3

from ARIMA_implementation_rough import *
from update_data import *


def test_nextDayIsPredicted():
    """
    Test that the arima function returns an extra day than the input data
    """
    data = getData()
    arima_data = ARIMA_predict()

    assert (len(data[0]) + 1) == len(arima_data[0][0])


def test_sameNumberOfStdevsAsDays():
    """
    Test that the same number of standard deviations are returned as there
    are days that were predicted in the data
    """
    data = getData()
    arima_data = ARIMA_predict()

    assert (len(arima_data[0][0]) -
            len(data[0])) == len(arima_data[1])


def test_sameNumberOfPricesAsDays():
    """
    Test that the same number of prices are returned in the arima data
    as there are days that are returned
    """
    data = ARIMA_predict()

    assert len(data[0][0]) == len(data[0][1])
