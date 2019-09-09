# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:38:49 2019

@author: hArSHA
"""

import os
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


# Load the image from the source file
image_file = "C:/Users/harsh/OneDrive/Pictures/Saved Pictures/Mini Art.jpg"
image = Image.open(image_file)

blurred_image = image.filter(ImageFilter.BLUR)
sharpened_image = image.filter(ImageFilter.SHARPEN)

# Display it
fig = plt.figure(figsize=(16, 12))

# Plot original image
a=fig.add_subplot(1, 3, 1)
image_plot_1 = plt.imshow(image)
a.set_title("Original")

# Plot blurred image
a=fig.add_subplot(1, 3, 2)
image_plot_2 = plt.imshow(blurred_image)
a.set_title("Blurred")

# Plot sharpened image
a=fig.add_subplot(1, 3, 3)
image_plot_3 = plt.imshow(sharpened_image)
a.set_title("Sharpened")

plt.show()