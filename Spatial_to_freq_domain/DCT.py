from PIL import Image
from google.colab.patches import cv2_imshow
import cv2
import numpy as np 
import matplotlib.pyplot as plt

im = cv2.imread("citlogo.png",1)

#discrete cosine transformation
from scipy.fftpack import dct
d=dct(im,type=2)
cv2_imshow(d)

#this displays a black and white conversion image
#Even though it puts up a random a random image, what we get is the correct image(in frequency domain),
#to know whether the coversion has any effect on the image, check the folder Application of filters in frequency domain
