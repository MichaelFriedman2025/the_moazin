from confluent_kafka import Producer
import json
import os
from logs import Logger


class KafkaPublisher:

    def __init__(self):
        self.logger = Logger.get_logger(name="load_informetion/kafka_publisher")
        kafka_uri = os.getenv("KAFKA_URI","localhost:9092")
        try:
            producer_config = {"bootstrap.servers": kafka_uri}
            self.producer = Producer(producer_config)
            self.logger.info("the kafka publisher connect successfully")
        except Exception as error:
            self.logger.error("ooooopsss kafka bublisher not connect beacuse: ",error)


    def prduce_data(self,data):
        try:
            value = json.dumps(data).encode("utf-8")
            self.producer.produce(topic="metadata",value=value)
            self.producer.flush()
            self.logger.info("the data prduce successfully")
        except Exception as error:
            self.logger.error("ooooopsss the data not prudced beacuse: ",error)