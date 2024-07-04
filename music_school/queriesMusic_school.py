from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['music_school']


#Task 1
def searchNameandAgeandteacher(instrument,age,teacher):
    collection_student = db['students']
    collection_courses = db["courses"]
    query = {"teacher":teacher}
    x_courses = collection_courses.find(query, {"students": 1, "_id": 0})
    students = []
    for x in x_courses:
        students = x["students"]

    result = []

    for name in students:
        x_students = collection_student.find({"instrument": instrument, "age": {"$lt": age}, "name": name})
        result.append(x_students)
    for oneresult in result:
        for student in oneresult:
            print(student)
    return result
#----------------------------------------------
#Task 2
def countstudentsfromateacher(teacher,instrument):
    collection_courses = db["courses"]
    collection_students = db["students"]
    query = {"teacher":teacher}
    x_courses = collection_courses.find(query)
    for x in x_courses:
        students = x["students"]

    result = []
    for student in students:
        print(student)
        x_students = collection_students.find({"name":student,"instrument":instrument})
        result.append(x_students)
    return len(result)


#----------------------------------------------
#Task 3
#Note: Before an instrument there is always CCC
def updateCourseTransfertoDifferentTeacher(toTransferteacher2,time,course):
    collection_courses = db["courses"]
    query = {"name":course,"time":time}
    collection_courses.update_one(query, {"$set": {"teacher": toTransferteacher2}})
#----------------------------------------------
#Task 4
def searchForStudentsWithNoInstruments():
    collection_students = db["students"]
    query = {"instrument": {"$exists": False}}
    x_students = collection_students.find(query)
    for student in x_students:
        print(student)
#----------------------------------------------
searchNameandAgeandteacher("violin",10,"Riebon")    
print(countstudentsfromateacher("Stock","piano"))
updateCourseTransfertoDifferentTeacher("Guo",2025,"CCCViolin")
searchForStudentsWithNoInstruments()

