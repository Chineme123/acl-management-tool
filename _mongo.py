from pymongo import MongoClient

client = MongoClient("mongodb+srv://chineme2101:xGaPZeocZ9YQX6pc@cluster0.eeocqz8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["acl_db"]
collection = db["acl_collection"]