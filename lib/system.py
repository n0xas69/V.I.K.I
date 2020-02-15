"""
toute les opérations système (tri fichier, backup, enregistrer fichier ...)
"""
import random
import os
import subprocess
import webbrowser
from lib.viki_voice import Voice

def salut():
    hello = ["salut", "bonjour", "yo"]
    Voice.talkToMe(random.choice(hello))

def launch_webbrower():
    webbrowser.open("http://www.google.fr")


if __name__ == "__main__":
    print("test classe system...")
