import numpy as np
import cv2 as cv

# Draw a black dackground
img = np.zeros((512, 512, 3), np.uint8)

# Draw a polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape(-1, 1, 2)
img = cv.polylines(img, [pts], True, (255, 255, 0))

# Show the image
cv.imshow('Polygon', img)
cv.waitKey(0)
cv.destroyAllWindows()