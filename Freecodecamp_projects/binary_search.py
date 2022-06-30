#! /usr/bin/env python3

import random
from time import time

list = []

while len(list) < 1000:
    x = random.randint(1, 10000)
    list.append(x)

find = 7999
list.append(find)
list.sort()

# Incase search
def naive_search():
    start = time()
    for i in list:
        if i == find:
            return i
            print(time() - start)
            break
    print("Naive search done!\n")

# Binary search
def binary_search():
    high = list[-1]
    low = list[0]
    print(high)
    print(low)
    x = True
    start = time()
    while x:
        x = (low + high) // 2
        print(x)
        if x >= find:
            high = x
        else:
            high = high
        if x <= find:
            low = x
        else: low = low
        if x == find:
            print(x)
            print(time() - start)
            break

naive_search()
binary_search()
