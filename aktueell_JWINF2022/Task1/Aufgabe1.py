

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
vokale = ["a","e","i","o","u","ä","ö","ü","A","E","I","O","U","Ä","Ö","Ü"]


#Die drei Regeln
def checkIfReim(wort1,wort2):
    statement = False




    vokaleListeFuerWort1 = []
    vokaleListeFuerWort2 = []
    vordererBuchstabeFuerWort1 = ""
    vordererBuchstabeFuerWort2 = ""
    counter = 0
    #--------------------------------------Wort1----------------------------------------------------------------------
    for einVokal in vokale:
        for oneletter in wort1:
            if oneletter == einVokal:

                if vordererBuchstabeFuerWort1 == "e" and einVokal == "u" or einVokal == "i":
                    vokaleListeFuerWort1.append(vordererBuchstabeFuerWort1 + einVokal)
                elif vordererBuchstabeFuerWort1 == "a" and einVokal == "i" or einVokal == "u":
                    vokaleListeFuerWort1.append(vordererBuchstabeFuerWort1 + einVokal)
                elif vordererBuchstabeFuerWort1 == "ä" and einVokal == "u":
                    vokaleListeFuerWort1.append(vordererBuchstabeFuerWort1 + einVokal)
                elif vordererBuchstabeFuerWort1 == "E" and einVokal == "u" or einVokal == "i":
                    vokaleListeFuerWort1.append(vordererBuchstabeFuerWort1 + einVokal)
                elif vordererBuchstabeFuerWort1 == "A" and einVokal == "i" or einVokal == "u":
                    vokaleListeFuerWort1.append(vordererBuchstabeFuerWort1 + einVokal)
                elif vordererBuchstabeFuerWort1 == "Ä" and einVokal == "u":
                    vokaleListeFuerWort1.append(vordererBuchstabeFuerWort1 + einVokal)
                else:
                    vokaleListeFuerWort1.append(einVokal)
        #            if wort1[counter] + 1 ==






    print(vokaleListeFuerWort1)
    counter += 1





print(checkIfReim("Taifun","schule"))



























