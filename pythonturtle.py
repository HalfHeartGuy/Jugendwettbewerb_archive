import turtle



#Aufgabe 1

#Methodename:berechnenLandnahme
#Eingabe:eine Liste von Koordinaten (Set mit 4 interger)
#[(2.3.5.5), (1,2,4,4) , (3,1,6,3)]
#[(2,3.5.5), (1,2,4,4) , (3,1,6,3)]
#Ausgabe:eine Liste von Koordinaten (Set mit 4 interger)
#print (2,3,5,5) genehmigt/abgelehnt


#Schritt 1 mit einer Methode zu überprüfen ob 2 Rechtecken sich überschneiden.
##Methodename:hatUeberschneidung
#Eingabe:2 Set/Liste mit jeweils 4 int
##Ausgabe: true/false
list = [(1,2,3,5), (2,2,3,5), (3,2,3,5)]
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
#Fall1:Oben rechts Ecke vom rechteck1 ist innerhalb rechteck2
#Fall2:Unten linke ecke vom rechteck1 ist innerhalb rechteck2
#Fall3:Oben links Ecke von Rechteck2 ist innerhalb Rechteck1
#Fall4:Unten Rechts Ecke von Rechteck2 ist innerhalb Rechteck1
#Fall 5:Beide Ecken von Rechteck 2 sind außerhalb vom rechteck1.
#Fall6:Beide Ecken von Rechteck 2 sind außerhalb rechteck1.
def berecheneLandnahme(kordinatenliste):
    resultdic = {}
    dictionary = {}
    for onerechteck in kordinatenliste:

        dictionary[onerechteck]=True

        for vierecke in dictionary.keys():

            Status = hatUeberschneidung(vierecke,onerechteck)
            if Status:
                dictionary[onerechteck]=False
                resultdic[onerechteck] = False
                dictionary.popitem()
                break
            else:
                resultdic[onerechteck] = True
                break

    return resultdic





resultdic = berecheneLandnahme([(2,3,5,5),(1,2,4,4),(3,1,6,3),(2,5,7,8),(9,10,13,14)])
"""
    if rechteck2Y2 < rechteck1_groesster_y and rechteck2Y2 > rechteck1_kleinster_y:
        rechteck2X2 = rechteck2[2]
        if rechteck2X2 < rechteck1_groesster_x and rechteck2X2 > rechteck1_kleinster_x:

            return False
    elif Rechteck2X1 < rechteck1_groesster_x and Rechteck2X1 > rechteck1_kleinster_x:
        rechteck2Y1 = rechteck2[1]
        if rechteck2Y1 < rechteck1_groesster_y and rechteck2Y1 > rechteck1_kleinster_y:
            return False
    else:
        return True
"""
#Schritt 2:vergleich ein Rechtecken mit vorherigen(mit Statusspeicherung)
#[(1,2,3,5):True, (3,2,1,5):False, ....,]


#for eachRechteck in list

"""
dict = {}

for eachRechteck in list:

    for oneRechteck in dict.keys():
        if dict.get(oneRechteck):
            hatUeberschneidung = hatUeberschneidung(eachRechteck,oneRechteck)


dict2 = {"key1":True , "key2":False}
"""



def drawsquare(coordinates,statement):



    turtle.penup()
    turtle.goto(coordinates[0] * 10, coordinates[1] * 10)
    turtle.begin_fill()
    turtle.pendown()
    for i in range(0,2):
        turtle.forward(coordinates[2] * 10 - coordinates[0] * 10)

        turtle.left(90)
        turtle.forward(coordinates[3] * 10 - coordinates[1] * 10)
        turtle.left(90)

    if statement == False:
        turtle.color("red")
        turtle.end_fill()
    else:
        turtle.color("green")
        turtle.end_fill()

def countrycolor(resultdic):
    for oneitem in resultdic:
        drawsquare(oneitem,resultdic[oneitem])
    turtle.done()


countrycolor(resultdic)


