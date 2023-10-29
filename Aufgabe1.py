def finde_naechste_zahlenpaare(matrix, ziel):
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

    # Gib das nächstgelegene und das zweitnächste Zahlenpaar zurück
    return paar_entfernungen[0][0], paar_entfernungen[1][0] if len(paar_entfernungen) > 1 else None

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

# Finde das nächste und das zweitnächste Zahlenpaar zur Zielzahl
resultat = finde_naechste_zahlenpaare(matrix, ziel)
print("Das nächste Zahlenpaar ist:", resultat[0], "\nDas zweitnächste Zahlenpaar ist:", resultat[1])
