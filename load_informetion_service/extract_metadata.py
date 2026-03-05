from pathlib import Path
import time


class Metadata:

    @staticmethod
    def extract_metadata(path: Path):
        return {
            "file_name": path.name,
            "creation_date": Metadata.extract_creation_date(path.stat().st_birthtime),
            "size": path.stat().st_size,
            "full_path": str(path.absolute()),
        }

    @staticmethod
    def extract_creation_date(epoch_time):
        return time.strftime("%Y-%m-%d %H-%M-%S", time.gmtime(epoch_time))
