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
    if website == "impot" or "impots" or "impôt":
        webbrowser.open("https://www.impots.gouv.fr/portail/")

    elif website == "page jaune" or "pages jaunes" or "pagesjaunes":
        webbrowser.open("https://www.pagesjaunes.fr/")

    elif website == "facebook" or "face book":
        webbrowser.open("https://www.facebook.com/")

    else:
        webbrowser.open("http://www.google.fr")
    

def meteo():
    pass


if __name__ == "__main__":
    print("test classe system...")

