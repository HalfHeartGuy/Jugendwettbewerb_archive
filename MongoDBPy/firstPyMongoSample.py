import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_minecraft_player = myclient["minecraft"]
col_minecraft = db_minecraft_player["users"]


one_document = col_minecraft.find_one()
print(f"find out document: {one_document}")



mydict = { "Firstname": "John", "Lastname": "Douglas","Age": 25,"school": ["MIT","High Street 52"], "gender":"m", "country":"US"}


x = col_minecraft.insert_one(mydict)


all_documents = col_minecraft.find()

for document in all_documents:
    print(f"document: {document}")


print(f"find all documents: {all_documents}")
