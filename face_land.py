from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
import cv2
import argparse

# Initialize face detector and create face landmark predictor
print("[INFO] loading facial landmark predictor ...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the video stream and allow camera sensor to warm up
print("[INFO] camera sensor warming up ...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

while True:
    frame=vs.read()
    frame = imutils.resize(frame, width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in grayscale
    rects =  detector(gray,0)

    for rect in rects:
        shape = predictor(gray,rect)
        shape = face_utils.shape_to_np(shape)

        for (x,y) in shape:
            cv2.circle(frame,(x,y), 1, (0,0,255),-1)

        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)& 0xFF

        if key == ord("q"):
            break
cv2.destroyAllWindows()
vs.stop()
    
