from PIL import Image
from google.colab.patches import cv2_imshow
import cv2
import numpy as np 
import matplotlib.pyplot as plt

im = cv2.imread("citlogo.png",1)

#smoothening - average filtering
blur = cv2.blur(im,(5,5))

plt.subplot(121),plt.imshow(im),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

#smoothening - median filtering
median = cv2.medianBlur(im,5)
plt.subplot(121),plt.imshow(im),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
