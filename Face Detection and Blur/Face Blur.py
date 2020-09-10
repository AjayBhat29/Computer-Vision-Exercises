#Importing the libraries
#import numpy as np
import cv2
import dlib

# Creating the video capture and face detector objects
video_capture = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

#Setting variables for tracking(blurring and framing)
blurred = False
framed = False

#Start capturing frames in the main loop
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frame = cv2.resize(frame,(640,480))
    #Convert each frame to gray and detect faces
    if (ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rects = detector(gray, 0)

        #For each detected face,replace the pixels of original frame with blurred pixels
        for rect in rects:
            x = rect.left()
            y = rect.top()
            x1 = rect.right()
            y1 = rect.bottom()

            if blurred:
                frame[y:y1, x:x1] = cv2.blur(frame[y:y1, x:x1], (30, 30))

            if framed:
                cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
        
        # Finally, displaying the resulting frame
        cv2.imshow('Video Feed', frame)

    ch = 0xFF & cv2.waitKey(1)

    # press "b" to toggle blurring.
    if ch == ord('b'):
        blurred = not blurred

    # press "f" to toggle the frame.
    if ch == ord('f'):
        framed = not framed

    # press "q" to quit the program.
    if ch == ord('q'):
        break

# When everything is done, releasing the video captures
video_capture.release()
cv2.destroyAllWindows()