import speech_recognition as sr
from tools.falar_texto import *

def ouvir():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="pt-BR")
        return texto.lower()
    except sr.UnknownValueError:
        falar("Não entendi o que você disse")
        return ""
    except sr.RequestError as e:
        falar("Não foi possível obter resposta do serviço de reconhecimento de voz; {0}".format(e))
        return ""
