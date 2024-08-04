import datetime
from pprint import pprint

USERNAME = "maksimtolmachev2010"
PASSWORD = "HZuwTvUzg97kWkOB"


from pymongo.mongo_client import MongoClient
from bson import Decimal128

uri = f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.dizm1eb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client["new_db"]

prod_coll = db["products"]

products = [
    {
        "title": "bread",
        "price": 45,
        "remains": 678,
        "comment": "no suger",
        "contain_gluten": True,
        "date": datetime.datetime.utcnow()

    },
    {
        "title": "soft drink",
        "price": 24,
        "remains": 567,
        "comment": "really sweat",
        "contain_gluten": False,
        "date": datetime.datetime(year=2024, month=8, day=10, hour=5)

    },
    {
        "title": "milk",
        "price": 70,
        "remains": 7098,
        "comment": "suger contain",
        "contain_gluten": True,
        "date": datetime.datetime.now() - datetime.timedelta(days=1)

    },
    {
        "title": "vinegar",
        "price": 27,
        "remains": 788,
        "comment": "suger contain, taste like apple",
        "contain_gluten": False,
        "date": datetime.datetime.now() + datetime.timedelta(days=56)
    }
]
prod_coll.insert_many(products)

# query = []
# responce = prod_coll.aggregate(query)
# pprint(list(responce))

query = [
    {"$match": {"contain_gluten": False}}

]
query = [
    {"$match": {"contain_gluten": False}}
]
responce = prod_coll.aggregate(query)
pprint(list(responce))

