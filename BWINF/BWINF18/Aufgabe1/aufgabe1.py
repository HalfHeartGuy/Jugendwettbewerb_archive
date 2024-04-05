




spiel_felder = [i for i in range(0,101)]
alle_Leiter = [(6,27),(14,19),(31,42),(38,46),(51,59),(53,21),(57,96),(65,85),(68,80),(70,76),(92,98)]




#Anhand der Informationen aus alle_leiter, wird die neue Position der Spielfigur berechnet.
def sprung_leiter(cur_pos:int) -> tuple [bool,int]:
    pass



#Hier wird die neue Position der Spielfigur berechnet, wenn man einmal würfelt und auf ein normales Feld kommt. 
def wuerfel_einmal(cur_pos:int, wuerfel_punkt) -> int:
    pass
    
#folgende Funktion soll für eine angegebene Zahl zwischen 1 und 6 berechnen, 1. ob die Spielfigur auf das Zielfeld (100) erreicht,2. wie oft man würfeln muss, um das Zielfeld zu erreichen.
#Es ist das Leiterspiel heißt es gibt Leitern, die die Figur sofort auf ein anderes Feld versetzen , aber diese können die Figur auch zurücksetzen.Das Spielbrett ist auf BWINF_37_Aufgaben_WEB.pdf zu finden bei Aufgabe 1.


def leiterspiel_spiel_main(zahl:int)->tuple[bool,int]:


    #wiederhole folgende Schritte mit einer while-Schleife, bis die Spielfigur das Zielfeld erreicht.
    cur_pos = wuerfel_einmal(jetzt_pos, zahl)
    if_sprung, new_pos = sprung_leiter(new_pos)
    
    if if_sprung:
        cur_pos = new_pos
    


    return (True,50)
