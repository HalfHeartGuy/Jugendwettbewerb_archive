def task1():
    counter = 0
    while counter < 10:
        counter += 1
        print(counter)


#task1()

def task2(counter):
    for i in range(1,counter + 1):
        result = ""
        for j in range(0,i):
            if j == 0:
                result = i
            else:
                result = str(result) + " " + str(i)

        print(result)
task2(5)