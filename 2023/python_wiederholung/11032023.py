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

#task6([10, 20, 33, 46, 55])

def task7(given_string:str):
    x = given_string.count("Emma")
    print("Emma appeared " + str(x) + " times.")

#task7("Emma is good developer. Emma is a writer.")

def task8(counter):
    if counter == 1:
        print(counter)
    else:
        for i in range(1,counter + 1):
            counter_string = ""

            for j in range(0,i):
                counter_string = str(counter_string) + " " + str(i)
            print(counter_string)

#task8(5)

def task9(original_number):
    original_number = str(original_number)
    if str(original_number[0]) == str(original_number[-1]):
        print("original number " + str(original_number))
        print("Yes. given number is palindrome number")
    else:
        print("original number " + str(original_number))
        print("No. given number is not palindrome number")

#task9(125)

def task10(list1:list,list2:list):
    result_list = []
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)
    for num2 in list2:
        if num2 % 2 == 0:
            result_list.append(num2)
    return result_list
print(task10([10, 20, 25, 30, 35],[40, 45, 60, 75, 90]))

