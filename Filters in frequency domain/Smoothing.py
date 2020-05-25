#importing packages
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import numpy as np

#Read image
img=cv2.imread('image.jpg',0)

#transformation to frequency domain using fast fourier transformation

from scipy import fftpack
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

#applying filter over the transformed image 
fshift=np.float32(fshift)
fshift = cv2.GaussianBlur(fshift,(5,5),0)

#converting the transformed image to usable format(human understandable format)
#To check whether the application of filter in frequency domain has any effect or not
magnitude_spectrum = np.log(np.abs(fshift))
temp=magnitude_spectrum*img
img_restored = cv2.GaussianBlur(temp,(5,5),0)

#Plotting the image
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_restored)
plt.title('real'), plt.xticks([]), plt.yticks([])
plt.show()
