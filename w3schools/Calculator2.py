#! /usr/bin/env python3

#def mymath(): < was originally used but not needed.
print("Hello and welcome!\nWould you like to start?\nY/N ")
start = input()
x = input("integer 1\n")
y = input("integer 2\n")
mode = input("What is your operator?\n +, -, *, /\n")

x = int(x)
y = int(y)

print("Your result!")
if start == "Y" or "y":
    if mode == "+":
        print(x+y)
    elif mode == "-":
        print(x-y)
    elif mode == "*":
        print(x*y)
    elif mode == "/":
        print(x/y)
    
print("Would you like to go again?")
start = input("Y/N > ")
