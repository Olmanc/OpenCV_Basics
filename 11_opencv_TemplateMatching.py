from cv2 import cv2
import numpy as np

#read image
img_rgb = cv2.imread('matchingTemplate.jpg')
#grayscale for procesing
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#read template
template = cv2.imread('template.jpg',0)
#template sizes
w, h = template.shape[::-1]

#match grayscale image with template
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
#matchin threshold
threshold = 0.95
#locate matches
loc = np.where( res >= threshold)

#for each match found
for pt in zip(*loc[::-1]):
    #mark matches with rectangle
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

#show results in color image
cv2.imshow('Detected',img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()