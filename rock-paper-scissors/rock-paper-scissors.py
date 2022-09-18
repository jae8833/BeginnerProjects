# play rock paper scissors with the computer

import random

while True:
    user = input("Choose 'R' for rock, 'P' for paper, 'S' for scissors, or 'Q' to quit: ").lower()
    if user == 'q':
        print("GGs")
        break
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print("Tie")
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        print("User won")
    elif (user == 's' and computer == 'r') or (user == 'r' and computer == 'p') or (user == 'p' and computer == 's'):
        print("Computer won")
    else:
        print("Please only input 'R', 'P', 'S', or 'Q'")

