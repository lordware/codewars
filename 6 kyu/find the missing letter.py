def find_missing_letter(chars):
    al = "abcdefghijklmnopqrstuvwxyz"
    index = al.find(chars[0])
    print(index)
    if index == -1:
        al = al.upper()
        index = al.find(chars[0])

    for x in range(len(chars)):
        if chars[x] != al[index + x]:
            return al[index + x]
