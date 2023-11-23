
terminTabelle = [["0","0","0","0","0","0","0"],
                 ["?","0","0","?","?","0","0"],
                 ["X","X","X","?","X","X","X"],
                 ["X","?","?","?","X","?","X"],
                 ["0","?","X","X","?","0","0"],
                 ["?","X","?","X","0","?","?"]]

terminTabelle2 = [["0","0","0","0","0"],
                  ["?","?","X","X","?"],
                  ["X","?","?","?","?"],
                  ["X","X","0","?","?"],
                  ["X","0","0","?","?"]]


terminTabelle3 = [["0","?","0","0","0","0","0","0","0","0"],
                  ["X","X","X","0","?","?","X","0","0","?"],
                  ["?","?","0","0","?","?","?","0","0","?"],
                  ["X","X","X","?","X","?","?","X","?","?"],
                  ["?","?","?","?","X","X","?","?","X","?"],
                  ["?","?","X","0","?","?","?","?","?","X"],
                  ["X","?","X","0","X","X","X","X","0","X"],
                  ["?","X","?","0","X","?","X","?","X","X"]
                ]

terminTabelle4 = [["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
                  ["0","0","?","?","0","X","?","?","X","?","X","X","?","X","0","X","?","X","X","?"],
                  ["X","X","?","0","?","?","?","0","X","?","0","?","?","?","X","0","0","X","X","?"],
                  ["?","?","0","?","X","X","X","X","?","?","?","X","?","?","?","?","?","0","?","X"],
                  ["X","X","?","?","X","0","0","X","0","0","?","X","X","?","X","?","0","?","?","X"],
                  ["?","X","?","?","X","?","X","X","?","X","?","X","X","?","?","?","?","0","X","0"],
                  ["0","X","X","?","?","?","?","?","0","?","?","?","?","X","X","?","?","X","?","0"],
                  ["?","?","X","X","?","?","?","X","0","?","0","?","?","?","X","?","?","0","0","?"],
                  ["0","0","X","?","X","0","?","X","X","?","?","X","?","?","X","0","?","X","0","?"],
                  ["?","?","?","?","0","?","?","?","?","?","?","?","?","X","?","?","?","X","X","X"],
                  ["X","?","?","?","X","?","?","?","0","X","?","X","0","?","0","?","0","0","X","0"],
                  ["X","?","?","X","?","?","0","?","X","?","?","?","X","?","?","0","?","0","X","0"],
                  ["0","?","0","?","X","?","?","X","X","?","0","0","?","?","?","?","?","0","?","?"],
                  ["0","?","X","?","?","?","?","X","?","X","?","X","X","?","?","?","X","?","0","X"]
]

def otherbetterday(spalte,zeile,termintabelle):
    bestday = termintabelle[zeile][spalte]
    if bestday == "X":
        if "0" or "?" in termintabelle[zeile]:
            return False
        else:
            return True

    elif bestday == "?":
        if "0" in termintabelle[zeile]:
            return False
        else:
            return True

    else:
        return True


def terminplaner(termintabelle):

    terminVeraenderung_tage = []
    for i in range(0,len(termintabelle[0])):#Diese for-Schleife ist für die Spalten der Tabelle
        counter = 0
        for j in range(0,len(termintabelle)):#Zeile



            if otherbetterday(i,j,termintabelle) == False:
                counter += 1
        terminVeraenderung_tage.append(counter)

    return terminVeraenderung_tage


def messageGenerator():
    allday = terminplaner(terminTabelle4)
    bestday = min(allday)
    bestdays = []
    print(allday)

    counter = 0
    while counter < len(allday) - 1:
        if allday[counter] == bestday:
            bestdays.append(counter + 1)

        counter += 1
    bestdays = str(bestdays)
    print("Die besten Tage ist/sind: " + str(bestdays[1:-1]) + ".Tag. Es müsste(n) " + str(bestday) + " Termin verändert werden." )

messageGenerator()



#Es bleibt Datei 4 und 5
#2. Ein Aufruf alle 6 Tests
#3. Dokumentiation

