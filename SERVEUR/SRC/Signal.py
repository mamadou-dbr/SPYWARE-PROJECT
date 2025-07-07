import socket
from datetime import datetime

def EnvoiSignalFermeture(IPClient, PORTClient):
    try:
        ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ClientSocket.connect((IPClient, int(PORTClient)))

        ClientSocket.sendall(b"FERMER")

        ClientSocket.close()

        print(f"Signal de fermeture envoyé au client {IPClient}:{PORTClient}")

    except Exception as e:
        print(f"Erreur lors de l'envoi du signal de fermeture au client {IPClient}:{PORTClient} : {e}")

def EnvoiSignalFermetureClients():
    try:
        # Lecture des adresses IP et ports des clients depuis le fichier clients.txt
        with open("clients.txt", "r") as f:
            for Line in f:
                IPClient, PORTClient = Line.strip().split(":")
                EnvoiSignalFermeture(IPClient, PORTClient)

    except FileNotFoundError:
        print("Le fichier clients.txt n'existe pas.")
