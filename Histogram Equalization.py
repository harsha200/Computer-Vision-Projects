# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 00:18:03 2019

@author: hArSHA
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image as mp_image
from skimage import exposure

# Required magic to display matplotlib plots in notebooks
#%matplotlib inline

# Load the image from the source file
image_file = "C:/Users/harsh/OneDrive/Pictures/Saved Pictures/city.jpg"
image = mp_image.imread(image_file)

# Display it
#plt.imshow(image)

plt.hist(image.ravel())
plt.show()

plt.hist(image.ravel(), bins=255, cumulative=True)
plt.show()

# Histogram Equalization
image_eq = exposure.equalize_hist(image)

fig = plt.figure(figsize=(20, 252))

# Subplot for original image
a=fig.add_subplot(3,3,1)
imgplot = plt.imshow(image)
a.set_title('Original')

# Subplot for equalized image
a=fig.add_subplot(3,3,3)
imgplot = plt.imshow(image_eq)
a.set_title('Histogram Equalized')