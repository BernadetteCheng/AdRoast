"""
    Name: CleaningToolkit.py
    Purpose: Clean raw google advertisement dataset
"""
import pandas as pd
import requests
from lxml import html
import requests
import numpy as np
from bs4 import BeautifulSoup as bs
import urllib.request as urllib
from selenium.webdriver.common.by import By
from selenium import webdriver
import random

class Analysis:

    """
        Purpose: Initializer
    """
    def __init__(self):
        self.datasets = {}

        self.cost = {'100-1k' : [100, 1000],
                     '≤ 100' : [0, 100],
                     '1k-50k' : [1000, 50000],
                     '> 100k' : [100000, 10000000],
                     '50k-100k' : [50000, 100000]}

        self.impression = {'≤ 10k' : [0, 10000],
                           '10k-100k' : [10000, 100000],
                           '100k-1M' : [100000, 1000000],
                           '1M-10M' : [1000000, 10000000],
                           '> 10M' : [10000000, 1000000000]}

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
        #self.datasets[data_name] = self.datasets[data_name][['Ad_ID',
        #                                                     'Ad_URL',
        #                                                     'Ad_Type',
        #                                                     'cost',
        #                                                     'impression',
        #                                                     'effect']]

        #self.datasets[data_name] = self.datasets[data_name].rename(columns={'Ad_ID' : 'id',
        #                                                                    'Ad_URL' : 'url',
        #                                                                    'Ad_Type' : 'type'})

        self.datasets[data_name] = self.datasets[data_name][['id',
                                                             'effect',
                                                             'colorfullness',
                                                             'edges',
                                                             'r_mean',
                                                             'r_variance',
                                                             'r_kurtosis',
                                                             'r_skewness',
                                                             'g_mean',
                                                             'g_variance',
                                                             'g_kurtosis',
                                                             'g_skewness',
                                                             'b_mean',
                                                             'b_variance',
                                                             'b_kurtosis',
                                                             'b_skewness']]

    """
        Purpose: Maps cost feature
    """
    def costs(self, row):
        return random.randint(self.cost[row.Spend_USD][0], self.cost[row.Spend_USD][1])

    """
        Purpose: Maps impressions feature
    """
    def impressions(self, row):
        return random.randint(self.impression[row.Impressions][0], self.impression[row.Impressions][1])

    """
        Purpose: Grabs image from url and saves as required name
    """
    def grab_image(self, url, image_name):
        try:
            driver = webdriver.Chrome('C:\\Users\\Taha Masood\\Downloads\\chromedriver.exe')
            driver.get(url)

            print(driver.page_source)
            driver.close()
        except:
            print('no image')

    """
        Purpose: Pulls all images from the current dataset
    """
    def pull_images(self, data_name):
        for row in self.datasets[data_name].itertuples():
            self.grab_image(row[3], row[2] + '.jpg')

    """
        Name: drop_null
        Purpose: Drops all null values in a given feature
    """
    def drop_null(self, data_name, feature_name):
        assert self.exists_df(data_name), 'Dataset does not exist'
        self.datasets[data_name] = self.datasets[data_name].dropna(subset=[feature_name])
        self.datasets[data_name] = self.datasets[data_name][self.datasets[data_name].img != 'f']

    """
        Name: ready_parse
        Purpose: Cleans for only required data
    """
    def ready_parse(self, data_name):
        assert self.exists_df(data_name), 'Dataset does not exist'

        self.datasets[data_name] = self.datasets[data_name][['id',
                                                             'url',
                                                             'type',
                                                             'cost',
                                                             'impression',
                                                             'effect',
                                                             'img']]

    """
        Name: 'download_images'
        Purpose: Downloads required images to appropriate location
    """
    def download_images(self, data_name):
        assert self.exists_df(data_name), 'Dataset does not exist'

        for sample in self.datasets[data_name].itertuples():
            current_url = sample[8]
            print(current_url)

            filename = 'Images\\' + sample[2] + '.jpg'
            req = requests.get(current_url, allow_redirects=True)
            open(filename, 'wb').write(req.content)

    """
        Name: 'append_df'
        Purpose: Appends two datasets together
    """
    def append_df(self, data_name_one, data_name_two, resultant_dataset):
        assert self.exists_df(data_name_one), 'Dataset does not exist!'
        assert self.exists_df(data_name_two), 'Dataset does not exist!'
        assert not self.exists_df(resultant_dataset), 'Dataset already exists!'

        self.datasets[resultant_dataset] = self.datasets[data_name_one].append(self.datasets[data_name_two], ignore_index=True)

    """
        Name: get_df
        Purpose: Returns the appropriate dataframe back to simulation
    """
    def get_df(self, data_name):
        assert self.exists_df(data_name), 'Dataset does not exist!'
        return self.datasets[data_name]

    """
        Purpose: Adds external dataset to current instance
    """
    def add_df(self, data_name, dataframe):
        assert not self.exists_df(data_name), 'Dataset already exists'

        self.datasets[data_name] = dataframe