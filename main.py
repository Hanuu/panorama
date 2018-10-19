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

    # image_from_path1 = imutils.resize(image_from_path1, width=300)
    # image_from_path2 = imutils.resize(image_from_path2, width=300)

    stitcher = PanoramaStitcher()

    combined_image = stitcher.stitch_two_images(image_from_path2, image_from_path1)

    # cv2.imshow("Combined Image", combined_image)
    # cv2.waitKey(0)
    return combined_image

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
    "test_data/translation/input1_image1.jpg",
    "test_data/translation/input2_image1.jpg")
cv2.imshow("combined_rotate_image1", combined_rotate_image1)
cv2.waitKey(0)
cv2.imwrite("test_result/combined_rotate_image1.jpg", combined_rotate_image1)

combined_rotate_image2 = return_stitched_image(
    "test_data/translation/input1_image2.jpg",
    "test_data/translation/input2_image2.jpg")
cv2.imshow("combined_rotate_image2", combined_rotate_image2 )
cv2.waitKey(0)
cv2.imwrite("test_result/combined_rotate_image2.jpg", combined_rotate_image2)