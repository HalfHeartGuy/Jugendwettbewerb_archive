


class Maschine:
    def __init__(self, my_color, my_name, my_weight, my_ProduceBy):
        self.color = my_color
        self.name = my_name
        self.weight = my_weight
        self.ProduceBy = my_ProduceBy

    def __str__(self):
       return "Mein Schiff heißt {0},hat die Farbe {1}.Es wiegt ungefähr {2} Kilogramm. Sein Produzent ist die {3} ."\
            .format(self.name, self.color, self.weight, self.ProduceBy)

    def change_color(self,new_color):
        print("Heute hat mein Schiff eine andere Farbe, nämlich {0}".format(new_color))
        self.color = new_color

Schiff = Maschine("ship","silver",100,"Mariane")
print(Schiff)

Schiff.change_color("brown")
print(Schiff)