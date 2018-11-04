"""
Main function for stitching two images.
Design Doc: https://docs.google.com/document/d/1785FwZ11CizzumJ3CRqsoBdRwDlqTid2EWIUzbM2B2I/edit?usp=sharing

"""

from panorama_stitch import PanoramaStitcher
import imutils
import cv2

def return_stitched_image(path1, path2):
    """

    :param path1: path of the image that is standing still
    :param path2: path of the image that is being added
    :return: image
    """
    image_from_path1 = cv2.imread(path1)
    image_from_path2 = cv2.imread(path2)
    print("size",image_from_path1.shape)
    print("size",image_from_path2.shape)

    #Assuming that both pictures have same ratio of width and height.
    max_width_and_height = min(image_from_path2.shape[0], image_from_path1.shape[0])
    image_from_path1 = imutils.resize(image_from_path1, width=max_width_and_height, height=max_width_and_height )
    image_from_path2 = imutils.resize(image_from_path2, width=max_width_and_height, height=max_width_and_height )

    stitcher = PanoramaStitcher()

    combined_image = stitcher.stitch_two_images(image_from_path2, image_from_path1)

    # cv2.imshow("Combined Image", combined_image)
    # cv2.waitKey(0)
    return combined_image

combined_scaled_input1 = return_stitched_image(
    "test_data/scale/translation/input1_image1.jpg",
    "test_data/scale/translation/scaled_by_half_image1_input2.jpg")
cv2.imshow("combined_scaled_image_1", combined_scaled_input1)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_scale_image1.jpg", combined_scaled_input1)

combined_scaled_input2 = return_stitched_image(
    "test_data/scale/translation/input1_image2.jpg",
    "test_data/scale/translation/scaled_by_half_image2_input2.jpg")
cv2.imshow("combined_scaled_image_2", combined_scaled_input2)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_scale_image2.jpg", combined_scaled_input2)

combined_scaled_input3 = return_stitched_image(
    "test_data/scale/translation/scaled_by_half_image1_input1.jpg",
    "test_data/scale/translation/input2_image1.jpg")
cv2.imshow("combined_scaled_image_3", combined_scaled_input3)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_scale_image3.jpg", combined_scaled_input3)

combined_scaled_input4 = return_stitched_image(
    "test_data/scale/translation/scaled_by_half_image2_input1.jpg",
    "test_data/scale/translation/input2_image2.jpg")
cv2.imshow("combined_scaled_image_4", combined_scaled_input4)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_scale_image4.jpg", combined_scaled_input4)

combined_scaled_input5 = return_stitched_image(
    "test_data/scale/rotate/input1_image1.jpg",
    "test_data/scale/rotate/scaled_by_half_image1_input2.jpg")
cv2.imshow("combined_scaled_image_5", combined_scaled_input1)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_scale_image5.jpg", combined_scaled_input5)

combined_scaled_input6 = return_stitched_image(
    "test_data/scale/rotate/input1_image2.jpg",
    "test_data/scale/rotate/scaled_by_half_image2_input2.jpg")
cv2.imshow("combined_scaled_image_6", combined_scaled_input6)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_scale_image2.jpg", combined_scaled_input6)

combined_scaled_input7 = return_stitched_image(
    "test_data/scale/rotate/scaled_by_half_image1_input1.jpg",
    "test_data/scale/rotate/input2_image1.jpg")
cv2.imshow("combined_scaled_image_7", combined_scaled_input7)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_scale_image3.jpg", combined_scaled_input7)

combined_scaled_input8 = return_stitched_image(
    "test_data/scale/rotate/scaled_by_half_image2_input1.jpg",
    "test_data/scale/rotate/input2_image2.jpg")
cv2.imshow("combined_scaled_image_8", combined_scaled_input8)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_scale_image8.jpg", combined_scaled_input8)

combined_translation_image1 = return_stitched_image(
    "test_data/translation/input1_image1.jpg",
    "test_data/translation/input2_image1.jpg")
cv2.imshow("combined_translation_image1", combined_translation_image1)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_translation_image1.jpg", combined_translation_image1)

combined_translation_image2 = return_stitched_image(
    "test_data/translation/input1_image2.jpg",
    "test_data/translation/input2_image2.jpg")
cv2.imshow("combined_translation_image2", combined_translation_image2 )
cv2.waitKey(0)
cv2.imwrite("test_result/combined_translation_image2.jpg", combined_translation_image2)

combined_rotate_image1 = return_stitched_image(
    "test_data/rotate/input1_image1.jpg",
    "test_data/rotate/input2_image1.jpg")
cv2.imshow("combined_rotate_image1", combined_rotate_image1)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_rotate_image1.jpg", combined_rotate_image1)

combined_rotate_image2 = return_stitched_image(
    "test_data/rotate/input1_image2.jpg",
    "test_data/rotate/input2_image2.jpg")
cv2.imshow("combined_rotate_image2", combined_rotate_image2 )
cv2.waitKey(0)
cv2.imwrite("test_result/combined_rotate_image2.jpg", combined_rotate_image2)