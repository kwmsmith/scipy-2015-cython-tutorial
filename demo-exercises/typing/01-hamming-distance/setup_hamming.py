from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["hamming_cython.pyx", "hamming_cython_solution.pyx"]))
