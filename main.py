from panorama_stitch import PanoramaStitcher
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("--first", required=True)
ap.add_argument("--second", required=True)
args = vars(ap.parse_args())

image1 = cv2.imread(args["first"])
image2 = cv2.imread(args["second"])
image1 = imutils.resize(image1, width=400)
image2 = imutils.resize(image2, width=400)

example1 = PanoramaStitcher()

combined_image = example1.stitch_two_images(image1, image2)


cv2.imshow("Image1", image1)
cv2.imshow("Image2", image2)
cv2.imshow("Combined Image", combined_image)
cv2.waitKey(0)