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
        self.images[image_name] = cv2.imread(filepath)

    """
        Name: print_image()
        :param image_name: String - Name of the image to view
        Purpose: Displays image within current instance
    """
    def print_image(self, image_name):
        assert self.exists_image(self, image_name), 'Image does not exist!'
        cv2.imshow(image_name, self.images[image_name])
