import numpy as np
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Zadanie na ocenę dostateczną


def renew_pictures():
    img = []
    kernel = np.ones((3, 3), np.uint8)
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
  #  kernel = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]], np.uint8)

    for i in range(1, 5):
        print(i)
        if (i == 1):
            img.append(cv.imread('figures/crushed.png', 0))
        else:
            img.append(cv.imread('figures/crushed'+str(i)+'.png', 0))
        opening = cv.morphologyEx(
            img[i-1], cv.MORPH_OPEN, kernel, iterations=1)
        closing = cv.morphologyEx(
            opening, cv.MORPH_CLOSE, kernel, iterations=1)
        opening = cv.morphologyEx(
            closing, cv.MORPH_OPEN, kernel, iterations=2)
        closing = cv.morphologyEx(
            opening, cv.MORPH_CLOSE, kernel, iterations=2)
        opening = cv.morphologyEx(
            opening, cv.MORPH_OPEN, kernel, iterations=3)
        closing = cv.morphologyEx(
            opening, cv.MORPH_CLOSE, kernel, iterations=2)
        if (i == 1):
            cv.imwrite('results/crushed.jpg', closing)
        else:
            cv.imwrite('results/crushed'+str(i)+'.png', closing)
    cv.waitKey(0)
    cv.destroyAllWindows()
    # ---------------
    # Do uzupełnienia
    # ---------------
    pass

# Zadanie na ocenę dobrą


def own_simple_erosion(image):
    new_image = np.zeros(image.shape, dtype=image.dtype)
    kernel = np.array([[0, 1, 0],
                       [1, 1, 1],
                       [0, 1, 0]], np.uint8)

    return new_image


# Zadanie na ocenę bardzo dobrą
def own_erosion(image, kernel=None):
    if kernel is None:
        kernel = np.array([[0, 1, 0],
                           [1, 1, 1],
                           [0, 1, 0]], np.uint8)

    pass
