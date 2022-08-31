import itertools


def permutations(string):
    res = [''.join(p) for p in itertools.permutations(string)]
    res = set(res)
    return list(res)
