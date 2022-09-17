# makes the computer keep guessing the user's number of choice until correct

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

    # makes the computer computer guess until correct
    guess = 0
    low = 1
    high = num
    correct = False
    while not correct:
        guess = (low + high) // 2
        s = input(f"Is the number you're thinking of greater than (G), less than (L), or equal (E) to {guess}? ").lower()
        if s == "g":
            low = guess + 1
        elif s == "l":
            high = guess - 1
        elif s == "e":
            correct = True
    
    print("Yay!")
        

main()