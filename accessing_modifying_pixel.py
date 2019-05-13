import cv2 as cv

# Load and Read the image file
img = cv.imread('face1.jpg')

# Accessing the pixel
px = img[200, 200]
print (px)

# accessing red value
red = img.item(10, 10, 2)
print (red)

# accessing image properties
print ('Shape:', img.shape)
print ('Size: ', img.size)
print ('Type: ', img.dtype)

# Image ROI(Region Of Image)
part_image = img[280:340, 330:390]
img[50:50, 100:100] = part_image

# splitting and merging images
# b, g, r = cv.split(img)
# img = cv.merge((b, g, r))

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()