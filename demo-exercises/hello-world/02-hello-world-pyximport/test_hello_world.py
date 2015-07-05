from timeit import timeit

def pyadd(a, b):
    return 3.1415926 * a + 2.718281828 * b

print 'Pure Python version: %fs' % timeit('pyadd(1, 2)', 'from __main__ import pyadd')
print 'Cython version: %fs' % timeit('add(1, 2)', 'from cython_hello_world import add')
