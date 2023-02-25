class Person():
    def __init__(self,name:str,size:float,hair_color:str):
        self.name = name
        self.size = size
        self.hair_color = hair_color

    def __str__(self):
        return "ich bin {}, {} Jahre alt,und habe {} Haare.".format(self.name,self.size,self.hair_color)


class Student(Person):
    def __init__(self,name:str,size:float,hair_color:str,school:str):
        super().__init__(name,size,hair_color)

        self.school = school
    def __str__(self):
        return "ich bin {}, {} Jahre alt, habe {} Haare und studiere in {}".format(self.name,self.size,self.hair_color,self.school)
    def goto_school(self):
        print("Today is my first day at school{}".format(self.school))

    def change_size(self,new_size:int):
        self.size = 2


student1 = Student("John",12,"braun","PMGF")

student1.change_size(1.7)
print(student1)




class Jugendwettbewerb():
    def __init__(self,richtung,jahr,location):
        self.richtung = richtung
        self.jahr = jahr
        self.location = location
    def __str__(self):
        return "Die Richtung ist {} und dies findet im Jahr {} statt.Die Adresse wo der Wettbewerb sich befindet ist {}".format(self.richtung,self.jahr,self.location)
    def change_location(self,new_location):
        self.new_location = new_location
        self.location = self.new_location
        print("Der neue Standort ist in {}".format(self.location))

Jugendwettbewerb1 = Jugendwettbewerb("Musik",2023,"Wendlingen")
print(Jugendwettbewerb1)
print(Jugendwettbewerb1.change_location("Waiblingen"))

class Jugendmusizieren(Jugendwettbewerb):
    def __init__(self,richtung,jahr,location,instrument):
        super().__init__(richtung,jahr,location)

        self.instrument = instrument
    def __str__(self):
        return "Im Jahr {} findet das Jugend Musiziert in {} und es wird dort {} gespielt.".format(self.jahr,self.location,self.instrument)
    def change_location(self,new_location):
        self.new_location = new_location
        self.location = self.new_location

        print("The new location is: {}".format(self.new_location))


    def use_instrument(self,instrument):
        self.instrument = instrument
        print("Das Instrument, das gespielt wird, ist die {}.".format(self.instrument))



Jugendmusizieren1 = Jugendmusizieren("Musik",2023,"Wendlingen","Geige")
Jugendmusizieren1.change_location("Köngen")
Jugendmusizieren1.use_instrument("Bratsche")
print(Jugendmusizieren1)


import datetime



x = datetime.datetime.now()
print(x.minute)


print(min(2,5,11))


