from pathlib import Path

from extract_metadata import Metadata as md
from kafka_publisher import KafkaPublisher


producer = KafkaPublisher()
try:
    p = Path(__file__).parent.parent / "podcasts"

    for f in p.iterdir():
        data = md.extract_metadata(f)
        producer.prduce_data(data)
except Exception as error:
    print("❌ERROR:", error)
