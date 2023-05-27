
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


valid = True


def isDuplicateAvailable(numbers: list):
    zeros = numbers.count(0)
    print(len(set(numbers)))
    print(len(numbers) - zeros)
    if zeros == 9 or len(set(numbers)) > len(numbers) - zeros:
        return True
    if len(set(numbers)) != (len(numbers) - zeros):
        valid = False
        return valid
    else:
        return True

def isRowValid(mysudoku: list):
    for onelist in mysudoku:
        valid_2 = isDuplicateAvailable(onelist)
        if valid_2 == False:
            return valid_2
    return True

"""
def isColumnValid(mysudoku: list):
    for i in range(0, 9):
        rowList = []
        for j in range(0, 9):
            rowList.append(mysudoku[j][i])
        valid = isDuplicateAvailable(rowList)
        if valid == False:
            return False
    return True

print("Column ist:" , isColumnValid(sudoku))


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

def is3x3BoxValid(_3x3Box:list) -> bool:
    box_values = []
    for row in range(0,3):
        for col in range(0,3):
            box_values.append(_3x3Box[row][col])

    return isDuplicateAvailable(box_values)




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


"""
print(isRowValid([[5,4,0,1,7,2,8,3,9],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]))