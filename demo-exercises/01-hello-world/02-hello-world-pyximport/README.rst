=====================================
Cython "Hello World!" using pyximport
=====================================

This demo / exercise has a fully worked example automatically compiling a
simple Cython function with the ``pyximport`` Cython utility.

Please explore the files in this directory to get a sense for how things are
arranged:

* ``cython_hello_world.pyx`` -- this is where the excitement happens!  For now,
  it just provides a simple ``add()`` function.
* ``use_pyximport.py`` -- this is a simple Python script that uses
  ``pyximport`` to automatically compile the Cython source file on the fly at
  import time.

To kick the tires from Linux or OS X, please do the following from the
appropriate command prompt for your system::

    $ python use_pyximport.py

On Windows, run the following from your Anaconda command window::

    $ python use_pyximport.py

Note: pyximport may need more configuration on Windows to help it find the
right compiler; as such, this example may not work out of the box.
