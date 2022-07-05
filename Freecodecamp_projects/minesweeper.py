#! /usr/bin/env python3

# Resources
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# https://www.freecodecamp.org/news/python-projects-for-beginners/#minesweeper-python-project
# https://www.youtube.com/watch?v=8ext9G7xspg&t=5236s

import random
import re

# Make class and initialize it
class game:
    def __init__(self, dim_size, num_bomb):
        self.dim_size = dim_size
        self.num_bomb = num_bomb
    
        self.board = self.board()
        self.neighboring_bomb()
        self.dug = set()

# Make board
    def board(self):
        # Making board
        board = [[None for i in range(self.dim_size)] for i in range(self.dim_size)]
        # Planting bombs
        bomb = 0
        while bomb < self.num_bomb:
            location = random.randint(0, self.dim_size**2 -1)
            row, column = location // self.dim_size, location % self.dim_size
            # column = location % self.dim_size
            if board[row][column] == "x":
                continue
            board[row][column] == "x"
            bomb +=1
        return board

# Set numbers for neighboring bombs
    def neighboring_bomb(self):
        for row in range(self.dim_size):
            for column in range(self.dim_size):
                if self.board[row][column] == "x":
                    continue
                self.board[row][column] = self.get_bomb_num(row, column)

    def get_bomb_num(self, row, column):
        bomb_count = 0
        for row in range(max(0, row-1), min(self.dim_size-1, row+1)):
            for column in range(max(0, column-1), min(self.dim_size-1, column+1)):
                if row == row and column == column:
                    continue
                if self.board[row][column] == "x":
                    bomb_count += 1
        return bomb_count

    def dig(self, row, col):
        self.dug.add((row,col))
        if self.board[row][col] == "x":
            return False
        elif self.board[row][col] > 0:
            return True
        for row in range(max(0, row-1), min(self.dim_size-1, row+1)):
            for column in range(max(0, column-1), min(self.dim_size-1, column+1)):
                if(row, col) in self.dug:
                    continue
                self.dig(row, col)
        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "

def play(dim_size = 10, num_bomb = 10):
    board = game(dim_size, num_bomb)
    sage = True
    while len(board.dug) < board.dim_size ** 2 - num_bomb:
        print(board)
        user_input = re.split("\s*,\s*", input("Pick a spot! x,y"))
        row, col = int(user_input[0]), int(user_input[1])
        if row <0 or roe >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location. Try again.")
            continue
        safe = board.dig(row, col)
        if not sage:
            break
    if safe:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost")
        board.dug = [(row, col) for row in range(board.dim_size) for c in range(boad.dim_size)]
        print(board)

if __name__ == "__main__":
    play()
