import functools; light_switch = lambda n, lights: (1 << n) - 1 in functools.reduce(lambda x, s: x | {y ^ sum(1 << y for y in s) for y in x}, lights, {0})

# or 

def light_switch(n, lights):
    result = {0}
    for s in lights:
        result |= {x ^ sum(1 << x for x in s) for x in result}
    return (1 << n) - 1 in result
