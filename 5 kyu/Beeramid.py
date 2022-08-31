def beeramid(bonus, price):
    beer = int(bonus / price)
    needed = 1
    stage = 1
    if beer < 1:
        return 0
    else:
        while beer >= needed:
            stage += 1
            needed += stage ** 2
    if needed > beer:
        return stage - 1
    else:
        return stage
