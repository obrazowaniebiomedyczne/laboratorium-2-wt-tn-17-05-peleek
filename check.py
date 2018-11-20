from solution import *
from obpng import read_png, write_png
import cv2 as cv

print("- Ocena dostateczna")
renew_pictures()


print("- Ocena dobra")
image = cv.imread("figures/result.png", 0)
erosion = own_simple_erosion(image)
cv.imwrite("own_erosion.png", erosion)

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
