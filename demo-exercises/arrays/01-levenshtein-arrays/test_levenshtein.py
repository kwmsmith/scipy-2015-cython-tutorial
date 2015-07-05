from timeit import timeit

import levenshtein
import levenshtein_cython
import levenshtein_cython_solution

def test(func):
    assert func("kitten", "sitting") == 3
    assert func("sitting", "kitten") == 3
    assert func("", "asdf") == 4
    assert func("jkl;", "") == 4
    assert func("", "") == 0
    assert func("qwerty", "qwerty") == 0

test(levenshtein.levenshtein_distance)
test(levenshtein_cython.levenshtein_distance)
test(levenshtein_cython_solution.levenshtein_distance)

N = 20000

print "*" * 80
print "python levenstein(): %.2f" % timeit("levenshtein_distance('kitten', 'sitting')",
                                           "from levenshtein import levenshtein_distance",
                                           number=N)
print "cython levenstein(): %.2f" % timeit("levenshtein_distance('kitten', 'sitting')",
                                           "from levenshtein_cython import levenshtein_distance",
                                           number=N)
print "optimized levenstein(): %.2f" % timeit("levenshtein_distance('kitten', 'sitting')",
                                           "from levenshtein_cython_solution import levenshtein_distance",
                                           number=N)
print "*" * 80

