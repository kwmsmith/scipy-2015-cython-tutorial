from __future__ import print_function
from timeit import timeit

print("*" * 80)
print("python hamming_sum(): %.2f" % timeit('hamming_sum("qwertyuio", "asdfghjkl")',
                                            'from hamming import hamming_sum'))
print("cython hamming_sum(): %.2f" % timeit('hamming_sum("qwertyuio", "asdfghjkl")',
                                            'from hamming_cython import hamming_sum'))
print("optimal hamming_sum(): %.2f" % timeit('hamming_sum("qwertyuio", "asdfghjkl")',
                                            'from hamming_cython_solution import hamming_sum'))
print("-" * 80)
print("python hamming_loop(): %.2f" % timeit('hamming_loop("qwertyuio", "asdfghjkl")',
                                             'from hamming import hamming_loop'))
print("cython hamming_loop(): %.2f" % timeit('hamming_loop("qwertyuio", "asdfghjkl")',
                                             'from hamming_cython import hamming_loop'))
print("optimal hamming_loop(): %.2f" % timeit('hamming_loop(b"qwertyuio", b"asdfghjkl")',
                                             'from hamming_cython_solution import hamming_loop'))
print("*" * 80)
