#!/bin/bash

src_dir=`pwd`

export arm=arm-linux-gnueabihf-
export arm64=aarch64-linux-gnu-

function replace_arch {
    find $1 -iname '*.whl' -exec sh -c 'x="{}"; mv "$x" `echo $x | sed "s/x86_64.whl$/$arch_name.whl/"`' \;
}

export arch=$1
export CC=${!arch}gcc
export CXX=${!arch}g++
export LD=${!arch}ld
export STRIP=${!arch}strip


if [ "$arch" == "arm" ]; then
    export arch_name=armv7l
fi
if [ "$arch" == "arm64" ]; then
    export arch_name=aarch64
fi
curl -s https://api.github.com/repos/panda-official/TimeSwipe/releases/latest | grep "browser_download_url.*timeswipe.*$arch_name.deb" | cut -d : -f 2,3 | tr -d \"  | wget -qi -
dpkg -i *.deb && rm *.deb && \
file /usr/lib/libtimeswipe.a && \
file /usr/lib/libtimeswipe.so.0.0.8 && \
OVERRIDE_INCLUDES=/usr/include/aarch64-linux-gnu/python3.8\ /usr/include/python3.8 OVERRIDE_LIBS=/usr/lib/libtimeswipe.a\ /usr/lib/libboost_python38.a python3.8 setup.py bdist_wheel --dist-dir /tmp/dist && python3.8 setup.py clean --all && replace_arch /tmp/dist $arch_name && \
OVERRIDE_INCLUDES=/usr/include/aarch64-linux-gnu/python3.7\ /usr/include/python3.7 OVERRIDE_LIBS=/usr/lib/libtimeswipe.a\ /usr/lib/libboost_python37.a python3.7 setup.py bdist_wheel --dist-dir /tmp/dist && python3.7 setup.py clean --all && replace_arch /tmp/dist $arch_name && \
find /tmp/dist -iname "*.whl" -exec cp {} ${src_dir} \; && \
dpkg -r timeswipe

