#!/usr/bin/python3
 
import pymongo
 
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient["test"]
mycol = mydb["fuck"]
test = { "name": "ann", "number": "1", "url": "https://www.runoob.com" }
x=mycol.insert_one(test)
print(x)
