import cv2 as cv

# Load image with resizable window
img = cv.namedWindow('face1.jpg')

# Display the image
cv.imshow('My_image', img)
cv.waitKey(0)
cv.destroyAllWindows()