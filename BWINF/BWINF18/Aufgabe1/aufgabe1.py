

class Leiterspiel:
    def __init__(self):
        self.spiel_felder = [i for i in range(0,101)]
        self.alle_Leiter = [(6,27),(14,19),(31,42),(33,38),(46,62),(51,59),(53,21),(57,96),(65,85),(68,80),(70,76),(92,98)]
        self.cur_pos = 0
        self.counter = 0
        self.verwendete_felder = []
    #Anhand der Informationen aus alle_leiter, wird die neue Position der Spielfigur berechnet.
    def __sprung_leiter(self, cur_pos:int) -> tuple [bool,int]:
        for oneleiter in self.alle_Leiter:
            if cur_pos == oneleiter[0]:
                return (True, oneleiter[1])
            elif cur_pos == oneleiter[1]:
                return (True, oneleiter[0])
        
            
        return False, cur_pos

        
    #Hier wird die neue Position der Spielfigur berechnet, wenn man einmal würfelt und auf ein normales Feld kommt. 
    def __wuerfel_einmal(self,cur_pos:int, wuerfel_punkt) -> int:
        self.counter += 1
        print(f"Ich habe bereits  {self.counter} mal gewürfelt")
        if cur_pos + wuerfel_punkt > 100:
            new_pos = 100 - (cur_pos + wuerfel_punkt - 100)
        else:
            new_pos = cur_pos + wuerfel_punkt
        return new_pos
    
    def leiterspiel_spiel_main(self,wuerfel_punkt:int)->tuple[bool,int]:

        self.cur_pos = self.__wuerfel_einmal(self.cur_pos, wuerfel_punkt)
        if_sprung, new_pos = self.__sprung_leiter(self.cur_pos)

        if if_sprung:
            self.cur_pos = new_pos

        self.verwendete_felder.append(self.cur_pos)


        
        print("cur_pos: ", self.cur_pos)
ein_leiterspiel = Leiterspiel()


import datetime
wuerfel_punkt = 4

start = datetime.datetime.now()
#Variante 1: Es dürfen nur maximal 100/wuerfel_punkt mal gewürfelt werden.

#Variante 2: Das gleiche feld darf nicht zweimal betreten werden





while ein_leiterspiel.cur_pos != 100 and ein_leiterspiel.counter <= 100/wuerfel_punkt:
    ein_leiterspiel.leiterspiel_spiel_main(wuerfel_punkt)

end = datetime.datetime.now()
print(f"Es hat {end-start} Sekunden gedauert, um das Spiel zu beenden.")
                







 