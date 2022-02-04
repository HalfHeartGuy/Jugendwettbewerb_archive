warteschlange = [4.14, 3.63, 3.92, 7.95, 5.23, 3.30, 4.86, 15.06]
auffahrt1 = []
auffahrt2 = []
auffahrt3 = []
uebrigerplatz1 = 20.0
uebrigerplatz2 = 20.0
uebrigerplatz3 = 20.0
def fährebegleiter(warteschlange,uebrigerplatz1,uebrigerplatz2,uebrigerplatz3):
    faehre = []
    print(warteschlange)
    for onecar in warteschlange:
        if onecar + 0.3 < float(uebrigerplatz1):
            auffahrt1.append(onecar)
            autoplatz1 = onecar + 0.3
            uebrigerplatz1 = uebrigerplatz1 - autoplatz1
            print("parkbahn1" + str(auffahrt1))
        else:
            if onecar + 0.3 < float(uebrigerplatz2):
                auffahrt2.append(onecar)
                autoplatz2 = onecar + 0.3
                uebrigerplatz2 = uebrigerplatz2 - autoplatz2
                print("parkbahn2" + str(auffahrt2))

            else:
                if onecar + 0.3 < float(uebrigerplatz3):
                    auffahrt3.append(onecar)
                    autoplatz3 = onecar + 0.3
                    uebrigerplatz3 = uebrigerplatz3 - autoplatz3
                    print("parkbahn3" + str(auffahrt3))



    faehre.append(auffahrt1)
    faehre.append(auffahrt2)
    faehre.append(auffahrt3)
    return faehre


print(fährebegleiter(warteschlange,uebrigerplatz1,uebrigerplatz2,uebrigerplatz3))






