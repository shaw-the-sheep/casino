from tkinter import Label
from random import random, randint

class Connect4:
    def __init__(self):
        
        self.balance = 0
        self.winning_times = 0
        self.columns_count = [0]*7
        self.grid = [[" " for i in range(7)] for j in range(6)]

    def domove(self, column, frame, restart_func, updating_func):
        print(self.columns_count)
        row = 5-self.columns_count[column]
        print(row, column)

        self.grid[row][column] = "R"
        label = Label(frame, bg = "red", width=10, height=2, bd=1, relief="solid")
        label.grid(row=row+1, column=column)

        player_win = self.check(column, restart_func, updating_func, 1)
        if player_win:    
            return

        self.computer(frame, restart_func, updating_func)

        print(self.columns_count)


    def check(self, column, restart_func, updating_func, player):
        self.columns_count[column] += 1
        
        if self.winnigstate(self.grid):
            if player == 1:
                self.winning_times += 1
                self.balance += 10
                print("You win")
            restart_func()
            updating_func()
            self.columns_count = [0]*7
            self.grid = [[" " for i in range(7)] for j in range(6)]
            return True

        elif self.is_full(self.grid):
            restart_func()
            self.columns_count = [0]*7
            self.grid = [[" " for i in range(7)] for j in range(6)]

        return False

    def winnigstate(self, grid):
        if self.horizontal_win(grid) or self.vertical_win(grid) or self.diagonal_win(grid):
            return True
        return False

    def horizontal_win(self, grid):
        for i in range(6):
            for j in range(4):
                if grid[i][j] == grid[i][j+1] == grid[i][j+2] == grid[i][j+3] != " ":
                    return True
        return False
    
    def vertical_win(self, grid):
        for i in range(3):
            for j in range(7):
                if grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j] != " ":
                    return True
        return False
    
    def diagonal_win(self, grid):
        for i in range(3):
            for j in range(4):
                if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == grid[i+3][j+3] != " ":
                    return True
        for i in range(3):
            for j in range(3, 7):
                if grid[i][j] == grid[i+1][j-1] == grid[i+2][j-2] == grid[i+3][j-3] != " ":
                    return True
        return False

    def is_full(self, grid):
        for i in range(6):
            for j in range(7):
                if grid[i][j] == " ":
                    return False
        return True
    
    def computer(self, frame, restart_func, updating_func):
        p = 0.7
        block, column, row = self.block(frame, restart_func, updating_func)
        if block and random() < p:
            print("block")
            self.columns_count[column] += 1
            label = Label(frame, bg = "yellow", width=10, height=2, bd=1, relief="solid")
            label.grid(row=row+1, column=column)        
        else:
            computer_win = self.win(frame, restart_func, updating_func)
            if computer_win:
                print("computer win")
                return
            column = randint(0, 6)
            row = 5 - self.columns_count[column]
            print(row, column)
            self.grid[row][column] = "Y"
            label = Label(frame, bg = "yellow", width=10, height=2, bd=1, relief="solid")
            label.grid(row=row+1, column=column)
            self.check(column, restart_func, updating_func, 2)


    def block(self, frame, restart_func, updating_func):
        for i in range(6):
            row = 5 - self.columns_count[i]
            self.grid[row][i] = "R"
            if self.winnigstate(self.grid):
                self.grid[row][i] = "Y"
                return True , i, row
            else:
                self.grid[row][i] = " "
        return False, -1, -1

    def win(self, frame, restart_func, updating_func):
        for i in range(6):
            row = 5 - self.columns_count[i] 
            self.grid[row][i] = "Y"
            if self.winnigstate(self.grid):
                label = Label(frame, bg = "yellow", width=10, height=2, bd=1, relief="solid")
                label.grid(row=row+1, column=i)
                restart_func()
                updating_func()
                self.columns_count = [0]*7
                self.grid = [[" " for i in range(7)] for j in range(6)]
                return True
            else:
                self.grid[row][i] = " "
        return False
    
