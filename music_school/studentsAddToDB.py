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
    {"name": "John", "age": 10, "instrument": "drums"},
    {"name": "Jane", "age": 11, "instrument": "piano"},
    {"name": "Bob", "age": 12, "instrument": "drums"},
    {"name": "Alice", "age": 13, "instrument": "violin"},
    {"name": "Charlie", "age": 14, "instrument": "piano"},
    {"name": "David", "age": 15, "instrument": "piano"},
    {"name": "Eve", "age": 16, "instrument": "violin"},
    {"name": "Frank", "age": 17, "instrument": "drums"},
    {"name": "Grace", "age": 18, "instrument": "piano"},
    {"name": "Heidi", "age": 19, "instrument": "piano"}
]

collection_student.insert_many(students)


schools = [
    {"name" : "CCCS", "location" : "Peking", "capacity" : 100}
]

collection_school.insert_many(schools)

teachers = [
    {"name": "Stock", "age": 30, "instrument": "violin", "school": "CCCS"},
    {"name": "Riebon", "age" : 40, "instrument": "drums", "school": "CCCS"},
    {"name": "Guo", "age" : 35, "instrument": "piano", "school": "CCCS"}
]

collection_teachers.insert_many(teachers)


courses = [
    {"instrument" : "violin" , "name" : "CCCViolin" , "teacer" : "Stock" , "students" : ["Alice", "Eve"]},
    {"instrument" : "drums" , "name" : "CCCDrums" , "teacer" : "Riebon" , "students" : ["John", "Bob", "Frank"]},
    {"instrument" : "piano" , "name" : "CCCPiano" , "teacer" : "Guo" , "students" : ["Jane", "Charlie", "David", "Grace", "Heidi"]}
]

collection_courses.insert_many(courses)