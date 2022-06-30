#! /usr/bin/env python3

import random
from time import time
from string import ascii_letters

# List to search and number to find
list, find_number = [], 7999
while len(list) < 10000:
    x = random.randint(1, 10000)
    list.append(x)
list.append(find_number)
# Sorting list
list.sort()

# Naive search
def naive_search():
    y, start = 0, time()
    for i in list:
        y += 1
        if i == find_number:
            return i, y, time() - start, "Naive search done!\n"
            break

# Binary search
def binary_search():
    high, low, x, y, start = list[-1], list[0], True, 0, time()
    while x:
        y += 1
        x = (low + high) // 2
        high = x if x >= find_number else high
        low = x if x <= find_number else low
        if x == find_number:
            return x, y, time() - start, "Binary search done!"
            break

print(naive_search())
print(binary_search())
