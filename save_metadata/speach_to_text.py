import speech_recognition as sr
from logs import Logger


class STT:

    def __init__(self):
        self.logger = Logger.get_logger(name="save_metadat/stt")
        self.r = sr.Recognizer()


    def convert_stt(self,filename):
        try:
            with sr.AudioFile(filename) as source:
                audio_data = self.r.record(source)
                text = self.r.recognize_google(audio_data)
                self.logger.info(f"the audio converted to text, the text: {text}")
            return text
        except Exception as error:
            self.logger.error(f"the path of filename its not correct beacose: {error}")