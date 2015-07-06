from timeit import timeit

import levenshtein_cython
import levenshtein_solution

def test(func):
    assert func("kitten", "sitting") == 3
    assert func("sitting", "kitten") == 3
    assert func("", "asdf") == 4
    assert func("jkl;", "") == 4
    assert func("", "") == 0
    assert func("qwerty", "qwerty") == 0

# test(levenshtein_cython.levenshtein_distance)
test(levenshtein_solution.levenshtein_distance)

N = 200000

print "*" * 80
print "wrapped levenshtein(): %.2f" % timeit("levenshtein_distance('kitten', 'sitting')",
                                        "from levenshtein_solution import levenshtein_distance",
                                        number=N)
print "*" * 80
