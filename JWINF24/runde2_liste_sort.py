eingabe_liste = ["liebe","Marx","Blut","Mandarine","Klaviert","Qibli"]
ergebnis_liste  = []
#sortiere zuerst die Eingabe Liste nach der Länge der Wörter und wenn die Länge gleich ist, dann alphabetisch ohne .sort()
#Ergebnis: ['Marx', 'liebe', 'Blut', 'Qibli', 'Mandarine', 'Klaviert']



while len(eingabe_liste) > 0:
    #Schritt 1
    kuerzeste_laenge = eingabe_liste[0]
    for wort in eingabe_liste:
        if len(wort) < len(kuerzeste_laenge) or (len(wort) == len(kuerzeste_laenge) and wort < kuerzeste_laenge):
            kuerzeste_laenge = wort
        
    eingabe_liste.remove(kuerzeste_laenge)
    ergebnis_liste.append(kuerzeste_laenge)

print("output_liste: ", ergebnis_liste)
