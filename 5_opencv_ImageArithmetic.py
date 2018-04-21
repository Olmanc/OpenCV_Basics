from cv2 import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

#add images (same size)
#add = img1+img2

#add pixel values - cap at 255 (same size)
#add = cv2.add(img1, img2)

#add image weight (alpha-gamma) (same size)
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

#image over image
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ] #region of image
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) #convert to grayscale

# binary inverse threshold (grayscale to black&white - inverted)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

# invert mask (logo to black)
mask_inv = cv2.bitwise_not(mask)

# get foreground and backgorund (bitwise AND with masks)
# transparent background
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# add foreground with background
result = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = result

cv2.imshow('weighted',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()