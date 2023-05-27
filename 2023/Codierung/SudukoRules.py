

sudoko = [[0,0,0,6,0,7,2,5,3],
          [5,2,8,9,1,3,6,4,7],
          [3,0,0,0,0,0,8,9,1],
          [9,1,4,8,7,6,5,3,2],
          [6,8,5,0,0,0,7,1,9],
          [7,3,2,1,5,9,4,6,8],
          [0,0,0,7,4,1,9,8,6],
          [4,9,1,2,6,8,3,7,5],
          [0,7,0,0,9,0,1,2,4]]



def isDuplicatAvailable(numbers: list) -> bool:
    while 0 in numbers:
        numbers.remove(0)

    return len(numbers) != len(set(numbers))

#print("isDuplicatAvailable:", isDuplicatAvailable([0,1,1,6,0,7,2,5,3]))


def isRowValid(sudoku: list):
    for onelist in sudoku:
        valid_2 = isDuplicatAvailable(onelist)
        if valid_2 == False:
            return valid_2
    return True

def isColumnValid(mySuduko:list) -> bool:
    for i in range(0, 9):
        rowList = []
        for j in range(0, 9):
            rowList.append(sudoko[j][i])
        valid = isDuplicatAvailable(rowList)
        if valid == False:
            return False
    return True


print(isColumnValid(sudoko))

print("isDuplicatAvailable",isDuplicatAvailable([4,9,1,7,6,8,3,7,5]))


# [[1,2,3,4...,7,8,9],...,[2,1,3,4,5,6,7,9,8]] -> [3x3Box_1, 3x3Box_2, ..., 3x3Box_9]
def transferSudukuBoxToSmall3x3Boxes(suduko:list[list]) -> list:
    listOf3x3Boxes = []

    for i in range(0,9,3):
        for j in range(0,9,3):
            _3x3Box = [suduko[row][col] for row in range(i,i+3) for col in range(j,j+3)]
            print(("_3x3Box", _3x3Box))
            listOf3x3Boxes.append(_3x3Box)
    return listOf3x3Boxes

def isSudukuBlockValid(mySuduko:list) ->bool:
    listOf3x3Boxes = transferSudukuBoxToSmall3x3Boxes(mySuduko)
    print(listOf3x3Boxes)

    return not any([isDuplicatAvailable(one3x3Box) for one3x3Box in listOf3x3Boxes])

print("isSudukuBlockValid", isSudukuBlockValid(sudoko))

import random
print("random list:", random.sample([1,2,3,4,5,6,7,8,9], 9))

# return one int number between 1-9, which is NEITHER in column NOR in row.
def createOneRandomCell(column:list, row: list) -> int:
    return random.choice([oneNumber for oneNumber in range(1,10) if oneNumber not  in column and oneNumber not in row])


listA = [2,3,4,6]
listB = [1,5,7]
print("createOneRandomCell:", createOneRandomCell(listA, listB))

# Darstellung1: [[x,x,x], [x,x,x],[x,x,x]]
# Darstellung2: Big Suduku matrx[[x,x,x,0,0,0,0,0,0],
#                                [x,x,x,0,0,0,0,0,0],
#                                [x,x,x,0,0,0,0,0,0],
#                                   ...
#                                [0,0,0,0,0,0,0,0,0]]
# Darstellung3: [x,x,x,x,x,x,x,x]

def createARandom3x3SudukoBox() -> list:
    return random.sample(range(1,10), 9)

def createOneSudukuMatrix() -> list:
    emptySuduku = []
    for x in range(0,9):
        emptySuduku.append([])
        for y in range(0,9):
            emptySuduku[x].append(0)

    print("emptySuduku", emptySuduku)
    return emptySuduku


def sudokuGenerator():

    for i in range(0,9):
        for j in range(0,9):
            randomNumberlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

            sudoko[i][j] = random.sample(randomNumberlist,1)[0]
            valid2 = False

            #print(sudoku)
            while valid2 == False:
                print(randomNumberlist)
                if isSudokuValid(sudoko) == True:
                    valid2 = True

                else:
                    sudoko[i][j] = random.sample(randomNumberlist, 1)[0]
                    randomNumberlist.remove(sudoko[i][j])



createOneSudukuMatrix()