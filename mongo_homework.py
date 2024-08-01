from pprint import pprint

USERNAME = "maksimtolmachev2010"
PASSWORD = "HZuwTvUzg97kWkOB"


from pymongo.mongo_client import MongoClient

uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.dizm1eb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client["Books"]

fantasy_books_coll = db["fantasy books"]

school_books_coll = db["school books"]

fantasy_books_coll.insert_one({"title": "Гра престолів", "cost": 500, "year_of_release": 2007, "number_of_pages": 206)

school_books_coll.insert_one({"title": "History", "class": 7, "number_of_pages": 78})
school_books_coll.insert_one({"title": "Maths", "class": 7, "number_of_pages": 68})
school_books_coll.insert_one({"title": "English", "class": 6, "number_of_pages": 49})
school_books_coll.insert_one({"title": "Science", "class": 7, "number_of_pages":86})
school_books_coll.insert_one({"title": "Art", "class": 7, "number_of_pages": 32})

query = {"title": {"$regex": "*History"}}
find_history = school_books_coll.find(query)
pprint(list(find_history))


