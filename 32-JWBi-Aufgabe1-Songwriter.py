

import random
from random import randint
#Design "Songwriter"
#Eingabe:eine Liste "KonsunantenUndVokale",Ausgabe:Songtext "mehrere Strophen"
#Schritt 1:erstelle eine Silbe mit der Eingabe "KomsunantenUndVokale","erstelleSilbe"


vokale = ["u","a"]
konsunanten = ["s","b"]
def erstelleSilbe (konsunanten,vokale):
    vokale = vokale[random.randint(0,len(konsunanten)) - 1]
    konsonant = konsunanten[random.randint(0,len(konsunanten)) - 1]
    silbe = konsonant + vokale

    return silbe

#silbe = erstelleSilbe(konsunanten,vokale)
#print(silbe)










#Schritt 2:erstelle eine Zeile mit ungeraden Anzahl von Silben,die gleich sind. Methode "erstelleZeile"


def erstelleZeile(kosonanten,vokale):
    ungeradeZahl = [1,3,5,7]
    counter = random.choice(ungeradeZahl)
    zeile = ""
    einsilbe = erstelleSilbe(kosonanten, vokale)
    for i in range(0,counter):
        zeile = zeile + einsilbe + ""
        if i == (counter - 1) / 2:
            zeile = zeile + "p di"
    return zeile
zeile = erstelleZeile(konsunanten,vokale)
print(zeile)
#Schritt 3;erstelle eine Strophe mit >=2 Zeilen, mit gleichen Anzahl der Silbenwiederholungen in allen Zeiten.Am Ende noch ein "Markiger Call".Methode "erstelleStrophe"
#Schritt 4;erstelle ein Song mit >= 2 Strophen , und entweder gleichen Anzahl von Zeilen,oder mit abwechselnde Anzahl von Zeilen.

