#! /usr/bin/env python3

# Resources:
# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=2531s
# https://www.ascii-code.com/
# https://docs.python.org/3/library/string.html

import random, string
# The tutorial manually created the list
# Imported string module instead
chars = string.ascii_letters + string.digits + string.punctuation
# Created the characters variable
# Did not use .printable due to white space 
print("Welcome to my Password Generator!")
num_pwds = int(input("How many passwords would you like? [int] "))
len_pwds = int(input("How long would you like your passwords to be? [int] "))

for n in range(num_pwds):
    passwords = ""
    # Needed to create empty variable for next for loop
    # This will be printed based on nume_pwds
    for l in range(len_pwds):
        passwords += random.choice(chars)
        # This adds one character at a time till len_pwds
    print(passwords)
