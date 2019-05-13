import cv2 as cv

# Capture the video
cap = cv.VideoCapture(0)

# define codec and create videowriter
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Output.avi', fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        # to flip the frame upside down
        #frame = cv.flip(frame, 0)

        # write the flipped frame
        out.write(frame)

        # show the frame
        cv.imshow('Video', frame)
        if cv.waitKey(1) == ord('q'):
            break

# Release the video capture object
cap.release()
out.release()
cv.destroyAllWindows()