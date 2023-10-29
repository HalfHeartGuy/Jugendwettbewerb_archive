
import turtle


'''


1 0 2 4 x x


0 0 3 0 5 x


0 0 1 0 x x


0 0 0 0 x 4


0 2 0 0 x 0


0 0 0 3 x 5


'''



myNumbers = [
            {"0":1,  "2":2, "3":4},
            {"2":3, "4":5},
            {"2":1, },
            {"5":4},
            {"1":2},
            {"3":3, "5":5}
]
#def call_distance(point1: (int,int), point2: (int,int)) -> int:





#Diese Funktion wandelt das Liste von Dicionary in eine Liste von Liste
def erstelle_matrix_aus_liste(liste_von_woerterbuechern,arukoneLaenge):
    a2dlistmyNumbers = []


    for i in range(0,arukoneLaenge):
        a2dlistmyNumbers.append([])
    for i in range(0,len(liste_von_woerterbuechern)):
        slotswhereNumbers = []
        keys = liste_von_woerterbuechern[i].keys()
        for j in keys:
            slotswhereNumbers.append(j)



        print(slotswhereNumbers)
        for j in range(0,arukoneLaenge):
            if str(j) in slotswhereNumbers:
                oneline = liste_von_woerterbuechern[i]
                a2dlistmyNumbers[i].append(oneline[str(j)])
            else:
                a2dlistmyNumbers[i].append(0)

    return a2dlistmyNumbers


def finde_alle_zahlenpaare(matrix, ziel):
    ziel_positionen = []  # Speichert die Positionen des Zielwerts
    andere_zahlen = {}  # Speichert die Positionen von Zahlen, die nicht das Ziel sind

    # Durchlaufe die Matrix und erfasse die Positionen aller Zahlen
    for i, zeile in enumerate(matrix):
        for j, zahl in enumerate(zeile):
            if zahl == ziel:
                ziel_positionen.append((i, j))
            elif zahl != 0:  # Ignoriere Nullen, da sie nicht als gültige Zahlen betrachtet werden
                if zahl in andere_zahlen:
                    andere_zahlen[zahl].append((i, j))
                else:
                    andere_zahlen[zahl] = [(i, j)]

    # Wenn das Ziel nicht gefunden wurde oder es keine anderen Zahlen gibt, beende die Funktion
    if not ziel_positionen or not andere_zahlen:
        return None

    # Berechnen der Entfernungen für jedes Zahlenpaar
    paar_entfernungen = []  # Liste, die die Zahlen und ihre minimalen Entfernungen speichert

    for zahl, positionen in andere_zahlen.items():
        min_entfernung = float('inf')  # Unendlich
        for pos in positionen:
            for ziel_pos in ziel_positionen:
                # Berechne die "Entfernung" zwischen den Positionen
                entfernung = abs(pos[0] - ziel_pos[0]) + abs(pos[1] - ziel_pos[1])
                if entfernung < min_entfernung:
                    min_entfernung = entfernung

        # Speichere die Zahl mit ihrer minimalen Entfernung
        paar_entfernungen.append((zahl, min_entfernung))

    # Sortiere die Paare basierend auf ihren Entfernungen
    paar_entfernungen.sort(key=lambda x: x[1])

    # Erstelle eine Liste der Zahlen, geordnet nach ihrer Entfernung zur Zielzahl
    geordnete_zahlen = [paar[0] for paar in paar_entfernungen]

    return geordnete_zahlen

# Test der Funktion mit einem Beispiel
matrix = [
    [1, 0, 2, 4, 0, 0],
    [0, 0, 3, 0, 5, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 2, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 5]
]
ziel = 1  # Dies ist die Zahl, die wir in der Matrix suchen

# Finde alle Zahlen, geordnet nach ihrer Nähe zur Zielzahl
resultat = finde_alle_zahlenpaare(matrix, ziel)
print("Geordnete Zahlen basierend auf der Nähe zur Zielzahl:", resultat)

