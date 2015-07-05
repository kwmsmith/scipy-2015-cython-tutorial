import pyximport; pyximport.install()
import cython_hello_world

print cython_hello_world.add(1,2)
