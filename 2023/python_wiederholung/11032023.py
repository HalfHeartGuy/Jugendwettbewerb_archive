def task1(firstnumber,secondnumber):
    if firstnumber * secondnumber <= 1000:
        print(firstnumber * secondnumber)
    else:
        print(firstnumber + secondnumber)





def task2(wiederholungen):
    previous_num = 0
    current_num = 0


    for i in range(wiederholungen):
        print("Current Number", current_num, "Previous Number ", previous_num, " Sum: ", current_num + previous_num)
        previous_num = current_num
        current_num = i + 1
#task2(10)

def task3():
    usersword = input("A word:")
    result = ""
    for i in range(0,len(usersword),2):
        result = result + usersword[i]
    return result

#print(task3())

def task4(word:str,number:int):
    if number <= len(word):
        result = word[number:]
    else:
        print("n muss kleiner als " + str(number) + "sein")


    return result
#print(task4("pynative",3))

def task5(numbers_x,numbers_y):
    if numbers_x[0] == numbers_x[-1]:
        print("Given list:" + str(numbers_x))
        print("The result is true")
    else:
        print("Given list:" + str(numbers_x))
        print("The result is false")
    if numbers_y[0] == numbers_y[-1]:
        print("Given list:" + str(numbers_y))
        print("The result is true")
    else:
        print("Given list:" + str(numbers_y))
        print("The result is false")

#task5([10, 20, 30, 40, 10],[75, 65, 35, 75, 30])

def task6(given_list):
    print("Divisible by 5:")
    for oneelement in given_list:
        if oneelement % 5 == 0:
            print(oneelement)

task6([10, 20, 33, 46, 55])

def task7()













