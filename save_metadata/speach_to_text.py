import speech_recognition as sr


class STT:

    def __init__(self):
        self.r = sr.Recognizer()


    def convert_stt(self,filename):
        with sr.AudioFile(filename) as source:
            audio_data = self.r.record(source)
            text = self.r.recognize_google(audio_data)
        return text  