from kafka_consumer import KafkaConsumer
from mongo_connection import MongoConnection
from elastic_connection import ElasticConnection
from speach_to_text import STT
import uuid

es = ElasticConnection()
consumer = KafkaConsumer()
fs = MongoConnection()
stt = STT()

try:
    while True:
        msg = consumer.consumer.poll()
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue
        
        data = consumer.recive_data(msg)
        data["id"] = str(uuid.uuid5(namespace=uuid.NAMESPACE_DNS,name=data["file_name"]))
        fs.save_data(data["full_path"],data["id"])
        data["text_from_audio"] = stt.convert_stt(data["full_path"])
        es.insert_data(data)

except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.consumer.close()
