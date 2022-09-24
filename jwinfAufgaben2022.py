

#Die beiden Worte enden gleich: Sie haben
#dieselbe maßgebliche Vokalgruppe, und nach der
#maßgeblichen Vokalgruppe enthalten beide Wörter
#dieselben Buchstaben in derselben Reihenfolge.
#Dabei ist eine Vokalgruppe eine längstmögliche
#Folge von unmittelbar aufeinanderfolgenden
#Vokalen (z.B. hat das Wort Taifun die Vokalgruppen
#‚ai‘ und ‚u‘), und die maßgebliche Vokalgruppe
#eines Wortes ist seine vorletzte Vokalgruppe, wenn
#das Wort zwei oder mehr Vokalgruppen enthält.
#Enthält ein Wort nur eine Vokalgruppe, ist seine
#maßgebliche Vokalgruppe die eine vorhandene
#Vokalgruppe.

#2.In jedem der beiden Wörter enthält die maßgebliche Vokalgruppe und was ihr folgt mindestens
#die Hälfte der Buchstaben.
#Keines der beiden Wörter darf mit dem kompletten anderen Wort enden.



import math
woerter = ["bemühen","Biene","breitschlagen","glühen","hersagen","Hygiene","Knecht","Recht","Schiene","schlank","Schwank"]
vokale = ["a","e","i","o","u"]


#Die drei Regeln
def checkIfReim(wort1,wort2):
    statement = False
    counter = 0
    if len(wort1) > len(wort2):
        counter = wort1
    else:
        counter = wort2

    # --------------------------1.Regel-------------------------------

    for i in range(1,len(counter)):
        for einVokal in vokale:
            if wort1[i * -1] == einVokal or wort2[i * -1] == einVokal:         #Notiz:Dieser Teil nochmal pberlegen zu bearbeiten.
                return statement
        if wort1[i * -1] != wort2[i * -1]:
            return statement





    alleVokaleInEinenWortFuerWort1 = []
    alleVokaleInEinenWortFuerWort2 = []
    for o in range(0,len(wort1)):
        for einVokalfuerWort1 in vokale:
            if wort1[o] == einVokalfuerWort1:
                alleVokaleInEinenWortFuerWort1.append(wort1[o])
    for o in range(0,len(wort2)):
        for einVokalfuerWort2 in vokale:
            if wort2[o] == einVokalfuerWort2:
                alleVokaleInEinenWortFuerWort2.append(wort2[o])
    #---------------------Vergleich von Vokalen--------------------------------------------
    vergleichFuerWort1 = ""
    vergleichFuerWort2 = ""
    counterForVergleichVonVokalen = 0
    if len(alleVokaleInEinenWortFuerWort1) > len(alleVokaleInEinenWortFuerWort2):
        counterForVergleichVonVokalen = len(alleVokaleInEinenWortFuerWort1)
    else:
        counterForVergleichVonVokalen = len(alleVokaleInEinenWortFuerWort2)
    for j in range(0,counterForVergleichVonVokalen):
        if alleVokaleInEinenWortFuerWort1[i] != alleVokaleInEinenWortFuerWort2[i]:
            return statement


print(checkIfReim("Baum","Traum"))



























