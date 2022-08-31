import re


def strip_comments(strng, markers):
    # print(f"string: {strng}, marker: {markers}")
    marker = []
    for y in markers:
        marker.append('\\' + y)
    checker = False
    for x in markers:
        if x in strng:
            checker = True
            break

    if checker:
        strng = strng.split('\n')
        res = []
        for x in strng:
            res.append(re.split("|".join(marker), x)[0].rstrip())
        return "\n".join(res)
    else:
        return strng
