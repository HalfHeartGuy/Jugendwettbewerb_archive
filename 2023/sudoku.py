import random

sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def isDuplicateInRow(row, number):
    return number in row

def isDuplicateInColumn(col, number):
    for row in sudoku:
        if row[col] == number:
            return True
    return False

def isDuplicateInBox(row, col, number):
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == number:
                return True
    return False

def isValidPlacement(row, column, number):
    return not isDuplicateInRow(sudoku[row], number) and not isDuplicateInColumn(column, number) and not isDuplicateInBox(row, column, number)

def findEmptyCell():
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return None

def solveSudoku():
    cell = findEmptyCell()

    if cell is None:
        return True

    row, col = cell

    for number in random.sample(range(1, 10), 9):
        if isValidPlacement(row, col, number):
            sudoku[row][col] = number

            if solveSudoku():
                return True

            sudoku[row][col] = 0

    return False

def sudokuGenerator():
    if solveSudoku():
        for row in sudoku:
            print(row)


sudokuGenerator()
