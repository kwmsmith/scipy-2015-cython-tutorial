=====================================
Cython "Hello World!" using distutils
=====================================

This demo / exercise has a fully worked example compiling a simple Cython
function with Python's builtin distutils package.

Please explore the files in this directory to get a sense for how things are
arranged:

* ``cython_hello_world.pyx`` -- this is where the excitement happens!  For now,
  it just provides a simple ``add()`` function.
* ``setup.py`` -- this is a simple Python script to run ``distutils`` and
  compile the Cython source file into an extension module.
* ``test_hello_world.py`` -- a simple test script to verify everything is
  working and to compare the timings of our Cython version with a pure Python
  version.

There is a ``Makefile`` for Linux and OS X and a ``build.bat`` file for Windows
to make the compilation process easier.

Using ``distutils`` gives us a lot of control over how the compilation process
proceeds.  Unlike Python, we have to remember to recompile after every time we
modify the Cython source code.

To kick the tires from Linux or OS X, please do the following from the
appropriate command prompt for your system::

    $ python setup.py build_ext -if
    $ python test_hello_world.py

On Windows, run the following from your Anaconda command window::

    $ python setup.py build_ext -if --compiler=mingw32
    $ python test_hello_world.py
