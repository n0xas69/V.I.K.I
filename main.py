import speech_recognition as sr
import os
from classes.salut import Speak


def command():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Prêt")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        voice_command = r.recognize_google(audio, language="fr-FR").lower()
        print("Commande : " + voice_command + '\n')

    # boucle si la commande passé n'est pas reconnu
    except sr.UnknownValueError:
        print("Commande inconnu")
        voice_command = command()

    return voice_command

def assistant(voice_command):
    ''' Condition suivant ce que l'utilisateur dit '''
    if "affiche salut" in voice_command:
        speak = Speak()
        speak.salut()

    elif "affiche sarce" in voice_command:
        print("sarce")


while True:
    assistant(command())
