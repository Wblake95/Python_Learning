#! /usr/bin/env python3

import random
import datetime as dt

def guessme(x):
    guess = x
    rand = random.randint(1,x)
    while guess != rand:
        guess = int(input(f"\nGuess a number between (1, {x}) "))
        if guess < rand:
            print("Your guess was to low!")
        elif guess > rand:
            print("Your guess was to high!")
    print(f"\nYou guessed correctly! ({guess})")

def guesscpu(high):
    feedback = ""
    low = 1
    #high = x
    while feedback != 'c':
        rand = random.randint(low, high)
        feedback = input(f"Is {rand} your number? [L,H, or C] ").lower()
        if feedback == "l":
            low = rand + 1
        elif feedback == "h":
            high = rand - 1
        elif low == high:
            break
    print(f"Yay! The computer guessed your number! {rand}")


greeting = dt.datetime.now()
if (int(greeting.strftime("%H"))) >= 17:
    print("Good evening!")
elif (greeting.strftime("%p")) == "AM":
    print("Good morning!")
elif (greeting.strftime("%p")) == "PM":
    print("Good afternoon!")


x = int(input("\nA simple guessing game first! You are the guesser! Pick x in (1, x) "))
guessme(x)

high = int(input("\n\nPick x (1,x) for the computer to Guess! "))
guesscpu(high)
