from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('handTest.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR (1) o IMREAD_UNCHANGED (-1) o GRAYSCALE (0)


#cv2.imshow('imagen', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.show()


cv2.imwrite('handGray.png', img)