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
 
    #Gradients
    #Laplacian
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    #x
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    #y
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)    

    #canny edge detection
    edges = cv2.Canny(frame,100,200)
    
    #show frames
    cv2.imshow('frame', edges)

    #press ESC to close
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()
#release resource (webcam)
cap.release()