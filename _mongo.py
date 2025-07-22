from pymongo import MongoClient

client = MongoClient("")
db = client["acl_db"]
collection = db["acl_collection"]