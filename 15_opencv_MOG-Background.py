#15
from cv2 import cv2
import numpy as np

#capture webcam
cap = cv2.VideoCapture(0)
#background substraction
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    #apply mask to frames
    fgmask = fgbg.apply(frame)
 
    #cv2.imshow('fgmask',frame)
    cv2.imshow('frame',fgmask)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()