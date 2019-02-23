"""
    Name: SimulateTraining.py
    Purpose: Simulates Training of the model on current data
"""

from Data.Analysis.CleaningToolkit import Analysis as an
from ImageExtraction.ImportImages import Images as im


def main():
    clean_data = an()
    an.import_csv(clean_data, 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Data\\GoogleData\\clean_final.csv', 'final')
    an.download_images(clean_data, 'final')

if __name__ == '__main__':
    main()
