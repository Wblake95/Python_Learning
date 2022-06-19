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
print("What is Binary Search?")
print("Binary Search is when you take a list, like a bookshelf, and search through it to find the thing you want!")
print("All you have to do is find out how long the list is and pic the middle number.")
print("After than compare your number to the one you picked.")
print("Lets give it a try!")

guessme(5)

print("So, how did you do?")
x = input("How many tries till you got it? ")
if x > 2:
    print("That was an unlucky guess!")
if x < 2:
    print("Good job!")
print("This idea can help you alot in the world. It can also help when learning to code.")
