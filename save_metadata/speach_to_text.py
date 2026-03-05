import speech_recognition as sr


class STT:

    def __init__(self):
        self.r = sr.Recognizer()


    def convert_stt(self,filename):
        with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
            audio_data = self.r.record(source)
            # recognize (convert from speech to text)
            text = self.r.recognize_google(audio_data)
        return text  