================================
Exercise adding type information
================================

This exercise will give you some more experience adding `cdef` functions in
Cython code.  The files are set up to make it easy to compare the performance
of your typed Cython code with the pure Python equivalent and an optimized
Cython version.

The ``levenshtein.py`` file has a few functions in it, some of which are called
by other functions.  This is an ideal opportunity to use the `cdef` function in
Cython to remove function call overhead.

``levenshtein_distance()`` computes the Levenshtein distance between two
strings and uses two helper functions, ``lev()`` and ``cost()``. 

The ``levenshtein_cython.pyx`` file has the exact same code as
``levenshtein.py``, and we will be converting the `def` functions into `cdef`
functions to speed things up.

The ``setup_levenshtein.py`` and ``test_levenshtein.py`` scripts are set up to
compile the Cython modules and compare the performance between the different
versions.

1. Compile the Cython extension modules and run the test script::

       $ python setup_levenshtein.py build_ext -if [--compiler=mingw32]
       $ python test_levenshtein.py

2. Change the `def` functions into `cdef` functions in
   ``levenshtein_cython.pyx`` to see if you can improve its performance.  
