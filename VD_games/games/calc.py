import random

RULES = "What is the result of the expression?"


def generate_round():
    first = random.randint(1, 25)
    second = random.randint(1, 25)
    operator = random.choice("+-*")
    match operator:
        case "+":
            result = first + second
        case "-":
            result = first - second
        case _:
            result = first * second
    return f"{first} {operator} {second}", str(result)

