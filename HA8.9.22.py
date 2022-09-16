
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


dritteSchlange = [{'start': [0, 0], 'stop': [1, 0], 'color': 'orange'}, {'start': [1, 0], 'stop': [2, 0], 'color': 'orange'}
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
    , {'start': [0, 5], 'stop': [0, 6], 'color': 'red'}
    , {'start': [0, 6], 'stop': [0, 7], 'color': 'red'}
    , {'start': [0, 7], 'stop': [1, 7], 'color': 'red'}
    , {'start': [1, 7], 'stop': [1, 6], 'color': 'red'}
    , {'start': [1, 6], 'stop': [1, 5], 'color': 'red'}
    , {'start': [1, 5], 'stop': [1, 4], 'color': 'red'}
    , {'start': [1, 4], 'stop': [2, 4], 'color': 'red'}
    , {'start': [2, 4], 'stop': [3, 4], 'color': 'red'}
    , {'start': [3, 4], 'stop': [4, 4], 'color': 'red'}
    , {'start': [4, 4], 'stop': [5, 4], 'color': 'red'}
    , {'start': [5, 4], 'stop': [6, 4], 'color': 'red'}
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
vierteSchlange =  [{'start': [0, 0], 'stop': [1, 0], 'color': 'orange'}, {'start': [1, 0], 'stop': [2, 0], 'color': 'orange'}
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
    , {'start': [0, 5], 'stop': [0, 6], 'color': 'red'}
    , {'start': [0, 6], 'stop': [0, 7], 'color': 'red'}
    , {'start': [0, 7], 'stop': [1, 7], 'color': 'red'}
    , {'start': [1, 7], 'stop': [2, 7], 'color': 'red'}
    , {'start': [2, 7], 'stop': [3, 7], 'color': 'red'}
    , {'start': [3, 7], 'stop': [4, 7], 'color': 'red'}
    , {'start': [4,7], 'stop': [5, 7], 'color': 'red'}
    , {'start': [5, 7], 'stop': [6, 7], 'color': 'red'}
    , {'start': [6, 7], 'stop': [7, 7], 'color': 'red'}
    , {'start': [7, 7], 'stop': [8, 7], 'color': 'red'}
    , {'start': [8, 7], 'stop': [9, 7], 'color': 'red'}
    , {'start': [9, 7], 'stop': [10, 7], 'color': 'red'}
    , {'start': [10, 7], 'stop': [10, 6], 'color': 'red'}
    , {'start': [10, 6], 'stop': [10, 5], 'color': 'red'}
    , {'start': [10, 5], 'stop': [10, 4], 'color': 'red'}
    , {'start': [10, 4], 'stop': [10, 3], 'color': 'orange'}
    , {'start': [10, 3], 'stop': [10, 2], 'color': 'orange'}
    , {'start': [10, 2], 'stop': [10, 1], 'color': 'orange'}
    , {'start': [10, 1], 'stop': [10, 0], 'color': 'orange'}
    , {'start': [10, 0], 'stop': [9, 0], 'color': 'orange'}
    , {'start': [9, 0], 'stop': [8, 0], 'color': 'orange'}
    , {'start': [8, 0], 'stop': [7, 0], 'color': 'orange'}
    , {'start': [7, 0], 'stop': [7, 1], 'color': 'orange'}
    , {'start': [7, 1], 'stop': [7, 2], 'color': 'orange'}
    , {'start': [7, 2], 'stop': [7, 3], 'color': 'orange'}
    , {'start': [7, 3], 'stop': [8, 3], 'color': 'orange'}
    , {'start': [8, 3], 'stop': [9, 3], 'color': 'orange'}
    , {'start': [9, 3], 'stop': [9, 2], 'color': 'orange'}
    , {'start': [9, 2], 'stop': [9, 1], 'color': 'orange'}
    , {'start': [9, 1], 'stop': [8, 1], 'color': 'orange'}
    , {'start': [8, 1], 'stop': [8, 2], 'color': 'orange'}

                   ]
fuenfteSchlange = [{'start': [-7, 7], 'stop': [-7, 6], 'color': 'orange'}
    ,{'start': [-7, 6], 'stop': [-7, 5], 'color': 'orange'}
    , {'start': [-7, 5], 'stop': [-7, 4], 'color': 'orange'}
    , {'start': [-7, 4], 'stop': [-6, 4], 'color': 'orange'}
    , {'start': [-6, 4], 'stop': [-5, 4], 'color': 'orange'}
    , {'start': [-5, 4], 'stop': [-4, 4], 'color': 'orange'}
    , {'start': [-4, 4], 'stop': [-4, 5], 'color': 'orange'}
    , {'start': [-4, 5], 'stop': [-4, 6], 'color': 'orange'}
    , {'start': [-4, 6], 'stop': [-5, 6], 'color': 'orange'}
    , {'start': [-5, 6], 'stop': [-6, 6], 'color': 'orange'}
    , {'start': [-6, 6], 'stop': [-6, 5], 'color': 'orange'}
    , {'start': [-6, 5], 'stop': [-5, 5], 'color': 'orange'}




    ,{'start': [-7, 7], 'stop': [-6, 7], 'color': 'orange'}
    , {'start': [-6, 7], 'stop': [-5, 7], 'color': 'orange'}
    ,{'start': [-5, 7], 'stop': [-4, 7], 'color': 'orange'}
    ,{'start': [-4, 7], 'stop': [-3, 7], 'color': 'orange'}
    ,{'start': [-3, 7], 'stop': [-2, 7], 'color': 'red'}
    , {'start': [-2, 7], 'stop': [-1, 7], 'color': 'red'}
    , {'start': [-1, 7], 'stop': [0, 7], 'color': 'red'}

    , {'start': [0, 7], 'stop': [1, 7], 'color': 'red'}
    , {'start': [1, 7], 'stop': [2, 7], 'color': 'red'}
    , {'start': [2, 7], 'stop': [3, 7], 'color': 'red'}
    , {'start': [3, 7], 'stop': [4, 7], 'color': 'red'}]







sechsteSchlange = [
    {'start': [-10, 7], 'stop': [-10, 6], 'color': 'orange'}
    ,{'start': [-10, 6], 'stop': [-10, 5], 'color': 'orange'}
    , {'start': [-10, 5], 'stop': [-10, 4], 'color': 'orange'}
    , {'start': [-10, 4], 'stop': [-9, 4], 'color': 'orange'}
    , {'start': [-9, 4], 'stop': [-8, 4], 'color': 'orange'}
    , {'start': [-8, 4], 'stop': [-8, 5], 'color': 'orange'}
    , {'start': [-8, 5], 'stop': [-8, 6], 'color': 'orange'}
    , {'start': [-8, 6], 'stop': [-9, 6], 'color': 'orange'}
    , {'start': [-9, 6], 'stop': [-9, 5], 'color': 'orange'}
    ,{'start': [-10, 7], 'stop': [-9, 7], 'color': 'orange'}
    ,{'start': [-9, 7], 'stop': [-8, 7], 'color': 'orange'}
    , {'start': [-8, 7], 'stop': [-7, 7], 'color': 'orange'}

    ,{'start': [-7, 7], 'stop': [-6, 7], 'color': 'orange'}
    , {'start': [-6, 7], 'stop': [-5, 7], 'color': 'orange'}
    ,{'start': [-5, 7], 'stop': [-4, 7], 'color': 'orange'}
    ,{'start': [-4, 7], 'stop': [-3, 7], 'color': 'orange'}
    ,{'start': [-3, 7], 'stop': [-2, 7], 'color': 'red'}
    , {'start': [-2, 7], 'stop': [-1, 7], 'color': 'red'}
    , {'start': [-1, 7], 'stop': [0, 7], 'color': 'red'}

    , {'start': [0, 7], 'stop': [1, 7], 'color': 'red'}
    , {'start': [1, 7], 'stop': [2, 7], 'color': 'red'}
    , {'start': [2, 7], 'stop': [3, 7], 'color': 'red'}
    , {'start': [3, 7], 'stop': [4, 7], 'color': 'red'}]










def turtledraw(ringelListe:list):

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





turtledraw(sechsteSchlange)
turtle.done()




"""
turtle.reset()

turtle.speed(25)
turtledraw(zweiteSchlange)
time.sleep(3)
turtle.reset()
turtle.speed(25)
turtledraw(dritteSchlange)
time.sleep(3)
turtle.reset()
turtle.speed(25)
turtledraw(vierteSchlange)
time.sleep(3)
turtle.reset()
"""











