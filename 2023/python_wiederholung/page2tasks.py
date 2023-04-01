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
#task5([12, 75, 150, 180, 145, 525, 50])



def task6(number:str):
    number = str(number)
    counter = 0
    while counter < len(number):

        counter += 1
    return counter
#print(task6("5789"))

def task7():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()


#task7()



def task8(input_list:list):
    for i in range(len(input_list) - 1,-1,-1):
        print(input_list[i])
#task8([10, 20, 30, 40, 50])


def task9():
    for i in range(-10,0):
        print(i)
#task9()


def task10():
    for i in range(5):
        print(i)
    else:
        print("Done!")
#task10()

start = 25
end = 50
def task11(start,end):
    for i in range(start,end):
        statement = True

        for j in range(2,i - 1):

            if i / j == round(i / j):
                statement = False
                continue
        if statement == True:
            print(i)


task11(25,50)

