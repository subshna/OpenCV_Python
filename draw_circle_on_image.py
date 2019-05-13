import numpy as np
import cv2

img = cv2.imread('../Images/dog_backpack.jpg')
#fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 30, color=(0, 0, 255), thickness=3)

# Show Image
cv2.namedWindow('Puppy_Bagpack')
cv2.setMouseCallback('Puppy_Bagpack', draw_circle)

while True:
    cv2.imshow('Puppy_Bagpack', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows