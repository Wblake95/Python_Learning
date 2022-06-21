#! /usr/bin/env python3

import random

# Was an interesting project.
# I struggled to figure out why my if arguments weren't working.
# I needed to wrap game() in a print function!
# However, it was interesting to actually use the return function.

# Lesson and Resources.
# URL:          https://www.youtube.com/watch?v=8ext9G7xspg&t=1274s @23:54.
# Other help:   https://www.w3schools.com/python/ref_keyword_return.asp

def game():
    user = input("Pick your choice! [r]ock, [p]aper, [s]cissors! ")
    computer = random.choice(['r', 'p', 's'])
    print(f"Player: {user}")
    print(f"Computer: {computer}")

    if user == computer:
        return "This was a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"

def is_win(player, CPU):
    if (player == 'r' and CPU == 's') or (player == 'p' and CPU == 'r') or (player == 's' and CPU == 'p'):
        return True

print(game())
