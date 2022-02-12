import random

from random import randint


"""
    <li>Schritt:Eine Methode schreiben um Brüche zu generieren</li>
    <ul>
        <li>Input:Schwierigkeitsgrad, Bsp:"leicht"</li>
        <li>Output:Bruch, Bsp:55/66</li>






    Stufe Länge von a /b Bedingung für p /q
    leicht 4 p+q ≤ 10
    mittel 5 10 < p+q ≤ 20
    schwer 5 20 < p+q ≤ 30
"""


def bruechegenerieren(schwierigskeitgrad):
    bruch = set()
    if schwierigskeitgrad == "leicht":
        a = random.randint(10,99)
        b = random.randint(10,99)
        bruch.add(a)
        bruch.add(b)
        return bruch


    elif schwierigskeitgrad == "mittel":
        a = random.randint(100, 999)
        b = random.randint(10, 99)
        bruch.add(a)
        bruch.add(b)
        print(bruch)
        return  bruch
    elif schwierigskeitgrad == "schwer":
        a = random.randint(100, 999)
        b = random.randint(10, 99)
        bruch.add(a)
        bruch.add(b)
        print(bruch)
        return  bruch


    else:
        print("what did you expect?")
        print(bruch)
        return  bruch

#Es gibt einen counter dass von 2 anfängt zu zählen.
#Falls der Zähler und der Nenner durch diesen counter teilen können (ohne Rest) dann werden Zähler und Nenner durch den counter dividiert.
#Falls der counter größer ist als den Zähler und den Nenner das heißt dann dass der Bruch vollständig gekürzt ist.
def bruechekuerzen(bruch):
    list_bruch = list(bruch)
    print(list_bruch)
    counter = 1
    while counter < counter + 1:
        counter += 1
        print(counter)

        if list_bruch[0] % counter == 0 and list_bruch[1] % counter == 0:
            list_bruch[0] = list_bruch[0] / counter
            list_bruch[1] = list_bruch[1] / counter
            print(list_bruch)
            counter = 1

        if counter > list_bruch[0] and counter > list_bruch[1]:
            break
        else:

            continue



bruch = bruechegenerieren("leicht")
bruechekuerzen(bruch)