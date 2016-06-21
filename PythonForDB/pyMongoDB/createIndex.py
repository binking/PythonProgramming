from pymongo import MongoClient
from datetime import datetime
import pymongo
def Main():
    client = MongoClient()
    db = client['test']
    index1 = db['restaurants'].create_index([
        ("cuisine", pymongo.ASCENDING)
    ])
    index2 = db.restaurants.create_index([
        ("cuisine", pymongo.ASCENDING),
        ("address.zipcode", pymongo.DESCENDING)
    ])
    print(index1)
    print(index2)

if __name__=='__main__':
    Main()