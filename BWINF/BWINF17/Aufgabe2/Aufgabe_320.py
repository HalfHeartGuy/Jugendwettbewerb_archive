#Generelle Aufgabenstellung:
#Das kleine Eichhörnchen Fritz wohnt im Rechteckwald, einem rechteckigen Gebiet bestehend aus
#Feldern.
#Fritz sucht einen Platz, an dem er seine Wintervorräte
#vergraben kann. Das Vergraben benötigt Zeit, und
#in dieser Zeit darf Fritz nicht von einem Raubvogel
#erspäht werden. Fritz hat bereits ausgekundschaftet,
#wie sich die Raubvögel im Rechteckwald üblicherweise verhalten.
#Ab dem ersten Sonnenstrahl beginnen die Vögel
#nach und nach, über den Wald zu fliegen. Alle fliegen
#parallel zu den Seiten des Waldes. Manche fliegen
#zwischen West- und Ostrand, andere zwischen Nordund Südrand des Waldes hin und her. Dabei halten
#sie nach Beute Ausschau: Sie überblicken kurz das
#Feld, über dem sie sich befinden, und dann fliegen sie
#zum nächsten Feld weiter. Das dauert insgesamt eine
#Minute. Die Sonne scheint genau 12 Stunden. Nur in
#dieser Zeit können die Vögel Beute erspähen.
#Am liebsten hätte Fritz ein absolut sicheres Feld, das
#nie von einem Vogel überblickt wird. Es kann allerdings
#sein, dass es ein solches Feld nicht gibt. Das ist aber
#nicht schlimm, denn Fritz braucht nur 30 Minuten, um
#seine Vorräte zu vergraben. Deswegen genügt ihm auch
#ein sicheres Feld: Ein Feld ist sicher, wenn es am Tag
#einen sicheren Zeitraum von 30 Minuten gibt, in denen
#kein Vogel das Feld überblicken kann.
#Junioraufgabe 2
#Schreibe ein Programm für Fritz. Gegeben sind die
#Größe des Rechteckwaldes, die Anzahl der Vögel und
#für jeden Vogel dessen Startfeld, -zeitpunkt und -flugrichtung. Das Startfeld ist ein Randfeld, und jeder
#Vogel fliegt von dort aus in der gegebenen Richtung
#zum gegenüberliegenden Randfeld und wieder zurück.
#1. Das Programm soll zunächst entscheiden, ob
#es absolut sichere Felder gibt. Wenn ja, soll es
#sie ausgeben.
#2. Außerdem soll das Programm sichere Felder
#finden, falls möglich, und für jedes dieser Felder
#einen sicheren Zeitraum ausgeben. Dazu kann
#das Programm simulieren, wie die Vögel während
#des Tages den Wald überfliegen.
#Das Bild zeigt einen Rechteckwald, der 15 Felder in
#Nord-Süd-Richtung mal 3 Felder in West-Ost-Richtung
#groß ist. Im Bild sind Startzeiten und Flugrichtungen
#der Vögel eingezeichnet. Die absolut sicheren Felder
#sind grün, die sicheren Felder gelb gefärbt.



#Schritt 0:
#Leeres Dictionary erstellen mit key für jede Minute aber ohne values
def create_empty_dict():
    empty_dict = {}
    for i in range(0,720):
        empty_dict[str(i)] = []
    return empty_dict
vogel_routen = create_empty_dict()

#Schritt 0.1:
#Waldfelder
def calc_forest_felder(forest_length,forest_width):
    wald_felder = []
    for i in range(forest_length):
        for j in range(forest_width):
            wald_felder.append([j,i])
    return wald_felder
print(calc_forest_felder(15,3))


# Schritt 1: Berechnung vom Routinplan für 1 angegeben Vogel (wann der Vogel bei welchem Feler vorbei fliegt) von diesem Vogel?
# Datenstruktur für diesen Routinplan: [{"21":(1,1)}, {"22":(1,2)}, {"23":(1,3)}, ...,{"35":(1,14)}, {"36": (1,13)},.., {"50":(1,0)}]
def vogel_routen_Berechner(start_vogel_pos, richtung, start_zeit,forest_length,forest_width):
    vogel_route = []
    start_x = start_vogel_pos[0]
    start_y = start_vogel_pos[1]
    counter = 0
    counter2 = 0
    up_down = 0
    if richtung == "sn":
        while counter + start_zeit < 720:
            while up_down == 0:

                vogel_routen[str(start_zeit+counter)].append([start_x, start_y-counter2])
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].append([start_x, start_y-counter2])
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0

       
        return vogel_routen
  
    elif richtung == "we":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].append([start_x+counter2, start_y])
                counter += 1
                counter2 += 1
                if counter2 == forest_width-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].append([start_x+counter2, start_y])
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        return vogel_routen
    
    elif richtung == "ns":
        while counter + start_zeit < 720:
            while up_down == 0:

                vogel_routen[str(start_zeit+counter)].append([start_x, start_y+counter2])
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].append([start_x, start_y+counter2])
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        return vogel_route
    elif richtung == "ew":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].append([start_x-counter2, start_y])
                counter += 1
                counter2 += 1
                if counter2 == 0:
                    up_down = 0

            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x-counter2, start_y]})
                counter += 1
                counter2 -= 1
                if counter2 == forest_width-1:
                    up_down = 1
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route

vogel1 = vogel_routen_Berechner((1,14), "sn", 20,15,3)
vogel2 = vogel_routen_Berechner((1,0), "we", 20,15,3)
print(vogel1)

#Berechnung wie lange ein Feld wieder von einem Vogel überflogen wird. Dabei den größten Zeitabstand nehmen. Es muss auch noch der Zeitabstand von Sonnenaufgang bis zu den ersten Vogelflug von dem feld berechnet werden.
#Ausgabe ist eine Zahl, die die Zeit in Minuten angibt den Zeitraum wann ein Feld wieder überflogen wird und alle Vögeln müssen berücksichtigt werden und die Anzahl der Vögeln sind beliebig.
#Man kann die Anzahl der Vögeln herausfinden, indem man die Länge der Elemente in der Liste von den Routen von den Vögeln nimmt.
def calc_feld_sicherheit(vogel_routen,feld):
    max_time = 0
    counter = 0
    #Jetzt wird jedes Element in der Liste Vogel_routen durchgegangen. Falls Feld = Element dann wird der counter um 1 erhöht. Wenn der counter bei 1 ist wird angefangen, die Zeit zu berechnen. Wenn dann counter 2 ist hört der timer auf und der timer wird ausgegeben.
    max_time2 = 0
    timer2 = 0
    for i in range(len(vogel_routen)):
        timer2 += 1

        for j in range(len(vogel_routen[str(i)])):

            if list(feld) == vogel_routen[str(i)][j]:
                if counter == 0:
                    max_time2 = timer2 - 1
                counter += 1
            if counter == 1:
                start_time = i
            if counter == 2:
                end_time = i
                if end_time - start_time > max_time:
                    max_time = end_time - start_time
    if max_time2 > max_time:
        return max_time2
    else:
        return max_time
#print(calc_feld_sicherheit(vogel_routen, (1,10)))
"""
leereFelder = []
for i in calc_forest_felder(15,3):
    if calc_feld_sicherheit(vogel_routen, i) < 30:
        leereFelder.append(0)
    elif calc_feld_sicherheit(vogel_routen, i) >= 30:
        leereFelder.append(1)
    else:
        leereFelder.append(2)
print(leereFelder)
"""