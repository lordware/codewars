def find_children(dancing_brigade):
    x = list(dancing_brigade)
    x.sort()
    x.sort(key=str.lower)
    return "".join(x)
