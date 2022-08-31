def snail(array):
    result = []
    while len(array) > 0:
        result += array[0]
        del array[0]

        if len(array) > 0:
            for i in array:
                result += [i[-1]]
                del i[-1]

            if array[-1]:
                result += array[-1][::-1]
                del array[-1]

            for x in reversed(array):
                result += [x[0]]
                del x[0]

    return result
