def pig_it(text):
    print(text)
    text = text.split(" ")
    for x in range(len(text)):
        if text[x] != '!':
            if text[x] != '?':
                text[x] = text[x][1:] + text[x][0]
                text[x] += "ay"
    return " ".join(text)
