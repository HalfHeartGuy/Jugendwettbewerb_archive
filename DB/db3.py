import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nether69",
  database = "schema_pythonlernen"
)
mycursor = mydb.cursor()

