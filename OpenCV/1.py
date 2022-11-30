import numpy as np
import cv2
img = cv2.imread('cat.jpg',1) 
#The function cv2.imread() has two arguments. The first refers to the image which needs to be read and the second refers to how the image needs to be read. The second argument can take values of 0,1,and -1. 0 will load the image in grayscale, -1 will load the image unchanged and 1 will load the image in color
# By default, 1 is chosen if the second argument is not specified
cv2.imshow('image',img) #show/display the image using the cv2.imshow() function
# The first argument is the title of the window where we want the image to be displayed. If the window doesn’t exist, a window of that name will be created. The second is the name of the variable which contains the image, which in this case is img which we created in the previous line.
cv2.waitKey(0)
cv2.destroyAllWindows()
# The next two lines of code are intended to display the image continuously until any key is pressed on the keyboard. Once a key is pressed the image displayed will automatically be destroyed as described by the last line of the code.
# cv2.imshow() command must always be put with cv2.waitkey() command. cv2.waitKey() is a keyboard binding function having it’s only argument as the time in milliseconds. The function waits for the specified number of milliseconds. If 0 is passed, it waits indefinitely until a key is stroked. It can also be set to detect specific key strokes, such as the key ‘q’ for quitting.