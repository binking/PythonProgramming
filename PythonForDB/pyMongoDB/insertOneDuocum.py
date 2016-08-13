#!/usr/bin/env python
# Shutdown MongoDB server : mongo admin --eval "printjson(db.shutdownServer())"
# or : db = connect("localhost:27017/admin"); db.shutdownServer();
from pymongo import MongoClient
from datetime import datetime

def Main():
    client = MongoClient()
    db = client['test']
    print(dir(client))
    result = db.restaurants.insert_one(
    {
        "address": {
            "street": "第二大道",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
            },
        "borough": "曼哈顿",
        "cuisine": "意大利风味",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "江智彬",
        "restaurant_id": "41704620"
    } )
    print(result.inserted_id)

if __name__=="__main__":
    Main()