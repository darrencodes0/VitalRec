from pymongo import MongoClient

#put whatever local host but mongodbcompass needs to have corresponding url
URL = "mongodb://localhost:27017"
client = MongoClient(URL)
db = client["users"]
user_table = db["user_credentials"]

