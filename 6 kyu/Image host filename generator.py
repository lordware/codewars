import random
import string


def generateName():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(6))
