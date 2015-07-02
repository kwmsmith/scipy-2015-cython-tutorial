The `check_env.py` script has been tested on Windows 7, 64-bit with the latest
version of Anaconda.

Please launch the Anaconda command prompt from the start menu after installing
Anaconda.

Use the `conda` command to install `libpython`:

    $ conda install libpython

Then run:

    $ python check_env.py

This will automaticallly compile the `hello_world.pyx` Cython source file into
an extension module, import it, and run a function inside to verify your
installation is working.

If your installation and setup is successful, you should see the following
output:

    ********************************************************************
    Hello World! [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    Cython Version: 0.22
    NumPy version: 1.9.2
    ********************************************************************
