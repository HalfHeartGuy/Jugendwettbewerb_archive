#Schritt 1:Funktion infinitiv(eingabe Wort),Ausgabe infinitiv vom Wort
#Schritt 2:eine liste erstellen die endungen heißt und alle unterschiedliche Deutsche Verbenendungen reintun.Längste kommen zuerst.
#Schritt 3:Die Liste endungen mit einer forschleife durchgehen.
#Schritt 4:Checken welche Endungen am Ende des Wortes ist.
#Schritt 5:Falls die letzten 4 Buchstaben tete sind dann zwischen e und t trennen.Dann hinten en hinzufügen.
#Schritt 6:Sonst einfach die Endung im Wort finden die Endung entfernen dann mit en erstzen.Falls die letzte Buchstabe e ist dann nur ein n hinter dem e hinzufügen.
#Schritt 7:Vorne falls es ein ge gibt dann ge entfernen.
#Schritt 8:Wort returnen.



def infinitiv(konjugierter_Verb):
    endungen = ["test","est","end","tet","ten","en","et","st","te","t","e"]
    for oneElement in endungen:
        if konjugierter_Verb[-len(oneElement):] == oneElement:
            if konjugierter_Verb[-4:] == "tete":
                konjugierter_Verb = konjugierter_Verb.split("et")
                konjugierter_Verb = konjugierter_Verb[0] + konjugierter_Verb[1]
            else:
                konjugierter_Verb = konjugierter_Verb.replace(oneElement,"")
            if konjugierter_Verb[-1] == "e":
                konjugierter_Verb = konjugierter_Verb + "n"

            elif konjugierter_Verb[-1] != "e":
                konjugierter_Verb = konjugierter_Verb + "en"
            break

    if konjugierter_Verb[-1] != "e" and konjugierter_Verb[-2:] != "en":
        konjugierter_Verb = konjugierter_Verb + "en"
    if konjugierter_Verb[0:2] == "ge":
        konjugierter_Verb = konjugierter_Verb.replace("ge","")

    return konjugierter_Verb


infinitivForm = infinitiv("beendet")
print(infinitivForm)


def test_infinitiv():
    assert infinitiv("sagte") == "sagen"
    assert infinitiv("leitete") == "leiten"
    assert infinitiv("geforscht") == "forschen"
    assert infinitiv("schweigend") == "schweigen"
    assert infinitiv("trag") == "tragen"
    assert infinitiv("forschte") == "forschen"
    assert infinitiv("lüftete") == "lüften"
    assert infinitiv("gemacht") == "machen"
    assert infinitiv("machte") == "machen"