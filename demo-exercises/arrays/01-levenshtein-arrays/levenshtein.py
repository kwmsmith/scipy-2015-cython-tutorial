import numpy as np

def levenshtein_distance(s, t):
    # for all i and j, d[i,j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t;
    # note that d has (m+1)*(n+1) values
    m = len(s)
    n = len(t)
    d = np.zeros((m+1, n+1), dtype=np.int32)

    # source prefixes can be transformed into empty string by
    # dropping all characters
    d[1:, 0] = np.arange(1, m+1, dtype=np.int32)

    # target prefixes can be reached from empty source prefix
    # by inserting every character
    d[0, 1:] = np.arange(1, n+1, dtype=np.int32)

    for j in range(1, n+1):
        for i in range(1, m+1):
            if s[i-1] == t[j-1]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j] + 1,
                              d[i, j-1] + 1,
                              d[i-1, j-1] + 1)
    return d[m, n]
