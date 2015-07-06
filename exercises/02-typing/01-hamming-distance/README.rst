================================
Exercise adding type information
================================

This exercise will give you some experience adding type information to Cython
code.  The files are set up to make it easy to compare the performance of your
typed Cython code with the pure Python equivalent and an optimized Cython
version.

The ``hamming.py`` file has two simple functions computing the Hamming distance
between two strings: ``hamming_sum()`` and ``hamming_loop()``.

``hamming_sum()`` computes the distance using Python's built-in ``sum()`` and
``zip()`` functions, and uses a generator expression for nice, clear, Pythonic
code.

``hamming_loop()`` computes the distance using a non-Pythonic ``for`` loop over
the indices into the string arguments.

The ``hamming_cython.pyx`` file has the exact same code as ``hamming.py``, and
we will be adding type information to these functions to help speed them up.

The ``setup.py`` and ``test_hamming.py`` scripts are set up to compile the
Cython modules and compare the performance between the different versions.

1. Compile the Cython extension modules and run the test script::

       $ python setup.py build_ext -if [--compiler=mingw32]
       $ python test_hamming.py

2. Add type information to ``hamming_cython.pyx`` to see if you can improve its
   performance.  

   Note that it is difficult to speed up ``hamming_sum()``, but
   ``hamming_loop()`` is much easier to improve with some simple type
   information.

   Hints: (1) Cython knows how to make C-style ``char *`` strings interoperate
   with Python strings; (2) make sure the ``for`` loop variable and the
   argument to ``range()`` have integral types.
