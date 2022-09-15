#Inhaltsverzeichnis:Zeile 11 - 46 Mathematisch
#Zeile 46-Ende Malen




import turtle
from turtle import *

ringelnListe1 = []
ringelnListe2 = [{'start': [0, 0], 'stop': [0, 1], 'color': 'orange'}, {'start': [0, 1], 'stop': [0, 2], 'color': 'orange'}, {'start': [0, 2], 'stop': [1, 2], 'color': 'red'}, {'start': [2, 2], 'stop': [2, 3], 'color': 'red'}]
#Matheamtisch
"""
def ringel(start:list,stop:list,color):
    einRingel = {}

    if color == "orange":

        einRingel["start"] = start
        einRingel["stop"] = stop
        einRingel["color"] = color
        return einRingel
    if color == "red":
        print(start)
        print(stop)
        if stop[0] == start[0]:
            if (stop[1] - start[1]) * 2 == 2:
                stop[1] += 1
            else:
                stop[1] = (stop[1] - start[1]) * 2

        if stop[1] == start[1]:
            if (stop[0] - start[0]) * 2 == 2:
                stop[0] += 1
            else:
                stop[0] = (stop[0] - start[0]) * 2

        einRingel["start"] = start
        einRingel["stop"] = stop
        einRingel["color"] = color
        return einRingel
    else:
        print("ungültige Eingabe")


eineRingel = ringel([0,0],[1,0],"orange")
ringelnListe1.append(eineRingel)

eineRingel = ringel(eineRingel["stop"],[1,1],"orange")
ringelnListe1.append(eineRingel)
eineRingel = ringel(eineRingel["stop"],[1,2],"red")
ringelnListe1.append(eineRingel)
eineRingel = ringel(eineRingel["stop"],[2,3],"red")
ringelnListe1.append(eineRingel)
#2.Ringel Liste


#Das mit 4 * 2 ist,weil vorher ein roter Ringel war.
#Malen

"""
groesse = 100

def turtledraw(ringelListe:list):






    for oneElement in ringelListe:
        for i in range(0,len(oneElement["stop"])):
            oneElement["stop"][i] = oneElement["stop"][i] * groesse




        turtle.penup()
        turtle.color(oneElement["color"])
        turtle.goto(oneElement["start"])

        turtle.pendown()
        turtle.pensize(10)
        turtle.goto(oneElement["stop"])
        turtle.color("blue")
        turtle.circle(2)

        if oneElement["color"] == "red":
            turtle.penup()
            if 0 == 1:
                print("error")
            elif oneElement["stop"][0] - oneElement["start"][0]:
                print(1)
                turtle.right(180)
                turtle.forward(groesse)
                turtle.color("blue")
                turtle.pendown()
                turtle.circle(2)
                turtle.right(180)
                turtle.penup()
                turtle.forward(groesse)
            elif oneElement["start"][0] - oneElement["stop"][0]:
                print(2)

                turtle.penup()
                turtle.forward(groesse)
                turtle.color("blue")
                turtle.circle(2)
                turtle.right(180)
                turtle.penup()
                turtle.forward(groesse)
                turtle.right(180)
            elif oneElement["stop"][1] - oneElement["start"][1]:
                print("3")

                turtle.right(90)
                turtle.penup()
                turtle.color("blue")
                turtle.forward(groesse)
                turtle.pendown()
                turtle.circle(2)
                turtle.right(180)
                turtle.penup()
                turtle.forward(groesse)
                turtle.right(90)
            elif oneElement["start"][1] - oneElement["stop"][1]:
                print("4")
                turtle.penup()
                turtle.left(90)
                turtle.color("blue")
                turtle.forward(groesse)
                turtle.pendown()
                turtle.circle(2)
                turtle.penup()
                turtle.right(180)
                turtle.forward(groesse)
                turtle.left(90)








turtledraw(ringelnListe2)

turtle.done()










