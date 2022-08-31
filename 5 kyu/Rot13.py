import string

dict1 = {
    'a': 'n',
    'b': 'o',
    'c': 'p',
    'd': 'q',
    'e': 'r',
    'f': 's',
    'g': 't',
    'h': 'u',
    'i': 'v',
    'j': 'w',
    'k': 'x',
    'l': 'y',
    'm': 'z'
}


def rot13(message):
    result = ""
    for x in message:
        if x.islower() and x.isalpha():
            index = string.ascii_lowercase.index(x)
        elif x.isupper() and x.isalpha():
            index = string.ascii_uppercase.index(x)
        else:
            result += x
            continue
        if index <= 12:
            newval = dict1.get(x.lower())
        else:
            for i, y in dict1.items():
                if y == x.lower():
                    newval = i

        if x.islower():
            result += newval
        else:
            result += newval.upper()
    return result
