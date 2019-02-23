"""
    Author: Taha Masood
    Name: ImportImages
    Purpose: Toolkit to handle importing images
"""

import cv2
import matplotlib
import math
import pandas as pd
import numpy as np
import time


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