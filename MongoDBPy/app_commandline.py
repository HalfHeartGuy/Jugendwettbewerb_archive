
#hi
import pymongo 
import json
import re

with open('D:\Workspace\Projects\Jugendwettbewerb_archive\MongoDBPy\commandlines.json', 'r') as f:
    commandlines = json.load(f)

commandlines = commandlines['commandlines']


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_app_Commandlines = myclient["App_commandlines"]
col_commandlines = db_app_Commandlines["commandlines"]



def searchCommandline(usercase: str, os: str) -> str:
    for command in commandlines:
        if command['usercase'].lower() == usercase.lower() and os in command['os']:
            return f"Command: {command['cmd']}\nDescription: {command['description']}\nExample: {command['example']}"
    return "No matching command found."

# Beispielaufruf
usercase_input = "create folder"
os_input = "Windows"
result = searchCommandline(usercase_input, os_input)
#print(result)




def add_new_commandlines(new_commandlines:list):
    col_commandlines.delete_many({commandlines})
    for one_commandline in new_commandlines:
        col_commandlines.insert_one(one_commandline)
##x = col_exercise.insert_one(mydict)

#add_new_commandlines(commandlines)

all_commandline = col_commandlines.find()

#for document in all_commandline:
#    print(f"one commandline:{document}")




# write a python function to search the commandline by usercase, using regular expression for following cases:
# 1. usercase contains "file". 2. usercase contains "folder". 3. usercase starts with "delete". 
# 4. usercase contains "current location". 
#def searchCommandlineByRegex(regex: str) -> list:
def searchCommandlineByRegex(regex: str) -> list:
    matching_commands = []
    for command in commandlines:
        if re.search(regex, command['usercase'], re.IGNORECASE):
            matching_commands.append(command)
    return matching_commands

def searchCommandlineByRegexBeginning(regex: str) -> list:
    matching_commands = []
    for command in commandlines:
        if re.search(f"^{regex}", command['usercase'], re.IGNORECASE):
            matching_commands.append(command)
    return matching_commands


# Example usage
regex_input = "file"
matching_commands = searchCommandlineByRegex(regex_input)
for command in matching_commands:
    print(f"Command: {command['cmd']}\nDescription: {command['description']}\nExample: {command['example']}")
    print("---------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
matching_commands = searchCommandlineByRegex("folder")
for command in matching_commands:
    print(f"Command: {command['cmd']}\nDescription: {command['description']}\nExample: {command['example']}")
    print("---------------------------------------------------")
matching_commands = searchCommandlineByRegexBeginning("delete")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")

for command in matching_commands:
    print(f"Command: {command['cmd']}\nDescription: {command['description']}\nExample: {command['example']}")
    print("---------------------------------------------------")
matching_commands = searchCommandlineByRegex("current location")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
for command in matching_commands:
    print(f"Command: {command['cmd']}\nDescription: {command['description']}\nExample: {command['example']}")
    print("---------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")





