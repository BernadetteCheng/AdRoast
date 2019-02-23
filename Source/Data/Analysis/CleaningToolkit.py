"""
    Name: CleaningToolkit.py
    Purpose: Clean raw google advertisement dataset
"""
import pandas as pd
import numpy as np


class Analysis:

    """
        Purpose: Initializer
    """
    def __init__(self):
        self.datasets = {}

        self.cost = {'100-1k' : 500,
                     '≤ 100' : 50,
                     '1k-50k' : 25000,
                     '> 100k' : 150000,
                     '50k-100k' : 75000}

        self.impression = {'≤ 10k' : 5000,
                           '10k-100k' : 50000,
                           '100k-1M' : 500000,
                           '1M-10M' : 5000000,
                           '> 10M' : 10000000}

    """
        Purpose: Indicates if dataset already exists
    """
    def exists_df(self, data_name):
        if data_name in self.datasets:
            return True
        else:
            return False

    """
        Purpose: Imports dataframe into current instance
    """
    def import_csv(self, file_path, data_name):
        assert not self.exists_df(data_name), 'Dataset already exists!'
        self.datasets[data_name] = pd.read_csv(file_path)

    """
        Purpose: Imports limited amount of dataframe into current instance
    """

    def import_csv_limited(self, file_path, data_name, nrows):
        assert not self.exists_df(data_name), 'Dataset already exists!'
        self.datasets[data_name] = pd.read_csv(file_path, nrows=nrows)

    """
        Purpose: Displays first five samples of dataset
    """
    def display_head(self, data_name):
        assert self.exists_df(data_name), 'Dataset does not exist!'
        print(self.datasets[data_name].head)

    """
        Purpose: Removes all entries which are not image data
    """
    def remove_non_image(self, data_name):
        assert self.exists_df(data_name), 'Dataset does not exist!'
        self.datasets[data_name] = self.datasets[data_name][self.datasets[data_name].Ad_Type == 'Image']

    """
        Purpose: Writes dataset to output csv file
    """
    def write_df(self, data_name, file_path):
        assert self.exists_df(data_name), 'Dataset does not exist!'
        self.datasets[data_name].to_csv(file_path)

    """
        Purpose: Purpose provides all unique features
    """
    def unique_samples(self, data_name):
        assert self.exists_df(data_name), 'Dataset does not exist!'
        print(self.datasets[data_name].Spend_USD.unique())
        print(self.datasets[data_name].Impressions.unique())

    """
        Purpose: Cleans features to ensure that the correct information
    """
    def clean_features(self, data_name):
        assert self.exists_df(data_name), 'Dataset does not exist!'

        self.datasets[data_name]['cost'] = self.datasets[data_name].apply(self.costs, axis=1)
        self.datasets[data_name]['impression'] = self.datasets[data_name].apply(self.impressions, axis=1)
        self.datasets[data_name]['effect'] = self.datasets[data_name]['impression'] / self.datasets[data_name]['cost']
        self.datasets[data_name] = self.datasets[data_name][['Ad_ID',
                                                             'Ad_URL',
                                                             'Ad_Type',
                                                             'cost',
                                                             'impression',
                                                             'effect']]

        self.datasets[data_name] = self.datasets[data_name].rename(columns={'Ad_ID' : 'id',
                                                                            'Ad_URL' : 'url',
                                                                            'Ad_Type' : 'type'})
    """
        Purpose: Maps cost feature
    """
    def costs(self, row):
        return self.cost[row.Spend_USD]

    """
        Purpose: Maps impressions feature
    """
    def impressions(self, row):
        return self.impression[row.Impressions]