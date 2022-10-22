import math
from math import sqrt
from math import floor
#Schritt 1:Eine Funktion die heißt skylineBerechner,mit diese Eingabe.Die Eingabe ist eine Dictionnary.Die Eingabe: z.B ["skyline":(0,0),"Gebäude1":(101,1)

#skyline ist immer bei den Koordinaten 0,0
#schritt 2:Abstand berechnen zwischen skyline und Gebäude
#Schritt 3:Den Abstand geteilt 100.
#schritt 4:Das ganze ergebnis in ein Liste packen




haus1 = [(-80,100),(-20,100),(-20,160),(-80,160)]
haus2 = [(60, 160), (120, 160), (120, 250), (60, 250)]
haus3 = [(-400, 200), (-300, 200), (-300, 300), (-400,300)]
hauser = [haus1,haus2,haus3]




def skylineBerechner(haueser):

    #schritt 1:gehe Liste von haueser durch.
    result = []
    for haus in haueser:
        abstandBerechnerResult = abstandBerechner(haus)
        abstandBerechnerResult = abstandBerechnerResult / 100 + 100
        result.append(floor(abstandBerechnerResult))

    # schritt 2:Für jedes Haus den Abstände zwischen Needle und den nahste Hausaecke.(Wir wolllen den minimal Abstand)
    # Schritt 3:Den minimal Abstand durch 100 teilen und noch mal + 100(ausnahme Fall 0 Meter:max Höhe 99 Meter).
    # schritt 4:Das ganze ergebnis in eine Liste packen und zurückgeben.
    return result
def abstandBerechner(einHaus):
    minimalAbstand = 0
    for oneCorner in einHaus:
        square = sqrt(oneCorner[0] ** 2 + oneCorner[1] ** 2)
        if minimalAbstand > square:
            minimalAbstand = square
        elif minimalAbstand == 0:
            minimalAbstand = square
    print(minimalAbstand)
    return minimalAbstand

print(skylineBerechner(hauser))
