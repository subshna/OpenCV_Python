# import the library
import cv2 as cv
print cv.__version__

# Load Cascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the image
my_image_color = cv.imread('face3.jpg')
my_image_gray = cv.cvtColor(my_image_color, cv.COLOR_BGR2GRAY)

# Detect the face
faces = face_cascade.detectMultiScale(my_image_gray,
                                      scaleFactor=1.05,
                                      minNeighbors=5)

# Print the type and values of the face object
print (type(faces))
print (faces)

# Draw a rectangle around the face
for x, y, w, h in faces:
    my_image_rect = cv.rectangle(my_image_color, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the image
    cv.imshow('Face Detection', my_image_rect)
    cv.waitKey(0)
    cv.destroyAllWindows()