Sudoku Solver in Python

A Python-based Sudoku solver that uses the backtracking algorithm to solve any standard 9×9 Sudoku puzzle. This project demonstrates recursion, logical problem-solving, and Python programming skills.

Features

Solves any 9×9 Sudoku puzzle automatically.

Ensures all Sudoku rules are respected:

No repeated numbers in rows.

No repeated numbers in columns.

No repeated numbers in 3×3 subgrids.

Prints the board in a clean, readable format.

Implements a recursive backtracking algorithm for efficient solving.

Easy to modify for custom puzzles.

Requirements

Python 3.x

No external libraries required; uses standard Python libraries only

Installation

Save the sudoku_solver.py file to your computer.

Run the script using Python:

python sudoku_solver.py

Usage

Define your Sudoku board as a 9×9 2D list, using 0 for empty cells:

board = [
    [0, 0, 5, 2, 6, 0, 7, 0, 1],
    [6, 8, 9, 6, 7, 0, 0, 9, 0],
    ...
]


Run the script. It will display:

The original Sudoku board

The solved Sudoku board

How It Works

The solver uses backtracking, a recursive approach to fill the board:

Finds the next empty cell.

Tries numbers 1 through 9 in that cell.

Checks if the number is valid according to Sudoku rules.

If valid, the number is placed, and the algorithm moves to the next empty cell recursively.

If no number is valid (dead-end), it backtracks to the previous cell and tries the next number.

Repeats until the board is completely solved.

Example

Original Board:

0 0 5 2 6 0 7 0 1
6 8 9 6 7 0 0 9 0
1 9 0 0 0 4 5 0 0
...


Solved Board:

4 3 5 2 6 9 7 8 1
6 8 9 1 7 5 4 3 2
1 9 2 8 3 4 5 6 7
...

Customization

You can replace the board variable with any 9×9 Sudoku puzzle.

Modify the print_board function to adjust the visual format.

Optional: integrate a GUI using Tkinter for interactive solving.

License

This project is available under the MIT License.