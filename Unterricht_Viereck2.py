import projectTurtle
import random

myturtle = turtle.Turtle()
myturtle.reset()













listevonfarben=[]
counter = 0
def getcolors():
    for i in range(0,1000):
        listevonfarben.append(random.randint(1,255))
        listevonfarben.append(random.randint(1,255))
        listevonfarben.append(random.randint(1,255))
    screen = myturtle.getscreen()
    screen.colormode(255)

def Rechteckmalen(länge, höhe, startx,starty,Farbe1,Farbe2,Farbe3):
    myturtle.color(Farbe1,Farbe2,Farbe3)
    myturtle.speed(3)
    myturtle.penup()
    myturtle.goto(startx,starty)
    myturtle.pendown()
    for i in range(0, 2):
        myturtle.forward(länge)
        myturtle.right(90)
        myturtle.forward(höhe)
        myturtle.right(90)
    myturtle.penup()

counter += 1
def possibletodraw2boxes(length,hight,distance):
    if length > distance * 3 and hight > distance * 2:
        return True
    elif length > distance * 2 and hight > distance * 3:
        return True
    else:
        return False


def rechteckschoner(startx, starty, distance, length, hight, mycolor, counter):


    Rechteckmalen(length, hight, startx, starty, mycolor[counter], mycolor[counter + 1], mycolor[counter + 2])
    draw2Kasten = possibletodraw2boxes(length,hight,distance)
    if draw2Kasten:
        if length > distance * 3:
            startxKasten1 = startx + distance
            startyKasten1 = starty - distance
            lengthKasten1 = random.randint(1,length - distance * 3)
            hightKasten1 = hight - distance * 2
            startxKasten2 = startxKasten1 + lengthKasten1 + distance
            startyKasten2 = startyKasten1
            lengthKasten2 = length - lengthKasten1 - distance * 3
            hightKasten2 = hightKasten1
        elif hight > distance * 3:
            startxKasten1 = startx + distance
            startyKasten1 = starty - distance
            lengthKasten1 = length - distance * 2
            hightKasten1 = random.randint(1,hight - distance * 3)
            startxKasten2 = startxKasten1
            startyKasten2 = startyKasten1 - hightKasten1 - distance
            lengthKasten2 = lengthKasten1
            hightKasten2 = hight - hightKasten1 - distance * 3

        counter += 3
        rechteckschoner(startxKasten1, startyKasten1, distance, lengthKasten1, hightKasten1, mycolor, counter)
        rechteckschoner(startxKasten2, startyKasten2, distance, lengthKasten2, hightKasten2, mycolor, counter)










getcolors()
rechteckschoner(-300, 400, 20, 500, 600, listevonfarben, counter)