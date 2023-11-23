import random
from random import *
#difficulty = input("Leicht oder Mittel oder Schwer:")



def generateEmptyField(rechteckHoehe,rechteckBreite):#<- Generiert ein leeres Feld
    emptyField = []
    for i in range(0,rechteckHoehe):
        emptyField.append([])

    for i in range(0,rechteckHoehe):
        for j in range(0,rechteckBreite):
            emptyField[i].append("")

    for line in emptyField:
        print(line)
    return emptyField


def checkWordsFit(rechteckHoehe,rechteckBreite,wortliste):
    for word in wortliste:
        laengsteSeite = 0
        if rechteckHoehe > rechteckBreite:
            laengsteSeite = rechteckHoehe
        else:
            laengsteSeite = rechteckBreite
        if len(word) > laengsteSeite:
            return False
        rechteckFlaeche = rechteckHoehe * rechteckBreite
        buchstabenZaehler = 0
        verwendeteBuchstaben = []


        for wort in wortliste:
            for letter in wort:
                if letter not in verwendeteBuchstaben:
                    verwendeteBuchstaben.append(letter)
                    buchstabenZaehler += 1
        if rechteckFlaeche < buchstabenZaehler:
            return False

    return True





def wordRandomizer(wortliste,diffuclty,rechteckHoehe,rechteckBreite):
    resultField = generateEmptyField(rechteckHoehe,rechteckBreite)
    wortliste.sort(reverse=True)
    print(checkWordsFit(rechteckHoehe,rechteckBreite,wortliste))
    wort = wortliste[0]
    print("-------------------------------Ausgaben über diese sind nur Tests---------------------------")
    richtung, wortposition = positioningLetters(rechteckBreite, rechteckHoehe, wort, wortliste)
    isPlacetaken = False


    if richtung == "senkrecht":

        for i in range(0,len(wort)):

            resultField[i][wortposition[0]] = wort[i]

    if richtung == "waagrecht":

        for i in range(0,len(wort)):
            resultField[wortposition[0]][i] = wort[i]

    if richtung == "diagonal":
        if not rechteckHoehe - len(wort) == 0 and rechteckBreite - len(wort) == 0:


            for i in range(0,len(wort)):
                resultField[wortposition[0] + i][i] = wort[i]
        else:
            wortposition[0] = 0
            wortposition[1] = 0

            for i in range(0,len(wort)):
                resultField[wortposition[0] + i][i] = wort[i]
    for line in resultField:
        print(line)


def positioningLetters(rechteckBreite, rechteckHoehe, wort, wortliste):
    richtungen = ["senkrecht", "waagrecht", "diagonal"]
    wortposition = [0, 0]  # x,y
    if rechteckHoehe - len(wort) < 0 and rechteckBreite - len(wort) < 0:
        print("Das folgende Wort ist ungültig:" + wort + ", weshalb das Wort nicht eingetragen werden konnte.")
        wortliste.remove(wort)




    else:
        if rechteckHoehe - len(wort) > -1:
            wortposition[1] = randint(0, rechteckHoehe - 2)


        else:
            wortposition[1] = randint(0, rechteckHoehe - 2)
            richtungen.remove("senkrecht")
            richtungen.remove("diagonal")

        if rechteckBreite - len(wort) > -1:
            wortposition[0] = randint(0, rechteckBreite - 2)


        else:
            richtungen.remove("waagrecht")
            richtungen.remove("diagonal")
            wortposition[0] = randint(0, rechteckBreite - 2)
    richtung = choice(richtungen)
    print(richtung)
    print(wortposition)
    return richtung, wortposition


wortliste = ["sus","Rad","wild"]
wordRandomizer(wortliste,"Leicht",4,4)

