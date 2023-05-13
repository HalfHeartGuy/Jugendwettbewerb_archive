class Persons:
    def __init__(self,id:int,lastName:str,firstName:str,age:int,city = "Stuttgart"):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
        self.age = age
        self.city = city
    def __str__(self):
        return "My Name is {} {}, I am {} years old, and living in {}.".format(self.firstName,self.lastName,self.age,self.city)

jiaen = Persons(1,"Guo","Jiaen",40, "Stuttgart")

print(jiaen)
