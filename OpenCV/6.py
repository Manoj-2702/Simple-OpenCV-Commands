import numpy as np
import cv2

# Just like in one-dimensional signals, images can also be filtered using various low-pass filters(LPF) and high pass filters(HPF). LPF helps in removing noise, blurring the image etc. HPF helps define the edges in any given image.
# Gaussian blurring is a kind of low-pass filter that uses a “Gaussian Kernel”. A “Gaussian Kernel” is a square array of pixels where the pixel values will correspond to a set of values of a Gaussian curve which means that the image will be blurred uniformly.
img = cv2.imread('cat.jpg')
cv2.GaussianBlur(img,(kernel_width,kernel_height),standard_deviation)

# To learn more about this visit this website
# https://computergraphics.stackexchange.com/questions/39/how-is-gaussian-blur-implemented
