import prompt

ROUNDS = 3


def run(game):
    print("Welcome to the VD games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.RULES)
    for _ in range(ROUNDS):
        question, correct = game.generate_round()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer != correct:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")