# Import Module
import numpy as np  # Numpy is for Array Handler
# Main Module Import From OpenCV Module
import cv2
import sys  # System
# Path Here Live Detection Face Capture File
# Open Frontal Camera ( Live Web Camera )
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video_camera = cv2.VideoCapture(0)  # Live Streaming Face Detection
while True:  # Face Frame
    ret, frame = video_camera.read()
    # Face Frame For Detected Face
    # Multi Scale For Multi Faces
    grayfaces = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        grayfaces,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(40, 40),
        # resize = (600, 600),
        flags=cv2.CASCADE_SCALE_IMAGE
    )


    print(faces)
    print(type(faces))
    # Created Rectangle For Face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 225),
                    2)  # Show Image For Live Face Detected
    # windows function
    cv2.imshow('FaceDetection', frame)  # Exit Function
    # exit key function if you click the Q keyword then Quit the windows
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release function
cv2. video_capture.release()
# Destroyed Open Windows And Kill Memory Storage
cv2.destroyAllWindows()
