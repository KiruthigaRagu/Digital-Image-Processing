#import libraries
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import numpy as np

#read image
img=cv2.imread('image.jpg',1)

#EROSION
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
plt.imshow(erosion)

dilation = cv2.dilate(img,kernel,iterations = 1)
plt.imshow(dilation)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
plt.imshow(opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
plt.imshow(closing)

#thinning
thinned = cv2.ximgproc.thinning(img)
cv2_imshow(thinned)
