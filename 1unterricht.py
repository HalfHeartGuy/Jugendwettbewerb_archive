import math
from math import *


haus1 = [(-80,100),(-20,100),(-20,160),(-80,160)]
haus2 = [(60, 160), (120, 160), (120, 250), (60, 250)]
haus3 = [(-400, 200), (-300, 200), (-300, 300), (-400,300)]
haeuser = [haus1,haus2,haus3]

#Aufgabe 1: schreibe eine Funktion abstance(point1, point2), die Abstand zwischen 2 Punkten zurückgibt.
#Aufgabe 2: schreibe eine Funktion maxHeight(distance) die maximal höhe von einem Gebäude zurückgibt,
#Aufgabe 3: Für eine vorgegebene Gebaeudeliste = [(-80,100), (-20,10),....], bitte den Abastand zwischen jeweiligem Gebäude und (0,0), und anschließend die max Höhe
# von jeweiligem Gebäude berechnen.



def skylineBerechner(haueser):
    result_for_height = []
    result_for_distance = []
    for haus in haueser:
        abstandBerechnerResult = abstand(haus)
        result_for_distance.append(abstandBerechnerResult)
        max_height = maxHeight(abstandBerechnerResult)
        result_for_height.append(max_height)
    resultforeverything = "maxHeights: " + str(result_for_height) + " distances:" + str(result_for_distance)
    return resultforeverything



def abstand(einHaus):
    minimalAbstand = 0
    for oneCorner in einHaus:
        result = sqrt(oneCorner[0] ** 2 + oneCorner[1] ** 2)
        if minimalAbstand > result:
            minimalAbstand = result
        elif minimalAbstand == 0:
            minimalAbstand = result


    return minimalAbstand

def maxHeight(distance):
    distance = distance / 100 + 100
    return distance


print(skylineBerechner(haeuser))



#------------------------------------------------------------------------------------------
