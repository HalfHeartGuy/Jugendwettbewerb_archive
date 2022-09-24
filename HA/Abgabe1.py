#Eine parent Klasse "Machine" hat Eigentschaften 1.Name,2.Purpose,3.Weight,4.Producessyl,5.Color
class Machine:
    def __init__(self,name,purpose,weight,producecompany,color):
        self.name = name
        self.purpose = purpose
        self.weight = weight
        self.producecompany = producecompany
        self.color = color
    def changeColor(self,newcolor):
        print("Die Maschine wurde von {0} zu {1} gefärbt".format(self.color,newcolor))
        self.color = newcolor
class Airplane(Machine):
    def __str__(self):
        return ("Die Maschine ist ein {0} und die soll {1}.Jedes Flugzeug wiegt ungefähr {2} t.Meiste große Flugzeuge sind von {3}.Alle Flugzeuge die grad gebaut worden sind {4}.".format(self.name,self.purpose,str(self.weight),self.producecompany,self.color))
x = Airplane("airplane","Menschen von Punkt a nach Punkt B bringen und dieses schneller als andere Verkehrsmittel und im Kampf zu benutzen",100,"Airbus , Boeing,Bombadier,Cessnar und Lockheed","white")
print(x)