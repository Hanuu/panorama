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

        homography_matrix = self.get_homography_matrix(key_points_from_image1, features_from_image1,
                                                       key_points_from_image2, features_from_image2)

        result = cv2.warpPerspective(image1, homography_matrix,
                                     (image1.shape[1] + image2.shape[1], image1.shape[0]))

        result[:image2.shape[0], :image2.shape[1]] = image2

        return result

    def get_key_points_and_features(self, image):
        """
        :param image:
        :return: (keypoints in np array, features)
        """
        (key_points, features) = cv2.xfeatures2d.SIFT_create().detectAndCompute(image, None)

        key_points = np.float32([element.pt for element in key_points])

        return (key_points, features)

    def get_homography_matrix(self, key_points_from_image1, features_from_image1,
                              key_points_from_image2, features_from_image2):
        """
        :param key_points_from_image1:
        :param features_from_image1:
        :param key_points_from_image2:
        :param features_from_image2:
        :return: homography matrix
        """
        raw_matches = cv2.DescriptionMatcher_create("BruteForce").knnMatch(features_from_image1,
                                                                           features_from_image2, 2)
        matches = []

        for raw_match in raw_matches:
            if len(raw_match) == 2 and raw_match.distance < raw_match.distance:
                matches.append((raw_match[0].trainIdx, raw_match[0].queryIdx))

        points_from_image1 = []
        points_from_image2 = []
        for match in matches:
            points_from_image1.append(match[1])
            points_from_image1.append(match[0])

        points_from_image1 = np.float32(points_from_image1)
        points_from_image2 = np.float32(points_from_image2)
        (homography_graph, status) = cv2.findHomography(points_from_image1, points_from_image2,
                                                        cv2.RANSAC, 5.0)

        return homography_graph
