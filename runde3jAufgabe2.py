
def bildeinlesen(fName :str):
    f = open(fName, encoding = "utf-8")
    magicNumber = f.readline().splitlines()
    size_x, size_y = f.readline().split()
    max = f.readline().splitlines()
    body = f.read().splitlines()
    f.close()

    img = []
    row = []
    body = [[int(x) for x in row.split()] for row in body]
    for i in range(len(body)):
        for j in range(0 ,len(body[i]) ,3):
            row.append(([body[i][j] ,body[i][ j +1], body[i][ j +2]]))
            if (len(row) == int(size_x)):
                img.append(row)
                row = []
    return img,row,body


message = ""
coordinates = [0 ,0]


# this function reads a message and a nunmber, and converts the number into ascii code and adds it to the message.
def messageAdder(message ,numberforascii):
    adderletter = chr(numberforascii)
    message = message + adderletter
    return message


# This function calculates new coordinates

def calcnewCoordinates(origCoords :list ,newCoords :list ,maxWidth :int ,maxHeight :int):
    origX = origCoords[0]
    origY = origCoords[1]
    newX = newCoords[0] - newCoords[0] // maxWidth * maxWidth
    newY = newCoords[1] - newCoords[1] // maxHeight * maxHeight

    if newX == 0 and newY == 0:
        return 0 ,0

    if origX + newX >= maxWidth:
        newX = newX - (maxWidth - origX)
        origX = 0
    if origY + newY >= maxHeight:
        newY = newY - (maxHeight - origY)
        origY = 0
    return origX + newX , origY + newY


# Diese Funktion liest ein Bild ein, sucht die Pixeln und anhand der Pixeln generiert dieses Programm eine Nachricht
def messageGenerator(imgList ,message):
    currentX = 0
    currentY = 0
    counter = 0
    while message[-2:] != ";§":

        rgbPixel = imgList[currentY][currentX]

        numberforASCII = rgbPixel[0]
        g_X ,b_Y = rgbPixel[1] ,rgbPixel[2]
        message = messageAdder(message ,numberforASCII)
        currentX ,currentY = calcnewCoordinates([currentX ,currentY] ,[g_X ,b_Y] ,len(imgList[0]) ,len(imgList))

        if currentX == 0 and currentY == 0:
            return message


# a function that puts a text into a file
def texttofile(message ,fname):
    with open(fname, 'w') as file:

        file.write(message)



for i in range(1 ,2):
    img ,row ,body = bildeinlesen(f"bild0{i}.ppm")
    print(img[0][0])

    texttofile(messageGenerator(img ,"") ,f"file{i}.txt")