#! /usr/bin/env python3

import time
# https://docs.python.org/3/library/time.html
# My comments will focus on what I learned from this project.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        # divmod will divide the left intiger by the right integer. Unless the right is smaller.
        # (integer, remander)
        # divmod(300, 60)
        # (5, 0)
        # divmod(3, 60)
        # (0, 3)
        timer = "{:02d}:{:02d}".format(mins, secs)
        # "{:02d}:{:02d}"
        # Variable will fill in the {}. The integer will replace the zeros.
        # The "0" will be inserted multiplied by the integer next to it.
            # e.g. input:"{:02d},{:02d},{:02d},{:02d}".format(0, 1, 10, 100)
            # e.g. output: "00,01,10,100"
        # The d stands for a base 10 number.
            # It will only accept an integer not a float.
            # However, it will still work. If you put a float, the output will just look weird.
        print(timer, end="\r")
        # The \r is a type of return function.
            # It will place the cursor at the beginning of the same line.
            # When it goes to print the next instruction, it will replace it with the updated number.
            # Instead of printing a new line every iteration.
            # 00:03 > 00:02 > 00:01 > stop.
        time.sleep(1)
        t -= 1

    print("timer completed!")

x = int(input("Please pick a time in seconds: "))
countdown(x)
