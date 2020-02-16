"""
toute les opérations système (tri fichier, backup, enregistrer fichier ...)
"""
import random
import os
import subprocess
import webbrowser
import lib.viki_voice as viki

def salut():
    hello = ["salut", "bonjour Talyov", "yo"]
    viki.talk(random.choice(hello))

def launch_webbrower(website):
    if website in "impots" or website in "impôts":
        webbrowser.open("https://www.impots.gouv.fr/portail/")

    elif website in "pagesjaunes" or website in "pages jaunes":
        webbrowser.open("https://www.pagesjaunes.fr/")

    elif website == "facebook":
        webbrowser.open("https://www.facebook.com/")

    else:
        webbrowser.open("http://www.google.fr")
    

def meteo():
    pass


if __name__ == "__main__":
    print("test classe system...")

