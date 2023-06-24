

import sudoku as sd
oneSudokuMatrix = sd.createOneEmptySudokuMatrix()

print("step 1 createOneEmptySudokuMatrix",oneSudokuMatrix)

#box1
oneSudokuMatrix[0] = sd.createARandom3x3SudukoBox()
#box2
oneSudokuMatrix[4] = sd.createARandom3x3SudukoBox()
#box3
oneSudokuMatrix[8] = sd.createARandom3x3SudukoBox()
#box4
box4 = oneSudokuMatrix[2]
#box 5
box5 = oneSudokuMatrix[1]

#box 6
box6 = oneSudokuMatrix[5]
#box7
box7 = oneSudokuMatrix[7]
#box8
box8 = oneSudokuMatrix[3]
#box9
box9 = oneSudokuMatrix[6]

#all 3 rows in box 4
for row in range(0, 3):
    numberInSameRow = oneSudokuMatrix[0][row*3:row*3 + 3] + oneSudokuMatrix[0][row*3:row*3 + 3]
    numberInSameColumn = [oneSudokuMatrix[8][row], oneSudokuMatrix[8][row + 3], oneSudokuMatrix[8][row + 6]]#no chamge
    numberInSameBox = box4
    box4[row + 6] = sd.createARandomNumber(numberInSameRow, numberInSameColumn, numberInSameBox)
#all 3 rows in box5
for row in range(0, 3):
    numberInSameRow = oneSudokuMatrix[0][row * 3:row * 3 + 3] +  oneSudokuMatrix[2][row * 3:row*3 + 3]
    numberInSameColumn = [oneSudokuMatrix[4][row], oneSudokuMatrix[4][row + 3], oneSudokuMatrix[4][row + 6]]#no chamge
    numberInSameBox = box5
    box5[row + 6] = sd.createARandomNumber(numberInSameRow, numberInSameColumn, numberInSameBox)

#all rows in box 6
for row in range(0, 3):
    numberInSameRow = oneSudokuMatrix[4][row * 3:row*3 + 3]
    numberInSameColumn = [oneSudokuMatrix[2][row], oneSudokuMatrix[2][row + 3], oneSudokuMatrix[2][row + 6],oneSudokuMatrix[8][row], oneSudokuMatrix[2][row + 3], oneSudokuMatrix[2][row + 6]]#no chamge
    numberInSameBox = box6
    box6[row + 6] = sd.createARandomNumber(numberInSameRow, numberInSameColumn, numberInSameBox)
#all rows in box 7
for row in range(0, 3):
    numberInSameRow = oneSudokuMatrix[8][row * 3:row*3 + 3]
    numberInSameColumn = [oneSudokuMatrix[1][row], oneSudokuMatrix[1][row + 3], oneSudokuMatrix[1][row + 6],oneSudokuMatrix[4][row], oneSudokuMatrix[4][row + 3], oneSudokuMatrix[4][row + 6]]#no chamge
    numberInSameBox = box7
    box7[row + 6] = sd.createARandomNumber(numberInSameRow, numberInSameColumn, numberInSameBox)
#all rows in box8
for row in range(0, 3):
    numberInSameRow = oneSudokuMatrix[4][row * 3:row*3 + 3] + oneSudokuMatrix[5][row*3:row*3+3]
    numberInSameColumn = [oneSudokuMatrix[0][row], oneSudokuMatrix[0][row + 3], oneSudokuMatrix[0][row + 6]]#no chamge
    numberInSameBox = box8
    box8[row + 6] = sd.createARandomNumber(numberInSameRow, numberInSameColumn, numberInSameBox)

#all rows in box9
for row in range(0, 3):
    numberInSameRow = oneSudokuMatrix[7][row * 3:row*3 + 3] + oneSudokuMatrix[8][row*3:row*3+3]
    numberInSameColumn = [oneSudokuMatrix[0][row], oneSudokuMatrix[0][row + 3], oneSudokuMatrix[0][row + 6],oneSudokuMatrix[3][row], oneSudokuMatrix[3][row + 3], oneSudokuMatrix[3][row + 6]]#no chamge
    numberInSameBox = box8
    box9[row + 6] = sd.createARandomNumber(numberInSameRow, numberInSameColumn, numberInSameBox)

for row in oneSudokuMatrix:
    print(row)
