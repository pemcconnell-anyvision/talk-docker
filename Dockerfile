FROM python:3.7

RUN apt update -yq && \
    apt install -yq \
        build-essential cmake \
        libopenblas-dev liblapack-dev \
        libx11-dev libgtk-3-dev \
        python python-dev python-pip \
        python3 python3-dev python3-pip

RUN pip3 install numpy dlib face_recognition opencv-python
