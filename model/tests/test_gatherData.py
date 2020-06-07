#!/usr/bin/python3

from gatherData import *


def test_requestAllData():
    """
    We can't test for a specific number of days in the data because
    there may be gaps due to holidays etc.
    Check that requesting with none as the number of days gives back
    some data
    """
    data = requestData(None)
    assert len(data) != 0
