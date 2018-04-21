from cv2 import cv2
import numpy as np

#read image
img = cv2.imread('hand.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

#detect corners (amount 20)
corners = cv2.goodFeaturesToTrack(gray, 20, 0.01, 10)
#collect corners
corners = np.int0(corners)

#mark detected corners
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)

#show results
cv2.imshow('Corner',img)

cv2.waitKey(0)
cv2.destroyAllWindows()