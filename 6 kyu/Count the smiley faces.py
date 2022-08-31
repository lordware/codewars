def count_smileys(arr):
    counter = 0
    eye = [":", ";"]
    nose = ["-", "~"]
    m = [")", "D"]
    for x in arr:
        y = list(x)
        if len(y) == 2:
            if y[0] in eye and y[1] in m:
                counter += 1
        else:
            if y[0] in eye and y[1] in nose and y[2] in m:
                counter += 1
    return counter
