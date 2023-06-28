

#step 1 create one empty sudoku matrix
def createOneEmptySudokuMatrix() -> list:
    emptySudoku = []
    for x in range(0,9):
        emptySudoku.append([])
        for y in range(0,9):
            emptySudoku[x].append(0)

    return emptySudoku
import random

def createARandom3x3SudukoBox() -> list:
    return random.sample(range(1,10), 9)


def transferSudukuBoxToSmall3x3Boxes(suduko:list[list]) -> list:
    listOf3x3Boxes = []

    for i in range(0,9,3):
        for j in range(0,9,3):
            _3x3Box = [suduko[row][col] for row in range(i,i+3) for col in range(j,j+3)]
            print(("_3x3Box", _3x3Box))
            listOf3x3Boxes.append(_3x3Box)
    return listOf3x3Boxes

def isRowValid(mySuoku:list) -> list:
    pass
def createARandomNumber(availableNumbesinSameRow:list,availableNumbersInSameColumn:list, avaialbleNumbersInSameBox):
    availableNUmbers = availableNumbesinSameRow + availableNumbersInSameColumn + avaialbleNumbersInSameBox
    listOfPossibleNumbers = [oneNumber for oneNumber in range(1,10) if oneNumber not in availableNUmbers]
    return random.choice(listOfPossibleNumbers)

