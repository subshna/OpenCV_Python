import cv2 as cv

# Load the image of color in graysacle
img = cv.imread('face1.jpg', 0)

# Write the image to another file
cv.imwrite('face1_grayscale.jpg', img)