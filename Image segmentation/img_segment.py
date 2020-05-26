#Import libraries
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import numpy as np

#read image
img=cv2.imread('image.jpg',1)

#check the shape of an image
img.shape

#resize the image(optional)
img = cv2.resize(img,(512,450))

#Image segmentation
#segmentation based on thresholding(mean)
gray_r = img.reshape(img.shape[0]*img.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 1
    else:
        gray_r[i] = 0
gray = gray_r.reshape(img.shape[0],img.shape[1])
plt.imshow(gray, cmap='gray')

#other method 
gray = img
gray_r = gray.reshape(img.shape[0]*img.shape[1])
for i in range(gray_r.shape[0]):
    if gray_r[i] > gray_r.mean():
        gray_r[i] = 3
    elif gray_r[i] > 0.5:
        gray_r[i] = 2
    elif gray_r[i] > 0.25:
        gray_r[i] = 1
    else:
        gray_r[i] = 0
gray = gray_r.reshape(img.shape[0],img.shape[1])
plt.imshow(gray, cmap='gray')



