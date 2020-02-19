docker run --rm -e DISPLAY=$DISPLAY --device /dev/snd -v $(pwd):/src -v /tmp/.X11-unix/:/tmp/.X11-unix/ -w /src -e QT_X11_NO_MITSHM=1 --device=/dev/video0 -ti demo:dlib python face.py

https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/
https://github.com/cmusatyalab/openface

- create a project to do face tracking + blurring
- run it in a container accessing host webcam and display on host
- create a base image + project image
- look at caching

===============================================================================

FROM python:3.7

RUN apt update -yq && \
    apt install -yq \
        libsdl2-dev \
        build-essential cmake \
        libopenblas-dev liblapack-dev \
        libx11-dev libgtk-3-dev \
        python python-dev python-pip \
        python3 python3-dev python3-pip

RUN pip3 install numpy dlib face_recognition
RUN pip3 install opencv-python

RUN sed -i.bak 's/none/read,write/g' /etc/ImageMagick-6/policy.xml

===============================================================================

import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)
face_locations = []

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    face_locations = face_recognition.face_locations(small_frame, model="cnn")
    for top, right, bottom, left in face_locations:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        face_image = frame[top:bottom, left:right]
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)
        frame[top:bottom, left:right] = face_image
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
