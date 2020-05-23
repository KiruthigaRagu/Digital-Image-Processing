from PIL import Image
from google.colab.patches import cv2_imshow
import cv2
import numpy as np 
import matplotlib.pyplot as plt

im = cv2.imread("citlogo.png",1)

#sharpening
kernel = np.array([[0,-1,0], 
                   [-1, 12,-1],
                   [0,-1,0]])
sharpened = cv2.filter2D(im, -1, kernel)

#display sharpened images
cv2_imshow(sharpened)

#another way
aw = cv2.addWeighted(im, 4, cv2.blur(im, (30, 30)), -4, 128)
cv2_imshow(aw)

#laplacian filter for sharpening
new_image = cv2.Laplacian(im,cv2.CV_64F)
plt.figure(figsize=(11,6))
plt.subplot(131), plt.imshow(im, cmap='gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(new_image, cmap='gray'),plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(im + new_image, cmap='gray'),plt.title('Resulting image')
plt.xticks([]), plt.yticks([])
plt.show()
