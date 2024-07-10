import datetime     

now_time = datetime.datetime.now()
print(now_time.minute)


your_birthday = datetime.datetime(1990, 1, 1)
print(f"Your birthday is {your_birthday}")




class Student:
    def __init__(self,name,age,instrument):
        self.name = name
        self.age = age
        self.location = instrument

    def store_in_mongoDB(self):
        col_students = db["students"]
        col_students.insert_one(self.__dict__)

import pymongo
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
db = mongo_client['music_school']
collection_students = db['students']

student1 = Student("John", 25, "drums")
student1.store_in_mongoDB()