import cv2 as cv

# Capture the video
cap = cv.VideoCapture(0)

while (cap.isOpened()):
    # Capture frame by frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

# Release the capture
cap.release()
cv.destroyAllWindows()