import math
import random

RULES = "Find the greatest common divisor of given numbers."


def generate_round():
    first = random.randint(1, 100)
    second = random.randint(1, 100)
    return f"{first} {second}", str(math.gcd(first, second))