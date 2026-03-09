import base64
from logs import Logger


class BDS:
    def __init__(self):
        self.logger = Logger.get_logger(name="save_metadata/bds")

        self.list_hostile_to_israel = "R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT"
        self.list_less_hostile_to_israel = "RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=="
        try:
            self.decoder()
            self.logger.info("the decoder work successfully")
        except Exception as error:
            self.logger.error(f"the decoder not work beacose: {error}")

    def decoder(self):
        self.list_hostile_to_israel = base64.b64decode(self.list_hostile_to_israel).decode('utf-8')
        self.list_less_hostile_to_israel = base64.b64decode(self.list_less_hostile_to_israel).decode('utf-8')

    def counter_words(self,text:str) -> int:
        try:
            counter = 0
            list_from_text = text.split(" ")
            all_list = [self.list_hostile_to_israel.split(","),self.list_less_hostile_to_israel.split(",")]
            for index in range(2):
                list_from_text_of_decode = all_list[index]
                for word in list_from_text_of_decode:
                    if " " in word:
                        for i in range(len(list_from_text)-1):
                            tow_words = " ".join([list_from_text[i],list_from_text[i+1]])
                            if tow_words.lower() == word.lower():
                                if index == 1:
                                    counter += 2
                                else:
                                    counter += 1
                    else:
                        for word_to_check in list_from_text:
                            if word_to_check.lower() == word.lower():
                                if index == 1:
                                    counter += 2
                                else:
                                    counter += 1
            self.logger.debug("the logic of counter word work successfully")
            return counter
        except Exception as error:
            self.logger.error(f"the logic not work beacose: {error}")
            return 0

    def bds_percent(self,text:str,counter:int) -> float:
        return 100 / len(text.split()) * counter

    def is_bds(self,percent:float) -> bool:
        if percent > 10:
            return True
        return False
    
    def bds_threat_level(self,percent:float) -> str:
        if percent < 10:
            return "none"
        elif percent < 20:
            return "medium"
        else:
            return "high"
    
    def make_metadata(self,text:str) -> dict:
        try: 
            counter = self.counter_words(text)
            percent = self.bds_percent(text,counter)
            data = {"bds_percent": percent,
                    "is_bds":self.is_bds(percent),
                    "bds_threat_level":self.bds_threat_level(percent)}
            self.logger.debug("the metadata of bds work good")
            return data
        except Exception as error:
            self.logger.error(f"the metadata of bds not work beacose: {error}")
            return {}           
