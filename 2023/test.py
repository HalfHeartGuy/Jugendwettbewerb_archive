sudoku = [
    [0, 0, 4, 0, 0, 3, 0, 0, 7],
    [9, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 1, 0],
    [0, 5, 0, 0, 7, 0, 0, 2, 0],
    [6, 0, 0, 8, 0, 5, 0, 0, 3],
    [0, 1, 0, 0, 3, 0, 0, 9, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 4, 0, 0, 0, 0, 0],
    [2, 0, 0, 6, 0, 0, 9, 0, 0]
]
valid = True


def isDuplicateAvailable(numbers: list):
    zeros = numbers.count(0)
    if len(set(numbers)) != (len(numbers) - zeros) + 1:
        valid = False
        return valid


def isRowValid(mysudoku: list):
    for onelist in mysudoku:
        valid_2 = isDuplicateAvailable(onelist)
        if valid_2 == False:
            return valid_2
    return True


def isColumnValid(mysudoku: list):
    for i in range(0, 9):
        rowList = []
        for j in range(0, 9):
            rowList.append(mysudoku[j][i])
        valid = isDuplicateAvailable(rowList)
        if valid == False:
            return False
    return True


def isBoxValid(mysudoku: list):
    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            box_values = []
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    box_values.append(mysudoku[row][col])
            valid = isDuplicateAvailable(box_values)
            if valid == False:
                return False
    return True


def isSudokuValid(mysudoku: list):
    valid = isRowValid(mysudoku)
    if valid == False:
        return False
    valid = isColumnValid(mysudoku)
    if valid == False:
        return False
    valid = isBoxValid(mysudoku)
    if valid == False:
        return False
    return True


if isSudokuValid(sudoku):
    print("Das Sudoku-Feld ist gültig.")
else:
    print("Das Sudoku-Feld ist ungültig.")
