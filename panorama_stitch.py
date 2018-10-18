"""
Panorama Stitching Class
Given two images, return a stitched image.
Two images could be rotated.

Design Doc: https://docs.google.com/document/d/1785FwZ11CizzumJ3CRqsoBdRwDlqTid2EWIUzbM2B2I/edit?usp=sharing

"""

import numpy as np
import imutils
import cv2

class PanoramaStitcher:

    def __int__(self):
        pass

    def stitch_two_images(self, image1, image2):
        """
        :param image1:
        :param image2:
        :return: stitched image
        """
        (key_points_from_image1, features_from_image1) = self.get_key_points_and_features(image1)
        (key_points_from_image2, features_from_image2) = self.get_key_points_and_features(image2)

    def get_key_points_and_features(self, image):
        """
        :param image:
        :return: (keypoints in np array, features)
        """
        (key_points, features) = cv2.xfeatures2d.SIFT_create().detectAndCompute(image, None)

        key_points = np.float32([element.pt for element in key_points])

        return (key_points, features)
