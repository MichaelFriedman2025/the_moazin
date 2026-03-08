from elasticsearch import Elasticsearch
import os



class ElasticConnection:

    def __init__(self):
        elastic_uri = os.getenv("ELASTIC_URI", "http://localhost:9200")
        self.client = Elasticsearch(elastic_uri)
        self.doing_scema()

    def doing_scema(self):
        if self.client.indices.exists(index="audio"):
            self.client.indices.delete(index="audio")
        scema = {
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "file_name": {"type": "keyword"},
                    "creation_date": {"type": "keyword"},
                    "size": {"type": "integer"},
                    "text_from_audio":{"type": "text"}
                }
            }
        }
        self.client.indices.create(index="audio",body=scema)

    def insert_data(self, data):
        self.client.update(index="audio", id=data["id"], doc=data,doc_as_upsert=True)
