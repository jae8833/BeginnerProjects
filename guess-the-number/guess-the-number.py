# makes user keep guessing the random number that is generated by the computer until correct

import random

def main():
    # get a positive integer from user
    while True:
        try:
            num = int(input("Input a positive integer greater than 1: "))
            if num <= 1:
                print("Please enter a positive integer value")
                continue
            else:
                break
        except ValueError:
            print("Please enter a positive integer value")
            continue

    # start the guessing game
    guessRandomNum(num)


def guessRandomNum(num):

    # get random number
    randomNum = random.randint(1, num)

    # make user guess until correct
    print(f"Guess the random number generated by the computer beween 1 and {num}")
    correct = False
    while not correct:
        while True:
            try:
                guess = int(input("Guess: "))
                if num <= 1:
                    print("Please enter a positive integer value")
                    ValueError
                else:
                    break
            except ValueError or guess <= 1:
                print("Please enter a positive integer value")
                continue
        if randomNum < guess:
            print("The random number is less than your guess.")
        elif randomNum > guess:
            print("The random number is greater than your guess.")
        else:
            print("Correct!")
            correct = True


main()