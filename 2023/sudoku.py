sudoku = [
    [0, 0, 4, 0, 0, 3, 0, 0, 7],
    [9, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 1, 0],
    [0, 5, 0, 0, 7, 0, 0, 2, 0],
    [6, 0, 0, 8, 0, 5, 0, 0, 3],
    [0, 1, 0, 0, 3, 0, 0, 9, 0],
    [0, 9, 0, 0, 0, 6, 0, 0, 0],
    [7, 0, 0, 4, 0, 0, 0, 0, 0],
    [2, 0, 0, 6, 0, 0, 9, 0, 0]
]
valid = True


def isDuplicateAvailable(numbers: list):


    zeros = numbers.count(0)

    if len(set(numbers)) != (len(numbers) - zeros) + 1:
        valid = False

        return valid 



def isColumnvalid(mysudoku: list):
    for onelist in mysudoku:
        valid_2 = isDuplicateAvailable(onelist)

    if valid_2 == False:
        return valid_2

    else:
        return True


print(isColumnvalid(sudoku))