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
#task2(5)

def task3(enternumber):
    result = 0
    for i in range(1,enternumber + 1):
        result += i
    return result
#print(task3(4))

def task4(given_number:int):
    for i in range(1,11):
        print(i * given_number)

#task4(3)

def task5(given_list:list):
    for i in given_list:

        if i > 500:
            break

        elif i > 150:
            continue
        else:
            if i % 5 == 0:
                print(i)
task5([12, 75, 150, 180, 145, 525, 50])