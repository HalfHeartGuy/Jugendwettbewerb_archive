list_1 = ["?","Wald","?","?","?","?","Wald", "See", "?", "Wiese","?","?","?"]
#second list in the yellow box in the pdf file as list

list_2 = ["Wald", "Wald", "Wiese", "Häuser", "Wüste", "Wald", "See", "Wald", "Wiese", "Sumpf", "Wüste", "See", "Häuser"]



#write a  function that is going to check, weather the known elements in list_1 are in the correct order in list_2
def __check_order(list_1:list[str],list_2:list[str])->bool:
    # Schritt 1: Überprüfen, ob die beiden Listen gleich sind.
    for i in range(len(list_1)):
        if list_1[i] != "?" and list_1[i] != list_2[i]:
            return False
    return True




#following function is going to put the first element from the second list to the end of the second list
def __shift_element(list_2:list[str])->list[str]:
    # Schritt 1: Das erste Element aus der zweiten Liste wird ans Ende der zweiten Liste geschoben.
    # Schritt 2: Die zweite Liste wird zurückgegeben.
    first_element = list_2[0]
    list_2.pop(0)
    list_2.append(first_element)
    return list_2





#task in the pdf file (after Junioraufgabe 2)
def vervollstaendige_landkarte(list_mit_luecken:list[str],list_vervollstaendigen:list[str])->list[str]:
    
    # Schritt 1: Überorüfen, ob die beiden Listen gleich sind.
    # Schritt 2: Wenn die Listen nicht gleich sind, dann schieben wir das erste Wort aus der zweiten Liste ans Ende der zweiten Liste
    # Schritt 3: Wiederhole Schritt 1 und Schritt 2, bis die Listen gleich sind.
    counter = 0

    while not __check_order(list_mit_luecken, list_vervollstaendigen):
        counter += 1
        list_vervollstaendigen = __shift_element(list_vervollstaendigen)
    print(counter)
    return list_vervollstaendigen

print(vervollstaendige_landkarte(list_1, list_2))