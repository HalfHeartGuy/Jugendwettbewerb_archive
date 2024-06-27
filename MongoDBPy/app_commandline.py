
#hi
import pymongo 
import json
import re
file_path = "D:\Workspace\Projects\Jugendwettbewerb_archive\MongoDBPy\commandlines.json"

#with open(file_path, "r") as file:
#    commandlines = json.load(file)



commandlines = \
[
 {"usercase":"create folder", "cmd": "mkdir", "os":["Windows", "Linux", "MacOs"], "description": "input: path/folder name", "example": "mkdir folder1"},
 {"usercase":"enter folder", "cmd": "cd", "os":["Windows", "MacOs"], "description": "input: path name", "example": "cd  D:\Workspace\Projects\Jugendwettbewerb_archive\MongoDBPy"},
 {"usercase":"delete folder", "cmd": "rmdir", "os":["Windows"], "description": "input:Folder name", "example": "rmdir ordnername"},
 {"usercase":"delete folder", "cmd": "rm -rf", "os":["Linux,MacOS"], "description": "input:Folder name. ACHTUNG: ORDNER WIRD OHNE HINWEIS GELÖSCHT", "example": "rm -rf ordnername"},
 {"usercase":"create file", "cmd": "echo. >", "os":["Windows"], "description": "input:echo. > file.txt", "example": "echo. > example.txt"},
 {"usercase":"create file", "cmd": "touch", "os":["macOS"], "description": "input:touch filename", "example": "touch filename.txt"},
 {"usercase":"delete file", "cmd": "rm", "os":["Windows", "Linux", "MacOs"], "description": "input: file name name", "example": "rm file1.txt"},
 {"usercase":"create one new python environment", "cmd": "python m -venv", "os":["Windows"], "description": "input: environment name", "example": "python -m venv myenv"},
 {"usercase":"create one new python environment", "cmd": "python(python version) m -venv", "os":["macOS"], "description": "input: python version(1,2,3); environement name", "example": "python3 -m venv myenv"},
 {"usercase":"activate one python enviroment", "cmd": "envname\Scripts\activate", "os":["Windows"], "description": "input: environment name", "example": "myenv\Scripts\activate"},
 {"usercase":"activate one python enviroment", "cmd": "source myenv/bin/activate", "os":["macOS"], "description": "input: environment name", "example": "source myenv/bin/activate"},
 {"usercase":"install a new module in one python environment", "cmd": "pip install", "os":["Windows","macOS"], "description": "input: module name", "example": "pip install module_name"},
 {"usercase":"open one file for reading in windows", "cmd": "type", "os":["Windows"], "description": "input: filename.txt", "example": "type filename.txt"},
 {"usercase":"open one file for writing in macOS", "cmd": "cat", "os":["macOS"], "description": "input: filename.txt", "example": "cat filename.txt"},
 {"usercase":"open one file for reading in Windows", "cmd": "echo text. >", "os":["Windows"], "description": "input: text, filename.txt", "example": "echo Dies ist ein Beispieltext. > filename.txt"},
 {"usercase":"open one file for reading in macOS", "cmd": "echo ""text"". >", "os":["macOS"], "description": "input: text, filename.txt;You don´t need the double quotation marks in the command", "example": "echo ""Dies ist ein Beispieltext."" > filename.txt"}




]


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





