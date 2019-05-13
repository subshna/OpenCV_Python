import numpy as np
import cv2 as cv

drawing = False
mode = True
ix, iy = -1, -1

def draw_circle_rect(event, x, y, flags, param):
    global ix, iy, drawing, mode, r, g, b

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
            else:
                cv.circle(img, (x, y), x/4, (b, g, r), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), (b, g, r), -1)
        else:
            cv.circle(img, (x, y), x/4, (b, g, r), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('Drawing')
cv.setMouseCallback('Drawing', draw_circle_rect)

while (1):
    cv.imshow('Drawing', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv.destroyAllWindows()