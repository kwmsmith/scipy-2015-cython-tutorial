from distutils.core import setup, Extension
from Cython.Build import cythonize

ld = Extension(name="levenshtein_cython",
                sources=["levenshtein_cython.pyx", "levenshtein.c"])
lds = Extension(name="levenshtein_solution",
                sources=["levenshtein_solution.pyx", "levenshtein.c"])

setup(ext_modules=cythonize([ld, lds]))
