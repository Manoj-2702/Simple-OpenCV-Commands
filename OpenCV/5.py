#  SHRINKING AND ZOOMING

import cv2
import numpy as np
img = cv2.imread('cat.jpg')
# res = cv2.resize(img,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_AREA)
res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_AREA)
cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
# there is an argument in the cv2.resize() function called interpolation. When the size of an image changes, we need to calculate the pixel values of the new image from the old one. This process is called interpolation and there are several ways of doing this; INTER_AREA is one such argument that helps us achieve this.
# Using cv2.INTER_AREA gives a pixelated image when zooming. To get a better image when zoomed, try more complex interpolation methods like cv2.INTER_CUBIC.



# res = cv2.resize(img,None,fx=10, fy=10, interpolation = cv2.INTER_AREA)