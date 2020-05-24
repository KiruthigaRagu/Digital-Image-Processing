#fast fourier transform

import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('image.jpg',0)

from scipy import fftpack

#fft with numpy array
f = np.fft.fft2(img)
f_shift = np.fft.fftshift(f)
f_complex = f_shift
cv2_imshow(f)
