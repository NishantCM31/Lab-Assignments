""" import numpy as np

# Example RGB image (3x3 image with RGB values)
rgb_image = np.array([
    [[123, 234, 132], [234, 123, 132], [111, 222, 123]],
    [[144, 222, 144], [122, 111, 222], [145, 145, 145]],
    [[200, 200, 200], [50, 50, 50], [80, 100, 120]]
])

# 1. Convert RGB image to grayscale
grayscale_image = np.mean(rgb_image, axis=2)
print("Grayscale image:\n", grayscale_image)

# 2. Apply a threshold to create a binary image
binary_image = np.where(grayscale_image > 128, 255, 0)
print("Binary image:\n", binary_image)
 """

import numpy as np

# Example RGB image (3x3 image with RGB values)
rgb_image = np.array([
    [[123, 234, 132], [234, 123, 132], [111, 222, 123]],
    [[144, 222, 144], [122, 111, 222], [145, 145, 145]],
    [[200, 200, 200], [50, 50, 50], [80, 100, 120]]
])

# 1. Convert RGB image to grayscale
grayscale_image = np.mean(rgb_image, axis=2)
print("Grayscale Image:")
print(grayscale_image)

# 2. Apply a threshold to create a binary image
threshold = 128
binary_image = np.where(grayscale_image > threshold, 255, 0)

print("\nBinary Image (Threshold = 128):")
print(binary_image)
