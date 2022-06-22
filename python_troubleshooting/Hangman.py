#! /usr/bin/env python3

import random
from words import fruits
import string


def get_valid_words(fruits):
    word = random.choice(fruits)
    while "-" in word or " " in word:
        word = random.choice(fruits)

    return word.upper()

def hangman():
    word = get_valid_words(fruits)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives remaining. Used letters: "," ".join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives = lives - 1 
                print("letter is not in the word!")
    
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print(f"You died, sorry. The word was {word}.")
    else:
        print(f"You guessed the word, {word}!!!")

hangman()
