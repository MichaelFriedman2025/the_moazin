from pathlib import Path

from extract_metadata import Metadata as md
from kafka_publisher import KafkaPublisher
from logs import Logger

logger = Logger.get_logger(name="load_informetion/main")
producer = KafkaPublisher()
try:
    logger.info("starting the system")
    try:
        p = Path(__file__).parent.parent / "podcasts"
        logger.info("the path its corrct :)")
    except Exception as error:
        logger.error("the path is not correct beacose: ",error)

    for f in p.iterdir():
        data = md.extract_metadata(f)
        producer.prduce_data(data)
except Exception as error:
    logger.error("the system fail beacose:",error)