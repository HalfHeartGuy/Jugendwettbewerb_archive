warteschlange = [4.14, 3.63, 3.92, 7.95, 5.23, 3.30, 4.86, 15.06]
faehre = []
auffahrt1 = []
auffahrt2 = []
auffahrt3 = []
uebrigerplatz1 = 20.0
uebrigerplatz2 = 20.0
uebrigerplatz3 = 20.0
def fährebegleiter(warteschlange,uebrigerplatz1,uebrigerplatz2,uebrigerplatz3):

    for onecar in warteschlange:
        if onecar + 0.3 < float(uebrigerplatz1):
            auffahrt1.append(onecar)
            uebrigerplatz1 = onecar + 0.3
        else:
            if onecar + 0.3 < float(uebrigerplatz2):
                auffahrt2.append(onecar)
                uebrigerplatz2 = onecar + 0.3

            else:
                if onecar + 0.3 < float(uebrigerplatz3):
                    auffahrt3.append(onecar)
                    uebrigerplatz3 = onecar + 0.3

                else:
                    faehre.append(auffahrt1)
                    faehre.append(auffahrt2)
                    faehre.append(auffahrt3)
                    return faehre


print(fährebegleiter(warteschlange,uebrigerplatz1,uebrigerplatz2,uebrigerplatz3))




