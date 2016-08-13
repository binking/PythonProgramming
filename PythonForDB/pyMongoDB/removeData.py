from pymongo import MongoClient
from datetime import datetime

def Main():
    client = MongoClient()
    db = client['test']
    coll = db['restaurants']
    result = coll.delete_many({"borough": u"曼哈顿"})
    print(result.deleted_count)

if __name__=='__main__':
    Main()