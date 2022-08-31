def move_zeros(lst):
    zeros = lst.count(0)
    res = []
    for x in range(zeros):
        lst.remove(0)

    for x in lst:
        res.append(x)
    for x in range(zeros):
        res.append(0)
    return res
