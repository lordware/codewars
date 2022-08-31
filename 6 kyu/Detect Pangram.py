def is_pangram(s):
    filter = [x.lower() for x in s if x.isalpha()]
    if len(set(filter)) == 26:
        return True
    return False
