from solution import *
from obpng import read_png, write_png
import cv2 as cv

print("- Ocena dostateczna")
renew_pictures()

kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]], np.uint8)

print("- Ocena dobra")
image = cv.imread("figures/crushed.png", 0)
erosion = own_simple_erosion(image)
erosion2 = cv.erode(image, kernel, iterations=1)
cv.imwrite("own_erosion.png", erosion)
cv.imwrite("erosion.png", erosion2)

"""
print("- Ocena bardzo dobra")
read_png("figures/crushed.png")
kernel = np.array([[0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0],
                   [1, 1, 1, 1, 1],
                   [0, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0]])
erosion = own_erosion(image, kernel)
write_png("results/own_erosion.png")
"""
