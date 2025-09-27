import tkinter as tk
from tkinter import messagebox

board = [
    [0, 0, 5, 2, 6, 0, 7, 0, 1],
    [6, 8, 9, 6, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 6, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]


def is_valid(board, num, pos):
    # Checks the row.
    row = board[pos[0]]
    if num in row:
        return False 
    
    # Checks the column.
    column_check = []
    for i in range(9):
        column_check.append(board[i][pos[1]])

    if num in column_check:
        return False
         
    # Checks the 3×3 box.
    box_row = (pos[0] // 3)  
    box_column = (pos[1] // 3) 

    start_row = box_row * 3 
    start_column = box_column * 3

    for i in range(start_row, start_row+3):
        for j in range(start_column, start_column+3):
            if board[i][j] == num:
                return False 

    return True 

def find_empty_cells(board):
    """
    Returns the row and column of an empty cell.
    """
    # Iterating over rows
    for i in range(len(board)):
        # Iterating over columns
        for j in range(len(board[0])):
            if board[i][j] == 0:
                # Checking if row and column value hold 0, if True then return the row and column
                return (i, j)
            
    return None 


def solve(board):
    # First looking if any empty cell present in the board
    is_empty_cell = find_empty_cells(board)
    if not is_empty_cell:
        # If none of the empty cells are found return True
        return True

    solved = False 

    for num in range(1,10): # Trying numbers between [1-9]
        if is_valid(board, num, is_empty_cell): # Checking if the positiion of the number is valid to be plaaced
            board[is_empty_cell[0]][is_empty_cell[1]] = num # If True substitute the number in the empty place
            solved = solve(board) # Function is recursively called, after the num is placed looking for further row , col where 0 is present and substiuting numbers from 1 to 9 in that cell
            if solved:
                return True

            board[is_empty_cell[0]][is_empty_cell[1]] = 0

    return False 
    
def print_board(board):
    """
    Prints the Sudoku board in a readable format.
    """
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(num)
            else:
                print(str(num) + " ", end="")

if __name__ == "__main__":
    print("Original Board: ")
    print_board(board)
    print("===============================================")
    print("\nSolved Board")
    solve(board)
    print_board(board)
