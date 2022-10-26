def checkifReim(wort1,wort2):
    ifReim = True
    vokaleausWort1 = vokaelauseinenWort(wort1)
    vokaleausWort2 = vokaelauseinenWort(wort2)
    #bei doppellauten ist die Zahl dahinter um 1 erhöht also auf die zweite Buchstabe bezogen.
    splitetdVokaleAusWort1 = []
    for oneitem in vokaleausWort1:
        splitetdVokaleAusWort1.append(oneitem.split(" "))
    splitetdVokaleAusWort2 = []
    for oneitem in vokaleausWort2:
        splitetdVokaleAusWort2.append(oneitem.split(" "))





    #Es würde sich ja nicht reimen wenn eines der beiden Wörter nur ein Vokal und das andere Wort mehrere Vokale.
    if len(vokaleausWort1) == 1 and len(vokaleausWort2) == 1:


        if splitetdVokaleAusWort1[0][1] == splitetdVokaleAusWort2[0][1]:
            for i in range(int(splitetdVokaleAusWort1[0][1]),len(wort1) - 1):
                if wort1[i] != wort2[i]:
                    ifReim = False

                    return str(wort1) + " und " + str(wort2) + " reimen sich nicht"







    elif len(vokaleausWort1) > 1 and len(vokaleausWort2) > 1:

        if splitetdVokaleAusWort1[1][1] == splitetdVokaleAusWort2[1][1]:
            for i in range(int(splitetdVokaleAusWort1[1][1]),len(wort1) - 1):
                if wort1[i] != wort2[i]:
                    ifReim = False
                    return str(wort1) + " und " + str(wort2) + " reimen sich nicht"


#------------Regel 2---------------------


    if len(wort1) > len(wort2):
        shortestWord = wort2
        longestWord = wort1
    else:
        shortestWord = wort1
        longestWord = wort2

    shortestWordExtra = shortestWord
    longestWordExtra = longestWord

    counter = 0
    for i in range(-1,-1 * len(shortestWord),-1):
        if shortestWordExtra[i] == longestWordExtra[i]:
            counter += 1
    if counter < len(shortestWord) / 2:
        ifReim = False
        return str(wort1) + " und " + str(wort2) + " reimen sich nicht"





    #------------Regel3-------------------------

    ifwortinwort = longestWord.find(shortestWord)
    if len(longestWord) - len(shortestWord) == ifwortinwort:
        ifReim = False
        return str(wort1) + " und " + str(wort2) + " reimen sich nicht"







    if ifReim == True:
        return str(wort1) + " und " + str(wort2) + " reimen sich."







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





wort1 = "singen"
wort2 = "klingen"
print(checkifReim(wort1,wort2))