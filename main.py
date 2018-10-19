from panorama_stitch import PanoramaStitcher
import imutils
import cv2

#
image1 = cv2.imread("test_data/translation/input1_image1.jpg")
image2 = cv2.imread("test_data/translation/input2_image1.jpg")
# image1 = imutils.resize(image1, width=100)
# image2 = imutils.resize(image2, width=100)

example1 = PanoramaStitcher()

combined_image = example1.stitch_two_images(image2,image1)


# cv2.imshow("Image1", image1)
# cv2.imshow("Image2", image2)
cv2.imshow("Combined Image", combined_image)
cv2.waitKey(0)