time = (
    ('years', 31536000),
    ('days', 86400),
    ('hours', 3600),
    ('minutes', 60),
    ('seconds', 1),
)


def format_duration(seconds):
    result = []
    print(seconds)
    returns = ""
    if seconds == 0:
        return 'now'
    for name, count in time:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    if len(result) > 2:
        returns = ', '.join(result[0:-1])
        returns += f' and {result[-1:][0]}'
    else:
        returns = ' and '.join(result)
    return returns
