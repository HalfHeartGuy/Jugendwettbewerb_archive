
def vogel_routen_Berechner(start_vogel_pos, richtung, start_zeit,forest_length,forest_width):
    vogel_route = []
    start_x = start_vogel_pos[0]
    start_y = start_vogel_pos[1]
    counter = 0
    counter2 = 0
    up_down = 0
    if richtung == "sn":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y-counter2]})
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y-counter2]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        vogel_route.append({str(720):[start_x, start_y]})   
        return vogel_route
  
    elif richtung == "we":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 += 1
                if counter2 == forest_width-1:
                    up_down = 1
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route
    
    elif richtung == "ns":
        counter2 = 0
        while counter + start_zeit < 720:
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 0

            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x+counter2, start_y]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 1
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route
    elif richtung == "ew":
        while counter + start_zeit < 720:
            while up_down == 1:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y+counter2]})
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0

            while up_down == 0:
                vogel_route.append({str(start_zeit+counter):[start_x, start_y+counter2]})
                counter += 1
                counter2 += 1
                if counter2 == forest_width-1:
                    up_down = 1
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route




vogel2 = vogel_routen_Berechner((1,0), "we", 20, 15, 3)
#Schritt 2: Berechne wie viele Minuten ein Vogel wieder braucht um bei einem Feld wieder vorbei zu fliegen. Ein Vogel braucht 1 Minute um ein Feld zu überfliegen.
#Eingaben Beispiel: # Eingaben: Feld (2,1), wald_breite = 3, wald_hoehe = 15, Routinplan = [{"21":(2,1)}, {"22":(2,2)}, {"23":(2,3)}, ...,{"35":(2,14)}, {"36": (2,13)},.., {"49":(2,1)}]
#Ausgabe: 28
def calc_vogel_rueckkehr_zeit(feld,wald_breite, wald_hoehe, start_zeit):
    vogel1 = vogel_routen_Berechner((1,14), "sn", start_zeit, wald_hoehe, wald_breite)
    routinenplan = vogel1

    routinenplaene = []
    routinenplan.append(vogel1)
    
    
    counter = 0
    for i in range(0,len(routinenplan)):
        for j in range(0,len(routinenplan[i])):
            if routinenplan[i][j][str(start_zeit + j)] == feld:
                

print(calc_vogel_rueckkehr_zeit((1,2), 3, 15, 20))
#print(calc_vogel_rueckkehr_zeit((1,2), 3, 20, 20))
#print(calc_vogel_rueckkehr_zeit((1,2), 3, 15, 50))
#print(calc_vogel_rueckkehr_zeit((2,1), 3, 15, 20))
