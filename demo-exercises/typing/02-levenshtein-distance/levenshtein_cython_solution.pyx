def levenshtein_distance(s, t):
    return lev(s, len(s), t, len(t))

cdef int lev(char *s, int len_s, char *t, int len_t):
    if len_s == 0 or len_t == 0:
        return len_s or len_t
    cdef:
        int lev_s = lev(s, len_s-1, t, len_t  ) + 1
        int lev_t = lev(s, len_s  , t, len_t-1) + 1
        int lev_b = lev(s, len_s-1, t, len_t-1) + cost(s, len_s, t, len_t)
    if lev_s < lev_t and lev_s < lev_b:
        return lev_s
    elif lev_t < lev_s and lev_t < lev_b:
        return lev_t
    else:
        return lev_b

cdef int cost(char *s, int len_s, char *t, int len_t):
    return s[len_s-1] != t[len_t-1]
