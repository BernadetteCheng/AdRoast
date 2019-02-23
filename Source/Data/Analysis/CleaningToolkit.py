"""
    Name: CleaningToolkit.py
    Purpose: Clean raw google advertisement dataset
"""
import pandas as pd
import numpy as np

class analysis:

    """
        Purpose: Initializer
    """
    def __init__(self):
        self.datasets = {}

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
