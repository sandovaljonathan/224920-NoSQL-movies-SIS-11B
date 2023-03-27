from pymongo import MongoClient

CLIENT = MongoClient('mongodb://localhost:27017')
db = CLIENT['movies']

collection = db['movies_collection']