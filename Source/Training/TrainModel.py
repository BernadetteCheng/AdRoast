"""
    Author: Taha Masood
    Name: TrainModel
    Purpose: Train model on advertisement data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error
from sklearn import ensemble
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle

class Train:

    """
        Purpose: Initializer
    """
    def __init__(self):
        self.train = {}
        self.parameters = {'n_estimators' : 10000,
                           'max_leaf_nodes': 3,
                           'max_depth' : 2,
                           'learning_rate' : 0.1,
                           'criterion' : 'mse'}

    """
        Purpose: Train model for adroast application
    """
    def train_model(self, input_features, target_values):

        gradient_boosting_regressor = ensemble.GradientBoostingRegressor(**self.parameters)

        X_train, X_test, y_train, y_test = train_test_split(input_features, target_values, test_size=0.1)
        gradient_boosting_regressor.fit(X_train, y_train)

        y_pred = gradient_boosting_regressor.predict(X_train)
        print(mean_absolute_error(y_train, y_pred))

        y_pred = gradient_boosting_regressor.predict(X_test)
        print(mean_absolute_error(y_test, y_pred))

        filename = 'adroast_model.sav'
        pickle.dump(gradient_boosting_regressor, open(filename, 'wb'))


    """
        Purpose: Train model for adroast application
    """
    def model_evaluation(self, input_features, target_values):

        prediction_information = []

        leave_one_out = LeaveOneOut()
        for train_index, test_index in leave_one_out.split(input_features):
            gradient_boosting_regressor = ensemble.GradientBoostingRegressor(**self.parameters)
            X_train, X_test = input_features[train_index], input_features[test_index]
            y_train, y_test = target_values[train_index], target_values[test_index]

            gradient_boosting_regressor.fit(X_train, y_train)

            y_pred = gradient_boosting_regressor.predict(X_train)
            prediction_information.append(y_pred)
            print(mean_absolute_error(y_train, y_pred))

            y_pred = gradient_boosting_regressor.predict(X_test)
            prediction_information.append(y_pred)
            print(mean_absolute_error(y_test, y_pred))
