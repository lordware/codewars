def one_two_three(n):
    res = []
    up_to_nine = 0
    num2 = ""
    num1 = ""
    for x in range(n):
        num2 += '1'
        up_to_nine += 1
        if up_to_nine == 9:
            num1 += "9"
            up_to_nine = 0

    if n < 9:
        num1 = str(n)
    elif up_to_nine > 0 and n > 9:
        num1 += str(up_to_nine)
    if n < 1:
        num1 = '0'
        num2 = '0'

    res.append(int(num1))
    res.append(int(num2))
    return res
