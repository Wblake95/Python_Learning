#! /usr/bin/env python3

try:
#trying to find a module in the parent package
    from home import words
    print(words.debug)
    del words
except ImportError:
print("Relative import failed")

try:
#Trying to find module on sys.path
    import words
    print(words.debug)
except ModuleNotFoundError:
print("Absolute import failed")
