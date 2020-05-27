#import libraries
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import numpy as np

#read image
img=cv2.imread('image.jpg',1)


#REGION BASED SEGMENTATION

from skimage.filters import sobel

region = sobel(img)

fig, ax = plt.subplots(figsize=(4, 3))
ax.imshow(region, cmap=plt.cm.gray, interpolation='nearest')
ax.axis('off')
ax.set_title('Region based segmentation')
