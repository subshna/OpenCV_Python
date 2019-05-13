import cv2 as cv

# Load the color image in grayscale
img = cv.imread('face3.jpg', 0)

# Display the image
cv.imshow('Image', img)

# Close the window on escape keypress and save on 'S'
k = cv.waitKey(0)
print (k)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('grayscale_face3.jpg', img)
    cv.destroyAllWindows()
