import re
import pymongo
from pymongo import MongoClient


def search_players_by_age_school_lastname(lowerthanage, school_country, lastname):
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db_app_Commandlines = myclient["minecraft"]
    col_commandlines = db_app_Commandlines["users"]

    
    # Search for players matching the criteria
    players = col_commandlines.find({"age": {"$lt": lowerthanage}, "school.country": school_country, "lastname": {"$regex": lastname}})
    
    # Print the results
    for player in players:
        print(player)
    return players
def search_players_by_os(os):

    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db_app_Commandlines = myclient["minecraft"]
    col_commandlines = db_app_Commandlines["users"]

    players = col_commandlines.find({"os": os})
    
    for player in players:
        print(player)
    return players

def search_players_by_firstname(firstname):

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db_app_Commandlines = myclient["minecraft"]
    col_commandlines = db_app_Commandlines["users"]


    regex_firstname = re.compile(firstname, re.IGNORECASE)
    
    players = col_commandlines.find({"firstname": regex_firstname})
    
    for player in players:
        print(player)
    return players
#Write a code so that I can read what is the output of the functions above.
print(search_players_by_age_school_lastname(15, "USA", "J"))