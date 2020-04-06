import speech_recognition as sr
import os
import lib.system as sys
import lib.viki_voice as viki
import lib.commands as com
import lib.weather as weather

# first_commnand nous indique si choix multiple
def command(first_command=True):

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Prêt...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        voice_command = r.recognize_google(audio, language="fr-FR").lower()

        if first_command == True:
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
            viki.talk("Quelle page voulez-vous ouvrir ?")
            # On appel la méthode command pour affecter ce qu'on dit à website
            website = command(first_command=False)
            sys.launch_webbrower(website)

    elif com.list_command.get(4) in voice_command:
        exit()
    
    elif com.list_command.get(5) in voice_command:
        city = weather.get_town()
        temp = weather.get_weather(city)
        viki.talk(f"Il fait {temp}° à {city}")


while True:
    assistant(command())

