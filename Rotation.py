# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:45:39 2019

@author: hArSHA
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
 
Eagle = cv2.imread('C:/Users/harsh/OneDrive/Pictures/Saved Pictures/Eagle.jpg')

# input shape
w, h = Eagle.shape[1], Eagle.shape[0]

# create rotation matrix
rot_angle = 45 # in degrees
scale = 1 # keep the size same
rotation_matrix = cv2.getRotationMatrix2D((w/2,h/2),rot_angle,1)

# apply translation operation using warp affine function. 
output_size = (w*2,h*2)
translated_flower = cv2.warpAffine(Eagle, rotation_matrix, output_size)

plt.imshow(translated_flower)
plt.axis('off')
plt.show()
