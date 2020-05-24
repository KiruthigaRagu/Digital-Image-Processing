import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('anthropod.jpg',0)

#discrete fourier transformation
def dft(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)
    
 k=dft(img)
 cv2_imshow(k)
