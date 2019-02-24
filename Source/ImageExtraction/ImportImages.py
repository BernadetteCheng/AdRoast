"""
    Author: Taha Masood
    Name: ImportImages
    Purpose: Toolkit to handle importing images
"""

import cv2
import numpy as np
import scipy
from scipy import stats
from scipy.misc import imread
import random
import os
from PIL import Image as im
import matplotlib.pyplot as plt


class Images:

    """
        Purpose: Initializer
    """
    def __init__(self):
        self.images = {}

    """
        Name: exists_image()
        :param image_name: String - Name of image to check
        Purpose: Determines if a requested image already exists in the current
                 analysis instance.
        :return image_exists: Boolean - True if image exists in current instance,
                                        false otherwise.
    """
    @staticmethod
    def exists_image(self, image_name):
        if (image_name in self.images):
            return True
        else:
            return False

    """
        Name: import_image()
        :param filepath: String - Path to the input JPEG file
        :param image_name: String - Assigned name of the image
        Purpose: Reads in image data from raw JPEG file and adds to dictionary
    """
    def import_image(self, filepath, image_name):
        assert not self.exists_image(self, image_name), 'Image already exists!'
        self.images[image_name] = cv2.imread(filepath, cv2.COLOR_BGR2RGB)

    """
        Name: print_image()
        :param image_name: String - Name of the image to view
        Purpose: Displays image within current instance
    """
    def print_image(self, image_name):
        assert self.exists_image(self, image_name), 'Image does not exist!'
        cv2.imshow(image_name, self.images[image_name])
        cv2.waitKey()

    """
        Name: brief_feature
        Purpose: Conducts brief feature extraction
    """
    def brief_feature_extraction(self, image_name):
        assert self.exists_image(self, image_name), 'Image does not exist'

        star = cv2.FeatureDetector_create("STAR")
        brief = cv2.DescriptorExtractor_create("BRIEF")

        star_detection = star.detect(self.images[image_name], None)
        star_detection, descriptions = brief.compute(self.images[image_name], star_detection)

        print(brief.getInt('bytes'))
        print(descriptions.shape)

    def sift_feature_extraction(self, image_name):
        assert self.exists_image(self, image_name), 'Image does not exist'
        gray = cv2.cvtColor(self.images[image_name], cv2.COLOR_BGR2GRAY)

        sift = cv2.SIFT()
        kp = sift.detect(gray, None)
        img = cv2.drawKeypoints(gray, kp)

        cv2.imwrite('sift_keypoints.jpg', img)

    """
        Purpose: Determines the colorfulness level of a given image
        Status: Complete
    """
    def image_colorfulness(self, image_name):
        assert self.exists_image(self, image_name), 'Image does not exist!'

        (R,G,B) = cv2.split(self.images[image_name].astype('float'))
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
    def harris_corner_detection(self, image_name, display_image):
        assert self.exists_image(self, image_name), 'Image does not exist!'

        gray_component = cv2.cvtColor(self.images[image_name], cv2.COLOR_BGR2GRAY)

        gray_component = np.float32(gray_component)
        destination = cv2.cornerHarris(gray_component, 2, 3, 0.04)
        destination = cv2.dilate(destination, None)

        if display_image:
            self.images[image_name][destination > 0.01 * destination.max()] = [0, 0, 255]

            cv2.imshow('destination', self.images[image_name])
            if cv2.waitKey(0) & 0xff == 27:
                cv2.destroyAllWindows()

        return len(destination)

    """
        Purpose: Analyzes the RGB Histogram of an advertisement
    """
    def rgb_hist(self, image_name, display):
        assert self.exists_image(self, image_name), 'Image does not exist!'
        colour = ('b', 'g', 'r')
        rgb_histograms = []

        for i, colour in enumerate(colour):
            rgb_histogram = cv2.calcHist([self.images[image_name]], [i], None, [256], [0, 256])
            rgb_histograms.append(rgb_histogram)

            if display:
                plt.plot(rgb_histogram, color=colour)
                plt.xlim([0, 256])

        if display:
            plt.show()

        return(rgb_histograms)

    """
        Purpose: Analyzes the Histogram of an advertisement
    """
    def hist(self, image_name):
        assert self.exists_image(self, image_name), 'Image does not exist'

        histogram = plt.hist(self.images[image_name].ravel(), 256, [0, 256]);
        print(type(histogram))
        plt.show()

    """
        Purpose: Analyzes specific components of the rgb_histogram
    """
    def rgb_hist_analysis(self, image_name):
        assert self.exists_image(self, image_name), 'Image does not exist'

        specific_amounts = []
        histograms = self.rgb_hist(image_name, False)

        for histogram in histograms:
            mean = np.mean(histogram)
            variance = np.var(histogram) / mean
            kurtosis = scipy.stats.kurtosis(histogram) / mean
            skewness = scipy.stats.skew(histogram) / mean

            specific_amounts.append(float(mean))
            specific_amounts.append(float(variance))
            specific_amounts.append(float(kurtosis))
            specific_amounts.append(float(skewness))

        return specific_amounts

    """
        Name: grab_features
        Purpose: Cleans and extracts required image features
    """
    def grab_features(self, final_df):
        final_df['colorfullness'] = final_df.apply(self.colorful, axis=1)
        final_df['edges'] = final_df.apply(self.edges, axis=1)
        final_df['r_mean'] = final_df.apply(self.rmean, axis=1)
        final_df['r_variance'] = final_df.apply(self.rvar, axis=1)
        final_df['r_kurtosis'] = final_df.apply(self.rkurtosis, axis=1)
        final_df['r_skewness'] = final_df.apply(self.rskew, axis=1)
        final_df['g_mean'] = final_df.apply(self.gmean, axis=1)
        final_df['g_variance'] = final_df.apply(self.gvar, axis=1)
        final_df['g_kurtosis'] = final_df.apply(self.gkurtosis, axis=1)
        final_df['g_skewness'] = final_df.apply(self.gskew, axis=1)
        final_df['b_mean'] = final_df.apply(self.bmean, axis=1)
        final_df['b_variance'] = final_df.apply(self.bvar, axis=1)
        final_df['b_kurtosis'] = final_df.apply(self.bkurtosis, axis=1)
        final_df['b_skewness'] = final_df.apply(self.bskew, axis=1)

        return final_df

    """
        Purpose: Receives updated feature from image
    """
    def colorful(self, row):
        try:
            return self.image_colorfulness(row.id)
        except:
            print('Exception')

    """
        Purpose: Receives updated feature from image
    """
    def edges(self, row):
        try:
            return self.harris_corner_detection(row.id, False)
        except:
            print('Exception')

    """
        Purpose: Receives updated feature from image
    """
    def rmean(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[0]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def rvar(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[1]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def rkurtosis(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[2]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def rskew(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[3]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def gmean(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[4]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def gvar(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[5]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def gkurtosis(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[6]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def gskew(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[7]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def bmean(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[8]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def bvar(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[9]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def bkurtosis(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[10]
        except:
            print('Exception')
    """
        Purpose: Receives updated feature from image
    """
    def bskew(self, row):
        try:
            return self.rgb_hist_analysis(row.id)[11]
        except:
            print('Exception')