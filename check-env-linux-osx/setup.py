from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'hello_world',
  ext_modules = cythonize("hello_world.pyx"),
)
