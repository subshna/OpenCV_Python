import cv2 as cv
print cv.__version__

# Capture the Video
my_video = cv.VideoCapture(0)

while True:

    # Check if loaded correctly
    check, frame = my_video.read()
    print (check, '\n', frame)

    # Show the captured frame in video
    cv.imshow('Capturing', frame)

    # Set the quit
    key = cv.waitKey(1)
    if key == ord(('q')):
        break

# Release the Video
my_video.release()
cv.destroyAllWindows()