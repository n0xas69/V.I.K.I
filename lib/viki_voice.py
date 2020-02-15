from gtts import gTTS
import os

def talk(audio):
    print(audio)
    for line in audio.splitlines():
        text_to_speech = gTTS(text=audio, lang="fr")
        text_to_speech.save("audio.mp3")
        os.startfile("audio.mp3")
