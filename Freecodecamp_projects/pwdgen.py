#! /usr/bin/env python3

import random, string

chars = string.ascii_letters + string.digits + string.punctuation
num_pwds = int(input("Number of passwords? [int] "))
len_pwds = int(input("Length of passwords? [int] "))

for n in range(num_pwds):
    passwords = ""
    for l in range(len_pwds):
        passwords += random.choice(chars)
    print(passwords)

print("This is a place holder for saving passwords")
