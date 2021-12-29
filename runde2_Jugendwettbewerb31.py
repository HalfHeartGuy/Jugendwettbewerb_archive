#Das hier sind alle Deutsche Endungen die nicht wiederholt nicht wiederholt sihd.
#  test est st te tet et t ten en end
#das Ganze muss von den kürzesten bis längsten sein Endungen sein.
#Wenn zwei Endungen gleich lang sind ist es egal in welcher Rheinfolge die beiden stehen
#Schritt2:Eingabe:
#Endungen von kürzesten bis längsten.
#Diese Funktion checkt zuerst die kürzeste Endung.
#Wenn die nicht passt dann sucht es den nächst längeren.
#Die Endung wird in eine Variable gespeichert und die Variable wird returned.
#Ausnahmnefall:
#Wenn eine kürzere Endung und eine längere Endung passen dann wird der längere ausgewählt.

#Die Endung im Wort wird dann durch en ersetzt.
#Ausnahmefall:
#Wenn die letzte Buchstaben ein e ist dann wird nur ein en hinzugefügt.



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


infinitivForm = infinitiv("geforscht")
print(infinitivForm)


def test_infinitiv():
    assert infinitiv("sagte") == "sagen"
    assert infinitiv("leitete") == "leiten"
    assert infinitiv("geforscht") == "forschen"
    assert infinitiv("schweigend") == "schweigen"
    assert infinitiv("trag") == "tragen"