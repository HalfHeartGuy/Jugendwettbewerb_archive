
'''
homework 2024-6-28
database: music_school
task 1:
- create collections:
   - "students(name:str,age:int,location:string)", 
   - "schools(name:str, location:str, capacity:int)", 
   - "course(instrument:str, name:str, time:str, teacher:str,students:list[str], school:str)"
   - "teacher"(instrument(s):list[str], name:str, age:int, school:str)

taks 2:
- insert data into the collections. with at least 1 music school, and 3 teachers with different instruments , 10 students  

task 3 (write queries):
- to lookup young students, from echterdingen under age 10 learning, "violion" from teacher "Frau Riebon" 
- to lookup, how many students are learning "piano" from teacher "Frau Stock"
- for course "violin" in 2025, update the course belonging to "Frau Riebon" to "Herr Guo"
- finde students who are not in any course*
'''

import datetime

now_time = datetime.datetime.now()
print(now_time)

your_birthday = datetime.datetime(2010, 1, 1, 7, 30, 10)
print("your_birthday",  your_birthday.strftime('%d.%m.%Y %H:%M:%S'))
# tag.monat.Jahr
#create one time object for wednesday, 7:30

#course_day = datetime.datetime(year=2025, hour=7, minute=30, day=1)
# "wednesday, 7:30" (year)

import pymongo
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_music_school = mongo_client["music_school"]

class Student:
    def __init__(self, name, age, instrument,location):
        self.name = name
        self.age = age
        self.instrument = instrument
        self.location = location

    def store_in_mongoDB(self):
      col_students = db_music_school["students"]
      col_students.insert_one(self.__dict__)

    def update_in_mongoDB(self):
        col_students = db_music_school["students"]
        col_students.update_one({"name":self.name}, {"$set": {"age": self.age, "instrument": self.instrument, "location": self.location}})

    def delete_in_mongoDB(self):
        col_students = db_music_school["students"]
        col_students.delete_one({"name":self.name})
    def __str__(self):
        return f"Student(name:{self.name}, age:{self.age}, instrument:{self.instrument}, location:{self.location})"

def find_students(query:dict) -> list[Student]:
    col_students = db_music_school["students"]
    students = col_students.find(query)
    result = []  
    
    for student in students:
        if "instrument" not in student:
            student["instrument"] = None
        result.append(Student(student["name"], student["age"], student["instrument"], student["location"]))   
    return result

print("student result 1")
result = find_students({"age":{"$lt": 12}})
for student in result:
    print(student)
print("student result 2")
result = find_students({"age":10})
for student in result:
    print(student)

class School:
    def __init__(self, name, location, capacity):
        self.name = name
        self.location = location
        self.capacity = capacity

    def store_in_mongoDB(self):
        col_schools = db_music_school["schools"]
        col_schools.insert_one(self.__dict__)

    def update_in_mongoDB(self):
        col_schools = db_music_school["schools"]
        col_schools.update_one({"name":self.location}, {"$set": {"location": self.name, "capacity": self.capacity}})

    def __str__(self):
        return f"School(name:{self.name}, location:{self.location}, capacity:{self.capacity})"
def find_schools(query:dict) -> list[School]:
    col_schools = db_music_school["schools"]
    schools = col_schools.find(query)
    result = []  
    for school in schools:
        result.append(School(school["name"], school["location"], school["capacity"]))   
    return result
print("schoolresult")
schoolresult = find_schools({"name":"CCCS"})
for school in schoolresult:
    print(school)
print("schoolresult2")
schoolresult2 = find_schools({})
for school in schoolresult2:
    print(school)




class Course:
    def __init__(self, instrument, name, time, teacher, students):
        self.instrument = instrument
        self.name = name
        self.time = time
        self.teacher = teacher
        self.students = students

    def store_in_mongoDB(self):
        col_courses = db_music_school["courses"]
        col_courses.insert_one(self.__dict__)

    def update_in_mongoDB(self):
        col_courses = db_music_school["courses"]
        col_courses.update_one({"name":self.name}, {"$set": {"instrument": self.instrument, "time": self.time, "teacher": self.teacher, "students": self.students}})

    def __str__(self):
        return f"Course(instrument:{self.instrument}, name:{self.name}, time:{self.time}, teacher:{self.teacher}, students:{self.students})"
def find_courses(query:dict) -> list[Course]:
    col_courses = db_music_school["courses"]
    courses = col_courses.find(query)
    result = []  
    for course in courses:
        print(course)
        result.append(Course(course["instrument"], course["name"], course["time"], course["teacher"], course["students"]))   
    return result
print("course_result")
course_result = find_courses({"name":"violin"})
for course in course_result:
    print(course)
print("course_result2")
course_result2 = find_courses({})
for course in course_result2:
    print(course)
print("course_result3")
course_result3 = find_courses({"teacher":"F.Riebon"})
for course in course_result3:
    print(course)

class Teacher:
    def __init__(self, name, age, instrument, school):
        self.name = name
        self.age = age
        self.instrument = instrument

        self.school = school

    def store_in_mongoDB(self):
        col_teachers = db_music_school["teachers"]
        print("!teacher!")
        print(self.__dict__)
        col_teachers.insert_one(self.__dict__)

    def update_in_mongoDB(self):
        col_teachers = db_music_school["teachers"]
        col_teachers.update_one({"name":self.name}, {"$set": {"age": self.age, "instrument": self.instrument, "school": self.school}})

    def __str__(self):
        return f"Teacher(name:{self.name}, age:{self.age}, instrument:{self.instrument},school:{self.school})"

def find_teachers(query:dict) -> list[Teacher]:
    col_teachers = db_music_school["teachers"]
    teachers = col_teachers.find(query)
    result = []  
    for teacher in teachers:
        print(teacher)
        result.append(Teacher(teacher["instrument"], teacher["name"], teacher["age"], teacher["school"]))   
    return result

teacherresult = find_teachers({"name":"F.Stock"})
print("teacherresult1")
for teacher in teacherresult:
    print(teacher)
print("teacherresult2")
teacherresult2 = find_teachers({})
for teacher in teacherresult2:
    print(teacher)
    
