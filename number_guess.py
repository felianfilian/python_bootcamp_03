# number guessing game
# number 1 to 100
# easy or har level (5)or 10 guesses

import random

EASY_LEVEL = 10
HARD_LEVEL = 5


def start():
    def check_guess(guess, number, chances):
        if guess > number:
            print("too high")
            return chances - 1
        elif guess < number:
            print("too low")
            return chances - 1

    def set_difiiculty():
        level = input("Choose easy (0) or hard (1) level\n")
        if level == "1":
            print("Hard level")
            return HARD_LEVEL
        else:
            print("Easy level")
            return EASY_LEVEL

    number = random.randint(1, 100)
    chances = set_difiiculty()
    not_guessed = True

    while not_guessed:
        print(f"Chances: {chances}")
        guess = int(input("Guess the number between 1 and 99:\n"))
        chances = check_guess(guess, number, chances)
        if chances == 0:
            print("You loose")
            not_guessed = False
        if guess == number:
            print("You found the number")
            not_guessed = False

    print("Game finished")
