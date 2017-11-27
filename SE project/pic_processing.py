import cv2
import numpy as np
import matplotlib.pyplot as plt
def pictransformation():
    img = cv2.imread('edited.jpg', cv2.IMREAD_GRAYSCALE)
    IMREAD_COLOR =1
    IMREAD_UNCHANGED =-1

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([5, 10], [8, 10], 'e', linewidth=5)//errorline
#plt.show()
