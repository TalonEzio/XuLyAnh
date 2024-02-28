import os
import numpy as np
import cv2

basePath: str = os.path.dirname(__file__) + '\\Images\\'
imageName = 'rgb-color-model.png'

if __name__ == "__main__":
    fullPath: str = basePath + imageName
    winName = 'original'

    image = cv2.imread(fullPath,cv2.IMREAD_COLOR)

    cv2.namedWindow(winName, cv2.WINDOW_NORMAL)

    cv2.imshow(winName, image)

    r,g,b = cv2.split(image)
    zero = np.zeros(b.shape, dtype='uint8')

    r = cv2.merge([r,zero,zero])
    g = cv2.merge([zero,g,zero])
    b = cv2.merge([zero,zero,b])
    cv2.imshow('r',r)
    cv2.imshow('g',g)
    cv2.imshow('b',b)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

