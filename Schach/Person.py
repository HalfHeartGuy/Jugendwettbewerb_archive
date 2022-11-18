


class Person():
    def __init__(self, vorname:str, nachname:str):
        self.vorname = vorname
        self.nachname = nachname


    def printPerson(self):
        print("Ich bin {} {}.".format(self.vorname, self.nachname))




jiaen = Person(vorname="jiaen", nachname="Guo")
jiaen.printPerson()
