# import the library
import cv2 as cv
print cv.__version__
# glob here finds all the images in the path
import glob

# Find all the images in the path
all_images = glob.glob('*.jpg')

for img in all_images:
    # Load the images
    my_image = cv.imread(img, 0)

    # Resize the image
    img_resize = cv.resize(my_image, (650, 325))

    # display the images
    cv.imshow(img, img_resize)
    cv.waitKey(500)
    cv.destroyAllWindows()