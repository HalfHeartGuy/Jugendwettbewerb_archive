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
        print(bruch)


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
def bruechekuerzen:




bruechegenerieren("are")