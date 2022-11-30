# we can also use the matplotlib library to display the images. Matplotlib is a plotting library that gives us publication quality plots of our data.
import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('cat.jpg', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()


# The first two lines are the same as the previous code. The third line imports the pyplot package from matplotlib and the fourth reads the image in grayscale.. The following link explains the meaning of the various arguments line 5: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
