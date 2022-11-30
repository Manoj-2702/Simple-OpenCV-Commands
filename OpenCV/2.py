# If you want to destroy any specific window, pass the exact window name as the argument into this function.
import numpy as np
import cv2
img = cv2.imread('cat.jpg')
cv2.imshow('image',img)
i = cv2.waitKey(0) 
if i == 27: 
    cv2.destroyAllWindows()
elif i == ord('s'):
    cv2.imwrite('cat_saved.jpg',img)
cv2.destroyAllWindows()