def hamming_sum(s0, s1):
    if len(s0) != len(s1):
        raise ValueError()
    return sum(c0 != c1 for (c0, c1) in zip(s0, s1))

def hamming_loop(s0, s1):
    if len(s0) != len(s1):
        raise ValueError()
    count = 0
    for i in range(len(s0)):
        count += (s0[i] != s1[i])
    return count
