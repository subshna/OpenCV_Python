import numpy as np
import cv2 as cv

# Create an empty function
def does_nothing():
    pass

# Create a black image window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('Trackbar')

# Create the trackbar for change color
cv.createTrackbar('R', 'Trackbar', 0, 255, does_nothing)
cv.createTrackbar('G', 'Trackbar', 0, 255, does_nothing)
cv.createTrackbar('B', 'Trackbar', 0, 255, does_nothing)

# Create a switch for on/off functionality
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'Trackbar', 0, 1, does_nothing)

# Show the image
while (1):
    cv.imshow('Trackbar', img)
    if cv.waitKey(1) == 27 & 0xFF:
        break

    # Get current position of four trackers
    r = cv.getTrackbarPos('R', 'Trackbar')
    g = cv.getTrackbarPos('G', 'Trackbar')
    b = cv.getTrackbarPos('B', 'Trackbar')
    s = cv.getTrackbarPos(switch, 'Trackbar')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()