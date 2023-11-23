
openfile = open("bild01.ppm", encoding = "utf-8")
magicNumber = openfile.readline().splitlines()
size_x, size_y = openfile.readline().split()
max = openfile.readline().splitlines()
body = openfile.read().splitlines()
openfile.close()

image = []
row = []
body = [[int(x) for x in row.split()] for row in body]
for i in range(len(body)):
    for j in range(0,len(body[i]),3):
        row.append(([body[i][j],body[i][j+1], body[i][j+2]]))
        if(len(row) == int(size_x)):
            image.append(row)
            row = []
print(image)

def inttostr(integer):
    string = chr(integer)
    return string


def newcoordinates(x,y,g,b,imgwidth,imgheight):
    newxpos = g-g// imgwidth*imgwidth
    newypos = b-b// imgheight*imgheight
    newx = 0
    newy = 0
    if x + newxpos >= imgwidth:
        newx = newxpos - (imgwidth - x)

    else:
        newx = x + newxpos
    if y + newypos >= imgheight:
        newy = newypos - (imgheight - y)
    else:
        newy = y + newypos
    if newxpos == 0 and newypos == 0:
        return  0,0
    return newx,newy



def encoder(image):
    imgwidth = len(image[0])
    imgheight = len(image)
    x = 0
    y = 0
    message = ""
    while 0!=1 :
        message += inttostr(image[y][x][0])

        x,y=newcoordinates(x,y,image[y][x][1],image[y][x][2],imgwidth,imgheight)

        if x == 0 and y == 0:
            break
    return message
print(encoder(image))