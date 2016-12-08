import numpy as np
import cv2

cap = cv2.VideoCapture(0)

last_frame = None
delta = None
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    cur_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    if last_frame is not None:
        last_gray = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
        delta = cv2.absdiff(cur_gray,last_gray)

    last_frame=frame.copy()
    # Display the resulting frame
    if delta is not None:
        cv2.imshow('frame',delta)
    else:
        cv2.imshow('frame',cur_gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

