from pymongo import MongoClient
import datetime
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
    {"name": "John", "age": 10, "location": "Stuttgart"},
    {"name": "Jane", "age": 11, "instrument": "drums", "location": "Berlin"},
    {"name": "Bob", "age": 9, "instrument": "violin", "location": "Munich"},
    {"name": "Alice", "age": 13, "instrument": "piano", "location": "Hamburg"},
    {"name": "Charlie", "age": 14, "instrument": "drums", "location": "Frankfurt"},
    {"name": "David", "age": 15, "instrument": "drums", "location": "Cologne"},
    {"name": "Eve", "age": 16, "instrument": "piano", "location": "Dusseldorf"},
    {"name": "Frank", "age": 17, "instrument": "violin", "location": "Dortmund"},
    {"name": "Grace", "age": 18, "instrument": "drums", "location": "Essen"},
    {"name": "Heidi", "age": 19, "instrument": "piano", "location": "Leipzig"}
]

collection_student.insert_many(students)


schools = [
    {"name" : "CCCS", "location" : "Peking", "capacity" : 100}
]

collection_school.insert_many(schools)

teachers = [
    {"name": "F.Stock", "age": 30, "instrument": "piano", "school": "CCCS"},
    {"name": "F.Riebon", "age" : 40, "instrument": "violin", "school": "CCCS"},
    {"name": "H.Guo", "age" : 35, "instrument": "drums", "school": "CCCS"}
]

collection_teachers.insert_many(teachers)
course_day = datetime.datetime(year=2025, hour=7, minute=30, day=1,month=1,second=1)


courses = [
    {"instrument" : "piano" , "name" : "piano for advanced" , "teacher" : "F.Stock" , "students" : ["Alice", "Eve", "Heidi"],"time":"monday " + str(course_day.strftime('%H:%M,%Y'))},
    {"instrument" : "violin" , "name" : "Violin for beginners" , "teacher" : "F.Riebon" , "students" : ["John", "Bob", "Frank"],"time":"thursday " + str(course_day.strftime('%H:%M,%Y'))},
    {"instrument" : "drums" , "name" : "drums for advanced" , "teacher" : "H.Guo" , "students" : ["Jane", "Charlie", "David", "Grace"],"time":"monday " + str(course_day.strftime('%H:%M,%Y'))}
]

collection_courses.insert_many(courses)