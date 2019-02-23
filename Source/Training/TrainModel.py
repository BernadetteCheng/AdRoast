"""
    Author: Taha Masood
    Name: TrainModel
    Purpose: Train model on advertisement data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import ensemble
from sklearn import linear_model
import pickle

class Train:

    """
        Purpose: Initializer
    """
    def __init__(self):
        self.train = {}
        self.parameters = {'n_estimators' : 10,
                      'max_depth' : 20,
                      'learning_rate' : 1,
                      'criterion' : 'mse'}

    """
        Purpose: Train model for adroast application
    """
    def train_model(self, input_features, target_values):
        gradient_boosting_regressor = ensemble.GradientBoostingRegressor(**self.parameters)
        gradient_boosting_regressor.fit(input_features, target_values)

        filename = 'adroast_model.sav'
        pickle.dump(gradient_boosting_regressor, open(filename, 'wb'))