def anagrams(word, words):
    res = []
    for x in words:
        if sorted(x) == sorted(word):
            res.append(x)
    return res
