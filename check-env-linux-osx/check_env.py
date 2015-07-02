import os
import shutil
from subprocess import check_call, call

try:
    os.remove('hello_world.c')
except OSError:
    pass

try:
    os.remove('hello_world.so')
except OSError:
    pass

shutil.rmtree('build', ignore_errors=True)

check_call(r'python setup.py build_ext -if'.split())

import hello_world
import numpy as np
import Cython

print "*" * 80
print hello_world.hello_world(np.arange(10.))
print "Cython Version:", Cython.__version__
print "NumPy version:", np.__version__
print "*" * 80
