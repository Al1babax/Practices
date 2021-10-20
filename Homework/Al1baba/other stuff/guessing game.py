# Number Guessing Game

import random


def guessing_game():

    run_again = True
    random_number = random.randint(1, 9)

    while run_again:
        try:
            your_number = int(input("Guess a number (between 1 and 9): "))
        except TypeError:
            print("Your input is not a whole number")

        if your_number == random_number:
            print("Congratulation YOU WON!!!")
            run_again = False

        elif your_number < random_number:
            print(f"Your guess was too low: Guess a number higher than {your_number}")

        elif your_number > random_number:
            print(f"Your guess was too high: Guess a number lower than {your_number}")


def play():
    run_game = True

    while run_game:
        guessing_game()

        ask_user = (input(f"Do you want to play again select y/n? ")).lower()

        if ask_user == "y":
            run_game = True

        elif ask_user == "n":
            run_game = False


play()