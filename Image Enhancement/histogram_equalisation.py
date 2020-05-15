#Import packages
from PIL import Image
from google.colab.patches import cv2_imshow
import cv2
import numpy as np 
import matplotlib.pyplot as plt

#Read image in RGB format
im = cv2.imread("image.png",1)

#Create histogram bins
hist,bins = np.histogram(im.flatten(),256,[0,256])

#calculate the cummulative distribution function
cdf = hist.cumsum()

#Normalizing the cdf
cdf_normalized = cdf * hist.max()/ cdf.max()

#Plotting the normalized image
plt.plot(cdf_normalized, color = 'b')
plt.hist(im.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

# using OpenCV:
equ = cv2.equalizeHist(im)
res = np.hstack((im,equ))

#Plotting the enhanced image
cv2_imshow(res)
