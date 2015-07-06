def hamming_sum(s0, s1):
    if len(s0) != len(s1):
        raise ValueError()
    return sum(count(cs) for cs in zip(s0, s1))

cdef int count(tuple cs):
    return (cs[0] != cs[1])

def hamming_loop(char *s0, char *s1):
    if len(s0) != len(s1):
        raise ValueError()
    cdef:
        int N = len(s0)
        int i, count = 0
    for i in range(N):
        count += (s0[i] != s1[i])
    return count
