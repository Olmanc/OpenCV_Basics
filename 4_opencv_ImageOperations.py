from cv2 import cv2
import numpy as np

img = cv2.imread('hand.jpg', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]

#Region of Image
##roi = img[100:150, 100:150]
img[200:300, 200:300] = [255,255,255]

duplicate = img[150:250, 150:250]
img[0:100,0:100] = duplicate

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()