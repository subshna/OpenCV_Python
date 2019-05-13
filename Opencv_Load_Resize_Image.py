# import the library
import cv2 as cv
print cv.__version__

# Loading the image
# Where, 0=Grayscale, 1=RGB
my_image = cv.imread('Photo1.jpg', 0)

# Print the loaded image details
print (type(my_image))
print (my_image.shape, '\n')
print (my_image)

# Resize the image and display the same
resized_image = cv.resize(my_image, (600, 188))

cv.imshow('Image', resized_image)
cv.waitKey(2000)
cv.imwrite('Photo1_resize.jpg', resized_image)
cv.destroyAllWindows()