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
def caculatecounterofdigit(zahl):
    return  len(str(zahl))

def createrandomnumberwithcounterofdigit(count):
    result = 0
    for i in range(0,count):
        randomnumber = random.randint(1,9)
        result += 10 ** i * randomnumber

    return result



#print(createrandomnumberwithcounterofdigit(4))
#sumrange:[2 , 10]
#bsp:p zufallszahl zwischen 2 und 10 bsp:3
#bsp:q zufallszahl maximal sumrange[1] - q minimal:
def generatePQ(sumrange):
    p = random.randint(sumrange[0],sumrange[1])
    q = random.randint(2,sumrange - p)

def bruechegenerieren(schwierigskeitgrad):
    bruch = set()
    if schwierigskeitgrad == "leicht":
        a = random.randint(10,99)
        b = random.randint(10,99)
        p_q = bruechekuerzen([a,b])
        p = p_q[1][0]
        q = p_q[1][1]
        if p + q <= 10:
            bruch.add("a:" + str(a))
            bruch.add("b:" + str(b))
            bruch.add("p:" + str(p))
            bruch.add("q:" + str(q))

            print(str(bruch) + "nicht gekürzter Bruch+" + "gekürzter Bruch")
            return bruch


        else:
            return bruechegenerieren(schwierigskeitgrad)


    elif schwierigskeitgrad == "mittel":
        a = random.randint(100, 999)
        b = random.randint(10, 99)
        bruch.add(a)
        bruch.add(b)
        return  bruch
    elif schwierigskeitgrad == "schwer":
        a = random.randint(100, 999)
        b = random.randint(10, 99)
        bruch.add(a)
        bruch.add(b)

        return  bruch


    else:
        print("error")
        return bruch

#Es gibt einen counter dass von 2 anfängt zu zählen.
#Falls der Zähler und der Nenner durch diesen counter teilen können (ohne Rest) dann werden Zähler und Nenner durch den counter dividiert.
#Falls der counter größer ist als den Zähler und den Nenner das heißt dann dass der Bruch vollständig gekürzt ist.
def bruechekuerzen(bruch):
    list_original = bruch
    list_bruch = list(bruch)
    counter = 1
    result = []
    while counter < counter + 1:
        counter += 1

        if list_bruch[0] % counter == 0 and list_bruch[1] % counter == 0:
            list_bruch[0] = int(list_bruch[0] / counter)
            list_bruch[1] = int(list_bruch[1] / counter)
            counter = 1

        if counter > list_bruch[0] and counter > list_bruch[1]:
            result.append(list_original)

            result.append(list_bruch)
            return result
            break
        else:

            continue

print(bruechegenerieren("leicht"))

#Hier in dieser Funktion wird eingegeben wie viele Aufgaben generiert werden sollten und welcher Schwierigskeitgrad es ist.

"""
def wiederholungsanzahl():
    anzahl = input("wie viele Aufgaben sollen generiert werden?")
    schwierigskeitgrad = input("welcher schwierigskeitgrad soll es sein?")
    results = []
    for i in range(0,int(anzahl)):
        bruch = bruechegenerieren(schwierigskeitgrad)
        result = bruechekuerzen(bruch)
        results.append(result)
    return results

results = wiederholungsanzahl()
print(results)
"""
