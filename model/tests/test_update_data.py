#!/usr/bin/python3

from update_data import *


def test_requestAllData():
    """
    Check that data can be requested and the data that is returned is
    not empty
    """
    data = getData()
    # we can't check that the data we get has the right number of
    # values because we wont know how many days will be in the new
    # data
    assert len(data) != 0


def test_requestDataAfterPreviousRequest():
    """
    Check that empty data is not returned after we have previously
    requested data
    """
    getData()
    data = getData()
    assert len(data) != 0
