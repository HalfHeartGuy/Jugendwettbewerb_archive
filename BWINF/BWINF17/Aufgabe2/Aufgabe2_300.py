
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
print(vogel2)