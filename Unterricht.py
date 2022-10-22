import random
import projectTurtle
from projectTurtle import *
from random import randint

screen = turtle.getscreen()
screen.clear()
screen.title("Game")
screen.colormode(255)
myTurtle = turtle.Turtle()
myTurtle.reset()


def colors():
    colors = []
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colors.append(r)
    colors.append(g)
    colors.append(b)
    return colors
def candraw2boxes(laenge, hoehe, abstand):
    if laenge > 3 * abstand and hoehe > 2 * abstand:
        return True

    elif laenge > 2 * abstand and hoehe > 3 * abstand:
        return True


    else:
        False


def rechteck(laenge, hoehe, x, y,color):
    myTurtle.penup()
    myTurtle.goto(x, y)
    myTurtle.pendown()
    myTurtle.color((color))
    for i in range(0, 2):
        myTurtle.forward(laenge)
        myTurtle.right(90)
        myTurtle.forward(hoehe)
        myTurtle.right(90)
def rechteck_schoner(abstand,laenge,hoehe,startX,starty,color):

    rechteck(laenge,hoehe,startX,starty,color)
    draw2boxes = candraw2boxes(laenge,hoehe,abstand)
    if draw2boxes:
        start1x = startX + abstand
        start1y = starty - abstand
        if laenge > 3 * abstand:
            laenge1 = random.randint(1,laenge - 3 * abstand)
            hoehe1 = hoehe - 2 * abstand
            start2x = start1x + laenge1 + abstand
            start2y = start1y
            laenge2 = laenge - laenge1 - 3 * abstand
            hoehe2 = hoehe1

        elif laenge > 2 * abstand:
            laenge1 = laenge - 2 * abstand
            hoehe1 = random.randint(1,hoehe - 3 * abstand)
            start2x = start1x
            start2y = start1y - laenge1 - abstand
            hoehe2 = hoehe - hoehe1 - 3
            laenge2 = laenge1
        color = colors()
        rechteck_schoner(abstand,laenge1,hoehe1,start1x,start1y,color)
        rechteck_schoner(abstand,laenge2,hoehe2,start2x,start2y,color)
color = colors()
rechteck_schoner(10,200,400,-100,100,color)