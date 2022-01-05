

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


def erstelleZeile(kosonanten,vokale,counter):


    zeile = ""
    einsilbe = erstelleSilbe(kosonanten, vokale)
    for i in range(0,counter):
        zeile = zeile + einsilbe + ""
        if i == (counter - 1) / 2:
            zeile = zeile + "p di"
    return zeile
#Schritt 3;erstelle eine Strophe mit >=2 Zeilen, mit gleichen Anzahl der Silbenwiederholungen in allen Zeiten.Am Ende noch ein "Markiger Call".Methode "erstelleStrophe"

def erstelleStrophe(konsonanten,vokale):

    calls = ["yo man","LOL","Your world is"]
    ungeradeZahl = [3, 4, 6]
    counterforStrophe = random.choice(ungeradeZahl)

    strophe = []
    call = random.choice(calls)
    if counterforStrophe != 1:
        counterforStrophe = counterforStrophe - 1

    for i in range(0,counterforStrophe):

        zeile = erstelleZeile(konsonanten,vokale,counterforStrophe)
        strophe.append(zeile)
    strophe.append(call)
    return strophe








#Schritt 4;erstelle ein Song mit >= 2 Strophen , und entweder gleichen Anzahl von Zeilen,oder mit abwechselnde Anzahl von Zeilen.
def erstelleSong(konsonanten,vokale):
    numbers = [3,4,6]
    counter = random.choice(numbers)
    song = []
    for i in range(0,counter):
        strophe = erstelleStrophe(konsonanten,vokale)
        song.append(strophe)
    return song

song = erstelleSong(konsunanten,vokale)
def printing(song):
    for line in song:
        for oneline in line:
            print(oneline)

printing(song)



