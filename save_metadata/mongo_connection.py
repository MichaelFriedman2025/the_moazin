from pymongo import MongoClient
import gridfs
import os
from logs import Logger


class MongoConnection:

    def __init__(self):
        self.logger = Logger.get_logger(name="save_metadat/mongo_connection")
        try:
            mongo_uri = os.getenv("MONGO_URI","mongodb://localhost:27017")
            self.client = MongoClient(mongo_uri)
            self.db = self.client["data"]
            self.fs = gridfs.GridFS(self.db)
            self.logger.info("the connection to mongo db connect successfully")
        except Exception as error:
            self.logger.error(f"connection to mongo failed beacose: {error}")
    
    def save_data(self,path,id):
        try:
            with open(path,"rb") as f:
                self.fs.put(f,uniqe_id=id)
            self.logger.info("the data stored in mongo db successfully")
        except Exception as error:
            self.logger.error(f"the path is not correct beacose: {error}")
