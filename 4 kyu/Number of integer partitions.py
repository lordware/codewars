def parts(n):
    return [1] + [0] * n


def partitions(n):
    part = parts(n)
    for t in range(1, n + 1):
        for i, x in enumerate(range(t, n + 1)):
            part[x] += part[i]
    return part[n]
