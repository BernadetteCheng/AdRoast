"""
    Name: SimulateTraining.py
    Purpose: Simulates Training of the model on current data
"""

from Data.Analysis.CleaningToolkit import Analysis as an
import pandas as pd

def main():
    data_analysis = an()

    an.import_csv(data_analysis, 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Training\\FinalTrain.csv', 'current')
    an.import_csv(data_analysis, 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Data\\GoogleData\\original.csv', 'initial')

    initial_df = an.get_df(data_analysis, 'initial')
    current_df = an.get_df(data_analysis, 'current')
    an.add_df(data_analysis, 'description', current_df.describe())
    an.write_df(data_analysis, 'description', 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Training\\Summary.csv')

    initial_df = initial_df.rename(columns={'Ad_ID' : 'id'})

    clean_df = current_df.merge(initial_df, on='id', how='left')
    clean_df = clean_df[['id',
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
                         'b_skewness',
                         'Spend_USD',
                         'Impressions']]

    an.add_df(data_analysis, 'clean', clean_df)
    an.clean_features(data_analysis, 'clean')
    an.write_df(data_analysis, 'clean', 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Training\\FinalCompleteTrain.csv')


if __name__ == '__main__':
    main()
