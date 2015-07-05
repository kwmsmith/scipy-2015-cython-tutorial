def levenshtein_distance(s, t):
    return lev(s, len(s), t, len(t))

def lev(s, len_s, t, len_t):
    if len_s == 0 or len_t == 0:
        return len_s or len_t
    return min(lev(s, len_s-1, t, len_t  ) + 1,
               lev(s, len_s  , t, len_t-1) + 1,
               lev(s, len_s-1, t, len_t-1) + cost(s, len_s, t, len_t)) 

def cost(s, len_s, t, len_t):
    return s[len_s-1] != t[len_t-1]
