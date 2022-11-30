# It is possible to convert gray scale image to a binary image using a technique called image thresholding.

# Let’s assume that we want the threshold to be 127, then everything that was 127 and under would be converted to 0 (or black)and everything above 127 would be converted to 255 (or white).

# If you don’t convert to grayscale before performing image thresholding, you will get threshold pictures, but there will be color, which doesn’t really help in most cases. This is the reason it is recommended to convert all images to gray scale before performing any binary thresholding operations.


from cv2 import threshold
import numpy as np
import cv2
img = cv2.imread('cat.jpg',1)
# The first argument is the source image, which should be a color image. The second argument specifies that the image should be converted to the Gray color space.
# The color is converted from BGR to Gray. This is because OpenCV reads color images in the BGR format and not in the RGB format. If you need the RGB image for any reason, you can use this same command with the second argument as cv2.COLOR_BGR2RGB.
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
th1,threshold=cv2.threshold(img,127,255,cv2.THRESH_BINARY)   #The second argument is the threshold value which is used to classify the pixel values, usually in the range between 125-150.

# In some cases, we will need to adapt to a specific picture, say a book, which has many curvatures that may cause shadows at the curvatures. In this case, with simple binary thresholding, the region at the curvature will be completely turned to black, making the entire exercise useless. For this reason, we can use adaptive thresholding.
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

# Here, the first argument img is the variable name of the image which needs to be thresholded. The second argument 255 is the value which needs to be applied if a pixel value is greater than the calculated threshold. The third argument cv2.ADAPTIVE_THRESH_MEAN_C indicates that the threshold is calculated using the mean of values around a pixel. cv2.THRESH_BINARY specifies the type  of thresholding to be performed after a threshold is calculated. The third argument tells the block size around a pixel which is taken to calculate the mean. In this case, a 11×11 grid around every pixel is taken to calculate the mean. The last argument specifies an overall negative correction which needs to be applied after calculating the mean. In this case, the threshold for every pixel will be [mean(11×11 grid around pixel) – 2 ]