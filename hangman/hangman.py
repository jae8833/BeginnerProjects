# play hangman where the computer chooses a random word in the english_words_set
from words import words
import random

def main():
    word = " "
    while " " in word or "-" in word:
        word = random.choice(words)
    playHangman(word)

def playHangman(word):
    lives = 6
    used_characters = []
    letter_word = []
    while lives >= 1:
        word_list = [letter if letter in letter_word else "-" for letter in word]
        if not "-" in word_list:
            break
        print("You have used these letters: ", " ".join(used_characters))
        print("Word:", " ".join(word_list))
        print(f"Lives: {lives}")
        letter = input("Guess a letter: ").lower()
        if letter in used_characters or letter in letter_word:
            print()
            print("You have already guessed that letter!")
        elif not letter.isalpha() or not len(letter) == 1:
            print()
            print("Guess a valid letter!")
        elif letter in word:
            letter_word.append(letter)
        else:
            used_characters.append(letter)
            lives -= 1
        print()

    if lives < 1:
        print(f"You lose. The word was {word}")
    else:
        print(f"You win! The word was {word}")

    print()


main()

