import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nether69",
  database = "schema_pythonlernen"
)
mycursor = mydb.cursor()



def selectAllPersons():

  global x
  mycursor.execute("select * from mc_player")
  for x in mycursor:
    print(x)
selectAllPersons()

print(type(mycursor))
selectAllPersons()




def createonePersonInDb(person:list,myDB):
    sql_insert = "INSERT INTO `schema_pythonlernen`.`mc_player` (`player_ID`,`player_name`, `player_country`, `age`, `school`) VALUES (%s, %s, %s, %s,&s);"

    mycursor.execute(sql_insert,person)
    mydb.commit()

myPersonList = []


for i in range(5):
  onePerson = (20,f"Vorname{i}",f"player_country{i}", 10 + i,"2020-01-01")
  myPersonList.append(onePerson)



createonePersonInDb(20,"Scholz","DE",60,7)

selectAllPersons()


print("mycursor.rowcount:" , mycursor.rowcount)

