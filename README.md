![](https://github.com/panda-official/TimeSwipe.py/workflows/Workflow/badge.svg) [![PyPI version](https://badge.fury.io/py/timeswipe.svg)](https://badge.fury.io/py/timeswipe)

## Install from binary wheels

### Raspbian
```
sudo apt-get update
sudo apt install python3-pip
sudo pip3 install https://github.com/panda-official/TimeSwipe.py/releases/tag/<VERSION>/timeswipe-<VERSION>-cp37-cp37m-linux_armv7l.whl
```

### Arch linux
```
sudo pacman -S python-pip
sudo pip3 install wheel
sudo pip3 install https://github.com/panda-official/TimeSwipe.py/releases/tag/<VERSION>/timeswipe-<VERSION>-cp37-cp37m-linux_aarch64.whl

```

## Install from source wheel

### Raspbian

Install timeswipe driver deb packet from https://github.com/panda-official/TimeSwipe/releases

```
sudo apt-get update
sudo apt install python3-pip cmake g++ make libboost-python-dev
sudo pip3 install --upgrade pip
sudo pip3 install -i https://test.pypi.org/simple/ --upgrade timeswipe1
```

### Arch linux

Install timeswipe driver arch packet from https://github.com/panda-official/TimeSwipe/releases

```
sudo pacman -S python-pip cmake gcc make boost pkgconf
sudo pip3 install --upgrade pip
sudo pip3 install wheel
sudo pip3 install -i https://test.pypi.org/simple/ --upgrade timeswipe1
```

## Develop

### Prepare on Raspbian

Install timeswipe deb packet from https://github.com/panda-official/TimeSwipe/releases

```
sudo apt install git cmake g++ make libboost-python-dev
sudo pip3 install pylddwrap wheel
```

### Prepare on Arch linux

Install timeswipe arch packet from https://github.com/panda-official/TimeSwipe/releases

```
sudo pacman -S python-pip cmake gcc make boost pkgconf git
sudo pip3 install pylddwrap wheel
```

### Build source wheel
```
git clone https://github.com/panda-official/TimeSwipe.py
cd TimeSwipe.py
python3 setup.py sdist
```

### Build binary wheel
```
git clone https://github.com/panda-official/TimeSwipe.py
cd TimeSwipe.py
python3 setup.py bdist_wheel
```

