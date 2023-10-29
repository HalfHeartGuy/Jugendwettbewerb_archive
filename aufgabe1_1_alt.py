matrix = [
    [1, 0, 2, 4, 0, 0],
    [0, 0, 3, 0, 5, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 2, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 5]
]

def findnumbersinthewalls(matrix,):
    for i in range(0,len(matrix[1])):
        if matrix[0][i] != 0:
            return matrix[0][i]
    for i in range(0,len(matrix[1])):
        if matrix[-1][i] != 0:
            return  matrix[-1][i]
    for i in range(0,len(matrix[1])):
        if matrix[i][0] != 0:
            return matrix[i][0]
    for i in range(0,len(matrix[1])):
        if matrix[i][-1] != 0:
            return matrix[i][-1]

print(findnumbersinthewalls(matrix))

def toconnecttwonumberpairs(obrigefunktionaufruf,matrix):