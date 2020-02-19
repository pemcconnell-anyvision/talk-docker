im doing terrible things ...
============================

this is only for some fun

```sh

# ahem ..

docker run \
  --rm \
  --device /dev/snd \
  --device=/dev/video0 \
  -e DISPLAY=$DISPLAY \
  -e QT_X11_NO_MITSHM=1 \
  -v $(pwd):/src \
  -v /tmp/.X11-unix/:/tmp/.X11-unix/ \
  -w /src \
  -ti demo:dlib \
    python face.py
```
