list = [(1,2,3,5), (2,2,3,5), (3,2,3,5)]
result_dictionary = {}


import turtle
turtle.bgcolor("white")
turtle.pencolor("black")
turtle.penup()
#def task():
turtle.speed(2)

def hatUeberschneidung(rechteck1,rechteck2):
    rechteck1_groesster_x = rechteck1[2]
    rechteck1_groesster_y = rechteck1[3]
    rechteck1_kleinster_x = rechteck1[0]
    rechteck1_kleinster_y = rechteck1[1]
    rechteck2Y2 = rechteck2[3]
    Rechteck2X1 = rechteck2[0]
    rechteck2Y1 = rechteck2[1]
    rechteck2X2 = rechteck2[2]

    return (rechteck2Y2 < rechteck1_groesster_y and rechteck2Y2 > rechteck1_kleinster_y and rechteck2X2 < rechteck1_groesster_x and rechteck2X2 > rechteck1_kleinster_x) \
            or(Rechteck2X1 < rechteck1_groesster_x and Rechteck2X1 > rechteck1_kleinster_x and rechteck2Y1 < rechteck1_groesster_y and rechteck2Y1 > rechteck1_kleinster_y) \
            or (Rechteck2X1 < rechteck1_groesster_x and Rechteck2X1 > rechteck1_kleinster_x and rechteck2Y2 < rechteck1_groesster_y and rechteck2Y2 > rechteck1_kleinster_y) \
            or (rechteck2Y2 < rechteck1_groesster_x and rechteck2X2 > rechteck1_kleinster_x and Rechteck2X1 < rechteck1_groesster_y and rechteck2Y1 > rechteck1_kleinster_y)\
            or (rechteck2Y2 > rechteck1_groesster_y and rechteck2Y1 < rechteck1_kleinster_y) and rechteck2X2 < rechteck2X2 and rechteck2X2 > rechteck1_kleinster_x\
            or (rechteck2Y2 > rechteck1_groesster_x and rechteck2Y1 < rechteck1_kleinster_y and Rechteck2X1 < rechteck1_groesster_x and Rechteck2X1 > rechteck1_kleinster_x)\
            or (rechteck2X2 > rechteck1_groesster_x and Rechteck2X1 < rechteck1_kleinster_y and rechteck2Y2 < rechteck1_groesster_y and rechteck2Y2 > rechteck1_kleinster_y)\


def countrycolour(koordinatenliste):
    dictionary = {}
    for onerechteck in dictionary:
        dictionary


"""
for onerechteck in list:

    if len(result_dictionary) == 0:
        turtle.goto(onerechteck[0] * 100, onerechteck[1] * 100)

        for i in range(0,2):
            turtle.pendown()
            turtle.forward(onerechteck[2] * 100 - onerechteck[0] * 100)
            turtle.left(90)
            turtle.forward(onerechteck[3] * 100 - onerechteck[1] * 100)

            turtle.left(90)
"""





#for i in range(0,4):
#    turtle.forward(50)
#    turtle.right(90)

