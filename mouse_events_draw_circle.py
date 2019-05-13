import cv2 as cv
import numpy as np

# To display all the events is opencv
#events = [x for x in dir(cv) if 'EVENT' in x]
#print (events)

# mouse callback function
def draw_circle(event, x, y, flags, param):
    #print (event, x, y)
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), 1)

# Create a black image and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('Image')
cv.setMouseCallback('Image', draw_circle)

while (1):
    cv.imshow('Image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()