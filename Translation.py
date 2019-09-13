# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 17:45:39 2019

@author: hArSHA
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
 
flower = cv2.imread('C:/Users/harsh/OneDrive/Pictures/Saved Pictures/Flower.png')

# input shape
w, h = flower.shape[1], flower.shape[0]

# create translation matrix
tx = w/2 # half of width
ty = h/2 # half of height
translation_matrix = np.float32([[1,0,tx],
                                 [0,1,ty]])

# apply translation operation using warp affine function. 
output_size = (w*2,h*2)
translated_flower = cv2.warpAffine(flower, translation_matrix, output_size)

plt.imshow(translated_flower)
plt.axis('off')
plt.show()
