import cython
import numpy as np

@cython.boundscheck(False)
@cython.wraparound(False)
def levenshtein_distance(char *s, char *t):
    # for all i and j, d[i,j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t;
    # note that d has (m+1)*(n+1) values
    cdef:
        int i, j
        int m = len(s)
        int n = len(t)
        int[:,::1] d = np.zeros((m+1, n+1), dtype=np.int32)

    for i in range(1, m+1):
        d[i, 0] = i

    for j in range(1, n+1):
        d[0, j] = j

    for j in range(1, n+1):
        for i in range(1, m+1):
            if s[i-1] == t[j-1]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j] + 1,
                              d[i, j-1] + 1,
                              d[i-1, j-1] + 1)
    return d[m, n]
