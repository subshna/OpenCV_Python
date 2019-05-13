import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw as diagonal blue line
img = cv.line(img, (0,0), (511, 511), (255, 0, 0), 3)

# Draw Rectangle
img = cv.rectangle(img, (384, 0), (510, 128), (0,255, 0), 3)

# Draw Circle
img = cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# Draw Ellipse
img = cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)

# Draw a polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape(-1, 1, 2)
img = cv.polylines(img, [pts], True, (255, 255, 0))

# Draw text
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img, 'OpenCV', (10, 450), font, 4, (255, 255, 255), 2, cv.LINE_AA)

cv.imshow('Drawing', img)
cv.waitKey(0)
cv.destroyAllWindows()