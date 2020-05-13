from PIL import Image
from google.colab.patches import cv2_imshow
import cv2
import numpy as np 
import matplotlib.pyplot as plt

#Read image in RGB format
im = cv2.imread("image.png",1)

#view image
cv2_imshow(im)

#converting image to HSV colour model
im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

#converting image to HSV colour model
im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

#converting image to CMYK colour model
im_cmyk=cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)

cv2_imshow(im_cmyk)
