import sys
import random

number = (random.int(1, 107))
guesses = 0

while guesses < 5:
    guess = int(input('Enter an integer from 1 to 107'))
    guesses += 1
    print("this is your percent of guesses" %guesses)

    if guesses > number:
        print("guess was to low")

        elif guesses < number:
        print("guess was to high")

        elif guesses == number:
        break

guess = str(guesses)
print("the real number was ", number)