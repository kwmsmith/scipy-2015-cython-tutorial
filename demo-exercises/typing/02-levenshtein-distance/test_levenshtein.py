from timeit import timeit

N = 1

print "*" * 80
print "python levenshtein(): %.2f" % timeit('levenshtein_distance("qwertyuio", "asdfghjkl")',
                                            'from levenshtein import levenshtein_distance',
                                            number=N)
print "cython levenshtein(): %.2f" % timeit('levenshtein_distance("qwertyuio", "asdfghjkl")',
                                            'from levenshtein_cython import levenshtein_distance',
                                            number=N)
print "optimal levenshtein(): %.2f" % timeit('levenshtein_distance("qwertyuio", "asdfghjkl")',
                                             'from levenshtein_cython_solution import levenshtein_distance',
                                             number=N)
print "*" * 80
