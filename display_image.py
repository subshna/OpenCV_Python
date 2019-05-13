import cv2 as cv

# Load the color image in grayscale
img = cv.imread('face1.jpg', 0)

# display the image
cv.imshow('My_Image', img)
cv.waitKey(0)
cv.destroyAllWindows()