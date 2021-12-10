# step1 Split die Eingabe "myletterSquence" in eine Liste von Buchstaben :["A","C","D",..."F"
# step 2 Berechne die Anzahl der Felder zwischen jeweils  2 benachnarter Buchstaben[2,1,...,5]
# step3 Berechne die Possibility für jedes Element aus der Liste ,das das Ergebnis von Step 2 ist.[4/15,5/15...}
# step4:myResult = Multiplikationsprodukt  von ALLEN Elemente aus Step 3

import math
possibilityTable = {"1":5/15,"2":4/15,"3":3/15,"4":2/15,"5":1/15}

lettterSquence = "A-C-D-B-E-A-F"
def caculatePossibility(myPossibilityDic,myletterSquence):
    myResult = 0
    step1_result = step1(myletterSquence)
    print(step1_result)

    step2_result = step2(step1_result)
    print(step2_result)

    step3_result = step3(myPossibilityDic,step2_result)
    print(step3_result)

def step1(myletterSquence):
    return myletterSquence.split("-")



def step2(listofsuquence):
    results = []
    for i in range(0,len(listofsuquence) - 1):
        abstand = abs(ord(listofsuquence[i]) - ord(listofsuquence[i + 1]))
        results.append(abstand)
    return results
def step3(myPossibilityDic,step2Results):
    results = []
    for i in range(0,len(step2Results)):
        wahrscheinlichkeit = myPossibilityDic[str(step2Results[i])]
        results.append(wahrscheinlichkeit)
    return results




caculatePossibility(possibilityTable,lettterSquence)