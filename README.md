# hotword-asteroid
Hotword detection to asteroid os

## setup

from https://asteroidos.org/wiki/building-asteroidos/, I needs to build software with docker.

```
sudo docker run --rm -it -v /etc/passwd:/etc/passwd:ro -u "$(id -u):$(id -g)"   -v "$HOME/.gitconfig:/$HOME/.gitconfig:ro" -v "$(pwd):/asteroid" asteroidos-toolchain   bash -c "source ./prepare-build.sh dervice && bitbake --software--"
```
**List --software--**
- python3-pkg-resources
- python3-setuptools
- python3-pip
- python3-numpy
- python3-wheel
- jack
- portaudio-v19
- python3-pyaudio

you want to upload ```.ipk``` from ```/build/tmp-glibc/deploy/ipk/armv7~~```
```sh
scp * root@ip_watch:/home/root/
```
ssh with root and install all
```sh
opkg install *
```

install by pip:
```sh
pip3 install --no-dependencies EfficientWord-Net
pip3 install requests
```

and install TensorFlow Lite by https://pypi.org/project/tflite-runtime/#files

```sh
pip3 install https://files.pythonhosted.org/packages/db/31/6d9e8790e188fd4c8647e8cdaece76e12155f2666453b030d91d194ea202/tflite_runtime-2.7.0-cp39-cp39-manylinux2014_armv7l.whl
```

## Test

upload test.py

```sh
scp test.py root@ip_watch:/home/ceres/
```
run with ```ceres``` user
```sh
python3 test.py
```
