# the implementation of the Zhang-Suen Thinning Algorithm for skeletonization is by Linbo<linbo.me> on github

import matplotlib.pyplot as plt
import skimage.io as io
import cv2
import numpy as np
from skimage.filters import threshold_otsu
from imutils import paths

def neighbours(x,y,image):
    "Return 8-neighbours of image point P1(x,y), in a clockwise order"
    img = image
    x_1, y_1, x1, y1 = x-1, y-1, x+1, y+1
    return [ img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],     # P2,P3,P4,P5
                img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1] ]    # P6,P7,P8,P9

def transitions(neighbours):
    "No. of 0,1 patterns (transitions from 0 to 1) in the ordered sequence"
    n = neighbours + neighbours[0:1]      # P2, P3, ... , P8, P9, P2
    return sum( (n1, n2) == (0, 1) for n1, n2 in zip(n, n[1:]) )  # (P2,P3), (P3,P4), ... , (P8,P9), (P9,P2)

def zhangSuen(image):
    "the Zhang-Suen Thinning Algorithm"
    Image_Thinned = image.copy()  # deepcopy to protect the original image
    changing1 = changing2 = 1        #  the points to be removed (set as 0)
    while changing1 or changing2:   #  iterates until no further changes occur in the image
        # Step 1
        changing1 = []
        rows, columns = Image_Thinned.shape               # x for rows, y for columns
        for x in range(1, rows - 1):                     # No. of  rows
            for y in range(1, columns - 1):            # No. of columns
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1     and    # Condition 0: Point P1 in the object regions 
                    2 <= sum(n) <= 6   and    # Condition 1: 2<= N(P1) <= 6
                    transitions(n) == 1 and    # Condition 2: S(P1)=1  
                    P2 * P4 * P6 == 0  and    # Condition 3   
                    P4 * P6 * P8 == 0):         # Condition 4
                    changing1.append((x,y))
        for x, y in changing1: 
            Image_Thinned[x][y] = 0
        # Step 2
        changing2 = []
        for x in range(1, rows - 1):
            for y in range(1, columns - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, Image_Thinned)
                if (Image_Thinned[x][y] == 1   and        # Condition 0
                    2 <= sum(n) <= 6  and       # Condition 1
                    transitions(n) == 1 and      # Condition 2
                    P2 * P4 * P8 == 0 and       # Condition 3
                    P2 * P6 * P8 == 0):            # Condition 4
                    changing2.append((x,y))    
        for x, y in changing2: 
            Image_Thinned[x][y] = 0
    return Image_Thinned

def output_thresholded_thinned(path):
    imagePaths = list(paths.list_images(path))

    # loop over the image paths
    for imagePath in imagePaths:
        # extract the class label from the filename
        split_list = imagePath.split('\\')
        train_test = split_list[-3]
        label = split_list[-2]

        op_path = "C:/Users/ayaey/Desktop/cdss_final_project/" + path+"_tg_thin/" + train_test + "/" + label + "/"
        op_thresh_path = "C:/Users/ayaey/Desktop/cdss_final_project/" + path+"_otsu_thresh/" + train_test + "/" + label + "/"
        
        Img_Original =  cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
        Img_Original = cv2.resize(Img_Original, (224, 224))

        # threshold the image such that the drawing appears as white on a black background
        Otsu_Threshold = threshold_otsu(Img_Original)   
        BW_Original = Img_Original < Otsu_Threshold 
        
        BW_Skeleton_uint8 = (BW_Original * 255).astype(np.uint8)
        cv2.imwrite(op_thresh_path+f"otsu_{split_list[-1]}.png", ~BW_Skeleton_uint8)

        BW_Skeleton = zhangSuen(BW_Original)

        BW_Skeleton_uint8 = (BW_Skeleton * 255).astype(np.uint8)
        cv2.imwrite(op_path+f"thin_{split_list[-1]}.png", ~BW_Skeleton_uint8)

output_thresholded_thinned('spiral')
output_thresholded_thinned('wave')
