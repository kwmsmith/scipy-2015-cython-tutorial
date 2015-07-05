Hello World in Cython
=====================

This is a simple get-your-feet-wet exercise in Cython.  The goal is to show
you different ways to run Cython code -- interactively with IPython,
dynamically compiled with pyximport, and statically generated and compiled
with Python's distutils module.

The three subdirectories contain a self-contained example of how to run and
interact with Cython in a different way.

1. You can use Python's distutils to manually create a Cython extension
   module.  This method gives you the most control and allows you to
   distribute the generated C-extension module without a Cython dependency.

   Inside the `01-hello-world-distutils` directory, do the following, depending
   on your platform:

   Mac / Linux: Run the following to compile the extension module::

        python setup.py build_ext --inplace

   Windows: run the following, making note of the extra command::

        python setup.py build_ext --inplace --compiler=mingw32

   If successful, you will see a new extension module in your directory.  It
   will be named `cython_hello_world.so` on Mac or Linux,
   `cython_hello_world.pyd` on Windows.

   Run the test script to import and use your new extension module::

       $ python test_hello_world.py
       Pure Python version: 0.293585s
       Cython version: 0.115184s

2. In the `02-hello-world-pyximport` directory, the script `use_pyximport.py`
   will automatically compile the `cython_hello_world.pyx` file for you and
   import it, allowing you to treat a `.pyx` file as if it is a regular `.py`
   file.  Run this script and verify that it works for you::

        $ python use_pyximport.py
        8.578156256

3. In the `03-hello-world-ipynb` directory, open the ipython notebook file
   `cython-hello-world.ipynb`::

      $ ipython notebook cython-hello-world.ipynb

  Run through and execute the cells there; if successful, you are set up to
  interactively use Cython from within IPython.

4. You can also type in the contents of the IPython notebook into a
   (non-notebook) ipython session (if the notebook is not available to you or
   you prefer the IPython qt console).  The %%cython magic will work there as
   well.
