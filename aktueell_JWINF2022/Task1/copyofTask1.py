def checkifReim(wort1,wort2):
    ifReim = True
    vokaleausWort1 = vokaelauseinenWort(wort1)
    vokaleausWort2 = vokaelauseinenWort(wort2)
    #bei doppellauten ist die Zahl dahinter um 1 erhöht also auf die zweite Buchstabe bezogen.
    splitetdVokaleAusWort1 = []
    for oneitem in vokaleausWort1:
        splitetdVokaleAusWort1.append(oneitem.split(" "))
    splitetdVokaleAusWort2 = []



    return vokaleausWort1,vokaleausWort2






#vokale aus einen Wort holen
def vokaelauseinenWort(wort):
    vokale = ["a","e","i","o","u","A","E","I","O","U","ä","ü","ö","Ä","Ü","Ö"]
    vokaleListeFuerWort = []




    for i in range(len(wort) - 1,-1,-1):

        for oneVokal in vokale:
            if wort[i] == oneVokal:
                if wort[i - 1] == "a" or wort[i - 1] == "A" and wort[i] == "u":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))

                elif wort[i - 1] == "a" or wort[i - 1] == "A" and wort[i] == "i":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))

                elif wort[i - 1] == "e" or wort[i - 1] == "E" and wort[i] == "i":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))


                elif wort[i - 1] == "e" or wort[i - 1] == "E" and wort[i] == "u":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))


                elif wort[i - 1] == "ä" or wort[i - 1] == "Ä" and wort[i] == "u":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))

                elif wort[i - 1] == "i" or wort[i - 1] == "I" and wort[i] == "e":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))

                elif wort[i - 1] == "e" or wort[i - 1] == "E" and wort[i] == "e":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))
                elif wort[i - 1] == "a" or wort[i - 1] == "A" and wort[i] == "a":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))
                elif wort[i - 1] == "o" or wort[i - 1] == "O" and wort[i] == "o":
                    vokaleListeFuerWort.append(wort[i - 1] + wort[i] + " " + str(i))







                else:

                    if i + 1 < len(wort):
                        if wort[i + 1] != "u" and wort[i + 1] != "i" and wort[i + 1] != "e":
                            vokaleListeFuerWort.append(wort[i] + " " + str(i))
                    if wort.endswith(oneVokal) and wort[-2] != oneVokal:
                        vokaleListeFuerWort.append(wort[i] + " " + str(i))

    return vokaleListeFuerWort





wort1 = "Bankterrase"
wort2 = "Schwank"
print(checkifReim(wort1,wort2))