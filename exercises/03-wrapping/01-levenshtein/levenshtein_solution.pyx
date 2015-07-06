cdef extern from "levenshtein.h":
    int levenshtein_dist(char *s, char *t)

def levenshtein_distance(s, t):
    ld = levenshtein_dist(s, t)
    if ld < 0:
        raise RuntimeError()
    return ld
