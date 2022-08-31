def find(sequence):
    sequence.sort()
    length = len(sequence)
    x = int((sequence[length - 1] - sequence[0] )/ length)
    start = sequence[0]
    for y in range(1, length):
        if sequence[y] - start != x:
            return start + x
        else:
            start = sequence[y]