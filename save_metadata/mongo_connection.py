from pymongo import MongoClient
import gridfs
import os

class MongoConnection:

    def __init__(self):
        mongo_uri = os.getenv("MONGO_URI","mongodb://localhost:27017")
        self.client = MongoClient(mongo_uri)
        self.db = self.client["data"]
        self.fs = gridfs.GridFS(self.db)
    
    def save_data(self,path,id):
        with open(path,"rb") as f:
            self.fs.put(f,uniqe_id=id)