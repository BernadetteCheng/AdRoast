"""
    Name: SimulateTraining.py
    Purpose: Simulates Training of the model on current data
"""

from Data.Analysis.CleaningToolkit import Analysis as an


def main():
    clean_dataset = an()
    an.import_csv_limited(clean_dataset, 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Data\\GoogleData\\clean_data.csv', 'google', 1)
    an.pull_images(clean_dataset, 'google')
    #an.remove_non_image(clean_dataset, 'google')
    #an.clean_features(clean_dataset, 'google')
    #an.write_df(clean_dataset, 'google', 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Data\\GoogleData\\clean_data.csv')

if __name__ == '__main__':
    main()
