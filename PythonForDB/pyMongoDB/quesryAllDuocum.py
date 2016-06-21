from pymongo import MongoClient
import json
def findAll():
    client = MongoClient()
    db = client['test']
    coll = db.restaurants
    cursor = coll.find()
    for document in cursor:
        print(document)

def find_field_in_embeded_docu():
    client = MongoClient()
    db = client['test']
    coll = db.restaurants
    cursor = coll.find({'address.street' : '第二大道'})
    print(type(cursor))
    for document in cursor:
        print(type(document))
        data = json.dumps(document)
        print(data)

def find_field_in_array():
    client = MongoClient()
    db = client['test']
    coll = db.restaurants
    cursor = coll.find({'grades.grade' : 'B'})
    for document in cursor:
        print(document)

def find_field_use_comparison():
    client = MongoClient()
    db = client['test']
    coll = db.restaurants
    cursor = coll.find({'grades.score' : {'$gt':3}})
    for document in cursor:
        print(document)

def find_field_use_and():
    client = MongoClient()
    db = client['test']
    coll = db.restaurants
    cursor = coll.find({'address.zipcode' : '10075', 'cuisine' : 'Italian'})
    for document in cursor:
        print(document)

def find_field_use_or():
    client = MongoClient()
    db = client['test']
    coll = db.restaurants
    cursor = coll.find({'$or' : [{'cuisine' : 'Italian'},
                                {'address.zipcode' : '10075'}]})
    for document in cursor:
        print(document)

if __name__=="__main__":
    print('find_field_in_embeded_docu')
    find_field_in_embeded_docu()
    print('-'*30)
    #print('find_field_in_array')
    #find_field_in_array()
    #print("-"*30)
    #print('find_field_use_comparison')
    #find_field_use_comparison()
    #print("-"*30)
    #print('find_field_use_and')
    #find_field_use_and()
    #print("-"*30)
    #print('find_field_use_or')
    #find_field_use_or()
    #print("-"*30)
