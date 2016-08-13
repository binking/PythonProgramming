from pymongo import MongoClient
from datetime import datetime

def Main():
    client = MongoClient()
    db = client['test']
    coll = db['restaurants']

    cursor = db.restaurants.aggregate([
           {"$group": {"_id": "$borough", "count": {"$sum": 1}}}
        ])
    for document in cursor:
        print(document)

    cursor = db.restaurants.aggregate([
        {"$match": {"borough": "Queens", "cuisine": "Brazilian"}},# Filter
        {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}}
    ])
    for document in cursor:
        print(document)


if __name__=='__main__':
    Main()

