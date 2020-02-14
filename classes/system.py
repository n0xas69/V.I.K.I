'''affiche salut en console'''
import random
import os
from gtts import gTTS
import subprocess
import webbrowser

class System:

    def __init__(self):
        pass

    def talkToMe(self, audio):

        print(audio)
        for line in audio.splitlines():
            text_to_speech = gTTS(text=audio, lang='fr')
            text_to_speech.save('audio.mp3')
            os.startfile('audio.mp3')
            # PLAYERPATH = r"C:\Program Files\VideoLAN\VLC\vlc.exe"
            # FILEPATH = r"D:\DEV\audio.mp3"
            # subprocess.call([PLAYERPATH, FILEPATH])

    def salut(self):
        hello = ["salut", "bonjour", "yo"]
        self.talkToMe(random.choice(hello))

        
    def launch_webbrower(self):
        webbrowser.open("http://www.google.fr")
        
