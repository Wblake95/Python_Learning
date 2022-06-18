#! /usr/bin/env python3

import random
import datetime as dt

def guessme(x):
    guess = 0
    rand = random.randint(1,x)

    while guess != rand:
        print(f"Guess a number between 1 and {x}")
        print("What is your first guess?")
        guess = int(input())
        if guess < rand:
            print("Your guess was to low!")
        elif guess > rand:
            print("Your guess was to high!")
    print("You guessed correctly!")


x = dt.datetime.now()
if (int(x.strftime("%H"))) >= 17:
    print("Good evening!")
elif (x.strftime("%p")) == "AM":
    print("Good morning!")
elif (x.strftime("%p")) == "PM":
    print("Good afternoon")

guessme(10)
