import os

def VerificationSESSION():
    
    while True:
        try:
            CheminFichier = "SESSION.txt"
            if os.path.exists(CheminFichier):
                with open(CheminFichier, "r") as f:
                    Contenu = f.read().strip()

                if Contenu != "0":
                    print("Le statut de la session est différent de 0. Arrêt du serveur.")
                    os._exit(1) 

            else:
                print("Le fichier de statut de la session n'existe pas. Le serveur continue de fonctionner.")

        except Exception as e:
            print(f"Une erreur s'est produite lors de la vérification du statut de la session : {e}")

def ChangerStatutSession():
    try:
        CheminFichier = "SESSION.txt"

        with open(CheminFichier, "w") as f:
            f.write("1")

        print("Le statut de la session a été changé avec succès.")

    except Exception as e:
        print(f"Une erreur s'est produite lors du changement de statut de session : {e}")


def ChangementStatut0():
    try:
        CheminFichier = "SESSION.txt"

        with open(CheminFichier, "w") as f:
            f.write("0")

        print("Le statut de la session a été remis à 0.")

    except Exception as e:
        print(f"Une erreur s'est produite lors du changement de statut de session : {e}")


