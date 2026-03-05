from confluent_kafka import Consumer, Message
import json 
import os

class KafkaConsumer:

    def __init__(self):
        kafka_uri = os.getenv("KAFKA_URI","localhost:9092")
        consumer_config = {"bootstrap.servers": kafka_uri,"group.id": "save_metadata","auto.offset.reset": "earliest"}
        self.consumer = Consumer(consumer_config)
        self.consumer.subscribe(["metadata"])
    
    @staticmethod
    def recive_data(msg:Message):
        value = msg.value().decode("utf-8")
        return json.loads(value)






