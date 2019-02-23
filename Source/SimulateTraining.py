"""
    Name: SimulateTraining.py
    Purpose: Simulates Training of the model on current data
"""

from Data.Analysis.CleaningToolkit import Analysis as an
from ImageExtraction.ImportImages import Images as im


def main():
    image_analysis = im()
    im.import_image(image_analysis, 'Data\\Images\\10795125566885164803.jpg', 'original')
    im.image_colorfulness(image_analysis, 'original')
    im.harris_corner_detection(image_analysis, 'original', False)
    im.rgb_hist_analysis(image_analysis, 'original')

if __name__ == '__main__':
    main()
