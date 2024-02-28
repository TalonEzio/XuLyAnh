import os
import numpy as np
import cv2

basePath: str = os.path.dirname(__file__) + '\\..\\Images\\'
imageName = 'test.png'

if __name__ == "__main__":
    fullPath: str = basePath + imageName
    winName = 'original'

    image = cv2.imread(fullPath, cv2.IMREAD_COLOR)

    cv2.namedWindow(winName)

    img2 = 255 - image

    cv2.imshow(winName, image)
    cv2.imshow('Solved', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
