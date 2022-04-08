#Aufgabe 1

#Methodename:berechnenLandnahme
#Eingabe:eine Liste von Koordinaten (Set mit 4 interger)
#[(2.3.5.5), (1,2,4,4) , (3,1,6,3)]
#[(2,3.5.5), (1,2,4,4) , (3,1,6,3)]
#Ausgabe:eine Liste von Koordinaten (Set mit 4 interger)
#print (2,3,5,5) genehmigt/abgelehnt


#Schritt 1 mit einer Methode zu überprüfen ob 2 Rechtecken sich überschneiden.
##Methodename:hatUeberschneidung
#Eingabe:2 Set/Liste mit jeweils 4 int
##Ausgabe: true/false
list = [(1,2,3,5), (2,2,3,5), (3,2,3,5)]
def hatUeberschneidung(rechteck1,rechteck2):
    rechteck1_groesster_x = rechteck1[2]
    rechteck1_groesster_y = rechteck1[3]
    rechteck1_kleinster_x = rechteck1[0]
    rechteck1_kleinster_y = rechteck1[1]
    if rechteck2[3] < rechteck1_groesster_y and rechteck2[3] > rechteck1_kleinster_y:
        if rechteck2[2] < rechteck1_groesster_x and rechteck2[2] > rechteck1_kleinster_x:

            return False
    elif rechteck2[0] < rechteck1_groesster_x and rechteck2[0] > rechteck1_kleinster_x:
        if rechteck2[1] < rechteck1_groesster_y and rechteck2[1] > rechteck1_kleinster_y:
            return False
    else:
        return True

#Schritt 2:vergleich ein Rechtecken mit vorherigen(mit Statusspeicherung)
#[(1,2,3,5):True, (3,2,1,5):False, ....,]


#for eachRechteck in list


dict = {}

for eachRechteck in list:

    for oneRechteck in dict.keys():
        if dict.get(oneRechteck):
            hatUeberschneidung = hatUeberschneidung(eachRechteck,oneRechteck)


dict2 = {"key1":True , "key2":False}

