#!/usr/bin/env python
# Interate with MongoDB with PyMongo
from pymongo import MongoClient
import json, os

class MongoDB():
    def __init__(self, name, empty=True):
        self.db_name = name
        self.coll= set()
        if empty:
            if self.db_conn.get_database(self.db_name): # If the database exited, drop it
                self.db_conn.drop_database(self.db_name)
                self.db_conn = MongoClient()[self.db_name]
        else:
            self.db_conn = MongoClient()[self.db_name]

    def insertData(self, coll, json={}):
        # give data in json format
        self.coll.add(coll)
        result = self.db_conn[coll].insert_one(json)
        return result

    def queryData(self, coll, condition={}):
        # condition is a dict object
        result = []
        cursor = self.db_conn[coll].find(condition)
        if cursor!= None:
            for docu in cursor:
                object_id = docu.pop('_id')
                result.append(docu)
            return result
        else:
            return False

    def stopMongoDB(self):
        os.system('mongo admin --eval "printjson(db.shutdownServer())"')
