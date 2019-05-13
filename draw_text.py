import numpy as np
import cv2 as cv

# draw the black background
img = np.zeros((512, 512, 3), np.uint8)

# Draw text
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img, 'OpenCV', (10, 450), font, 4, (255, 255, 255), 2, cv.LINE_AA)

# display image
cv.imshow('Text', img)
cv.waitKey(0)
cv.destroyAllWindows()