import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nether69",
  database = "schema_pythonlernen"
)
mycursor = mydb.cursor()


#for x in myresult:
#  print(x)
def registerMultipleNewPlayer(persons:list):
  sql_insert = "INSERT INTO `schema_pythonlernen`.`mc_player` (`player_name`, `player_country`, `age`, `school`) VALUES (%s, %s, %s,%s);"
  mycursor.executemany(sql_insert,persons)


  mydb.commit()


persons_list = [("Tom","DE",70,2),
                ("Michael","DE",14,2)]
registerMultipleNewPlayer(persons_list)


def countplayer():
  mycursor.execute("SELECT COUNT(player_ID) from mc_player;")

  result = mycursor.fetchone()
  print(result[0])
#countplayer()

def getDetailsofOldPlayer():
  mycursor.execute("SELECT * FROM mc_player WHERE age > 50")
  myresult = mycursor.fetchall()

  for x in myresult:
    print(x)
#getDetailsofOldPlayer()
