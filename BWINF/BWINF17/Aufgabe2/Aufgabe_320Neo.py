

# Schritt 0: Allgemeine Aufgabenbeschreibung
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


def create_empty_dict():
    empty_dict = {}
    for i in range(0,721):
        empty_dict[str(i)] = [-1,-1]
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


# Schritt 1: Berechnung vom Routinplan für 1 angegeben Vogel (wann der Vogel bei welchem Feler vorbei fliegt) von diesem Vogel?
# Datenstruktur für diesen Routinplan: [{"21":(1,1)}, {"22":(1,2)}, {"23":(1,3)}, ...,{"35":(1,14)}, {"36": (1,13)},.., {"50":(1,0)}]
"""
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
                vogel_routen[str(start_zeit+counter)].clear()
                vogel_routen[str(start_zeit+counter)].append(start_x)
                vogel_routen[str(start_zeit+counter)].append(start_y+counter2)
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].clear()

                vogel_routen[str(start_zeit+counter)].append(start_x)
                vogel_routen[str(start_zeit+counter)].append(start_y+counter2)

                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0

       
        return vogel_routen
  
    elif richtung == "we":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].clear()

                vogel_routen[str(start_zeit+counter)].append(start_y)
                vogel_routen[str(start_zeit+counter)].append(start_x+counter2)
                counter += 1
                counter2 += 1
                if counter2 == forest_width-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].clear()

                vogel_routen[str(start_zeit+counter)].append(start_y)
                vogel_routen[str(start_zeit+counter)].append(start_x+counter2)
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        return vogel_routen
    
    elif richtung == "ns":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].clear()

                vogel_routen[str(start_zeit+counter)].append(start_y+counter2)
                vogel_routen[str(start_zeit+counter)].append(start_x)
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].clear()
                vogel_routen[str(start_zeit+counter)].append(start_y+counter2)
                vogel_routen[str(start_zeit+counter)].append(start_x)
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        return vogel_route
    elif richtung == "ew":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].clear()
                vogel_routen[str(start_zeit+counter)].append(start_y)
                vogel_routen[str(start_zeit+counter)].append(start_x-counter2)
                counter += 1
                counter2 += 1
                if counter2 == 0:
                    up_down = 0

            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].clear()
                vogel_routen[str(start_zeit+counter)].append(start_y)
                vogel_routen[str(start_zeit+counter)].append(start_x-counter2)
                counter += 1
                counter2 -= 1
                if counter2 == forest_width-1:
                    up_down = 1
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route
"""

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
                vogel_route.append({str(start_zeit+counter):[start_x, start_y-counter2]})
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y-counter2]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        vogel_route.append({str(720):[start_x, start_y]})   
        return vogel_route
  
    elif richtung == "we":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 += 1
                if counter2 == forest_width-1:
                    up_down = 1
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route
    
    elif richtung == "ns":
        counter2 = 0
        while counter + start_zeit < 720:
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 0

            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 1
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route
    elif richtung == "ew":
        while counter + start_zeit < 720:
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y+counter2]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0

            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y+counter2]})
                counter += 1
                counter2 += 1
                if counter2 == forest_width-1:
                    up_down = 1
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route



startPos = [0,0]
richtung = "we"
startZeit = 20
forest_length = 15
forest_width = 3

einVogelRoute = vogel_routen_Berechner(startPos, richtung, startZeit, forest_length, forest_width)
for i in range(startZeit,721):
    if vogel_routen[str(i)] == [-1,-1]:

        vogel_routen[str(i)].clear()
    vogel_routen[str(i)].append(einVogelRoute[i-startZeit][str(i)])
startPos = [1,14]
richtung = "sn"
startZeit = 20
forest_length = 15
forest_width = 3
einVogelRoute2 = vogel_routen_Berechner(startPos, richtung, startZeit, forest_length, forest_width)
for i in range(startZeit,721):
    if vogel_routen[str(i)] == [-1,-1]:

        vogel_routen[str(i)].clear()
    vogel_routen[str(i)].append(einVogelRoute2[i-startZeit][str(i)])
print(vogel_routen)

#Berechnung wie lange ein Feld wieder von einem Vogel überflogen wird. Dabei den größten Zeitabstand nehmen. Es muss auch noch der Zeitabstand von Sonnenaufgang bis zu den ersten Vogelflug von dem feld berechnet werden.
#Man kann die Anzahl der Vögeln herausfinden, indem man  die Länge der Liste im vogel_routen value nimmt.Anzahl der Vögeln sind beliebig.
#Das Ergebnis sieht folgende Maßen aus:wald_felder_sicherheit_stufe = [[2,0,2],..., [2,0,2]].Die Länge der inneren Liste ist die Breite vom Wald und wie viele Listen es in der Liste gibt ist die Länges des Walds.
#Ob ein Feld unsicher, relativ sicher oder ganz sicher ist ist oben definiert.
#0 steht für unsicher, 1 für relativ sicher und 2 für ganz sicher.
#Ein Feld ist relativ sicher, wenn es am Tag einen sicheren Zeitraum von 30 Minuten gibt, in denen kein Vogel das Feld überblicken kann.
# [[2,0,2],..., [2,0,2]] Es soll ungefähr so ausgegeben werden.
#Gehe dabei folgendermaßen vor.
#Benutze die Liste vogel_routen


#Schreibe zuerst eine Hilfsfunktion, die ein Feld als Eingabe hat und die Sicherheitsstufe als Ausgabe hat.
def calc_feld_sicherheit1Feld(vogel_routen,feld:list):
    #Gehe durch die Liste vogel_routen durch.
    #Nimm die values von diesen Listen.
    #Falls das Feld, das in der Eingabe steht, gar nicht vorkommt, dann ist dann ist das Feld ganz sicher.
    #Falls das Feld, das in der Eingabe steht, vorkommt, dann berechne wie lange ein Feld wieder überflogen wird und nehme dabei den größten Zeitabstand.
    #Wenn der Zeitabstand von einem Feld 30 Minuten oder größer ist, dann ist das Feld relativ sicher.
    #Wenn der Zeitabstand von einem Feld unter 30 Minuten ist, dann ist das Feld unsicher.
    #Welche minute es grad am Tag ist, ist der key von der Liste vogel_routen.
    #Die values von dieser Liste sind die Positionen von den Vögeln.
    begintocount = False
    maxAbstand = 0
    counter = 0
    #Wenn das Feld, das in der Eingabe steht überflogen wird, dann fängt counter an +1 zu zählen und das wiederholt sich und begintocount wird auf True gesetzt.Dann wird nicht mehr gezählt und begintocount wird auf False gesetzt, falls das Feld wieder überflogen wird.
    #Wenn counter > maxAbstand ist, dann setze maxAbstand = counter.
    
    for i in range(0,721):
        for oneFeld in vogel_routen[str(i)]:
            if begintocount == True:
                counter += 1

            if begintocount == True and oneFeld == feld:
                if counter > maxAbstand:
                    maxAbstand = counter
                counter = 0
            
            if oneFeld == feld:
                begintocount = True

    if maxAbstand >= 30:
        return 1
    elif maxAbstand == 0:
        return 2
    elif maxAbstand < 30:
        return 0

        
print(calc_feld_sicherheit1Feld(vogel_routen,[2,10]))


def calc_sicherheitstufe(vogel_routen,forest_length,forest_width,waldfelder):
    #Generiere zuerst eine Liste von den Waldfeldern.
    #Also [[]] Liste in Liste.
    #Die innere Liste ist so lang wie der Wald breit ist.
    #Die Anzahl von den inneren Listen ist forest_width.
    #Setze dort erstmal überall 0 hin.
    wald_felder_sicherheit_stufe = []
    for i in range(forest_length):
        wald_felder_sicherheit_stufe.append([0]*forest_width)
    print(wald_felder_sicherheit_stufe)
    #Dann musst du die Liste vogen_routen durchgehen.
    #Dann die values von diesen Listen nehmen.
    #Berechne wie lang ein Feld wieder überflogen wird und nehme dabei an einem Feld den größten Zeitabstand.Ein Vogel braucht immer 1 Minute um ein Feld zu überfliegen und kann dann diesen anschauen.
    #Wenn der Zeitabstand von einem Feld 30 Minuten ist, dann ist das Feld relativ sicher.
    #Wenn ein Feld gar nicht überflogen wird, dann ist das Feld ganz sicher.
    #Wenn der maximaler Abstand von einem Feld am Tag kleiner als 30 Minuten ist, dann ist das Feld unsicher.
    #Wenn ein Feld unsicher ist, dann setze dort 0 hin.
    #Wenn ein Feld relativ sicher ist, dann setze dort 1 hin.
    #Wenn ein Feld ganz sicher ist, dann setze dort 2 hin.
    #Schreibe zuerst eine Hilfsfunktion, die ein Feld als Eingabe hat und die Sicherheitsstufe als Ausgabe hat.
    
        
    for oneFeld in waldfelder:
        wald_felder_sicherheit_stufe[oneFeld[1]][oneFeld[0]] = calc_feld_sicherheit1Feld(vogel_routen,oneFeld)
    return wald_felder_sicherheit_stufe
    
    

waldfelder = calc_sicherheitstufe(vogel_routen,15,3,calc_forest_felder(15,3))
for oneFeld in waldfelder:
    print(oneFeld)
