from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["levenshtein_cython.pyx",
                             "levenshtein_cython_solution.pyx"]))
