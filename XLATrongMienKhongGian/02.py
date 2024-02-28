# đọc vào 1 ảnh màu hiển thị ra
# chuyển ảnh vừa đọc về gray scale

# chuyển ảnh ra mức xám theo tỷ lệ 0.39 | 0.5 | 0.11
import cv2
import numpy as np
import os

basePath: str = os.path.dirname(__file__) + '\\..\\Images\\'
imageName = 'test2.png'

if __name__ == "__main__":
    fullPath: str = basePath + imageName
    winName = 'original'

    image = cv2.imread(fullPath, cv2.IMREAD_COLOR)

    height, width, = image.shape[:2]

    gray_matrix_luminosity_method = np.zeros((height, width), dtype=np.uint8)

    gray_matrix_average_method = np.zeros((height, width), dtype=np.uint8)

    gray_matrix_lightness_method = np.zeros((height, width), dtype=np.uint8)

    luminosity_params = (0.39, 0.5, 0.11)

    for i in range(height):
        for j in range(width):

            b,g,r = image[i, j]

            #Luminosity Method
            gray_value_luminosity = int(luminosity_params[0] * r + luminosity_params[1] * g + luminosity_params[2] * b)
            gray_matrix_luminosity_method[i, j] = gray_value_luminosity

            #Average Method
            gray_value_average = (r + g + b) / 3
            gray_matrix_average_method[i, j] = gray_value_average

            #Lightness Method
            gray_value_lightness = (max(r, g, b) + min(r, g, b)) // 2
            gray_matrix_lightness_method[i, j] = gray_value_lightness

    cv2.imshow('Grayscale - Luminosity Method', gray_matrix_luminosity_method)
    cv2.imshow('Grayscale - Average Method', gray_matrix_average_method)
    cv2.imshow('Grayscale - Lightness Method', gray_matrix_lightness_method)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
