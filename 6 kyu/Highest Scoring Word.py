def high(x):
    x = x.split(' ')
    res = 0
    res_word = ""
    for y in x:
        ch = 0
        for z in y:
            ch += ord(z) - 96
        if ch > res:
            res = ch
            res_word = y
    return res_word