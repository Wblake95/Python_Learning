#! /usr/bin/env python3

# This "project" follows the guide from "Freecodecamp.com"
# link: https://www.freecodecamp.org/news/python-projects-for-beginners/
# Particular video used: https://www.youtube.com/watch?v=8ext9G7xspg&t=100s

# This is a madlib!
def myplay():
    global mainch
    global season
    global local
    global play
    while play != "Yes" or "No":
        if play == "Yes":
            break
        elif play == "No":
            print("Thanks for coming! Goodbye :)")
            break
        else:
            play = input("Maybe try capitalizing your response? [Yes/No] ")
            break
            
# Intro, this is the intro
name = input("Hi, What is your name? ")
print(f"Hi, {name} and welcome to this story! ")
adj = input("How would you decribe yourself? ")
print(f"Well, {name}. I think, {adj} describes you well!\n\n\n")


# Set-up, this is the set up
play = input(f"{name}, Would you like to hear a story? [Yes/No] ")
myplay()
mainch = input("What is a feminine name that you like? ")
season = input("Pick your favorite season! ")
local = input("Name a place like, a forest, that matches the season! ")


# Story, this is the story
while play == "Yes":
    print(f"\n\n\nThere once was a girl named {mainch} that liked the {season}.")
    print(f"She liked the {local} so much and would want to spend all of her time there with her friend.")
    sidech = input("Pick a name for her friend! ")
    print(f"{mainch} and {sidech} would both go on adventures together in the {local} during the {season}!\n\n\n")
   
    play = input("Do you like my story so far? [Yes/No] ")
    myplay()

    print(f"\n\n\nThats great! Anyway, they are on an adventure when {sidech} spots a Troll!")
    weapon = input("What weapon do they have?! ")
    print(f"{mainch} used the {weapon} to attack the Troll!")
    print(f"\"Wait!\" The Troll says! \"I don't want to fight.\" {mainch} was confused; she looked at {sidech}.\n{sidech} only shrugged their shoulders.\n")
    print(f"{mainch} said \"Then what do you want?\"")
    print("The Troll said \"I just wanted to go for a walk!\"")
    print(f"{sidech} said \"Sorry, for the disturbance.\"")
    print(f"The Troll looked frustrated. Then the Troll said \"Children are terrifying\"")
    print(f"{mainch} and {sidech} continued on their journey\n\n\n")

    print("They then come across a cave! However, they also see another path that leads to a Village.")
    choice = input("1. The cave! 2. The other path! [Cave/Path]")
    while choice != "Cave" or "Path":
        if choice == "Cave":
            print("They found The Mountain Beast!")
            break
        elif choice == "Path":
            print("They found a Leshen!")
            break
        else:
            print("Something broke!")
            break

    print(f"{mainch} used the {weapon} to attack The Mountain Beast!")
    print(f"{sidech} distracted the Beast by throwing rocks.")
    print(f"{mainch} and {sidech} defeated The Mountain Beast and won the day!")
    print("\n\n\n I hope you had fun :).")
    break

