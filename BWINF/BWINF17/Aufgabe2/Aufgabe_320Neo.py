def create_empty_dict():
    empty_dict = {}
    for i in range(0,721):
        empty_dict[str(i)] = [-1,-1]
    return empty_dict
vogel_routen = create_empty_dict()
#Schritt 0.1:
#Waldfelder
def calc_forest_felder(forest_length,forest_width):
    wald_felder = []
    for i in range(forest_length):
        for j in range(forest_width):
            wald_felder.append([j,i])
    return wald_felder


# Schritt 1: Berechnung vom Routinplan für 1 angegeben Vogel (wann der Vogel bei welchem Feler vorbei fliegt) von diesem Vogel?
# Datenstruktur für diesen Routinplan: [{"21":(1,1)}, {"22":(1,2)}, {"23":(1,3)}, ...,{"35":(1,14)}, {"36": (1,13)},.., {"50":(1,0)}]
"""
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
                vogel_routen[str(start_zeit+counter)].clear()
                vogel_routen[str(start_zeit+counter)].append(start_x)
                vogel_routen[str(start_zeit+counter)].append(start_y+counter2)
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].clear()

                vogel_routen[str(start_zeit+counter)].append(start_x)
                vogel_routen[str(start_zeit+counter)].append(start_y+counter2)

                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0

       
        return vogel_routen
  
    elif richtung == "we":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].clear()

                vogel_routen[str(start_zeit+counter)].append(start_y)
                vogel_routen[str(start_zeit+counter)].append(start_x+counter2)
                counter += 1
                counter2 += 1
                if counter2 == forest_width-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].clear()

                vogel_routen[str(start_zeit+counter)].append(start_y)
                vogel_routen[str(start_zeit+counter)].append(start_x+counter2)
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        return vogel_routen
    
    elif richtung == "ns":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].clear()

                vogel_routen[str(start_zeit+counter)].append(start_y+counter2)
                vogel_routen[str(start_zeit+counter)].append(start_x)
                counter += 1
                counter2 += 1
                if counter2 == forest_length-1:
                    up_down = 1
            while up_down == 1:
                vogel_routen[str(start_zeit+counter)].clear()
                vogel_routen[str(start_zeit+counter)].append(start_y+counter2)
                vogel_routen[str(start_zeit+counter)].append(start_x)
                counter += 1
                counter2 -= 1
                if counter2 == 0:
                    up_down = 0
        return vogel_route
    elif richtung == "ew":
        while counter + start_zeit < 720:
            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].clear()
                vogel_routen[str(start_zeit+counter)].append(start_y)
                vogel_routen[str(start_zeit+counter)].append(start_x-counter2)
                counter += 1
                counter2 += 1
                if counter2 == 0:
                    up_down = 0

            while up_down == 0:
                vogel_routen[str(start_zeit+counter)].clear()
                vogel_routen[str(start_zeit+counter)].append(start_y)
                vogel_routen[str(start_zeit+counter)].append(start_x-counter2)
                counter += 1
                counter2 -= 1
                if counter2 == forest_width-1:
                    up_down = 1
        vogel_route.append({str(720):[start_x, start_y]})
        return vogel_route
"""

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



startPos = [1,0]
richtung = "we"
startZeit = 20
forest_length = 15
forest_width = 3

einVogelRoute = vogel_routen_Berechner(startPos, richtung, startZeit, forest_length, forest_width)
for i in range(startZeit,721):
    if vogel_routen[str(i)] == [-1,-1]:

        vogel_routen[str(i)].clear()
    vogel_routen[str(i)].append(einVogelRoute[i-startZeit][str(i)])
print(vogel_routen)
startPos = [1,14]
richtung = "sn"
startZeit = 20
forest_length = 15
forest_width = 3
einVogelRoute2 = vogel_routen_Berechner(startPos, richtung, startZeit, forest_length, forest_width)
for i in range(startZeit,721):
    if vogel_routen[str(i)] == [-1,-1]:

        vogel_routen[str(i)].clear()
    vogel_routen[str(i)].append(einVogelRoute2[i-startZeit][str(i)])
print(vogel_routen)
