import cv2

img = cv2.imread('../Images/00-puppy.jpg')

while True:
    cv2.imshow('Puppy', img)

    #  if we have waited at least 1 ms AND we have pressed the ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()