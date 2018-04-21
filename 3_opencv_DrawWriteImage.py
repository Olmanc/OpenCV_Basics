import numpy as np
from cv2 import cv2

img = cv2.imread('handTest.jpg', cv2.IMREAD_COLOR)
#point a & point B
cv2.line(img, (0, 0), (150, 150), (0, 0, 0), 10)
#top left & bottom right
cv2.rectangle(img, (15,25), (200, 150), (255, 255, 255),7)
#negative width - fill shape
cv2.circle(img, (100, 63), 55, (255, 0, 0), -1)
##polygons
pts = np.array([[10,5],[20,30],[50,20],[100,200]], np.int32)
#pts = pts.reshape((-1,-1,2)) #reshapes array
cv2.polylines(img, [pts], True, (0, 0, 255), 4)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0,130), font, 1, (0,255,0), 2, cv2.LINE_AA)

cv2.imshow('line', img)

cv2.waitKey(0)
cv2.destroyAllWindows()