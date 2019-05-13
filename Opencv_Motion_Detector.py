# Import the library
import cv2 as cv
print cv.__version__

# Set the first frame
first_frame = None

# Capture the Video
my_video = cv.VideoCapture(0)

while True:

    # Check if captured
    check, frame = my_video.read()

    # Conver the image to Grayscale
    my_frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    my_frame_gray = cv.GaussianBlur(my_frame_gray, (21, 21), 0)

    # Set the first frame
    if first_frame is None:
        first_frame = my_frame_gray
        continue

    # Set the delta frame
    # Compare first frame to current frame
    delta_frame = cv.absdiff(first_frame, my_frame_gray)

    # Thershold frame
    thershold_frame = cv.threshold(delta_frame, 30, 255, cv.THRESH_BINARY)[1]
    thershold_frame = cv.dilate(thershold_frame, None, iterations=2)

    # Contours
    cnts, hierarchy = cv.findContours(thershold_frame.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Draw Rectangle for moing objects
    for contour in cnts:
        if cv.contourArea(contour) < 500:
            continue
        x, y, w, h = cv.boundingRect(contour)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the Captured frame of video
    cv.imshow('First Frame', first_frame)
    cv.imshow('Capturing First', my_frame_gray)
    cv.imshow('Delta frame', delta_frame)
    cv.imshow('Thershold frame', thershold_frame)
    cv.imshow('Detecting moving onject', frame)

    # Set the quit
    key = cv.waitKey(1)
    if (key == ord('q')):
        break

my_video.release()
cv.destroyAllWindows()