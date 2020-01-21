#/usr/bin/python

import pathlib
import lddwrap
import sys
import os
import os.path
import shutil

if len(sys.argv) < 3:
    print("Usage: %s <library> <output_dir> <dependency>" % (sys.argv[0]))
    sys.exit(-1)

path = pathlib.Path(sys.argv[1])
out_dir = pathlib.Path(sys.argv[2])
f = open(os.path.join(out_dir,'__init__.py'), 'w')
f.write("import ctypes\n")
f.write("import os.path\n")
libs = sys.argv[3:]
deps = lddwrap.list_dependencies(path=path)
for dep in deps:
    if not dep.soname:
        continue
    for lib in libs:
        if dep.soname.find(lib) == 0:
            shutil.copy(dep.path, out_dir)
            f.write("ctypes.CDLL(os.path.join(os.path.dirname(__file__),'"+os.path.basename(dep.path)+"'))\n")
            break;

f.write("from .timeswipe import *\n")
f.close()
