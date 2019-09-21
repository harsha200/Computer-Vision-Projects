# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:20:52 2019

@author: hArSHA
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
 
Eagle = cv2.imread('C:/Users/harsh/OneDrive/Pictures/Saved Pictures/Flower.png')

EagleGray = cv2.cvtColor(Eagle, cv2.COLOR_BGR2GRAY)

# harris corner parameters
block_size = 4 # Covariance matrix size
kernel_size = 3 # neighbourhood kernel
k = 0.01 # parameter for harris corner score

# compute harris corner
corners = cv2.cornerHarris(EagleGray, block_size, kernel_size, k)

# create corner image
display_corner = np.ones(EagleGray.shape[:2])
display_corner = 255*display_corner
# apply thresholding to the corner score
thres = 0.01 # more than 1% of max value
display_corner[corners>thres*corners.max()] = 10 #display pixel value

# set up display
plt.figure(figsize=(12,8))
plt.imshow(display_corner, cmap='gray')
plt.axis('off')