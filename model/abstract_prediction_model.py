#!/usr/bin/python3

from abc import *

"""
Abstract class for prediction models

All subclasses should implement the prediction method given some data
and return a tuple containing the data and any prediction errors as
floats
"""
class AbstractPredictionModel(ABC):
	@classmethod
	@abstractmethod
	def predict(self, data):
		pass
