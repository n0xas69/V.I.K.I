"""

Créateurs : 
Les sarces

Date de création :
le 16/02/2020

"""
import speech_recognition as sr
import os
import lib.system as sys
import lib.viki_voice as viki
import lib.commands as com


def command():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Prêt...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        voice_command = r.recognize_google(audio, language="fr-FR").lower()
        if voice_command not in com.list_command.values():
            viki.talk("Commande inconnu")
        print("Commande : " + voice_command + "\n")

    # Si viki ne comprends pas
    except sr.UnknownValueError:
        print("Je ne comprends pas")
        voice_command = command()

    return voice_command

def assistant(voice_command):
    # Condition suivant ce que l'utilisateur dit
    if com.list_command.get(1) in voice_command:
        print("Salut")

    elif com.list_command.get(2) in voice_command:
        sys.salut()

    elif com.list_command.get(3) in voice_command:
        sys.launch_webbrower()



while True:
    assistant(command())

