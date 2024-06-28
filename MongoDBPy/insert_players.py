from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['minecraft']
collection = db['users']

# Sample data
players = [
    {
        "firstname": "Alex",
        "lastname": "Johnson",
        "age": 12,
        "school": {"name": "Greenwood High", "city": "Austin", "country": "USA"},
        "os": "windows"
    },
    {
        "firstname": "Bella",
        "lastname": "Smith",
        "age": 15,
        "school": {"name": "Hillview Academy", "city": "Toronto", "country": "Canada"},
        "os": "macos"
    },
    {
        "firstname": "Charlie",
        "lastname": "Brown",
        "age": 14,
        "school": {"name": "Riverdale High", "city": "Chicago", "country": "USA"},
        "os": "linux"
    },
    {
        "firstname": "Dana",
        "lastname": "White",
        "age": 13,
        "school": {"name": "Sunnydale School", "city": "Sydney", "country": "Australia"},
        "os": "windows"
    },
    {
        "firstname": "Ethan",
        "lastname": "Clark",
        "age": 16,
        "school": {"name": "Mountain Ridge", "city": "Denver", "country": "USA"},
        "os": "playstation"
    },
    {
        "firstname": "Fiona",
        "lastname": "Davis",
        "age": 12,
        "school": {"name": "Lakeside School", "city": "Seattle", "country": "USA"},
        "os": "xbox"
    },
    {
        "firstname": "George",
        "lastname": "Harris",
        "age": 15,
        "school": {"name": "Pine Hill School", "city": "Vancouver", "country": "Canada"},
        "os": "macos"
    },
    {
        "firstname": "Hannah",
        "lastname": "Lewis",
        "age": 13,
        "school": {"name": "Cedar Grove", "city": "San Francisco", "country": "USA"},
        "os": "linux"
    },
    {
        "firstname": "Ian",
        "lastname": "Walker",
        "age": 14,
        "school": {"name": "Elmwood School", "city": "London", "country": "UK"},
        "os": "windows"
    },
    {
        "firstname": "Jenna",
        "lastname": "Martinez",
        "age": 16,
        "school": {"name": "Northview High", "city": "New York", "country": "USA"},
        "os": "playstation"
    }
]

# Insert documents
collection.insert_many(players)

print("Documents inserted successfully.")
