


from music_school_germany_datamodel import *
import music_school_germany_datamodel as msgd


def create_student(name, age, location):
    student = Student(name, age, location)
    student.store_in_mongoDB()

def get_all_students(query:dict) -> list[Student]:
    return msgd.find_students(query)

def create_school(name, location, capacity):
    school = School(name, location, capacity)
    school.store_in_mongoDB()
create_school("school1", "stuttgart", 100)

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