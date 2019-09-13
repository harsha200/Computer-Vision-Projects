# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:45:39 2019

@author: hArSHA
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
 
img = cv2.imread('C:/Users/harsh/OneDrive/Pictures/Saved Pictures/Flower.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
# sobel 
x_sobel = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=5)
y_sobel = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=5)

# laplacian
lapl = cv2.Laplacian(gray,cv2.CV_64F, ksize=5)

# gaussian blur
blur = cv2.GaussianBlur(gray,(5,5),0)
# laplacian of gaussian
log = cv2.Laplacian(blur,cv2.CV_64F, ksize=5)

plt.imshow(lapl)
plt.axis('off')
plt.show()