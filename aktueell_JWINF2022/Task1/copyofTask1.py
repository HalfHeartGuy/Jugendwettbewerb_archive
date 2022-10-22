




def checkifReim(wort1,wort2):
    vokale = ["a","e","i","o","u","A","E","I","O","U","ä","ü","ö","Ä","Ü","Ö"]
    vokaleListeFuerWort1 = []
    vokaleListeFuerWort2 = []


    #--------Wort1-------------
    #vokale aus Wort 1
    for i in range(len(wort1) - 1,-1,-1):
        ifskip = False

        for oneVokal in vokale:
            if wort1[i] == oneVokal:
                if wort1[i - 1] == "a" or wort1[i - 1] == "A" and wort1[i] == "u":
                    vokaleListeFuerWort1.append(wort1[i - 1] + wort1[i])
                    ifskip = True

                elif wort1[i - 1] == "a" or wort1[i - 1] == "A" and wort1[i] == "i":
                    vokaleListeFuerWort1.append(wort1[i - 1] + wort1[i])
                    ifskip = True


                elif wort1[i - 1] == "e" or wort1[i - 1] == "E" and wort1[i] == "i":
                    vokaleListeFuerWort1.append(wort1[i - 1] + wort1[i])
                    ifskip = True


                elif wort1[i - 1] == "e" or wort1[i - 1] == "E" and wort1[i] == "u":
                    vokaleListeFuerWort1.append(wort1[i - 1] + wort1[i])
                    ifskip = True


                elif wort1[i - 1] == "ä" or wort1[i - 1] == "Ä" and wort1[i] == "u":
                    vokaleListeFuerWort1.append(wort1[i - 1] + wort1[i])
                    ifskip = True



                else:
                    if wort1[i + 1] != "u" and wort1[i + 1] != "i":
                        print(wort1[i + 1])
                        vokaleListeFuerWort1.append(wort1[i])
    print(vokaleListeFuerWort1)











checkifReim("Taifun","Schule")