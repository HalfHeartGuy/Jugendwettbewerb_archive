

# homework 2024-7-7
# Task 1: complete module music_school_germany_backend_functions.py with classes(functions) for school, course, teacher
# Task 2: for each class/collection, write some find-functions find_xxx in same file
# Task 3: in current file music_school_germany_backend_functions.py, write following functions without usage of DB
# - create_student(name:str, age:int, location:str) -> None
# - create_teacher(xxx) -> None
# - create_course(xxx) -> None
# - create_school(xxx) -> None

# - get_all_teachers(query) -> list[Teacher]
# - get_all_courses(query) -> list[Course]
# - get_all_schools(query) -> list[School]
# - get_all_students(query) -> list[Student]

# - update_student(name:str, age:int, location:str) -> None
# - update_teacher(xxx) -> None
# - update_course(xxx) -> None
# - update_school(xxx) -> None

# - delete_student(name:str, age:int, location:str) -> None
# - delete_teacher(xxx) -> None
# - delete_course(xxx) -> None
# - delete_school(xxx) -> None

# task 4: For each function above in task 3, write some tests




from music_school_germany_datamodel import *
import music_school_germany_datamodel as msgd


def create_student(name, age, instrument,location):
    student = Student(name, age, instrument,location)
    student.store_in_mongoDB()


#create student
create_student("John", 25, "drums","Stuttgart")


def get_all_students(query:dict) -> list[Student]:
    return msgd.find_students(query)
#get all students
get_all_students({})

def update_student(name, age, instrument, location):
    student = Student(name, age, instrument,location)
    student.update_in_mongoDB()
# update student
update_student("John", 25, "drums","Zuffenhausen")

def delete_student(name, age, instrument,location):
    student = Student(name, age, instrument,location)
    student.delete_in_mongoDB()
#delete student
delete_student("John", 25, "drums","Zuffenhausen")

def create_school(name, location, capacity):
    school = School(name, location, capacity)
    school.store_in_mongoDB()
#create school
create_school("school1", "stuttgart", 100)

def update_school(name, location, capacity):
    school = School(name, location, capacity)
    school.update_in_mongoDB()

#update school
update_school("Central music school", "Peking", 200)

def get_all_schools(query:dict) -> list[School]:
    return msgd.find_schools(query)

#get all schools
get_all_schools({})

def delete_school(name, location, capacity):
    school = School(name, location, capacity)
    school.delete_in_mongoDB()
#delete school
delete_school("school1", "stuttgart", 100)

def create_teacher(name, age, instrument,school):
    teacher = Teacher(name, age,instrument, school)
    teacher.store_in_mongoDB()


#create teacher
create_teacher("F.Hans", 30, "drums","CCCS")

def update_teacher(name, age, instrument,school):
    teacher = Teacher(name, age,instrument, school)
    teacher.update_in_mongoDB()

#update teacher
update_teacher("F.Hans", 30, "violin","CCCS")

def get_all_teachers(query:dict) -> list[Teacher]:
    return msgd.find_teachers(query)
#get all teachers
get_all_teachers({})

def delete_teacher(name, age, instrument,school):
    teacher = Teacher(name, age,instrument, school)
    teacher.delete_in_mongoDB()
#delete teacher
delete_teacher("F.Hans", 30, "violin","CCCS")

def create_course(instrument, name, time, teacher, students):
    course = Course(instrument, name, time, teacher, students)
    course.store_in_mongoDB()
course_day = datetime.datetime(year=2025, hour=19, minute=50, day=1,month=1,second=1)
#create course
create_course("saxophone","saxophone for beginners" , "friday " + str(course_day.strftime("%H:%M,%Y")), "F.Hans", "John")

def update_course(instrument, name, time, teacher, students):
    course = Course(instrument, name, time, teacher, students)
    course.update_in_mongoDB()
#update course
update_course("saxophone","saxophone for beginners" , "friday " + str(course_day.strftime("%H:%M,%Y")), "F.Meyer", "John")

print("get all courses")
def get_all_courses(query:dict) -> list[Course]:
    return msgd.find_courses(query)
# get all courses
get_all_courses({})

def delete_course(instrument, name, time, teacher, students):
    course = Course(instrument, name, time, teacher, students)
    course.delete_in_mongoDB()
#delete course
delete_course("saxophone","saxophone for beginners" , "friday " + str(course_day.strftime("%H:%M,%Y")), "F.Meyer", "John")
