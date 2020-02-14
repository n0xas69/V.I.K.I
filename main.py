import speech_recognition as sr
import os

def command():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Prêt")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("Commande : " + command + '\n')

    # boucle si la commande passé n'est pas reconnu
    except sr.UnknownValueError:
        print("Commande inconnu")
        command = myCommand()

    return command

def assistant():
    ''' Condition suivant ce que l'utilisateur dit '''
    if "affiche salut" in command:
        print("Salut")

    elif "affiche sarce" in command:
        print("sarce")



