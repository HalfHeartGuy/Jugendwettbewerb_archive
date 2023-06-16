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

def fillBox(row, col):
    numbers = random.sample(range(1, 10), 9)
    index = 0

    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if isValidPlacement(row,col,numbers):
                sudoku[i][j] = numbers[index]
                index += 1
            else:

def sudokuGenerator():
    fillBox(0, 0)
    fillBox(3, 3)
    fillBox(6, 6)
   # fillBox(0, 6)f
   # fillBox(0, 3)
   # fillBox(3, 6)
   # fillBox(3, 0)
   # fillBox(6, 0)
   # fillBox(6, 3)


    for row in sudoku:
        print(row)


sudokuGenerator()
