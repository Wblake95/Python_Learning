#! /usr/bin/env python3

# Resources
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# https://www.freecodecamp.org/news/python-projects-for-beginners/#minesweeper-python-project
# https://www.youtube.com/watch?v=8ext9G7xspg&t=5236s

import random

# Make class and initialize it
class game:
    def __init__(self, dem_size, num_bomb):
        self.dem_size = dem_size
        self.num_bomb = num_bomb

# Make board
    def board(self):
        board = [[None for i in range(dem_size)] for i in range(dem_size)]
        bomb = 0
        while bomb < self.num_bom:
            location = random.randint(0, self.dem_size**2 -1)
            row = location // self.dem_size
            column = location % self.dem_size
            if board[row][column] == "x":
                continue
            board[row][column] == "x"
            bomb +=1
        return board

# Set numbers for neighboring bombs
    def neighboring_bomb(self):
        for row in range(max(0, row-1), min(self.dim_size-1, row+1)):
            for column in range(max(0, column-1), min(self.dim_size-1, column+1)):
                if board[row][column] == "x":
                    continue
                board[row][column] = self.get_bomb_num(row, columb)

    def get_bomb_num(self, row, column):
        bomb_count = 0
        for row in range(max(0, row-1), min(self.dim_size-1, row+1)):
            for column in range(max(0, column-1), min(self.dim_size-1, column+1)):
                if row == crow and column == ccolumn:
                    continue
                if self.board[row][column] == "x":
                    bomb_count += 1
        return bomb_count
