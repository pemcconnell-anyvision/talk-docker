docker-facerecognition demo
===========================

a throw-away repo used during a docker presentation

run from docker hub
-------------------

```sh
# this assumes the camera you want to connect to is /dev/video0

docker run --rm \
  --device /dev/video0 \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -v /tmp/.X11-unix/:/tmp/.X11-unix/ \
    -ti pemcconnell/facerecog
```

build
-----

```sh
# ahem ..
docker build -t=demo .

# this assumes the camera you want to connect to is /dev/video0
docker run \
  --rm \
  --device=/dev/video0 \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -v $(pwd):/src \
  -v /tmp/.X11-unix/:/tmp/.X11-unix/ \
  -w /src \
  -ti demo \
    python face.py
```
