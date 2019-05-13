import cv2 as cv
import matplotlib.pyplot as plt

# Load the image
img = cv.imread('face5.jpg', 0)

# display the image using matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
# to hide ticks of X and Y
plt.xticks([]), plt.yticks([])
plt.show()