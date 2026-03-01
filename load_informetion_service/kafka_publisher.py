from confluent_kafka import Producer
import json
import os

class KafkaPublisher:

    def __init__(self):
        kafka_uri = os.getenv("KAFKA_URI","localhost:9092")
        producer_config = {"bootstrap.servers": kafka_uri}
        self.producer = Producer(producer_config)

    def prduce_data(self,data):
        value = json.dumps(data).encode("utf-8")
        self.producer.produce(topic="metadata",value=value)
        self.producer.flush()