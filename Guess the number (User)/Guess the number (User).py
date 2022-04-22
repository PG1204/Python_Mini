from random import random


import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a single digit number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess too low. Guess again!")
        elif guess > random_number:
            print("Sorry, guess too high. Guess again!")

    print(f"Bingo! You've guessed the right number which is {random_number}.")

guess(10)