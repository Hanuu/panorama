import imutils
import cv2

def return_reduced_scale_by(reduction_percent, image_path):
    image_from_path = cv2.imread(image_path)
    resized_image = imutils.resize(image_from_path, width = int(image_from_path.shape[0] * reduction_percent), height = int(image_from_path.shape[1]* reduction_percent))
    return resized_image

cv2.imwrite("scaled_by_half_image2_input1.jpg", return_reduced_scale_by(0.5,"rotate/input1_image2.jpg"))
cv2.imwrite("scaled_by_half_image2_input2.jpg", return_reduced_scale_by(0.5,"rotate/input2_image2.jpg"))

# print(cv2.imread("rotate/input1_image2.jpg").shape)
# print(cv2.imread("rotate/scaled_by_half_image2_input1.jpg").shape)