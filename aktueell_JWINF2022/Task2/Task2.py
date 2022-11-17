def maxContainer(container1,container2):
    if container1 < container2:
        return container2
    else:
        return container1

containerlist = []
with open("container.txt",encoding="utf8") as file:
    for line in file:
        containerlist.append(line.strip().split(" "))

max = 0
counterformaxnumbers = 0
for onelist in containerlist:
    schwerereContainerList = []
    schwerereContainerList.append(maxContainer(int(onelist[0]),int(onelist[1])))
    for i in schwerereContainerList:
        if i > max:
            counterformaxnumbers = 0

            max = i

        if i == max:
            counterformaxnumbers += 1
if counterformaxnumbers >= 2:
    print("Es konnte kein bestimmter Container bestimmt werden.")
elif counterformaxnumbers == 1:
    counterSpalt = 0
    counterLine = 0
    for oneitem in containerlist:
        counterLine += 1
        counterSpalt = 0
        for oneiteminOneitem in oneitem:
            counterSpalt += 1
            if int(oneiteminOneitem) == max:
                print("Der schwerste Container ist bei x " + str(counterSpalt) + " und ist in der  " + str(counterLine) + ". Zeile.")

