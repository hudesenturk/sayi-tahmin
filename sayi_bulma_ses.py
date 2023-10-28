import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr

class SesliAsistan:
    def __init__(self):
        self.kayit = sr.Recognizer()

    def dinle(self):
        print("Ses ver")
        with sr.Microphone() as Kaynak:
            self.kayit.adjust_for_ambient_noise(Kaynak, duration=1)
            mikrofon = self.kayit.listen(Kaynak)
            ses = ""

            try:
                ses = self.kayit.recognize_google(mikrofon, language="tr-TR")
            except sr.UnknownValueError:
                print("anlamadım")
            except sr.RequestError:
                print("sistem arızalı")
            return ses

    def konus(self, metin):
        tts = gTTS(text=metin, lang="tr", slow=False)
        ses = r"C:\Users\hudes\OneDrive\Desktop\hude.py\islik.mp3"
        tts.save(ses)
        playsound(ses)
if __name__ == "__main__":
    asistan = SesliAsistan()
    asistan.konus("merhaba")


