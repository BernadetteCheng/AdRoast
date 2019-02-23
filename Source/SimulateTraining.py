"""
    Name: SimulateTraining.py
    Purpose: Simulates Training of the model on current data
"""

from Data.Analysis.CleaningToolkit import Analysis as an
from ImageExtraction.ImportImages import Images as im


def main():
    image_analysis = im()
    data_analysis = an()

    an.import_csv(data_analysis, 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Data\\GoogleData\\clean_final.csv', 'clean')
    final_df = an.get_df(data_analysis, 'clean')

    for row in final_df.itertuples():
        image_path = 'Images\\' + row[2] + '.jpg'
        im.import_image(image_analysis, image_path, row[2])

    final_df = final_df[['id', 'effect']]
    final_df = im.grab_features(image_analysis, final_df)
    final_df = final_df.dropna(subset=['r_mean'])
    final_df.to_csv('Training\\FinalTrain.csv')

if __name__ == '__main__':
    main()
