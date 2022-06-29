#! /usr/bin/env python3

# References
# https://www.youtube.com/watch?v=8ext9G7xspg&t=2153s
    # Couldn't figure out how her for statements worked
    # Attempted it my way
# https://www.youtube.com/watch?v=dK6gJw4-NCo

board = ["-","-","-","-","-","-","-","-","-"]
player = "x"
game_running = True
cpu = input("Would you like to play with the computer? [T/F] ").upper()
cpu = True if cpu == "T" else False

def print_board(board):
    row1,row2,row3 = board[0]+"|"+board[1]+"|"+board[2],board[3]+"|"+board[4]+"|"+board[5],board[6]+"|"+board[7]+"|"+board[8]
    print(row1+"\n"+row2+"\n"+row3)

def player_input():
    x = int(input(f"Place your {player}! "))
    while x:
        if board[x-1] == "x" or board[x-1] == "o":
            print_board(board)
            print("Oops, that spot is taken!")
            x = int(input(f"Place your {player}! "))
        else:
            board[x-1] = player
            break

def check_game_running(board): 
    global game_running
    # Row check
    if board[0] == board[1] == board[2] and board[0] != "-":
        print_board(board)
        print(f"{player} wins the game!")
        game_running = False
    if board[3] == board[4] == board[5] and board[3] != "-":
        print_board(board)
        print(f"{player} wins the game!")
        game_running = False
    if board[6] == board[7] == board[8] and board[6] != "-":
        print_board(board)
        print(f"{player} wins the game!")
        game_running = False
    # Column check
    if board[0] == board[3] == board[6] and board[0] != "-":
        print_board(board)
        print(f"{player} wins the game!")
        game_running = False
    if board[1] == board[4] == board[7] and board[1] != "-":
        print_board(board)
        print(f"{player} wins the game!")
        game_running = False
    if board[2] == board[5] == board[8] and board[2] != "-":
        print_board(board)
        print(f"{player} wins the game!")
        game_running = False
    # Diagonal check
    if board[0] == board[4] == board[8] and board[0] != "-":
        print_board(board)
        print(f"{player} wins the game!")
        game_running = False
    if board[2] == board[4] == board[6] and board[2] != "-":
        print_board(board)
        print(f"{player} wins the game!")
        game_running = False

def switch_player():
    global player
    player = "o" if player == "x" else "x"

def CPU(board):
    while player == "o":
        x = random.randint(0,8)
        while x:
            if board[x] == "x" or board[x] ==  "o":
                x = random.randint(0,8)
            else:
                board[x] = player 
                break
        break

while game_running:
    print_board(board)
    player_input()
    check_game_running(board)
    switch_player()
