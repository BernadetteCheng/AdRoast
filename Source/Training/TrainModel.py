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

from sklearn.model_selection import KFold
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
        self.parameters = {'n_estimators' : 1000,
                           'max_depth' : 2,
                           'learning_rate' : 0.1,
                           'criterion' : 'mse'}

    """
        Purpose: Train model for adroast application
    """
    def train_model(self, input_features, target_values):
        gradient_boosting_classifier = ensemble.GradientBoostingClassifier(**self.parameters)

        X_train, X_test, y_train, y_test = train_test_split(input_features, target_values, test_size = 0.1, random_state = 22)
        gradient_boosting_classifier.fit(X_train, y_train)

        y_pred = gradient_boosting_classifier.predict(X_train)
        print(accuracy_score(y_train, y_pred, normalize=True))

        y_pred = gradient_boosting_classifier.predict(X_test)
        print(accuracy_score(y_test, y_pred, normalize=True))

        filename = 'adroast_model.sav'
        pickle.dump(gradient_boosting_classifier, open(filename, 'wb'))

