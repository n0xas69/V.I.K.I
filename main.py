import speech_recognition as sr
import os
import lib.system as sys


def command():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Prêt...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        voice_command = r.recognize_google(audio, language="fr-FR").lower()
        print("Commande : " + voice_command + "\n")

    # si la commande passé n'est pas reconnu
    except sr.UnknownValueError:
        print("Commande inconnu")
        voice_command = command()

    return voice_command


def assistant(voice_command):
    """ Condition suivant ce que l'utilisateur dit """
    if "affiche salut" in voice_command:
        print("Salut")

    elif "dis bonjour" in voice_command:
        sys.salut()

    elif "ouvre internet" in voice_command:
        sys.launch_webbrower()


while True:
    assistant(command())
