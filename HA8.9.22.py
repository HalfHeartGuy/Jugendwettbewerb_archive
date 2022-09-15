
#Dies ist eine Codespar Edition(nicht das originelle)


import turtle
from turtle import *
import time
turtle.speed(25)
turtle.colormode(255)
ersteSchlange =[{'start': [0, 0], 'stop': [1, 0], 'color': 'orange'}, {'start': [1, 0], 'stop': [2, 0], 'color': 'orange'}
    , {'start': [2, 0], 'stop': [3, 0], 'color': 'orange'}
    , {'start': [3, 0], 'stop': [3, 1], 'color': 'orange'}
    , {'start': [3, 1], 'stop': [3, 2], 'color': 'orange'}
    , {'start': [3, 2], 'stop': [3, 3], 'color': 'orange'}
    , {'start': [3, 3], 'stop': [2, 3], 'color': 'orange'}
    , {'start': [2, 3], 'stop': [1, 3], 'color': 'orange'}
    , {'start': [1, 3], 'stop': [1, 2], 'color': 'orange'}
    , {'start': [1, 2], 'stop': [1, 1], 'color': 'orange'}
    , {'start': [1, 1], 'stop': [2, 1], 'color': 'orange'}
    , {'start': [2, 1], 'stop': [2, 2], 'color': 'orange'}
    , {'start': [0, 0], 'stop': [0, 1], 'color': 'orange'}
    , {'start': [0, 1], 'stop': [0, 2], 'color': 'orange'}
    , {'start': [0, 2], 'stop': [0, 3], 'color': 'orange'}
    , {'start': [0, 3], 'stop': [0, 4], 'color': 'orange'}
    , {'start': [0, 4], 'stop': [1, 4], 'color': 'orange'}
    , {'start': [1, 4], 'stop': [2, 4], 'color': 'orange'}
    , {'start': [2, 4], 'stop': [3, 4], 'color': 'orange'}
    , {'start': [3, 4], 'stop': [4, 4], 'color': 'orange'}
    , {'start': [4, 4], 'stop': [5, 4], 'color': 'orange'}
    , {'start': [5, 4], 'stop': [6, 4], 'color': 'orange'}
    , {'start': [6, 4], 'stop': [7, 4], 'color': 'orange'}
    , {'start': [7, 4], 'stop': [8, 4], 'color': 'orange'}
    , {'start': [8, 4], 'stop': [8, 3], 'color': 'orange'}
    , {'start': [8, 3], 'stop': [8, 2], 'color': 'orange'}
    , {'start': [8, 2], 'stop': [8, 1], 'color': 'orange'}
    , {'start': [8, 1], 'stop': [8, 0], 'color': 'orange'}
    , {'start': [8, 0], 'stop': [7, 0], 'color': 'orange'}
    , {'start': [7, 0], 'stop': [6, 0], 'color': 'orange'}
    , {'start': [6, 0], 'stop': [5, 0], 'color': 'orange'}
    , {'start': [5, 0], 'stop': [5, 1], 'color': 'orange'}
    , {'start': [5, 1], 'stop': [5, 2], 'color': 'orange'}
    , {'start': [5, 2], 'stop': [5, 3], 'color': 'orange'}
    , {'start': [5, 3], 'stop': [6, 3], 'color': 'orange'}
    , {'start': [6, 3], 'stop': [7, 3], 'color': 'orange'}
    , {'start': [7, 3], 'stop': [7, 2], 'color': 'orange'}
    , {'start': [7, 2], 'stop': [7, 1], 'color': 'orange'}
    , {'start': [7, 1], 'stop': [6, 1], 'color': 'orange'}
    , {'start': [6, 1], 'stop': [6, 2], 'color': 'orange'}]



zweiteSchlange = [{'start': [0, 0], 'stop': [1, 0], 'color': 'orange'}, {'start': [1, 0], 'stop': [2, 0], 'color': 'orange'}
    , {'start': [2, 0], 'stop': [3, 0], 'color': 'orange'}
    , {'start': [3, 0], 'stop': [3, 1], 'color': 'orange'}
    , {'start': [3, 1], 'stop': [3, 2], 'color': 'orange'}
    , {'start': [3, 2], 'stop': [3, 3], 'color': 'orange'}
    , {'start': [3, 3], 'stop': [2, 3], 'color': 'orange'}
    , {'start': [2, 3], 'stop': [1, 3], 'color': 'orange'}
    , {'start': [1, 3], 'stop': [1, 2], 'color': 'orange'}
    , {'start': [1, 2], 'stop': [1, 1], 'color': 'orange'}
    , {'start': [1, 1], 'stop': [2, 1], 'color': 'orange'}
    , {'start': [2, 1], 'stop': [2, 2], 'color': 'orange'}
    , {'start': [0, 0], 'stop': [0, 1], 'color': 'orange'}
    , {'start': [0, 1], 'stop': [0, 2], 'color': 'orange'}
    , {'start': [0, 2], 'stop': [0, 3], 'color': 'orange'}
    , {'start': [0, 3], 'stop': [0, 4], 'color': 'orange'}
    , {'start': [0, 4], 'stop': [0, 5], 'color': 'red'}
    , {'start': [0, 5], 'stop': [1, 5], 'color': 'red'}
    , {'start': [1, 5], 'stop': [1, 4], 'color': 'red'}
    , {'start': [1, 4], 'stop': [2, 4], 'color': 'red'}
    , {'start': [2, 4], 'stop': [3, 4], 'color': 'orange'}
    , {'start': [3, 4], 'stop': [4, 4], 'color': 'orange'}
    , {'start': [4, 4], 'stop': [5, 4], 'color': 'orange'}
    , {'start': [5, 4], 'stop': [6, 4], 'color': 'orange'}
    , {'start': [6, 4], 'stop': [7, 4], 'color': 'orange'}
    , {'start': [7, 4], 'stop': [8, 4], 'color': 'orange'}
    , {'start': [8, 4], 'stop': [8, 3], 'color': 'orange'}
    , {'start': [8, 3], 'stop': [8, 2], 'color': 'orange'}
    , {'start': [8, 2], 'stop': [8, 1], 'color': 'orange'}
    , {'start': [8, 1], 'stop': [8, 0], 'color': 'orange'}
    , {'start': [8, 0], 'stop': [7, 0], 'color': 'orange'}
    , {'start': [7, 0], 'stop': [6, 0], 'color': 'orange'}
    , {'start': [6, 0], 'stop': [5, 0], 'color': 'orange'}
    , {'start': [5, 0], 'stop': [5, 1], 'color': 'orange'}
    , {'start': [5, 1], 'stop': [5, 2], 'color': 'orange'}
    , {'start': [5, 2], 'stop': [5, 3], 'color': 'orange'}
    , {'start': [5, 3], 'stop': [6, 3], 'color': 'orange'}
    , {'start': [6, 3], 'stop': [7, 3], 'color': 'orange'}
    , {'start': [7, 3], 'stop': [7, 2], 'color': 'orange'}
    , {'start': [7, 2], 'stop': [7, 1], 'color': 'orange'}
    , {'start': [7, 1], 'stop': [6, 1], 'color': 'orange'}
    , {'start': [6, 1], 'stop': [6, 2], 'color': 'orange'}]


dritteSChlange = [{'start': [0, 0], 'stop': [1, 0], 'color': 'orange'}, {'start': [1, 0], 'stop': [2, 0], 'color': 'orange'}
    , {'start': [2, 0], 'stop': [3, 0], 'color': 'orange'}
    , {'start': [3, 0], 'stop': [3, 1], 'color': 'orange'}
    , {'start': [3, 1], 'stop': [3, 2], 'color': 'orange'}
    , {'start': [3, 2], 'stop': [3, 3], 'color': 'orange'}
    , {'start': [3, 3], 'stop': [2, 3], 'color': 'orange'}
    , {'start': [2, 3], 'stop': [1, 3], 'color': 'orange'}
    , {'start': [1, 3], 'stop': [1, 2], 'color': 'orange'}
    , {'start': [1, 2], 'stop': [1, 1], 'color': 'orange'}
    , {'start': [1, 1], 'stop': [2, 1], 'color': 'orange'}
    , {'start': [2, 1], 'stop': [2, 2], 'color': 'orange'}
    , {'start': [0, 0], 'stop': [0, 1], 'color': 'orange'}
    , {'start': [0, 1], 'stop': [0, 2], 'color': 'orange'}
    , {'start': [0, 2], 'stop': [0, 3], 'color': 'orange'}
    , {'start': [0, 3], 'stop': [0, 4], 'color': 'orange'}
    , {'start': [0, 4], 'stop': [0, 5], 'color': 'red'}
    , {'start': [0, 5], 'stop': [1, 5], 'color': 'red'}
    , {'start': [1, 5], 'stop': [1, 4], 'color': 'red'}
    , {'start': [1, 4], 'stop': [2, 4], 'color': 'red'}
    , {'start': [2, 4], 'stop': [3, 4], 'color': 'orange'}
    , {'start': [3, 4], 'stop': [4, 4], 'color': 'orange'}
    , {'start': [4, 4], 'stop': [5, 4], 'color': 'orange'}
    , {'start': [5, 4], 'stop': [6, 4], 'color': 'orange'}
    , {'start': [6, 4], 'stop': [7, 4], 'color': 'orange'}
    , {'start': [7, 4], 'stop': [8, 4], 'color': 'orange'}
    , {'start': [8, 4], 'stop': [8, 3], 'color': 'orange'}
    , {'start': [8, 3], 'stop': [8, 2], 'color': 'orange'}
    , {'start': [8, 2], 'stop': [8, 1], 'color': 'orange'}
    , {'start': [8, 1], 'stop': [8, 0], 'color': 'orange'}
    , {'start': [8, 0], 'stop': [7, 0], 'color': 'orange'}
    , {'start': [7, 0], 'stop': [6, 0], 'color': 'orange'}
    , {'start': [6, 0], 'stop': [5, 0], 'color': 'orange'}
    , {'start': [5, 0], 'stop': [5, 1], 'color': 'orange'}
    , {'start': [5, 1], 'stop': [5, 2], 'color': 'orange'}
    , {'start': [5, 2], 'stop': [5, 3], 'color': 'orange'}
    , {'start': [5, 3], 'stop': [6, 3], 'color': 'orange'}
    , {'start': [6, 3], 'stop': [7, 3], 'color': 'orange'}
    , {'start': [7, 3], 'stop': [7, 2], 'color': 'orange'}
    , {'start': [7, 2], 'stop': [7, 1], 'color': 'orange'}
    , {'start': [7, 1], 'stop': [6, 1], 'color': 'orange'}
    , {'start': [6, 1], 'stop': [6, 2], 'color': 'orange'}]







def turtledraw(ringelListe:list):
    turtle.pensize(10)
    turtle.pendown()
    turtle.color("blue")
    turtle.circle(1)
    turtle.penup()
    groesse = 35
    for oneElement in ringelListe:
        for i in range(0, len(oneElement["stop"])):
            oneElement["start"][i] = oneElement["start"][i] * groesse

            oneElement["stop"][i] = oneElement["stop"][i] * groesse

        turtle.penup()
        turtle.color(oneElement["color"])
        turtle.goto(oneElement["start"])

        turtle.pendown()
        turtle.pensize(10)
        turtle.goto(oneElement["stop"])
        turtle.color("blue")
        turtle.circle(1)





turtledraw(ersteSchlange)
time.sleep(3)
turtle.reset()
"""
turtle.speed(25)
turtledraw(zweiteSchlange)
time.sleep(3)
turtle.reset()
"""










