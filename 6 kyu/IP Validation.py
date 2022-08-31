def check_zero(str):
    if len(str) == 0:
        return False
    if str[0] == '0' and len(str) > 1:
        return False
    else:
        return True


def is_valid_IP(strng):
    arr = strng.split('.')
    if len(arr) != 4:
        return False

    if len(strng) == 0:
        return False
    for x in arr:
        checker = False
        if check_zero(x):
            if x.isnumeric():
                if 0 <= int(x) <= 255:
                    checker = True
        if not checker:
            return checker
    return checker