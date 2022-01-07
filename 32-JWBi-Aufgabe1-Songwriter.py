

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


def erstelleZeile(eineSilbe,counter):


    zeile = ""
    for i in range(0,counter):
        zeile = zeile + eineSilbe + ""
        if i == (counter - 1) / 2:
            zeile = zeile + "p di"

    return zeile


#print("eine Zeile:" + erstelleZeile(konsunanten,vokale,7))
#Schritt 3;erstelle eine Strophe mit >=2 Zeilen, mit gleichen Anzahl der Silbenwiederholungen in allen Zeiten.Am Ende noch ein "Markiger Call".Methode "erstelleStrophe"
muster = [3,3,5,6]
markigerCalls = ["cool!","yo!","fake news"]
def erstelleStrophe(konsonanten,vokale,zeileCoutner):
    strophe = ""
    anzahlDerSilbe = 5



    for repeat in range(0, zeileCoutner):
        silberinEinerZeile = erstelleSilbe(konsonanten, vokale)

        strophe = strophe + "\n" + erstelleZeile(silberinEinerZeile, anzahlDerSilbe)
    strophe = strophe + "\n" + random.choice(markigerCalls)
    return strophe

print("erstelleEinStroph:" + erstelleStrophe(konsunanten,vokale,3))









#Schritt 4;erstelle ein Song mit >= 2 Strophen , und entweder gleichen Anzahl von Zeilen,oder mit abwechselnde Anzahl von Zeilen.

def songWriter(konsonanten,vokale):
    numbers = [3 ,4,6]
    counter = random.choice(numbers)
    song = []
    for i in range(0,counter):
        strophe = erstelleStrophe(konsonanten,vokale)
        song.append(strophe)
    return song

song = songWriter(konsunanten,vokale)

#print("ein Song:" + (erstelleSong(konsunanten,vokale)))




