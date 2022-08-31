def valid_ISBN10(isbn):
    counter = 1
    result = 0
    validator = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X', '0']
    print(isbn)
    for x in str(isbn):
        if x not in validator or len(isbn) != 10:
            return False
        if x == 'X' and counter == 10:
            x = 10
        elif x == 'X':
            return False
        result += counter * int(x)
        counter += 1

    if result % 11 == 0:
        return True
    else:
        return False
