
class Animel:
    def __init__(self,my_speed,my_color,my_name,my_weight,my_lenght,my_age):
        self.speed = my_speed
        self.color = my_color
        self.legs = 4
        self.ears = 2
        self.tail = 1
        self.name = my_name
        self.weight = my_weight
        self.length = my_lenght
        self.age = my_age



    def __str__(self):
        return "Mein Hund heißt {0}, hat die Farbe {1}. UNd er ist heute {2} Jahre alt. UNd er ist sehr groß und ca. {3} Meter lang.Er hat {4} Ohren. "\
            .format(self.name,self.color,self.age,self.length,self.ears)
    def change_color(self,new_color):

        self.color = new_color

    def change_weight(self,new_weight):
        print("Ich füttere mein Hund mit Steak und er wiegt nun {0} kg".format((new_weight)))

        self.weight = new_weight






class Dog(Animel):
    def __init__(self,my_speed,my_color,my_name,my_weight,my_length,my_age,my_iq):
        super().__init__(my_speed,my_color,my_name,my_weight,my_length,my_age)
        self.iq = my_iq
    def go_to_school(self,new_iq):
        self.iq = new_iq



a_new_dog = Dog(5.5,"schwarz","Max",10.5,1.2,2.5,0)
print(a_new_dog)




