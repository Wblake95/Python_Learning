#! /usr/bin/env python3

#This "project" follows the guide from "Freecodecamp.com"
#link: https://www.freecodecamp.org/news/python-projects-for-beginners/
#Particular video used: https://www.youtube.com/watch?v=8ext9G7xspg&t=100s

#This is a madlib!
def chsadven():
    global mainch
    global sidech
    global local
    global season
    global noun
    global adj1
    global adj2
    global adj3
    global verb1
    global verb2
    global verb3
    global ansY
    global ansN
    global ansY
    global ansN
def myplay():
    while play != "Yes" of "No":
        score = 1
        score += 1
        if score = 3:
            break
        if play == "Yes":
            mainch = input("What is a feminine name that you like? ")
            season = input("Pick your favorite season! ")
            local = input("Name a place like, a forest, that matches the season! \n\n\n")
        elif play == "No":
            print("Thanks for coming! Goodbye :)")
        else:
            play = input("Maybe try capitalizing your response? [Yes/No]")
        score = 1
        score += 1
        if score = 3:
            break

def Mysomething():

#Intro, this is the intro
name = input("Hi, What is your name? ")
print(f"Hi, {name} and welcome to this madlib!")
adj = input("How would you decribe yourself? ")
print(f"Well, {name}. I think, {adj} describes you well!")

#Set-up, this is the set up
play = input(f"{name}, Would you like to hear a story? [Yes/No] ")
while play != "Yes" of "No":
    score = 1
    score += 1
    if score = 3:
        break

#Game, this is the game
while play == "Yes":
    print(f"There once was a girl that liked the {season}")
    print(f"She liked the {local} so much and would want to spend all of her time there with her friend.")
    sidech = input("Pick a name for her friend! ")
    print(f"{mainch} and {sidech} would both go on adventures together in the {local} during the {season}!")
    play = input("Do you like my story so far? [Yes/No]")
    if play == "Yes":
        print("")
    elif play == "No":
        break
    print(f"Thats great! Anyway, they are on an adventure when {sidech} spots a Troll!")
    weapon = input("What weapon do they have?! ")
    print(f"{mainch} used the {weapon} to attack the Troll!")
    print(f"\"Wait!\" The Troll says! \"I don't want to fight.\" {mainch} was confused; she looked at {sidech}.\n {sidech} only shrugged their shoulders.")
    print(f"[mainch] said \"Then what do you want?\"")
    print("The Troll said \"I just wanted to go for a walk!")
    print(f"{sidech} said \"Sorry, for the disturbance.\"")
    print(f"The Troll looked disturbed. Then they said \"Children are terrifying\"")
    print(f"{mainch} and {sidech} continued on their journey")
    play = "No"
