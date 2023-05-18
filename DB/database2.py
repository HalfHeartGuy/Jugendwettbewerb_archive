

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nether69",
  database = "schema_pythonlernen"
)
mycursor = mydb.cursor()
def findStudentsFromSchool(schoolname:str) -> list:

    sql_query = "SELECT student.player_name FROM student JOIN school ON student.school = school.idschool WHERE school.name = %s"
    query_parameters = (schoolname,)

    mycursor.execute(sql_query,query_parameters)
    students = mycursor.fetchall()
    for student in students:
        print(student[0])




findStudentsFromSchool("PMHG")

def createanewSchool(idschool,name,address,country,city):
    sql_query = "INSERT INTO `schema_pythonlernen`.`school` (`idschool`, `name`, `address`, `country`, `city`) VALUES (%s, %s, %s, %s, %s)"
    query_parameters = (idschool,name,address,country,city,)
    mycursor.execute(sql_query,query_parameters)

    mydb.commit()

#createanewSchool("12","UMKRS","Wagnerstraße 4","DE","70567 Stuttgart")

def letOldStudentsToUniversity(age:int, country:str):
    sql_query = "UPDATE student SET school = '12' WHERE age > %s AND player_country = %s"
    query_parameters = (age,country,)
    mycursor.execute(sql_query,query_parameters)
    mydb.commit()

letOldStudentsToUniversity(20,"DE")


