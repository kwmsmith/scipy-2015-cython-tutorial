The `check_env.py` script has been tested on Mac OS X and Linux.

It requires a recent (2.7.x) version of Python, a recent (>= 0.20) version of
Cython, and a recent (>= 1.8) version of NumPy.  These components can be
acquired via prepackaged Python distributions (recommended) such as Enthought's
Canopy or Continuum's Anaconda.

It also requires a working C/++ compiler, which can be acquired by installing
the OS X developer tools, or the appropriate Linux packages via `yum` or
`apt-get`.

Once these dependencies are in place, please run:

    $ python check_env.py

In the current directory.

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
