"""
    Name: Training.py
    Purpose: Trains the model on the current adroast data
"""

from Training.TrainModel import Train as tr
from Data.Analysis.CleaningToolkit import Analysis as an
from ImageExtraction.ImportImages import Images as im

def main():
    data_analysis = an()
    model_training = tr()

    an.import_csv(data_analysis, 'C:\\Users\\Taha Masood\\Desktop\\AdRoast\\Source\\Training\\FinalTrain.csv' , 'train')
    train_df = an.get_df('train')

    input_features = train_df[['colorfullness',
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

    target_features = train_df[['effect']]
    tr.train_model(model_training, input_features, target_features)

if __name__=='__main__':
    main()
