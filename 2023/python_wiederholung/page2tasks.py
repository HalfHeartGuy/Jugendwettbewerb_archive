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



def task6(number):
    number = str(number)
    counter = 0
    while counter < len(number):

        counter += 1
    return counter
#print(task6(1000000))

def task7():
    for i in range(5, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
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


#task11(25,50)


def task12(counter):
    num1 = 0
    num2 = 1
    for i in range(1,counter + 1):
        print(num1)
        result = num1 + num2
        num1 = num2
        num2 = result
#task12(10)

def task13(input_number):
    if input_number == 0:
        return 1
    else:
        result = 1
        for i in range(1,input_number + 1):
            result = result * i

        return result
#print(task13(4))

def task14(number):
    number = str(number)
    print(number[::-1])
#task14(76542)



def task15(given_list):
    for i in range(1,len(given_list) - 1,2):
        print(given_list[i])
#task15([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

def task16(num):
    print("This is task16")
    for i in range(0,num + 1):
        print("Current Number is: " + str(i) + " and the cube is " + str(i ** 3))
#task16(6)

def task17(n):
    result = 0
    twos = ""
    for i in range(1,n + 1):
        twos = twos + "2"

        result += int(twos)
    return result
#print(task17(5))


def task18():
    for i in range(1, 6):
        print("* " * i)
    for i in range(4, 0, -1):
        print("* " * i)


#task18()






def task2_1():
    num1 = input("Zahl 1:")
    num2 = input("Zahl 2:")
    print(int(num1) * int(num2))

#task2_1()


def task2_2():
    string1 = input("String1:")
    string2 = input("String2:")
    string3 = input("String3:")

    print(string1 + str("**") + string2 + str("**") + string3)

#task2_2()

def task2_4():
    num = input("Float Number:")
    print("%.2f" % float(num))

#task2_4()

def task2_5():
    float_numbers = []
    for i in range(1,6):
        num = float(input("Zahl " + str(i)))
        float_numbers.append(num)
    return float_numbers
#print(task2_5())



def task2_6():
    f = open("test.txt","r")
    f2 = open("new_file.txt","w")
    f_lines = f.readlines()
    del f_lines[4]
    for line in f_lines:
        f2.write(line)



    f.close()
    f2.close()
#task2_6()

def task2_7():
    names = input("Enter three names separated by spaces: ")
    name_list = names.split()

    if len(name_list) != 3:
        print("Please enter exactly three names.")
    else:
        print("The three names are:")
        for name in name_list:
            print(name)

#task2_7()

def task2_8():
    totalMoney = input("Total Money:")
    quantity = input("Quantity:")
    price = input("Price:")
    print("I have {} dollars so I can buy {} football for {} dollars.".format(totalMoney,quantity,price))
#task2_8()
import os
def task2_9():
    f = os.stat("test2.txt").st_size
    if f == 0:
        print("empty")
    else:
        print("not empty")


#task2_9()


def task2_10():
    f = open("test.txt","r")
    for i in range(1,4):
        f.readline()
    print(f.readline())
#task2_10()


def task3_1(name,age):
    print(name)
    print(age)
#task3_1("Moritz",13)


def task3_2(*args):
    print("Task 2")
    print("Printing Values")
    for i in args:
        print(i)
#task3_2(20,40,60)

def calculation(a, b):
    print("task 3")
    return a + b,a - b

#res = calculation(40, 10)
#print(res)

def task3_4(name,salary=9000):
    if salary == None:
        print("Name: {} salary: {}".format(name,9000))
    else:
        print("Name: {} salary: {}".format(name,salary))
#task3_4("Ben", 12000)
#task3_4("Jessa")



def task3_5(a,b):
    def inner_task3_5(a,b):
        return a + b
    return inner_task3_5(a,b) + 5
#print(task3_5(5,9))


def task3_6(a):
    if a == 0:
        return 0
    else:
        return a + task3_6(a - 1)

#print(task3_6(10))

def task3_7(name, age):
    print(name, age)

#task3_7("Emma", 26)

show_student = task3_7
#show_student("Emma", 26)

def task3_8():
    result_list = []
    for i in range(4,30,2):
        result_list.append(i)
    return result_list
#print(task3_8())

def task3_9(given_list):
    result = 0
    for i in given_list:
        if i > result:
            result = i
    return result


x = [4, 6, 8, 24, 12, 2]

#   print(task3_9(x))
def task4_1A(input_string):
    result = "{}{}{}".format(input_string[0],input_string[(len(input_string) // 2)],input_string[-1])
    print("Task 1A")
    print(result)
#task4_1A("James")


def task4_1B(input_string):
    print("Task 1B")
    print(input_string[round(len(input_string) // 2) - 2:round(len(input_string) // 2) + 1])
#task4_1B("JaSona")


def task4_2(string1,string2):
    mid_index = len(string1) // 2
    s3 = string1[:mid_index] + string2 + string1[mid_index:]
    print("Task2")
    print(s3)

#task4_2("Ault","Kelly")

def task4_3(string1,string2):
    string3 = string1[0] + string2[0] + string1[(len(string1) // 2)] + string2[(len(string2) // 2)] + string1[-1] + string2[-1]
    print("Task 3")
    print(string3)
#task4_3("America","Japan")

def task4_4(str1):
    result = ""
    halter = ""
    for oneletter in str1:
        if oneletter == oneletter.lower():
            result = result + oneletter
        else:
            halter = halter + oneletter
    result = result + halter
    print("Task4")
    print(result)
#task4_4("PyNaTive")

def task4_5(string):
    chars = 0
    digits = 0
    symbol = 0
    for oneletter in string:
        if oneletter.isalpha():
            chars += 1
        elif oneletter.isdigit():
            digits += 1
        else:
            symbol += 1
    print("Task 5")
    print("Total counts of chars, digits, and symbols ")
    print("chars = {}".format(chars))
    print("digits = {}".format(digits))
    print("symbol = {}".format(symbol))

#ask4_5("P@#yn26at^&i5ve")

def task4_6(s1,s2):
    s3 = ""
    if len(s1) > len(s2):
        longerString = s1
        shorterString = s2
    else:
        longerString = s2
        shorterString = s1


    for i in range(0,len(shorterString)):
        s3 = s3 + s1[i] + s2[(i + 1) * -1]

    print("Task 6")
    #print(s3)
    s3 = s3 + longerString[len(shorterString)]
    print(s3)
#task4_6("Abc","Xyz")

def task4_7(s1,s2):
    if len(s1) > len(s2):
        longerString = s1
        shorterString = s2
    else:
        longerString = s2
        shorterString = s1

    result = True

    for oneltter in shorterString:
        if oneltter not in longerString:
            result = False
    print("task 7")
    print(result)
#task4_7("Yn","PYnative")

def task4_8(str1:str):
    str1 = str1.lower()
    result = str1.count("usa")
    print("task 8")
    print("The USA count is: " + str(result))
#task4_8("Welcome to USA. usa awesome, isn't it()")


def task4_9(s1):
    average = 0
    sum1 = 0
    for onething in s1:
        if onething.isdigit():
            sum1 += int(onething)
            average += 1
    print("task 9")
    print("Sum is:" + str(sum1) + " Average is " + str(sum1 / average))
#task4_9("PYnative29@#8496")


def task4_10(s1):
    char_count = {}

    for char in s1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print("task10")
    print(char_count)


#task4_10("Apple")

def task4_11(s1):
    print("task 11:" + s1[::-1])
#task4_11("PYnative")

def task4_12(s1):
    print("Task 12:")
    print("Last occurrence of Emma starts at index {}".format(s1.rfind("Emma")))
#task4_12("Emma is a data scientist who knows Python. Emma works at google.")

def task4_13(s1:str):
    print("task 13")
    print("Displaying each substring")
    result = s1.split("-")
    for i in result:
        print(i)
#task4_13("Emma-is-a-data-scientist")

def task4_14(list1:list):
    result_list = []
    print("task 14")
    print("Original list of string")
    print(list1)

    for i in list1:
        if i:
            result_list.append(i)

    print("After removing empty strings")
    print(result_list)
#task4_14(['Emma', 'Jon', '', 'Kelly', None, 'Eric', ''])

def task4_15(s1):
    res = ""
    for onething in s1:
        if onething.isdigit():
            res = res + onething
        elif onething.isalpha():
            res = res + onething
        elif onething == " ":
            res = res + onething
        else:
            continue
    res = res.replace("  "," ")
    print("task15")
    print(res)
#task4_15("/*Jon is @developer & musician")

def task4_16(s1):
    res = ""
    for onething in s1:
        if onething.isdigit():
            res = res + str(onething)
    print("task16")
    print(res)
#task4_16("I am 25 years and 10 months old")


def task4_17(s1):
    zwischenschritt = ""
    for onething in s1:
        if onething == " ":
            digit = False
            alpha = False
            for onething2 in zwischenschritt:
                if onething2.isdigit():
                    digit = True
                if onething2.isalpha():
                    alpha = True
            if digit and alpha:
                print("task 17")
                print(zwischenschritt.strip())
            zwischenschritt = " "
        else:
            zwischenschritt = zwischenschritt + str(onething)



#task4_17("Emma25 is Data scientist50 and AI Expert")

def task4_18(s1):
    res = " "
    for onething in s1:
        if onething.isdigit():
            res = res + onething
        elif onething.isalpha():
            res = res + onething
        elif onething == " ":
            res = res + onething
        else:
            res = res + "#"
    print("task18")
    print(res.strip())

#task4_18("/*Jon is @developer & musician!!")


def task5_1(l1,l2):
    print("task 1")
    l1_1 = []
    l2_2 = []
    print("Element at odd-index positions from list one")

    for i in range(1,len(l1) - 1,2):

        l1_1.append(l1[i])
    print(l1_1)
    print("Element at even-index positions from list two")

    for j in range(0,len(l2) - 1,2):
        l2_2.append(l2[j])
    print(l2_2)
    print("Printing Final third list")
    print(l1_1 + l2_2)
#task5_1([3, 6, 9, 12, 15, 18, 21],[4, 8, 12, 16, 20, 24, 28])


def task5_2(l1:list):
    print("task 2")
    onepiece = l1.pop(4)

    print("List After removing element at index 4 " + str(l1))
    l1.insert(2,onepiece)
    print("List after Adding element at index 2 " + str(l1))
    l1.append(onepiece)
    print("List after Adding element at last " + str(l1))


#task5_2([34, 54, 67, 89, 11, 43, 94])


def task5_3(l1:list):
    chunk_size = len(l1) // 3
    chunk1 = l1[:chunk_size]
    chunk2 = l1[chunk_size:chunk_size * 2]
    chunk3 = l1[chunk_size * 2:]
    print("Chunk 1 " + str(chunk1))
    print("After reversing it " + str(chunk1[::-1]))
    print("Chunk 2 " + str(chunk2))
    print("After reversing it " + str(chunk2[::-1]))
    print("Chunk 3 " + str(chunk3))
    print("After reversing it " + str(chunk3[::-1]))



#task5_3([11, 45, 8, 23, 14, 12, 78, 45, 89])

def task5_4(l1:list):
    result_dictionary = {}
    for onenumber in l1:
        if onenumber in result_dictionary:
            result_dictionary[onenumber] += 1
        else:
            result_dictionary[onenumber] = 1
    print(result_dictionary)
#task5_4( [11, 45, 8, 11, 23, 45, 23, 45, 89])


def task5_5(l1:list,l2:list):
    result_tuple = zip(l1,l2)
    print(set(result_tuple))
#task5_5([2, 3, 4, 5, 6, 7, 8],[4, 9, 16, 25, 36, 49, 64])


def task5_6(s1:set,s2:set):
    s3 = s1.intersection(s2)
    print("Intersection is " + str(s3))
    for onenumber in s3:
        if onenumber in s1:
            s1.remove(onenumber)
    print("First Set after removing common element " + str(s1))
#task5_6({23, 42, 65, 57, 78, 83, 29},{57, 83, 29, 67, 73, 43, 48})

def task5_7(s1:set,s2:set):
    checker = s1.issubset(s2)
    print("First set is subset of second set - " + str(s1.issubset(s2)))
    print("Second set is subset of First set - " + str(s2.issubset(s1)))

    print("First set is Super set of second set - " + str(s1.issuperset(s2)))
    print("Second set is Super set of First set - " + str(s2.issuperset(s1)))

    if s1.issubset(s2):
        s1.clear()
    else:
        s2.clear()
    print("First set " + str(s1))
    print("Second Set " + str(s2))





#task5_7({27, 43, 34},{34, 93, 22, 27, 43, 53, 48})

def task5_8(roll_number:list,sample_dict:dict):
    for onenumber in roll_number:
        if onenumber not in sample_dict.values():
            roll_number.remove(onenumber)
    print("After removing unwanted elements from list" + str(roll_number))
#task5_8([47, 64, 69, 37, 76, 83, 95, 97],{'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97})

def task5_9(d1:dict):
    l1 = d1.values()
    l1 = set(l1)
    l1 = list(l1)
    print(l1)
#task5_9({'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54})


def task5_10(l1):
    l1 = set(l1)
    print(list(l1))
    t1 = l1
    print("tuple " + str(t1))
    print("min: " + str(min(t1)))
    print("max: " + str(max(t1)))
#task5_10([87, 45, 41, 65, 94, 41, 99, 94])


def task6_1(l1:list):
    print(list(reversed(l1)))
#task6_1([100, 200, 300, 400, 500])

def task6_2(l1,l2):
    l3 = []
    if len(l1) > len(l2):
        longerList = l1
        shorterList = l2
    else:
        longerList = l2
        shorterList = l1
    for i in range(0,len(shorterList)):
        l3.append(l1[i] + l2[i])
    if len(longerList) != len(shorterList):
        l3.append(longerList[len(shorterList):])
    print(l3)
#task6_2(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"])

def task6_3(l1):
    l2 = []
    for i in range(len(l1)):
        l2.append(l1[i] * l1[i])
    print(l2)
task6_3([1, 2, 3, 4, 5, 6, 7])


def task6_4(l1,l2):
    l3 = []
    for i in l1:
        for j in l2:
            l3.append(i + j)
    print(l3)
#task6_4(["Hello ", "take "],["Dear", "Sir"])

def task6_5(l1:list,l2:list):
    l2 = reversed(l2)


    t1 = zip(l1,l2)
    for oneitem in t1:
        oneitem = str(oneitem)
        oneitem = oneitem.replace("(","")
        print(oneitem.replace(")",""))

#task6_5([10, 20, 30, 40],[100, 200, 300, 400])

def task6_6(l1:list):
    l2 = []
    for oneitem in l1:
        if oneitem:
            l2.append(oneitem)
    l2 = filter(None,l2)
    print(list(l2))

#task6_6(["Mike", "", "Emma", "Kelly", "", "Brad"])

def task6_7(l1:list):
    l1[2][2].append(7000)

    print(l1)
#task6_7([10, 20, [300, 400, [5000, 6000], 500], 30, 40])

def task6_8(l1:list,l2):
    l1[2][1][2].extend(l2)
    print(l1)
task6_8(["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"],["h", "i", "j"])