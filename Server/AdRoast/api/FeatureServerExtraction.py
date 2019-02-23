"""
    Name: FeatureServerExtraction
    Purpose: Takes image input and provides resultant category
"""

import cv2
import pickle
import pandas as pd

MODEL_PATH = '/static/adroast_model.sav'

def extract_feature(filepath):
    ad_image = cv2.imread(filepath, cv2.COLOR_BGR2RGB)
    feature_set = {}

    feature_set['colorfullness'] = image_colorfulness(ad_image)
    feature_set['edges'] = harris_corner_detection(ad_image)

    feature_analysis = rgb_hist_analysis(ad_image)

    feature_set['r_mean'] = feature_analysis[0]
    feature_set['r_variance'] = feature_analysis[1]
    feature_set['r_kurtosis'] = feature_analysis[2]
    feature_set['r_skewness'] = feature_analysis[3]
    feature_set['g_mean'] = feature_analysis[4]
    feature_set['g_variance'] = feature_analysis[5]
    feature_set['g_kurtosis'] = feature_analysis[6]
    feature_set['g_skewness'] = feature_analysis[7]
    feature_set['b_mean'] = feature_analysis[8]
    feature_set['b_variance'] = feature_analysis[9]
    feature_set['b_kurtosis'] = feature_analysis[10]
    feature_set['b_skewness'] = feature_analysis[11]

    prediction_features = pd.DataFrame.from_dict(feature_set)

    adroast_model = pickle.load(open(MODEL_PATH, 'rb'))
    score = adroast_model.predict(prediction_features)

    grade = classify_effect(score)
    improvements = ['FIX UR ADS']

    return [grade, improvements, score[0]]

"""
    Purpose: Determines colorfulness feature of ad image
"""
@staticmethod
def image_colorfulness(image):
    (R,G,B) = cv2.split(image.astype('float'))
    RG = np.absolute(R - G)
    YB = np.absolute(((R + G) * 0.5) - B)

    (RGMEAN, RBSTD) = (np.mean(RG), np.std(RG))
    (YBMEAN, YBSTD) = (np.mean(YB), np.std(YB))

    STANDARD = np.sqrt((RBSTD ** 2) + (YBSTD ** 2))
    MEAN = np.sqrt((RGMEAN ** 2) + (YBMEAN ** 2))

    COLORFULNESS = (STANDARD + (0.3 * MEAN))
    return COLORFULNESS

"""
    Purpose: Provides the number of edges that were observed in the ad
"""
@staticmethod
def harris_corner_detection(image):
    gray_component = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_component = np.float32(gray_component)
    destination = cv2.cornerHarris(gray_component, 2, 3, 0.04)
    destination = cv2.dilate(destination, None)

    return len(destination)

"""
    Purpose: Analyzes specific components of the rgb_histogram
"""
@staticmethod
def rgb_hist_analysis(image):
    specific_amounts = []
    histograms = self.rgb_hist(image)

    for histogram in histograms:
        mean = np.mean(histogram)
        variance = np.var(histogram)
        kurtosis = scipy.stats.kurtosis(histogram)
        skewness = scipy.stats.skew(histogram)

        specific_amounts.append(float(mean))
        specific_amounts.append(float(variance))
        specific_amounts.append(float(kurtosis))
        specific_amounts.append(float(skewness))

    return specific_amounts

"""
    Purpose: Analyzes the RGB Histogram of an advertisement
"""
@staticmethod
def rgb_hist(image):
    colour = ('b', 'g', 'r')
    rgb_histograms = []

    for i, colour in enumerate(colour):
        rgb_histogram = cv2.calcHist([image, [i], None, [256], [0, 256])
        rgb_histograms.append(rgb_histogram)

    return(rgb_histograms)

"""
    Purpose: Grades customers advertisement specific to provided effect
"""
@staticmethod
def classify_effect(score):
    specific_score = int(score[0])

    if specific_score < 10:
        return 'Terrible'
    elif specific_score < 80:
        return 'Poor'
    elif specific_score < 220:
        return 'Fair'
    elif specific_score < 1200:
        return 'Good'
    elif specific_score < 5000:
        return 'Amazing'
    else:
        return 'Superb'
