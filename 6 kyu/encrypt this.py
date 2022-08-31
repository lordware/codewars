import re


def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)


def encrypt_this(text):
    if len(text) == 0:
        return ""

    text = text.split(" ")
    for x in range(len(text)):
        if len(text[x]) > 1:
            text[x] = swap(text[x], 1, len(text[x]) - 1)
        text[x] = re.sub(text[x][0], str(ord(text[x][0])), text[x], 1)
    return " ".join(text)
