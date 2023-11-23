import re


def textSearcher(geschichte_dateiname,satzFile):
    geschichtefile = open(geschichte_dateiname + ".txt","r")
    satzfile = open(satzFile + ".txt","r")
    satz = satzfile.readline()

    print(satz)

    geschichte = ""
    for line in geschichtefile:
        geschichte = geschichte + line


    satz = satz.split("_")

    for i in range(0,len(satz)):
        satz[i] = satz[i].strip()
    while "" in satz:
        for wort in satz:
            if wort == "":
                satz.remove(wort)





    command = ""
    for wort in satz:
        command = command + wort + ".*"

    endergebnis1 = []
    result1 = re.findall(command,geschichte)
    for i in range(0, len(result1)):

        if "," in result1[i]:
            zwischenergebnis = result1[i].split(",")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis1.append(j)
                    break
        if "?" in result1[i]:
            zwischenergebnis = result1[i].split("?")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis1.append(j)
                    break
        if "." in result1[i]:
            zwischenergebnis = result1[i].split(".")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis1.append(j)
                    break

        if ";" in result1[i]:
            zwischenergebnis = result1[i].split(";")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis1.append(j)
                    break
        if "!" in result1[i]:
            zwischenergebnis = result1[i].split("!")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis1.append(j)
                    break
    command = command.capitalize()
    result2 = re.findall(command,geschichte)
    endergebnis2 = []
    for i in range(0,len(result2)):


        if "," in result2[i]:
            zwischenergebnis = result2[i].split(",")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis2.append(j)
                    break
        if "?" in result2[i]:
            zwischenergebnis = result2[i].split("?")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis2.append(j)
                    break
        if "." in result2[i]:
            zwischenergebnis = result2[i].split(".")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis2.append(j)
                    break
        if ";" in result2[i]:
            zwischenergebnis = result2[i].split(";")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis2.append(j)
                    break
        if "!" in result2[i]:
            zwischenergebnis = result2[i].split("!")
            for j in zwischenergebnis:
                if satz[0] and satz[1] in j:
                    endergebnis2.append(j)
                    break
    endergebnis = endergebnis1 + endergebnis2

    if endergebnis == []:
        return "Es wurde nichts gefunden."


    geschichtefile.close()
    satzfile.close()
    return endergebnis





moeglicheSaetze = textSearcher("Alice_im_Wunderland","stoerung5")
for line in moeglicheSaetze:
    print(line)

    #test störung 4 nicht richtig(ein _ _ tag)