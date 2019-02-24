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
                           'max_depth' : 10,
                           'learning_rate' : 0.1,
                           'criterion' : 'mse'}

    """
        Purpose: Train model for adroast application
    """
    def train_model(self, input_features, target_values):
        gradient_boosting_classifier = ensemble.GradientBoostingClassifier(**self.parameters)

        X_train, X_test, y_train, y_test = train_test_split(input_features, target_values, test_size = 0.3, random_state = 52)
        gradient_boosting_classifier = gradient_boosting_classifier.fit(X_train, y_train)

        print(X_train)
        print(X_test)

        y_pred = gradient_boosting_classifier.predict(X_train)
        print(y_pred)
        print(accuracy_score(y_train, y_pred, normalize=True))

        feature_set = {}

        feature_set['colorfullness'] = 62.42930325
        feature_set['edges'] = 250
        feature_set['r_mean'] = 292.96875
        feature_set['r_variance'] = 4849356.5
        feature_set['r_kurtosis'] = 228.8076782
        feature_set['r_skewness'] = 14.91634846
        feature_set['g_mean'] = 292.96875
        feature_set['g_variance'] = 4930868.5
        feature_set['g_kurtosis'] = 223.5418701
        feature_set['g_skewness'] = 14.69216442
        feature_set['b_mean'] = 292.96875
        feature_set['b_variance'] = 4859313.5
        feature_set['b_kurtosis'] = 226.5546875
        feature_set['b_skewness'] = 6.227247715

        prediction_features = pd.DataFrame(feature_set, index=[0])
        print(prediction_features.head())



        X_test = X_test.append(prediction_features)

        y_pred = gradient_boosting_classifier.predict(X_test)
        print(y_pred)
        print(accuracy_score(y_test, y_pred, normalize=True))

        print(gradient_boosting_classifier.predict(prediction_features))

        filename = 'adroast_model.sav'
        pickle.dump(gradient_boosting_classifier, open(filename, 'wb'))
