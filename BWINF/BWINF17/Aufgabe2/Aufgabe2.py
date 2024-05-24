#Aufgabe 2
"""
Laura hat ein langes Regalbrett an ihrer Wand. Sie
möchte es hübscher einräumen. Außer ihren Büchern
sollen auf dem Regal auch vier Deko-Figuren stehen.
Sie überlegt sich, dass sie das Regal mit den
Figuren in fünf Abschnitte unterteilen kann. Diese
Abschnitte möchte sie mit ihren Büchern füllen.
Wie breit die Abschnitte sind, ist ihr egal. Sie
möchte aber, dass die Bücher im selben Abschnitt
alle ungefähr gleich hoch sind. Dazu möchte sie
sicherstellen, dass der Höhenunterschied zwischen
dem größten und dem kleinsten Buch im selben
Abschnitt höchstens 3 cm ist. Ob die Bücher in einem
Abschnitt inhaltlich zusammenpassen, spielt für
Laura keine Rolle. Nach dem Umräumen darf kein
Buch übrig bleiben.
Junioraufgabe 1
Schreibe ein Programm, das berechnet, ob eine Aufstellung der Bücher und Figuren nach Lauras
Wünschen möglich ist. Dein Programm soll auch für
größere Anzahlen von Deko-Figuren funktionieren.
Dazu bekommt es als Eingabe die Anzahl der
Figuren, die Anzahl der Bücher und für jedes Buch
dessen Höhe (in cm). Du kannst davon ausgehen,
dass alle Bücher und die Figuren zusammen auf das
Regal passen.
Gib zunächst aus, ob eine Aufstellung möglich ist.
Wenn ja, gib für jeden Abschnitt die Höhen der Bücher
aus.
Wende dein Programm auf die Beispiele an, die du
auf den BwInf-Webseiten findest.
"""
#Konzept für die Lösung:
#inputs: 
# Anname: Sonneschein fängt um 0 minuten an, bis 720 minuten
# rechteckewald: 3, 15
# Anzahl der Vögeln: 1 
# Sicherheitsstufe: 0 sehr gefährlich(weiß), 1 weniger gefährlich(gelb), 2 sicher(grün)
# wald_felder = [(0,0),(1,0),(2,0), ...., (14,0),(14,1),(14,2)]
# wald_felder_sicherheit_stufe = [2,2,2,...,2,2,2] -> das ist our Ausgabe vom Programm
# 
# "Randfelder" bedeuten Felder, wenn 
# 1. y != 0 und y != 14 dann muss x = 0 oder x = 2 sein  
# 2. x != 0 und x != 2 dann muss y = 0 oder y = 14 sein
# 3. Ecke Felder (0,0), (2,0), (0,14), (2,14)
# 
# Für diesen Vogel: start mit (1,0),  Richtung "sn"(Y-Richtung), fängt mit 20 minuten
# 
# was wäre dann der 
# Schritt 1: Berechnung vom Routinplan für 1 angegeben Vogel (wann der Vogel bei welchem Feler vorbei fliegt) von diesem Vogel?
# Datenstruktur für diesen Routinplan: [{"21":(1,1)}, {"22":(1,2)}, {"23":(1,3)}, ...,{"35":(1,14)}, {"36": (1,13)},.., {"50":(1,0)}]
# Schritt 2: Ausschließen aller "unsicheren" Felder aus wald_felder.



def calc_Randfelder(forest_length,forest_width):
    randfelder = []
    randfelder.append((0,0))
    randfelder.append((0,forest_width-1))
    randfelder.append((forest_length-1,0))
    randfelder.append((forest_length-1,forest_width-1))
    return randfelder


def calc_forest_felder(forest_length,forest_width):
    wald_felder = []
    for i in range(forest_length):
        for j in range(forest_width):
            wald_felder.append([j,i])
    return wald_felder

    

#Der Vogel braucht 1 Minute um ein Feld zu überfliegen und der Vogel soll hin und her fliegen.Er kehrt beim Randfeld um.
def vogel_routen_Berechner(start_vogel_pos, richtung, start_zeit,forest_length,forest_width):
    print(forest_length)
    vogel_route = []
    start_x = start_vogel_pos[0]
    start_y = start_vogel_pos[1]
    counter = 0
    counter2 = 0
    up_down = 0
    if richtung == "sn":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y+counter2]})
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y+counter2]})
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
        while counter + start_zeit < 720:
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0

            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 += 1
                if counter2 == forest_width-1:
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
                if counter2 == forest_length-1:
                    up_down = 1
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route

vogel1 = vogel_routen_Berechner((1,0), "sn", 20, 15, 3)
#for oneelement in vogel1:
 #   print(oneelement)
#Diese Funktion berechnet die Sicherheitsstufe für jedes Feld im Wald.
#Am Anfang ist jedes Feld auf Sicherheitsstufe 2.
#Wenn das Programm merkt, dass ein Vogel überhaupt auf ein Feld fliegt, dann wird die Sicherheitsstufe um 1 verringert..
#Dabei werden die Sicherheitsstufen elemente wie folgendes eingeteilt. Jedes Element wird auf die Koordinaten zugewiesen, wie der Index des Elements in der Koordinatenliste.
def calc_forest_sicherheit(wald_felder, vogel_routen,start_zeit):
    sicherheitsfelder = []
    for i in range(len(wald_felder)):
        sicherheitsfelder.append(2)
    vogel1 = vogel_routen[0]
    for i in range(0,len(wald_felder)):
        for j in range(0,len(vogel1)):
            if vogel1[j][str(start_zeit + j)] == wald_felder[i]:
                sicherheitsfelder[i] = 1
    #Berechen ab hier die Felder, die absolut unsicher sind und zeige die in der sicherheitsfelderliste mit 0 an.Definition von absolut unsicheren Feldern:
    #Wenn ein Feld innerhalb 30 Minuten von 2 Vögeln überflogen wird, dann ist das Feld absolut unsicher.
    """
    for i in range(0,len(wald_felder)):
        counter = 0
        for j in range(0,len(vogel1)):
            if vogel1[j][str(start_zeit + j)] == wald_felder[i]:
                counter += 1
        if counter >= 2:
            sicherheitsfelder[i] = 0
        """
    return sicherheitsfelder    
print(calc_forest_sicherheit(calc_forest_felder(15,3), [vogel1],20))


