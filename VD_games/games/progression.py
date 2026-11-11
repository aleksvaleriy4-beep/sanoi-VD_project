import random

RULES = "What number is missing in the progression?"


def make_progression(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(2, 9)
    numbers = make_progression(start, step, length)
    hidden = random.randint(0, length - 1)
    answer = str(numbers[hidden])
    numbers[hidden] = ".."
    question = " ".join(str(number) for number in numbers)
    return question, answer