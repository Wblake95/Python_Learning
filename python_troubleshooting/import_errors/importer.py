#! /usr/bin/env python3

try:
#trying to find a module in the parent package
# This one didn't work. I am not sure when I would use this. But I have it now.
    from home import words
    print(words.debug)
    del words
except ImportError:
print("Relative import failed")

try:
#Trying to find module on path
# This one works for hangman. I think it is because it is on the same path.
    import words
    print(words.debug)
except ModuleNotFoundError:
print("Absolute import failed")
