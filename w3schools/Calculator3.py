#! /usr/bin/env python3

cal_dict = {
        "sum": lambda x, y: x + y,
        "sub": lambda x, y: x - y,
        "mult": lambda x, y: x * y,
        "div": lambda x, y: x / y,
        "expo": lambda x, y: x ** y,
        }

start = input("Welcome to my new calculator! Would you like to continue? [Y/N] ").lower()
while start == "y":
    opper = input("What is your opperator? [Sum, Sub, Mult, Div, Expo] ").lower()
    x = int(input("What is your first int?: "))
    y = int(input("What is your second int?: "))
    print(cal_dict[f"{opper}"](x,y))
    start = input("Welcome to my new calculator! Would you like to continue? [Y/N] ").lower()
