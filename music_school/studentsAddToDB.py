from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['music_school']

collection_student = db['students']
collection_school = db['schools']
collection_teachers = db["teachers"]
collection_courses = db["courses"]
x = collection_student.delete_many({})
x = collection_school.delete_many({})
x = collection_teachers.delete_many({})
x = collection_courses.delete_many({})

students = [
    {"name": "John", "age": 10},
    {"name": "Jane", "age": 11, "instrument": "drums"},
    {"name": "Bob", "age": 9, "instrument": "violin"},
    {"name": "Alice", "age": 13, "instrument": "piano"},
    {"name": "Charlie", "age": 14, "instrument": "drums"},
    {"name": "David", "age": 15, "instrument": "drums"},
    {"name": "Eve", "age": 16, "instrument": "piano"},
    {"name": "Frank", "age": 17, "instrument": "violin"},
    {"name": "Grace", "age": 18, "instrument": "drums"},
    {"name": "Heidi", "age": 19, "instrument": "piano"}
]

collection_student.insert_many(students)


schools = [
    {"name" : "CCCS", "location" : "Peking", "capacity" : 100}
]

collection_school.insert_many(schools)

teachers = [
    {"name": "Stock", "age": 30, "instrument": "piano", "school": "CCCS"},
    {"name": "Riebon", "age" : 40, "instrument": "violin", "school": "CCCS"},
    {"name": "Guo", "age" : 35, "instrument": "drums", "school": "CCCS"}
]

collection_teachers.insert_many(teachers)
time = 2025

courses = [
    {"instrument" : "piano" , "name" : "CCCPiano" , "teacher" : "Stock" , "students" : ["Alice", "Eve", "Heidi"],"time":time},
    {"instrument" : "violin" , "name" : "CCCViolin" , "teacher" : "Riebon" , "students" : ["John", "Bob", "Frank"],"time":time},
    {"instrument" : "drums" , "name" : "CCCDrums" , "teacher" : "Guo" , "students" : ["Jane", "Charlie", "David", "Grace"],"time":time}
]

collection_courses.insert_many(courses)