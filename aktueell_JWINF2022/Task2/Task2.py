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
counterforgesamgtMaxContianer = 0
for i in containerlist:
    schwerereContianer = maxContainer(i[0],i[1])
    if int(schwerereContianer) > int(max):
        max = schwerereContianer
        counterforgesamgtMaxContianer += 1
    if int(schwerereContianer) == int(max):
        counterforgesamgtMaxContianer += 1

if counterforgesamgtMaxContianer > 1:
    print("Es konnte kein schwester Container bestimmt werden.")
if counterforgesamgtMaxContianer < 2:
    containerlist.sort()
    print(containerlist)