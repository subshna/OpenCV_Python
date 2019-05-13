import cv2
import numpy as np

blank_img = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

cv2.rectangle(blank_img, pt1=(200, 15), pt2=(500, 150), color=(0, 255, 0), thickness=10)

while True:
    cv2.imshow('Drawing', blank_img)
    if cv2.waitKey(1) & 0XFF == 27:
        break

cv2.destroyAllWindows()