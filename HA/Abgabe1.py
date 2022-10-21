import turtle







#Eine parent Klasse "Machine" hat Eigentschaften 1.Name,2.Purpose,3.Weight,4.Producessyl,5.Color
class Machine:
    def __init__(self,name,purpose,weight,producecompany,color,width:float,height:float,startx:float,starty:float):

        self.name = name
        self.purpose = purpose
        self.weight = weight
        self.producecompany = producecompany
        self.color = color
        self.width = width
        self.height = height
        self.startx = startx
        self.starty = starty
    def changeColor(self,newcolor):
        print("Die Maschine wurde von {0} zu {1} gefärbt".format(self.color,newcolor))
        self.color = newcolor
    def draw(self):
        myPen = turtle.Turtle()
        myPen.pencolor(self.color)
        myPen.penup()
        myPen.goto(self.startx,self.starty)
        myPen.pendown()
        myPen.write(self.name)







        myPen.goto(self.startx + self.width,self.starty)
        myPen.write(self.purpose)
        myPen.goto(self.startx + self.width,self.starty - self.height)
        myPen.goto(self.startx,self.starty - self.height)
        myPen.goto(self.startx,self.starty)

        myPen.penup()

        turtle.down()


machine = Machine("Alexa","Chatten",1.5,"Amazon","black",400,200,-100,0)
#machine.draw()
class Airplane(Machine):
    def __init__(self,name,purpose,weight,producecompany,color,engines,airplanetype,width:float,height:float,startx:float,starty:float):
        super().__init__(name,purpose,weight,producecompany,color,width,height,startx,starty)
        self.engines = engines
        self.airplanetype = airplanetype

    def draw_airplaneType(self):
        myPen = turtle.Turtle()
        myPen.pencolor(self.color)
        myPen.penup()
        myPen.goto(self.startx,self.starty)
        myPen.pendown()
        myPen.write(self.name)







        myPen.goto(self.startx + self.width,self.starty)
        myPen.write(self.airplanetype)
        myPen.goto(self.startx + self.width,self.starty - self.height)
        myPen.goto(self.startx,self.starty - self.height)
        myPen.goto(self.startx,self.starty)

        myPen.penup()

        turtle.done()





    def __str__(self):
        return ("Die Maschine ist ein {0} und die soll {1}.Jedes Flugzeug wiegt ungefähr {2} t.Meiste große Flugzeuge sind von {3}.Alle Flugzeuge die grad gebaut worden sind {4} Das folgende Flugzeug hat {5} Triebwerke und es ist eine {6}.".format(self.name,self.purpose,str(self.weight),self.producecompany,self.color,self.engines,self.airplanetype))
x = Airplane("airplane","Menschen von Punkt a nach Punkt B bringen und dieses schneller als andere Verkehrsmittel und im Kampf zu benutzen",100,"Airbus , Boeing,Bombadier,Cessnar und Lockheed","black",4,"A340-600",400,200,-100,0)
x.draw_airplaneType()