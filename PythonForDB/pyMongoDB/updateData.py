from pymongo import MongoClient
from datetime import datetime

def Main():
    client = MongoClient()
    db = client['test']
    coll = db['restaurants']
    result1 = coll.update_one(
        {"name": "Juni"},
        {
            "$set": {
                "cuisine": "American (New)"
            },
            "$currentDate": {"lastModified": True}
        }
    )

    result2 = coll.update_one(
        {"restaurant_id": "41156888"},
        {"$set": {"address.street": "East 31st Street"}}
    )

    results = coll.update_many(
        {"address.zipcode": "10016", "cuisine": "Other"},
        {
            "$set": {"cuisine": "Category To Be Determined"},
            "$currentDate": {"lastModified": True}
        }
    )

    replacement = coll.replace_one(
        {"restaurant_id": "41704620"},
        {
            "name": u"蒙奇D路飞",
            "address": {
                "coord": [-73.9557413, 40.7720266],
                "building": "1480",
                "street": u"清华东路35号",
                "zipcode": "100083"
            }
        }
    )
    vertify_replacement = cursor = coll.find({'name' : u"蒙奇D路飞"})
    print('Update One document')
    print('matching :', result1.matched_count)
    print('modified :', result1.modified_count)

    print('Update Embeded Field')
    print('matching :', result2.matched_count)
    print('modified :', result2.modified_count)

    print('Update many documents')
    print('matching :', results.matched_count)
    print('modified :', results.modified_count)

    print('Replace One document')
    print('matching :', replacement.matched_count)
    print('modified :', replacement.modified_count)

    for docu in vertify_replacement:
        print(docu)

if __name__=='__main__':
    Main()


