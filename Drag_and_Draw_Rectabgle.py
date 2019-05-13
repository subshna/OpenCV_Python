import cv2
import numpy as np

# variables
# True while mouse button down, false while mouse button up
drawing = False
ix, iy = -1, -1

# Function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)

# To Show the image
img = np.zeros((512, 512, 3), dtype=np.uint8)
cv2.namedWindow(winname='My Drawing')
cv2.setMouseCallback('My Drawing', draw_rectangle)

while True:
    cv2.imshow('My Drawing', img)
    # Check for ESC key Press
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows