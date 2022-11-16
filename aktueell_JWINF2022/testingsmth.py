#Regel1:findet in Schritt Vokalgruppen aus 1 Wort








vokal = ["a","e","i","o","u"]
#vokalgruppen in eines Wort mit mehr als 1 Vokalgruppen ist das vorletzte,beispiele Vokalgruppen in Wort
#"Taifun" ist "ai".
def getVokalgruppen() -> str:

    vokalgruppen = ""
    return vokalgruppen



#wenn zwei Worte gleiche Vokalgruppen haben,und auch gleichen Zeichen nach dieser Vokalgruppen haben,
#dann heißt es, dass diese zwei Worte "enden gleich"





#Regel2:Anzahl der Buchstaben in diesen "gleichen" Zeichen muss mindestens 50% der Anzehl der gesamten Buchstaben im Wort.
def endenGleich(wort1:str,wort2:str) -> str:
    pass

#Regel 3 ein WOrt darf nicht mit anderen Wort enden
def isWortPaar(wort1:str,wort2:str) -> bool:
    isEndeMitAnderenWort = wort1.endswith(wort2) or wort2.endswith(wort1)

    isWortPaar = isEndeMitAnderenWort and endenGleich(wort1,wort2)
    return isWortPaar

list2d = [[1,2],[5,4],[2,3]]
print(list2d[1][0])