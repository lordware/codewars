def last_digit(lst):
    res = 1
    if not lst:
        return 1
    for i in lst[::-1]:
        if res < 4:
            res = (i ** res)
        else:
            res = (i ** (res % 4 + 4))
    return res % 10
