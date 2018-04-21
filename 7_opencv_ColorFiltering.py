from cv2 import cv2
import numpy as np

#capture webcam
cap = cv2.VideoCapture(0)

while True:
    #read video
    _, frame = cap.read()

    #HSV - Hue Saturation Value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #range for filter
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    #mask shows red as positive (white) (shows red, blue, green)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #bitwise AND
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #show frames
    cv2.imshow('frame', res)

    #press ESC to close
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
#release resource (webcam)
cap.release()