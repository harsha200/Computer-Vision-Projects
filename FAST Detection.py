# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:20:52 2019

@author: hArSHA
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
 
def compute_fast_det(filename, is_nms=True, thresh = 10):
    """
    Reads image from filename and computes FAST keypoints.
    Returns image with keypoints
    filename: input filename
    is_nms: flag to use Non-maximal suppression
    thresh: Thresholding value
    """
    img = cv2.imread(filename)
   
    # Initiate FAST object with default values
    fast = cv2.FastFeatureDetector_create() 

    # find and draw the keypoints
    if not is_nms:
        fast.setNonmaxSuppression(0)

    fast.setThreshold(thresh)

    kp = fast.detect(img,None)
    cv2.drawKeypoints(img, kp, img, color=(255,0,0))
    
    return img

def main():
    
    Result = compute_fast_det('C:/Users/harsh/OneDrive/Pictures/Saved Pictures/Flower.png', True, 50)
    
    plt.imshow(cv2.cvtColor(Result, cv2.COLOR_BGR2RGB))
    
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
    