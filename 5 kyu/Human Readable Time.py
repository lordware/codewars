import time


def make_readable(seconds):
    hour = 0
    while seconds >= 86400:
        hour += 24
        seconds -= 86400
    result = time.strftime('%H:%M:%S', time.gmtime(seconds))
    result2 = time.strftime(':%M:%S', time.gmtime(seconds))
    if (int(result[0:2]) + hour) < 10:
        pr = f"0{int(result[0:2]) + hour}{result2}"
    else:
        pr = f"{int(result[0:2]) + hour}{result2}"
    return pr
