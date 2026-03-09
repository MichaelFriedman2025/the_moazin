from kafka_consumer import KafkaConsumer
from mongo_connection import MongoConnection
from elastic_connection import ElasticConnection
from speach_to_text import STT
from bds import BDS
from logs import Logger
import uuid


logger = Logger.get_logger(name="save_metadata/main")
es = ElasticConnection()
consumer = KafkaConsumer()
fs = MongoConnection()
stt = STT()
bds = BDS()


try:
    while True:
        msg = consumer.consumer.poll()
        if msg is None:
            continue
        if msg.error():
            logger.error(f"❌ the consumer have an Error: {msg.error()}")
            continue

        try:
            data = consumer.recive_data(msg)
            logger.debug(f"the data came successfully, the data: {data}")
            data["id"] = str(
                uuid.uuid5(namespace=uuid.NAMESPACE_DNS, name=data["file_name"])
            )
            logger.debug("the data.id maded successfully")

            fs.save_data(data["full_path"], data["id"])
            logger.debug("the data stored in mongo successfully")

            data["text_from_audio"] = str(stt.convert_stt(data["full_path"]))
            logger.debug("the text from stt insert in data successfully")

            bds_data = bds.make_metadata(data["text_from_audio"])
            data = {**data,**bds_data}
            es.insert_data(data)
            logger.debug(f"the data stored in elastic successfully, the data: {data}")

        except Exception as error:
            logger.error(f"❌ the consumer have an Error:{error}\n and data: {data}" )

except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.consumer.close()
