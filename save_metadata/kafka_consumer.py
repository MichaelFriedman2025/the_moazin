from confluent_kafka import Consumer, Message
import json 
import os
from logs import Logger

class KafkaConsumer:

    def __init__(self):
        self.logger = Logger.get_logger(name="save_metadata/kafka_consumer")
        try:
            kafka_uri = os.getenv("KAFKA_URI","localhost:9092")
            consumer_config = {"bootstrap.servers": kafka_uri,"group.id": "save_metadata","auto.offset.reset": "earliest"}
            self.consumer = Consumer(consumer_config)
            self.consumer.subscribe(["metadata"])
            self.logger.info("the kafka consumer connected successfully ")
        except Exception as error:
            self.logger.error(f"the connection to kafka consumer failed beacose: {error}")
    
    @staticmethod
    def recive_data(msg:Message):
        value = msg.value().decode("utf-8")
        return json.loads(value)






