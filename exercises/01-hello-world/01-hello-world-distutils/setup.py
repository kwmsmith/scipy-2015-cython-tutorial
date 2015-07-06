from distutils.core import setup
from Cython.Build import cythonize

setup(name="cython_hello_world",
      ext_modules = cythonize("cython_hello_world.pyx")
)
