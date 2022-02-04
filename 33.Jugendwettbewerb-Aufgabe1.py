warteschlange = [4.14, 3.63, 3.92, 7.95, 5.23, 3.30, 4.86, 15.06]
warteschlange2 = [6.96, 5.06, 3.77, 3.95, 3.91, 3.54, 4.26, 4.03,5.43, 4.04, 4.43, 4.12, 2.78]
warteschlange3 = [5.23, 4.41, 3.33, 13.13, 9.12, 4.38, 6.34, 5.37, 4.11, 3.74, 10.62]
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


print(fährebegleiter(warteschlange3,uebrigerplatz1,uebrigerplatz2,uebrigerplatz3))

print("-----------------------------------------------------Strategie2-------------------------------------------")
auffahrt1 = []
auffahrt2 = []
auffahrt3 = []
uebrigerplatz1 = 20.0
uebrigerplatz2 = 20.0
uebrigerplatz3 = 20.0
def fährebegleiter2(warteschlange,uebrigerplatz1,uebrigerplatz2,uebrigerplatz3):
    faehre2 = []
    print(warteschlange)
    counter = 0
    for onecar in warteschlange:

        parkplacefor1car = onecar + 0.3
        if parkplacefor1car > float(uebrigerplatz1) and parkplacefor1car > float(uebrigerplatz2) and parkplacefor1car > float(
                uebrigerplatz3):
            break

        counter += 1
        if counter > 3:
            counter = 1

        if counter == 1:

            if parkplacefor1car < uebrigerplatz1:
                auffahrt1.append(onecar)
                uebrigerplatz1 = uebrigerplatz1 - parkplacefor1car
                print("parkbahn1" + str(auffahrt1))

        elif counter  == 2:

            if parkplacefor1car < uebrigerplatz2:
                auffahrt2.append(onecar)
                uebrigerplatz2 = uebrigerplatz2 - parkplacefor1car
                print("parkbahn2" + str(auffahrt2))

        elif counter == 3:
            if parkplacefor1car < uebrigerplatz3:
                auffahrt3.append(onecar)
                uebrigerplatz3 = uebrigerplatz3 - parkplacefor1car
                print("parkbahn3" + str(auffahrt3))



    faehre2.append(auffahrt1)
    faehre2.append(auffahrt2)
    faehre2.append(auffahrt3)
    return faehre2



print(fährebegleiter2(warteschlange3,uebrigerplatz1,uebrigerplatz2,uebrigerplatz3))




